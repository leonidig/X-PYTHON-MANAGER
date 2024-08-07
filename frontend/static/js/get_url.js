function submitDropdownForm(theme) {
    document.getElementById('dropdownValue').value = theme;
    document.getElementById('dropdownForm').action = `/theme/${theme}`;
    document.getElementById('dropdownForm').submit();
}
