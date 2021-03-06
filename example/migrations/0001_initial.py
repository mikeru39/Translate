# Generated by Django 3.1 on 2020-08-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('name_af', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ar', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ar_dz', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ast', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_az', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_bg', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_be', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_bn', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_br', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_bs', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ca', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_cs', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_cy', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_da', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_de', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_dsb', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_el', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_en_au', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_en_gb', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_eo', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_es', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_es_ar', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_es_co', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_es_mx', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_es_ni', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_es_ve', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_et', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_eu', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_fa', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_fi', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_fr', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_fy', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ga', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_gd', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_gl', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_he', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_hi', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_hr', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_hsb', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_hu', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_hy', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ia', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ind', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ig', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_io', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_is', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_it', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ja', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ka', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_kab', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_kk', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_km', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_kn', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ko', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ky', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_lb', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_lt', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_lv', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_mk', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ml', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_mn', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_mr', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_my', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_nb', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ne', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_nl', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_nn', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_os', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_pa', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_pl', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_pt', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_pt_br', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ro', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_sk', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_sl', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_sq', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_sr', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_sr_latn', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_sv', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_sw', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ta', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_te', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_tg', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_th', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_tk', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_tr', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_tt', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_udm', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_uk', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_ur', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_vi', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_zh_hans', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('name_zh_hant', models.CharField(max_length=30, null=True, verbose_name='Name')),
                ('short_description', models.CharField(max_length=100, verbose_name='Short description')),
                ('short_description_af', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ar', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ar_dz', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ast', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_az', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_bg', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_be', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_bn', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_br', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_bs', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ca', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_cs', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_cy', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_da', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_de', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_dsb', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_el', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_en', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_en_au', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_en_gb', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_eo', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_es', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_es_ar', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_es_co', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_es_mx', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_es_ni', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_es_ve', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_et', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_eu', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_fa', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_fi', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_fr', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_fy', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ga', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_gd', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_gl', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_he', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_hi', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_hr', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_hsb', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_hu', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_hy', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ia', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ind', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ig', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_io', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_is', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_it', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ja', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ka', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_kab', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_kk', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_km', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_kn', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ko', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ky', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_lb', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_lt', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_lv', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_mk', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ml', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_mn', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_mr', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_my', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_nb', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ne', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_nl', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_nn', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_os', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_pa', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_pl', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_pt', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_pt_br', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ro', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ru', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_sk', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_sl', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_sq', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_sr', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_sr_latn', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_sv', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_sw', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ta', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_te', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_tg', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_th', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_tk', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_tr', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_tt', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_udm', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_uk', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_ur', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_uz', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_vi', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_zh_hans', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('short_description_zh_hant', models.CharField(max_length=100, null=True, verbose_name='Short description')),
                ('description', models.CharField(max_length=5000, verbose_name='Description')),
                ('description_af', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ar', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ar_dz', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ast', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_az', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_bg', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_be', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_bn', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_br', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_bs', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ca', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_cs', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_cy', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_da', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_de', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_dsb', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_el', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_en', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_en_au', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_en_gb', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_eo', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_es', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_es_ar', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_es_co', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_es_mx', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_es_ni', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_es_ve', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_et', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_eu', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_fa', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_fi', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_fr', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_fy', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ga', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_gd', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_gl', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_he', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_hi', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_hr', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_hsb', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_hu', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_hy', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ia', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ind', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ig', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_io', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_is', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_it', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ja', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ka', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_kab', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_kk', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_km', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_kn', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ko', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ky', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_lb', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_lt', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_lv', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_mk', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ml', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_mn', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_mr', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_my', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_nb', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ne', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_nl', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_nn', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_os', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_pa', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_pl', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_pt', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_pt_br', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ro', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ru', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_sk', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_sl', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_sq', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_sr', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_sr_latn', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_sv', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_sw', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ta', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_te', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_tg', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_th', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_tk', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_tr', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_tt', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_udm', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_uk', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_ur', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_uz', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_vi', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_zh_hans', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('description_zh_hant', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('quantity_of_lectures', models.IntegerField(verbose_name='Quantity of lectures')),
            ],
        ),
    ]
