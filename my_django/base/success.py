from rest_framework.response import Response

def SuccessResponse(data, message="", status="") :
    content={
        "success" : True,
        "message" : message,
        "data"    : data
    }
    return Response(data=content,status=status)
