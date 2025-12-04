import { useState } from "react";
import AddTaskForm from "../components/AddTaskForm";
import TaskList from "../components/TaskList";

function TasksPage() {
    const userId = 1; // можно подключить авторизацию
    const [reload, setReload] = useState(false);

    return (
        <div style={styles.container}>
            <h1 style={styles.title}>Мои задачи</h1>
            <AddTaskForm
                userId={userId}
                onTaskAdded={() => setReload(!reload)}
            />
            <TaskList key={reload} userId={userId} />
        </div>
    );
}

const styles = {
    container: {
        maxWidth: 800,
        margin: "0 auto",
        padding: "20px",
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        color: "#333",
    },
    title: {
        textAlign: "center",
        marginBottom: 20,
        color: "#4A90E2",
    },
};

export default TasksPage;
