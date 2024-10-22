from django.conf import settings
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receitas", "0003_rename_modo_de_preparo_receita_modo_preparo"),
    ]

    operations = [
        migrations.AddField(
            model_name="receita",
            name="pessoa",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
