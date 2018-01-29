# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import requests

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from navigator.settings import GIT_HUB_URL, REQUEST_TIME_OUT

from django.shortcuts import render


# Create your views here.

class Navigator(APIView):
    """
    Class Navigator
    This class is used for fetching api data.
    """
    __author__ = "Sanju Sci"
    __email__ = "sanju.sci9@gmail.com"

    def get(self, request):
        """
        Function get
        This function is used to get data from api.

        :param request:
            A request that contains request params.

        :return:
            Return  if exists else return empty dict.

        __author__ = "Sanjeev Kumar"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            return_data = []
            search = request.GET.get('search_term', None)
            if search:
                resp = External().get_repositories(search)
                if resp and 'items' in resp:
                    resp['items'] = sorted(
                        resp['items'],
                        key=lambda i: i['created_at'],
                        reverse=True
                    )[:5]
                    for lst in resp['items']:
                        fetch_commit = External().get_commits(lst['url'])
                        if len(fetch_commit) > 0:
                            result = {
                                'repository_name': lst['name'],
                                'owner_url': lst['owner']['url'],
                                'avatar_url': lst['owner']['avatar_url'],
                                'owner_login': lst['owner']['login'],
                                'sha': fetch_commit[0]['sha'],
                                'commit_message': fetch_commit[0]['commit'][
                                    'message'],
                                'commit_author_name': fetch_commit[0]['commit'][
                                    'author']['name'],
                                'created_at': lst['created_at']
                            }
                            return_data.append(result)
                else:
                    return Response(
                        'Git api response error!!',
                        status=status.HTTP_400_BAD_REQUEST
                    )
                return Response(return_data, status=status.HTTP_200_OK)
            else:
                return Response(
                    'Search parameter is missing!! Please check input!!',
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                str(e.message),
                status=status.HTTP_400_BAD_REQUEST
            )


class External:
    """
    Class External
    This Class is used to fetch and send data form external api
    """
    __author__ = "Sanju Sci"
    __email__ = "sanju.sci9@gmail.com"

    def __init__(self):
        self.api_url = GIT_HUB_URL
        self.headers = {
            "User-agent": "curl/7.43.0",
            "Content-Type": "application/json"
        }

    def get_repositories(self, params):
        """
        Function get_repositories
        This function is used to get git repositories using git api.

        :param params:
            A params that contains request query string value.

        :return:
            Return list of repositories if data fetch successfully from git api
            else return empty list.

        __author__ = "Sanju Sci"
        __email__ = "sanju.sci9@gmail.com"
        """
        try:
            api_url = self.api_url + "search/repositories?q=" + str(params)
            response = requests.get(
                api_url,
                headers=self.headers,
                timeout=REQUEST_TIME_OUT
            )
            resp = json.loads(response.text)
            print(resp)
            return resp
        except (ValueError, KeyError, TypeError):
            print(ValueError, KeyError, TypeError)
            print('Github api response error from get_repositories function!!')
            return []

    def get_commits(self, url):
        """
        Function get_commits
        This function is used to get git commits repository data using git api.

        :param url:
            A url that contains request query url.

        :return:
            Return list of commit repository data if fetch successfully data
            from api else return empty list.

        __author__ = "Sanju Sci"
        __email__ = "sanju.sci9@gmail.com"
        """

        try:
            api_url = url + '/commits'
            print(api_url)
            response = requests.get(
                api_url,
                headers=self.headers,
                timeout=REQUEST_TIME_OUT
            )
            resp = json.loads(response.text)
            return resp
        except (ValueError, KeyError, TypeError):
            print(ValueError, KeyError, TypeError)
            print('Github api response error from get_commits function!!')
            return []


def index(request):
    return render(request, 'api/index.html')


# def index2(request):
#     return render(request, 'api/a.html')