-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: remotemysql.com
-- Generation Time: Nov 03, 2022 at 01:35 PM
-- Server version: 8.0.13-4
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Jr1FnFEvhE`
--
CREATE DATABASE IF NOT EXISTS `Jr1FnFEvhE` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `Jr1FnFEvhE`;

-- --------------------------------------------------------

--
-- Table structure for table `assign_to_leader`
--

CREATE TABLE `assign_to_leader` (
  `aid` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `wid` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `assign_to_leader`
--

INSERT INTO `assign_to_leader` (`aid`, `lid`, `wid`, `date`, `status`) VALUES
(5, 7, 2, '2022-10-08', 'pending'),
(6, 12, 3, '2022-10-09', 'pending'),
(7, 12, 4, '2022-10-09', 'pending'),
(8, 12, 5, '2022-10-09', 'pending'),
(9, 12, 6, '2022-10-09', 'pending'),
(10, 8, 7, '2022-10-09', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `assign_to_member`
--

CREATE TABLE `assign_to_member` (
  `aid` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `wid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `assign_to_member`
--

INSERT INTO `assign_to_member` (`aid`, `lid`, `wid`, `date`, `status`) VALUES
(1, 11, 3, '2022-10-09', 'pending'),
(2, 2, 5, '2022-10-09', 'pending'),
(3, 2, 4, '2022-10-10', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `cid` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `complaint` varchar(500) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `doubt`
--

CREATE TABLE `doubt` (
  `did` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `doubt` varchar(500) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `feedback` varchar(500) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `leader`
--

CREATE TABLE `leader` (
  `id` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `leader`
--

INSERT INTO `leader` (`id`, `lid`, `fname`, `lname`, `gender`, `place`, `pin`, `post`, `email`, `phone`) VALUES
(3, 6, 'demo ', 'user', 'male', 'somewhere', 11111, 'hehe', 'aa@example.com', 1234),
(4, 7, 'demo user ', '2', 'male', 'd', 45, 'h', 'hdhd@hdh.cod', 2345678),
(5, 8, 'musadhiq', 'mp', 'male', 'tkm', 679332, 'chyd', 'musadhiq@gmail.com', 123456780),
(6, 9, 'sdfgb', '', 'male', 'sdf', 234, 'sdf', '', 12345),
(7, 12, 'leader', '1', 'male', 'asd', 5678, 'sdf', 'fghj@fds', 23456789);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `uname` varchar(25) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `uname`, `password`, `type`) VALUES
(1, 'admin', '123', 'admin'),
(4, 'asdfg', '123', 'leader'),
(5, 'testuser', '123', 'leader'),
(6, 'demouser', '123', 'leader'),
(7, 'demo2', '123', 'leader'),
(8, 'musadhiqmp', '123', 'leader'),
(9, 'asdfghj', '123', 'leader'),
(10, 'pablo', '123', 'member'),
(11, 'member', '123', 'member'),
(12, 'leader', '123', 'leader'),
(13, 'leader', '123', 'member'),
(14, 'leader', '123', 'member'),
(15, 'test', '123', 'member');

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `mid` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`mid`, `lid`, `fname`, `lname`, `gender`, `place`, `pin`, `post`, `email`, `phone`) VALUES
(1, 2, 'demo', 'member', 'female', 'tkm', 567, 'fsds', 'test@example.com', 123456789),
(2, 10, 'demo', 'member', 'male', 'tkm', 12345, 'chyd', 'msq@gmail.com', 12345678),
(3, 11, 'musadhiq', 'mp', 'male', 'qwe', 234, 'd', 'member@example.com', 1234567890),
(4, 14, 'member', '5', 'female', 'asdfg', 676123, 'gh', 'abijithp91@gmail.com', 45652),
(5, 15, 'testsdf', 'account', 'male', 'k', 456, 'jk', 'test@example.com', 23456789);

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `notificationid` int(11) NOT NULL,
  `notification` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`notificationid`, `notification`, `date`) VALUES
(13, 'one', '2022-10-17'),
(14, 'two', '2022-10-17'),
(15, 'three', '2022-10-17'),
(16, 'four', '2022-10-17'),
(17, 'avengers assamble', '2022-10-17');

-- --------------------------------------------------------

--
-- Table structure for table `works`
--

CREATE TABLE `works` (
  `workid` int(11) NOT NULL,
  `workname` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `status` varchar(10) COLLATE utf8_unicode_ci DEFAULT 'false'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `works`
--

INSERT INTO `works` (`workid`, `workname`, `description`, `date`, `status`) VALUES
(2, 'Billing Management', 'Billing Manager responsibilities include working with customers to reconcile billing issues, working with the accounting department to ensure all accounts are up to date, and helping with the training of new employees in the billing department. ', '2022-10-08', NULL),
(3, 'Payroll Accountant', 'Payroll accountants prepare employee salary statements and process paychecks. They maintain payroll files and create reports. Payroll accountants ensure all payroll procedures are in line with governmental laws and policies.', '2022-10-08', NULL),
(4, 'Budget Management', 'Our ideal candidate holds a degree in Accounting or Finance and is familiar with legal regulations of accounting and budgeting. You should combine excellent numeracy skills with the ability to analyze and present complex data.', '2022-10-08', 'complete');

-- --------------------------------------------------------

--
-- Table structure for table `worktomembers`
--

CREATE TABLE `worktomembers` (
  `wid` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `wname` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assign_to_leader`
--
ALTER TABLE `assign_to_leader`
  ADD PRIMARY KEY (`aid`);

--
-- Indexes for table `assign_to_member`
--
ALTER TABLE `assign_to_member`
  ADD PRIMARY KEY (`aid`);

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `doubt`
--
ALTER TABLE `doubt`
  ADD PRIMARY KEY (`did`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`fid`);

--
-- Indexes for table `leader`
--
ALTER TABLE `leader`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`mid`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`notificationid`);

--
-- Indexes for table `works`
--
ALTER TABLE `works`
  ADD PRIMARY KEY (`workid`);

--
-- Indexes for table `worktomembers`
--
ALTER TABLE `worktomembers`
  ADD PRIMARY KEY (`wid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assign_to_leader`
--
ALTER TABLE `assign_to_leader`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `assign_to_member`
--
ALTER TABLE `assign_to_member`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `doubt`
--
ALTER TABLE `doubt`
  MODIFY `did` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `leader`
--
ALTER TABLE `leader`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `mid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `notificationid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT for table `works`
--
ALTER TABLE `works`
  MODIFY `workid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `worktomembers`
--
ALTER TABLE `worktomembers`
  MODIFY `wid` int(11) NOT NULL AUTO_INCREMENT;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
