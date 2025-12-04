const API_URL = "http://localhost:8000"

export async function getTasks(userId) {
    const res = await fetch(`${API_URL}/task/get_all?user_id=${userId}`);

    if (!res.ok) throw new Error("Ошибка загрузк задач");

    return res.json();
}


export async function addTask(task) {
    const res = await fetch(`${API_URL}/task/add`,{
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(task)
    });
    if (!res.ok) throw new Error("Ошибка добавления задачи")
}

export async function deleteTask(taskId) {
    const res = await fetch(`${API_URL}/task/delete?task_id=${taskId}`,{
        method: "DELETE"
    });
    if (!res.ok) throw new Error("Ошибка удаления задачи")
}