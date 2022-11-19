from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
     print("Welcome URL is requested and display() is executed")
     ss="<center><h2 style='color:Blue;'>Hello User,Welcome to Django FirstProject FirstApp </h2> <hr color='yellow' width='80%' size='5'/></center>";
     return HttpResponse(ss);
     
     
     
def show(request):
     ss="<h2>Hello User,Welcome to Django Project with url Welcome2</h2>"
     return HttpResponse(ss);
     
def hello(request):
    print("hello URL is requested and hello() is executed")
    ss='''
        <html>
            <head>
                <title>Hello Webpage</title>
                <Style>
                     h1{
                        color:Red;
                        }
                     h2{
                        color:Blue;
                        }
                     h3{
                        color:Green;
                        }
                     h1,h2,h3{
                           background-color:lightyellow;
                           width:60%;
                           border:3px solid Black;
                      }
                
                
                
                </style>
            </head>
            <body>
                <center>
                    <h1>Hello User..</h1>
                    <hr color='violet' width='80%' />
                    <h2>Welcome to DJango-App</h2>
                    <hr color='violet' width='80%' />
                    <h3>Have a nice day..</h3>
                </center>
            
            
            </body>
        </html>
        ''';
    return HttpResponse(ss);
    
    
import time;   
def senddatetime(request):
    print("dtime/ URL is requested and senddatetime() is executed")
    ct=time.ctime()
    print("Client request date and time on server.. ",ct)
    ss='''
        <html>
            <head>
                <title>Date-Time Webpage</title>
                <Style>
                     h1{
                        color:Red;
                        }
                     h2{
                        color:Blue;
                        }
                     h3{
                        color:Green;
                        }
                     h1,h2,h3{
                           background-color:lightyellow;
                           width:60%;
                           border:3px solid Black;
                      }
                
                
                
                </style>
            </head>
            <body>
                <center>
                    <h1>Hello User, Welcome to Django..</h1>
                    <hr color='violet' width='80%' />
                    <h2>server Date and Time..</h2>
                    <hr color='violet' width='80%' />
                    <h3>''',ct,'''</h3>
                </center>
            
            
            </body>
        </html>
        ''';
    return HttpResponse(ss);



def demo(req):
    print("Multiple-Request-URLs same response"); 
    htmldata='''<center>
        <h1>Welcome Demo User...</h1>
        <hr />
        <h2>This is same output for different requests</h2> \
        <hr />
        <h3>Have a great day..</h3>
    </center>''';
    return HttpResponse(htmldata);
    
    
 #default-url-request-view-function   
def homepage(req):
    htmldata='''<center>
        <h1>Welcome to Default Homepage...</h1>
        <hr />
        <h2>Your request page is not found..</h2>
        <hr />
        <h3>Plz try other URL or Links..</h3>
    </center>''';
    return HttpResponse(htmldata);    
        
        