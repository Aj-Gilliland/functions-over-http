from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def heyDude(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")


def ageCal(request: HttpRequest, end: int, birthyear: int) -> HttpResponse:
    return HttpResponse(f"{end-birthyear}")


def orderUp(
    request: HttpRequest, burgers: int, fries: int, drinks: int
) -> HttpResponse:
    return HttpResponse(f"{(burgers*4.5)+(fries*1.5)+(drinks*1)}")
