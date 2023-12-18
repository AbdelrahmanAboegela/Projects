function addTask() {
    var taskInput = document.getElementById("taskInput");
    var taskText = taskInput.value.trim();
    if (taskText !== "") {
        var tasksList = document.getElementById("tasks");
        var listItem = document.createElement("li");
        listItem.innerHTML = taskText;
        var removeButton = document.createElement("button");
        removeButton.innerHTML = "X";
        removeButton.onclick = function () {
            tasksList.removeChild(listItem);
        };
        listItem.appendChild(removeButton);
        tasksList.appendChild(listItem);
        taskInput.value = "";
    }
}
