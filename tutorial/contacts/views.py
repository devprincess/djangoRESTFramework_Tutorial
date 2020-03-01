from django.shortcuts import render, redirect

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from contacts.models import Contact
from contacts.serializers import ContactSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from contacts.forms import ContactCreate


class ContactList(APIView):
    """
    List all contacts, or create a new contact.
    """

    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        #return Response(serializer.data)
        return render(request, 'contacts/contact_list.html', {'contactlist': contacts})

    def post(request):
        serializer = ContactCreate()
        if request.method == 'POST':
            serializer = ContactCreate(request.POST)
            if serializer.is_valid():
                serializer.save()
                return redirect('index')
            else:
                return HttpResponse("""your form is wrong, reload on <a href="{{ url: 'index' }}">reload</a>""")
                #return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return render(request, 'contacts/upload_contact.html', {'upload_contact': serializer})


class ContactDetail(APIView):
    """
    Retrieve, update or delete a contact.
    """

    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(request, contact_id):
        contact_id = int(contact_id)
        try:
            contact_sel = Contact.objects.get(id = contact_id)
        except Contact.DoesNotExist:
            return redirect('index')
        contact_form = ContactCreate(request.POST or None, instance = contact_sel)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('index')
        return render(request, 'contacts/upload_contact.html', {'upload_contact': contact_form})

    def delete(request, contact_id):
        contact_id = int(contact_id)
        try:
            contact_sel = Contact.objects.get(id = contact_id)
        except Contact.DoesNotExist:
            return redirect('index')
        contact_sel.delete()
        return redirect('index')