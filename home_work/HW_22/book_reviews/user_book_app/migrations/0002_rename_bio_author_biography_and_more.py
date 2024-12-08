# Generated by Django 5.1.2 on 2024-12-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_book_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='bio',
            new_name='biography',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='review_text',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer_name',
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['title'], name='user_book_a_title_9d5d0b_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['rating'], name='user_book_a_rating_f3aa43_idx'),
        ),
    ]