import { useState } from "react";
import { addTask } from "../api/tasks";

function AddTaskForm({ userId, onTaskAdded }) {
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!name || !description) return;

        try {
            await addTask({ user_id: userId, name, description });
            setName("");
            setDescription("");
            onTaskAdded();
        } catch (err) {
            console.error(err);
            alert("Не удалось добавить задачу");
        }
    };

    return (
        <form style={styles.form} onSubmit={handleSubmit}>
            <input
                style={styles.input}
                type="text"
                placeholder="Название задачи"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
            />
            <textarea
                style={styles.textarea}
                placeholder="Описание задачи"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                required
            />
            <button style={styles.button} type="submit">Добавить задачу</button>
        </form>
    );
}

const styles = {
    form: {
        display: "flex",
        flexDirection: "column",
        gap: "10px",
        marginBottom: "30px",
        background: "#F9F9F9",
        padding: "20px",
        borderRadius: "12px",
        boxShadow: "0 4px 12px rgba(0,0,0,0.05)",
    },
    input: {
        padding: "10px",
        borderRadius: "8px",
        border: "1px solid #ccc",
        fontSize: "16px",
    },
    textarea: {
        padding: "10px",
        borderRadius: "8px",
        border: "1px solid #ccc",
        fontSize: "16px",
        minHeight: "60px",
        resize: "vertical",
    },
    button: {
        padding: "12px",
        backgroundColor: "#4A90E2",
        color: "#fff",
        fontSize: "16px",
        border: "none",
        borderRadius: "8px",
        cursor: "pointer",
        transition: "background 0.3s",
    },
};

export default AddTaskForm;
