# diplom

поиск элемента по id
поиск элемента по name
поиск элемента по классу
поиск элемента по тэгу
поиск по тексту
поиск элемента Ожидание присутствия элемента в структуре документа.

title_is — ожидаем, что заголовок окна равен указанной строке (заголовок окна браузера, а не тег h1-h6 в структуре документа).
title_contains — ожидание, что заголовок окна содержит определённую строку текста.

visibility_of_element_located — ВНИМАТЕЛЬНО! Ожидание видимости элемента на экране.
visibility_of — ожидание видимости элемента WebElement (например, элемент, который ранее найден с помощью метода driver.find_elements_by_css_selector).
presence_of_all_elements_located — ожидание присутствия в документе всех элементов, найденных с помощью указанного локатора.
text_to_be_present_in_element — ожидание определённого текста внутри указанного элемента.
text_to_be_present_in_element_value — ожидание определённого текста внутри атрибута value элемента.
frame_to_be_available_and_switch_to_it — ожидание появления iframe на странице и переключение на него.
invisibility_of_element_located — ожидание невидимости элемента, найденного по указанному локатору.
element_to_be_clickable — ожидание активности элемента, являющегося экземпляром класса WebElement.
element_to_be_selected — ожидание, что элемент в выпадающем списке выбран.
element_located_to_be_selected — то же, что и предыдущая функция, но указывать элемент нужно через функции поиска (find_element_by_id, find_element_by_name и так далее).
element_selection_state_to_be — ожидание, что элемент выпадающего списка имеет определённое состояние.
element_located_selection_state_to_be — то же, что и предыдущая функция, но требуется поиск элемента через функции поиска (find_element_by_id, find_element_by_name и так далее).
alert_is_present — ожидания всплывающего окна на странице браузера.
