
from .student.get_group_list import get_group

from models.material import Material

def get_materials(group_id):
    try:
        group = get_group(group_id)
        if not group:
            return []
        materials = group.materials.select()
        return list(materials) if materials.exists() else []
    except Exception as e:
        print(e)
        return []
    
def get_materials_message(group_id: int, count: int):
    return (
        f"📁 *Guruh materiallari*\n\n"
        f"🆔 *Guruh ID:* `{group_id}`\n"
        f"📄 *Materiallar soni:* `{count}` ta\n\n"
        f"👇 Quyidagi menyudan kerakli materialni tanlang:"
    )

def get_material(material_id):
    return Material.get_by_id(material_id)

def get_material_message(material):
    return (
        f"📁 *Guruh materiallari*\n\n"
        f"🆔 *Guruh ID:* `{material.group_id}`\n"
        f"📄 *Material:* `{material.name}`\n"
        f"📅 *Material turi:* `{material.type}`\n"
    )