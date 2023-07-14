from odoo import http
from odoo.http import request


# auth -user  ===  then only login user access form 

class Teacherdata(http.Controller):
    @http.route('/teacher_webform', type='http' , auth="user" , website='True')
    def teacher_webform(self, **kw):
        countryid =request.env['res.country'].sudo().search([])
        print("exicute heare..............................",countryid)
        return http.request.render('sinstitute_certificate.create_teacher', {'country_id':countryid})
     
    @http.route('/teacher', type='http' , auth="user" , website='True')  
    def teacher(self, **kw):
        print("data has been cretaed.....", kw)
        abc = request.env['certificate.student'].sudo().create(kw)
        print(abc,"======================================")
        return request.render("sinstitute_certificate.demo_check")

    @http.route('/demo', type='http' , auth="public" , website='True') 
    def demo(self, **kw):
        return request.render("sinstitute_certificate.demo_check")
    
    
    @http.route('/testsss', type='http' , auth="public" , website='True') 
    def demoform (self, **kw):
        countryid =request.env['res.country'].sudo().search([])
        print("exicute heare..............................",countryid)
        return http.request.render('sinstitute_certificate.test', {'country_id':countryid})
   
    @http.route('/demo_data', type='http' , auth="user" , website='True')  
    def demoforms(self, **kw):
        print("data has been cretaed.....", kw)
        abc = request.env['certificate.student'].sudo().create(kw)
        print(abc,"======================================")
        return request.render("sinstitute_certificate.demo_check")

















