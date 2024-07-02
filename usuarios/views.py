from rest_framework.generics import CreateAPIView, UpdateAPIView
from .models import Usuario
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UpdateSMTPInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from .serializers import SendEmailSerializer
from django.conf import settings

class SendEmailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.email_smtp or not user.smtp_app_password:
                return Response({"error": "SMTP email or app password not set"}, status=status.HTTP_400_BAD_REQUEST)
            
            destinatario = serializer.validated_data['destinatario']
            asunto = serializer.validated_data['asunto']
            mensaje = serializer.validated_data['mensaje']
            pdf = serializer.validated_data['pdf']
            
            msg = MIMEMultipart()
            msg['From'] = user.email_smtp
            msg['To'] = destinatario
            msg['Subject'] = asunto

            msg.attach(MIMEText(mensaje, 'plain'))

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(pdf.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={pdf.name}')
            msg.attach(part)

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(user.email_smtp, user.smtp_app_password)
                server.sendmail(user.email_smtp, destinatario, msg.as_string())
                server.quit()
                return Response({"success": "Email sent successfully"}, status=status.HTTP_200_OK)
            except smtplib.SMTPException as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateSMTPInfoView(UpdateAPIView):
    model = Usuario
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateSMTPInfoSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistroView(CreateAPIView):
    model = Usuario
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(status=204)

class PerfilView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

class EditarPerfilView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        usuario = request.user
        serializer = UserSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
