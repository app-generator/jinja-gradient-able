# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/')
def index():
  try:
    return render_template( 'pages/index.html', segment='analytics', parent='dashboard')
  except TemplateNotFound:
    return render_template('pages/index.html'), 404


# UI Elemenets
 
@app.route('/bc_typography')
def bc_typography():
  return render_template('pages/bc_typography.html', segment='bc_typograohy', parent='pages')

@app.route('/icon-feather')
def icon_feather():
  return render_template('pages/icon-feather.html', segment='icon-feather', parent='pages')

# Table

@app.route('/tbl_bootstrap')
def tbl_bootstrap():
  return render_template('pages/tbl_bootstrap.html', segment='tbl_bootstrap', parent='pages')

# charts & maps

@app.route('/chart')
def chart_apex():
  return render_template('pages/chart-apex.html', segment='chart-apex', parent='pages')

@app.route('/map-google')
def map_google():
  return render_template('pages/map-google.html', segment='map-google', parent='pages')

# Pages 

@app.route('/user-profile')
def user_profile():
  return render_template('pages/user-profile.html', segment='user-profile', parent='pages')

@app.route('/sample-page')
def sample_page():
  return render_template('pages/sample-page.html', segment='sample-page', parent='pages')

# Authentication 

@app.route('/accounts/auth-signin')
def acc_auth_signin():
  return render_template('accounts/auth-signin.html', segment='auth-signin', parent='accounts')

@app.route('/accounts/auth-signup')
def acc_auth_signup():
  return render_template('accounts/auth-signup.html', segment='auth-signup', parent='accounts')

@app.route('/accounts/password-forgot')
def acc_forgot_password():
  return render_template('accounts/forgot-password.html', segment='forgot-password', parent='accounts')

@app.route('/accounts/password-change-done')
def acc_password_change_done():
  return render_template('accounts/password_change_done.html', segment='password-change-done', parent='accounts')

@app.route('/accounts/password-change')
def acc_password_change():
  return render_template('accounts/password_change.html', segment='password-change', parent='accounts')

@app.route('/accounts/password-reset-complete')
def acc_password_reset_complete():
  return render_template('accounts/password_reset_complete.html', segment='password-reset-complete', parent='accounts')

@app.route('/accounts/password-reset-done')
def acc_password_reset_done():
  return render_template('accounts/password_reset_done.html', segment='password-reset-done', parent='accounts')

@app.route('/accounts/recover-password')
def acc_recover_password():
  return render_template('accounts/recover-password.html', segment='recover-password', parent='accounts')

# Registration

@app.route('/registration/logged-out')
def logged_out():
  return render_template('registration/logged_out.html', segment='logged-out', parent='registraion')

@app.route('/registration/password-change-done')
def reg_password_change_done():
  return render_template('registration/password_change_done.html', segment='reg-password-change-done', parent='registraion')

@app.route('/registration/password-change-form')
def reg_password_change_form():
  return render_template('registration/password_change_form.html', segment='reg-password-change-form', parent='registraion')


def get_segment( request ): 
  try:
    segment = request.path.split('/')[-1]
    if segment == '':
      segment = 'index'
    return segment    
  except:
    return None  

# Custom Filter
@app.template_filter('replace_value')
def replace_value(value, arg):
  return value.replace(arg, ' ').title()