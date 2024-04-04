-- phpMyAdmin SQL Dump
-- version 4.9.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Фев 20 2024 г., 13:49
-- Версия сервера: 8.0.13
-- Версия PHP: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `rybin_Smart_Of`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Air_conditioners`
--

CREATE TABLE `Air_conditioners` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(10) NOT NULL,
  `state` tinyint(1) NOT NULL DEFAULT '0',
  `cabinet_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Air_conditioners`
--

INSERT INTO `Air_conditioners` (`id`, `name`, `state`, `cabinet_id`) VALUES
(1, '215T-1', 0, 1),
(2, '#2', 0, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `Cabinets`
--

CREATE TABLE `Cabinets` (
  `id` int(11) UNSIGNED NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `department` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Cabinets`
--

INSERT INTO `Cabinets` (`id`, `name`, `department`) VALUES
(1, '215Т', 'ОТП'),
(2, 'Лаборанская 215', 'ОТП'),
(18, '218Т', 'ОТП'),
(15, '207Т', 'ОТП'),
(19, '215111111111111111', 'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'),
(20, '215111111111111111', 'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'),
(21, '215111111111111111', 'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo');

-- --------------------------------------------------------

--
-- Структура таблицы `Cameras`
--

CREATE TABLE `Cameras` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(15) NOT NULL,
  `link` text NOT NULL,
  `cabinet_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Cameras`
--

INSERT INTO `Cameras` (`id`, `name`, `link`, `cabinet_id`) VALUES
(1, '№1', '', 1),
(2, '№2', '', 1),
(6, '№22', 'ссылка', 1),
(4, '№4', '', 1),
(5, '№21', 'https://i.ytimg.com/vi/j4UzvCj0jqo/maxresdefault.jpg', 15),
(7, '№24', 'ссылка', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `Conditions`
--

CREATE TABLE `Conditions` (
  `id` int(10) UNSIGNED NOT NULL COMMENT 'Процент открытия жалюзи или штор',
  `position` int(11) NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Electrical_lines`
--

CREATE TABLE `Electrical_lines` (
  `id` int(10) UNSIGNED NOT NULL,
  `state` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'вкл/выкл',
  `cabinet_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Electrical_lines`
--

INSERT INTO `Electrical_lines` (`id`, `state`, `cabinet_id`) VALUES
(1, 1, 1),
(2, 1, 15),
(3, 0, 15),
(4, 0, 15);

-- --------------------------------------------------------

--
-- Структура таблицы `Lamps`
--

CREATE TABLE `Lamps` (
  `id` int(10) UNSIGNED NOT NULL,
  `state` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'состояние',
  `setion_id` int(11) NOT NULL,
  `cabinet_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Motion_sensors`
--

CREATE TABLE `Motion_sensors` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(15) NOT NULL,
  `state` tinyint(1) NOT NULL DEFAULT '0',
  `cabinet_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Radiators`
--

CREATE TABLE `Radiators` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(15) NOT NULL,
  `temperature_id` int(11) NOT NULL,
  `condition_id` int(11) NOT NULL,
  `cabinet_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Sections`
--

CREATE TABLE `Sections` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Sections`
--

INSERT INTO `Sections` (`id`, `name`) VALUES
(1, '215T-1'),
(2, '215T-2');

-- --------------------------------------------------------

--
-- Структура таблицы `Temperature_sensors`
--

CREATE TABLE `Temperature_sensors` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(15) NOT NULL,
  `state` int(11) NOT NULL,
  `cabinet_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `Windows`
--

CREATE TABLE `Windows` (
  `id` int(10) UNSIGNED NOT NULL,
  `open_close` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Открыто или закрыто окно',
  `condition_id` int(11) NOT NULL,
  `cabinet_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Air_conditioners`
--
ALTER TABLE `Air_conditioners`
  ADD PRIMARY KEY (`id`),
  ADD KEY `air_conditioners_cabinet_id_foreign` (`cabinet_id`);

--
-- Индексы таблицы `Cabinets`
--
ALTER TABLE `Cabinets`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Cameras`
--
ALTER TABLE `Cameras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cameras_cabinet_id_foreign` (`cabinet_id`);

--
-- Индексы таблицы `Conditions`
--
ALTER TABLE `Conditions`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Electrical_lines`
--
ALTER TABLE `Electrical_lines`
  ADD PRIMARY KEY (`id`),
  ADD KEY `electrical_lines_cabinet_id_foreign` (`cabinet_id`);

--
-- Индексы таблицы `Lamps`
--
ALTER TABLE `Lamps`
  ADD PRIMARY KEY (`id`),
  ADD KEY `lamps_setion_id_foreign` (`setion_id`),
  ADD KEY `lamps_cabinet_id_foreign` (`cabinet_id`);

--
-- Индексы таблицы `Motion_sensors`
--
ALTER TABLE `Motion_sensors`
  ADD PRIMARY KEY (`id`),
  ADD KEY `motion_sensors_cabinet_id_foreign` (`cabinet_id`);

--
-- Индексы таблицы `Radiators`
--
ALTER TABLE `Radiators`
  ADD PRIMARY KEY (`id`),
  ADD KEY `radiators_condition_id_foreign` (`condition_id`),
  ADD KEY `radiators_temperature_id_foreign` (`temperature_id`),
  ADD KEY `radiators_cabinet_id_foreign` (`cabinet_id`);

--
-- Индексы таблицы `Sections`
--
ALTER TABLE `Sections`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `Temperature_sensors`
--
ALTER TABLE `Temperature_sensors`
  ADD PRIMARY KEY (`id`),
  ADD KEY `temperature_sensors_cabinet_id_foreign` (`cabinet_id`);

--
-- Индексы таблицы `Windows`
--
ALTER TABLE `Windows`
  ADD PRIMARY KEY (`id`),
  ADD KEY `windows_condition_id_foreign` (`condition_id`),
  ADD KEY `windows_cabinet_id_foreign` (`cabinet_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Air_conditioners`
--
ALTER TABLE `Air_conditioners`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `Cabinets`
--
ALTER TABLE `Cabinets`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT для таблицы `Cameras`
--
ALTER TABLE `Cameras`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `Conditions`
--
ALTER TABLE `Conditions`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'Процент открытия жалюзи или штор';

--
-- AUTO_INCREMENT для таблицы `Electrical_lines`
--
ALTER TABLE `Electrical_lines`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `Lamps`
--
ALTER TABLE `Lamps`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Motion_sensors`
--
ALTER TABLE `Motion_sensors`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Radiators`
--
ALTER TABLE `Radiators`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Sections`
--
ALTER TABLE `Sections`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `Temperature_sensors`
--
ALTER TABLE `Temperature_sensors`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `Windows`
--
ALTER TABLE `Windows`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
