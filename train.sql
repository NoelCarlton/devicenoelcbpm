DROP TABLE IF EXISTS driver;
DROP TABLE IF EXISTS alarm;
DROP TABLE IF EXISTS modules;
DROP TABLE IF EXISTS arguments;
DROP TABLE IF EXISTS avatars;
-- user device pwd ZC2019@bi.cbpm --
CREATE TABLE `train`.`driver` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` CHAR(15) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NOT NULL COMMENT '司机名字',
  `telephone` CHAR(12) NOT NULL COMMENT '电话，唯一查询关键',
  `age` INT NOT NULL DEFAULT 0 COMMENT '司机年龄',
  UNIQUE INDEX `telephone_UNIQUE` (`telephone` ASC),
  PRIMARY KEY (`id`, `telephone`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = '车载设备用于识别司机的司机信息';

CREATE TABLE `alarm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `driver` char(12) NOT NULL COMMENT '司机电话，用于查询关键，和司机关联，与mode构成复合主键',
  `type` char(8) NOT NULL COMMENT '报警类型，“抽烟”、“左顾右盼”.....',
  `trainSeries` char(7) NOT NULL COMMENT '车次',
  `deviceCode` char(10) NOT NULL COMMENT '车载设备编号',
  `createTime` datetime NOT NULL COMMENT '报警时间，由设备检测到报警时生成。注意设备要与时间服务器同步好时间。',
  `path` char(20) NOT NULL COMMENT '报警图片保存路径',
  `isUpload` int(11) NOT NULL DEFAULT '0' COMMENT '0已上传，1未上传',
  `model` varchar(20) NOT NULL COMMENT '车型车号+设备编号构成复合主键',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='报警记录表';

CREATE TABLE `train`.`modules` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `deviceCode` CHAR(10) NOT NULL COMMENT '车载设备编号',
  `trainSeries` CHAR(7) NOT NULL COMMENT '车次',
  `model` VARCHAR(20) NOT NULL COMMENT '车型车号',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = '设备信息记录表';


CREATE TABLE `train`.`arguments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `resolution` INT NOT NULL COMMENT '分辨率',
  `codeRate` INT NOT NULL COMMENT '码率',
  `bitRate` INT NOT NULL COMMENT '位率',
  `quality` CHAR(10) NOT NULL COMMENT '图片质量',
  `frame` INT NOT NULL COMMENT '帧率',
  `ip` CHAR(15) NOT NULL COMMENT 'IP地址',
  `gataway` CHAR(15) NOT NULL COMMENT '网关',
  `port` INT NOT NULL COMMENT '端口',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = '设备参数表';

CREATE TABLE `train`.`avatars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` INT NOT NULL DEFAULT 0 COMMENT '0彩色照片，1红外照片',
  `telephone` CHAR(12) NOT NULL COMMENT '司机电话',
  `avatar` VARCHAR(50) NOT NULL COMMENT '头像保存磁盘路径',
  `character` TEXT(200) NOT NULL COMMENT '特征值',
  PRIMARY KEY (`id`),
  INDEX `telephone_idx` (`telephone` ASC),
  CONSTRAINT `telephone`
    FOREIGN KEY (`telephone`)
    REFERENCES `train`.`driver` (`telephone`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = '司机头像表，一个司机最多能上传十张头像图片，五张彩色，五张红外，至少两张彩色或者至少两张红外';
