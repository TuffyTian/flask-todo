"""
 * @Author: Tuffy Tian 
 * @Date: 2020/4/20 3:24 PM 
 * @Last Modified by: Tuffy Tian 
 * @Last Modified time: 2020/4/20 3:24 PM
"""


def success_result(status=True, code=200, message="success", data=None):
    """ Successful Api Result """
    return {
        "status": status,
        "code": code,
        "data": data,
        "message": message
    }


def failure_result(code: int, message: str, status: bool = False):
    """ Aborted Api Result """
    return {
        "status": status,
        "code": code,
        "message": message
    }
