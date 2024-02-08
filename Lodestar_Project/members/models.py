from django.db import models

# Create your models here.
class accounts(models.Model):
    a_id = models.IntegerField(primary_key=True)
    ac_at = models.DateTimeField()
    email = models.CharField(max_length=255)
    a_name = models.CharField(max_length=255)
    gen = models.IntegerField()
    country = models.IntegerField()
    passw = models.CharField(max_length=100)

class users(models.Model):
    u_id = models.ForeignKey(accounts, to_field='a_id', primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    uc_at = models.DateTimeField()
    u_desc = models.CharField(max_length=255)
    #u_desc added

class servers(models.Model):
    se_id = models.IntegerField(primary_key=True)
    sc_at = models.DateTimeField()
    s_name = models.CharField(max_length=255)
    s_desc = models.CharField(max_length=255)
    owner_user_id = models.OneToOneField(users, to_field='u_id', on_delete=models.CASCADE)
    #removed server_image

    
class channels(models.Model):
    c_id = models.IntegerField(primary_key=True)
    se_id = models.ForeignKey(servers, to_field='se_id', on_delete=models.CASCADE)
    cc_at = models.DateTimeField()
    c_name = models.CharField(max_length=255)
    c_desc = models.CharField(max_length=255)
    #removed channel_image

class messages(models.Model):
    m_id = models.IntegerField(primary_key=True)
    b_id = models.IntegerField()
    u_id = models.OneToOneField(users, to_field='u_id', on_delete=models.CASCADE)
    mc_at = models.DateTimeField()
    c_id = models.OneToOneField(channels, to_field='c_id', on_delete=models.CASCADE)
    #removed status

class message_content(models.Model):
    b_id = models.OneToOneField(messages, to_field='b_id', primary_key=True, on_delete=models.CASCADE)
    b_type = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    #can be expanded upon with types

class user_list(models.Model):
    ul_id = models.OneToOneField(servers, to_field='se_id', primary_key=True, on_delete=models.CASCADE)
    u_id = models.ForeignKey(users, to_field='u_id', on_delete=models.CASCADE)


class role(models.Model):
    rp_id = models.IntegerField(primary_key=True)
    ul_id = models.ForeignKey(user_list, to_field='ul_id', on_delete=models.CASCADE)

class permissions(models.Model):
    p_id = models.IntegerField(primary_key=True)
    rp_id = models.IntegerField()
    se_media = models.BooleanField()
    se_msg = models.BooleanField()
    se_com = models.BooleanField()
    re_msg = models.BooleanField()

class role_profile(models.Model):
    rp_id = models.OneToOneField(role, to_field='rp_id', primary_key=True, on_delete=models.CASCADE)
    r_name = models.CharField(max_length=255)
    r_col = models.CharField(max_length=255)
    r_desc = models.CharField(max_length=255)
    p_id = models.OneToOneField(permissions, to_field='p_id', on_delete=models.CASCADE)

class commands(models.Model):
    co_id = models.IntegerField(primary_key=True)
    b_id =  models.OneToOneField(message_content, to_field='b_id', on_delete=models.CASCADE)

class media_collection(models.Model):
    m_id = models.IntegerField(primary_key=True)
    b_id =  models.OneToOneField(message_content, to_field='b_id', on_delete=models.CASCADE)

class report_type(models.Model):
    rt_id = models.IntegerField(primary_key=True)
    is_med = models.BooleanField()
    is_msg = models.BooleanField()
    is_usr = models.BooleanField()
    is_srv = models.BooleanField()
    is_chl = models.BooleanField()
    is_oth = models.CharField(max_length=255)
    
class report(models.Model):
    r_id = models.IntegerField(primary_key=True)
    u_id = models.OneToOneField(users, to_field='u_id', on_delete=models.CASCADE)
    rt_id = models.OneToOneField(report_type, to_field='rt_id', on_delete=models.CASCADE)


