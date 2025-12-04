import { useEffect, useState } from "react";
import { getTasks, deleteTask } from "../api/tasks";
import "../styles/TaskList.css";

function TaskList({ userId }) {
    const [tasks, setTasks] = useState([]);

    const fetchTasks = () => {
        getTasks(userId)
            .then((data) => setTasks(data))
            .catch((err) => console.error(err));
    };

    useEffect(() => {
        fetchTasks();
    }, [userId]);

    const handleDelete = async (taskId) => {
        if (!window.confirm("Вы уверены, что хотите удалить задачу?")) return;
        
        try {
            await deleteTask(taskId);
            fetchTasks(); // обновляем список после удаления
        } catch (err) {
            console.error(err);
            alert("Ошибка при удалении задачи");
        }
    };

    if (tasks.length === 0) {
        return <p className="empty-state">Задач нет</p>;
    }

    return (
        <div className="container">
            {tasks.map((task) => (
                <div key={task.task_id} className="card">
                    <div className="header">
                        <h3 className="title">{task.name}</h3>
                        <button
                            className="delete-button"
                            onClick={() => handleDelete(task.task_id)}
                        >
                            Удалить
                        </button>
                    </div>
                    <p className="description">{task.description}</p>
                    <small className="date">
                        Создано: {new Date(task.created_at).toLocaleString()}
                    </small>
                </div>
            ))}
        </div>
    );
}

const styles = {
    container: {
        display: "flex",
        flexDirection: "column",
        gap: "15px",
    },
    card: {
        background: "#fff",
        padding: "15px 20px",
        borderRadius: "12px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.05)",
        transition: "transform 0.2s",
    },
    header: {
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
    },
    title: {
        margin: 0,
        marginBottom: "5px",
        color: "#333",
    },
    description: {
        margin: 0,
        marginBottom: "8px",
        color: "#555",
    },
    date: {
        color: "#999",
        fontSize: "12px",
    },
    deleteButton: {
        padding: "6px 10px",
        backgroundColor: "#E94B35",
        color: "#fff",
        border: "none",
        borderRadius: "6px",
        cursor: "pointer",
        fontSize: "12px",
        transition: "background 0.3s",
    },
};

export default TaskList;