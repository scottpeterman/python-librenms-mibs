# SNMP MIB module (AE-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\AE-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:43 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class AeEquipmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ont", 1),
          ("ethernet", 2),
          ("pots", 3),
          ("video", 4),
          ("t1e1", 5),
          ("rfReturn", 6),
          ("wan", 7),
          ("iphost", 8))
    )



class AeEquipmentInstance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )



class AeAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283)
        )
    )
    namedValues = NamedValues(
        *(("eventOnly", 1),
          ("onBattery", 2),
          ("badBattery", 3),
          ("missingBattery", 4),
          ("laserEOL", 5),
          ("lowSigLevel", 6),
          ("linkDownPort1", 7),
          ("mgmtDhcpRenewal", 8),
          ("firmwareUpgradeFail", 9),
          ("timeUpdateFail", 10),
          ("voipDhcpRenewal", 11),
          ("voipRegistration", 12),
          ("voipRegAuth", 13),
          ("linkDownPort2", 14),
          ("linkDownPort3", 15),
          ("linkDownPort4", 16),
          ("linkDownPort5", 17),
          ("linkDownPort6", 18),
          ("linkDownPort7", 19),
          ("linkDownPort8", 20),
          ("voipConfigTftpFail", 21),
          ("upsMissing", 22),
          ("lowBattery", 23),
          ("ontT1E1HardwareFail", 24),
          ("tdmPort1LOS", 25),
          ("tdmPort1AIS", 26),
          ("tdmPort1Loopback", 27),
          ("tdmPort1Powerdown", 28),
          ("tdmPort1PWE3LOS", 29),
          ("tdmPort1PWE3FELOS", 30),
          ("tdmPort1FELOS", 31),
          ("tdmPort1PWE3Malformed", 32),
          ("tdmPort1PWE3Mismatch", 33),
          ("tdmPort2LOS", 34),
          ("tdmPort2AIS", 35),
          ("tdmPort2Loopback", 36),
          ("tdmPort2Powerdown", 37),
          ("tdmPort2PWE3LOS", 38),
          ("tdmPort2PWE3FELOS", 39),
          ("tdmPort2FELOS", 40),
          ("tdmPort2PWE3Malformed", 41),
          ("tdmPort2PWE3Mismatch", 42),
          ("tdmPort3LOS", 43),
          ("tdmPort3AIS", 44),
          ("tdmPort3Loopback", 45),
          ("tdmPort3Powerdown", 46),
          ("tdmPort3PWE3LOS", 47),
          ("tdmPort3PWE3FELOS", 48),
          ("tdmPort3FELOS", 49),
          ("tdmPort3PWE3Malformed", 50),
          ("tdmPort3PWE3Mismatch", 51),
          ("tdmPort4LOS", 52),
          ("tdmPort4AIS", 53),
          ("tdmPort4Loopback", 54),
          ("tdmPort4Powerdown", 55),
          ("tdmPort4PWE3LOS", 56),
          ("tdmPort4PWE3FELOS", 57),
          ("tdmPort4FELOS", 58),
          ("tdmPort4PWE3Malformed", 59),
          ("tdmPort4PWE3Mismatch", 60),
          ("tdmPort5LOS", 61),
          ("tdmPort5AIS", 62),
          ("tdmPort5Loopback", 63),
          ("tdmPort5Powerdown", 64),
          ("tdmPort5PWE3LOS", 65),
          ("tdmPort5PWE3FELOS", 66),
          ("tdmPort5FELOS", 67),
          ("tdmPort5PWE3Malformed", 68),
          ("tdmPort5PWE3Mismatch", 69),
          ("tdmPort6LOS", 70),
          ("tdmPort6AIS", 71),
          ("tdmPort6Loopback", 72),
          ("tdmPort6Powerdown", 73),
          ("tdmPort6PWE3LOS", 74),
          ("tdmPort6PWE3FELOS", 75),
          ("tdmPort6FELOS", 76),
          ("tdmPort6PWE3Malformed", 77),
          ("tdmPort6PWE3Mismatch", 78),
          ("tdmPort7LOS", 79),
          ("tdmPort7AIS", 80),
          ("tdmPort7Loopback", 81),
          ("tdmPort7Powerdown", 82),
          ("tdmPort7PWE3LOS", 83),
          ("tdmPort7PWE3FELOS", 84),
          ("tdmPort7FELOS", 85),
          ("tdmPort7PWE3Malformed", 86),
          ("tdmPort7PWE3Mismatch", 87),
          ("tdmPort8LOS", 88),
          ("tdmPort8AIS", 89),
          ("tdmPort8Loopback", 90),
          ("tdmPort8Powerdown", 91),
          ("tdmPort8PWE3LOS", 92),
          ("tdmPort8PWE3FELOS", 93),
          ("tdmPort8FELOS", 94),
          ("tdmPort8PWE3Malformed", 95),
          ("tdmPort8PWE3Mismatch", 96),
          ("configFileCommandError", 97),
          ("configFileMicError", 98),
          ("cachedConfigFileInUse", 99),
          ("cachedVoipConfigInUse", 100),
          ("mep1NeMaxLoss", 101),
          ("mep1NeAvgLoss", 102),
          ("mep1FeMaxLoss", 103),
          ("mep1FeAvgLoss", 104),
          ("mep1MaxDM", 105),
          ("mep1AvgDM", 106),
          ("mep1MaxDMVar", 107),
          ("mep1AvgDMVar", 108),
          ("mep1CcmLoc", 109),
          ("mep1CcmMac", 110),
          ("mep1CcmMeg", 111),
          ("mep1CcmMep", 112),
          ("mep1CcmPeriod", 113),
          ("mep1CcmRdi", 114),
          ("mep2NeMaxLoss", 115),
          ("mep2NeAvgLoss", 116),
          ("mep2FeMaxLoss", 117),
          ("mep2FeAvgLoss", 118),
          ("mep2MaxDM", 119),
          ("mep2AvgDM", 120),
          ("mep2MaxDMVar", 121),
          ("mep2AvgDMVar", 122),
          ("mep2CcmLoc", 123),
          ("mep2CcmMac", 124),
          ("mep2CcmMeg", 125),
          ("mep2CcmMep", 126),
          ("mep2CcmPeriod", 127),
          ("mep2CcmRdi", 128),
          ("mep3NeMaxLoss", 129),
          ("mep3NeAvgLoss", 130),
          ("mep3FeMaxLoss", 131),
          ("mep3FeAvgLoss", 132),
          ("mep3MaxDM", 133),
          ("mep3AvgDM", 134),
          ("mep3MaxDMVar", 135),
          ("mep3AvgDMVar", 136),
          ("mep3CcmLoc", 137),
          ("mep3CcmMac", 138),
          ("mep3CcmMeg", 139),
          ("mep3CcmMep", 140),
          ("mep3CcmPeriod", 141),
          ("mep3CcmRdi", 142),
          ("mep4NeMaxLoss", 143),
          ("mep4NeAvgLoss", 144),
          ("mep4FeMaxLoss", 145),
          ("mep4FeAvgLoss", 146),
          ("mep4MaxDM", 147),
          ("mep4AvgDM", 148),
          ("mep4MaxDMVar", 149),
          ("mep4AvgDMVar", 150),
          ("mep4CcmLoc", 151),
          ("mep4CcmMac", 152),
          ("mep4CcmMeg", 153),
          ("mep4CcmMep", 154),
          ("mep4CcmPeriod", 155),
          ("mep4CcmRdi", 156),
          ("mep5NeMaxLoss", 157),
          ("mep5NeAvgLoss", 158),
          ("mep5FeMaxLoss", 159),
          ("mep5FeAvgLoss", 160),
          ("mep5MaxDM", 161),
          ("mep5AvgDM", 162),
          ("mep5MaxDMVar", 163),
          ("mep5AvgDMVar", 164),
          ("mep5CcmLoc", 165),
          ("mep5CcmMac", 166),
          ("mep5CcmMeg", 167),
          ("mep5CcmMep", 168),
          ("mep5CcmPeriod", 169),
          ("mep5CcmRdi", 170),
          ("mep6NeMaxLoss", 171),
          ("mep6NeAvgLoss", 172),
          ("mep6FeMaxLoss", 173),
          ("mep6FeAvgLoss", 174),
          ("mep6MaxDM", 175),
          ("mep6AvgDM", 176),
          ("mep6MaxDMVar", 177),
          ("mep6AvgDMVar", 178),
          ("mep6CcmLoc", 179),
          ("mep6CcmMac", 180),
          ("mep6CcmMeg", 181),
          ("mep6CcmMep", 182),
          ("mep6CcmPeriod", 183),
          ("mep6CcmRdi", 184),
          ("mep7NeMaxLoss", 185),
          ("mep7NeAvgLoss", 186),
          ("mep7FeMaxLoss", 187),
          ("mep7FeAvgLoss", 188),
          ("mep7MaxDM", 189),
          ("mep7AvgDM", 190),
          ("mep7MaxDMVar", 191),
          ("mep7AvgDMVar", 192),
          ("mep7CcmLoc", 193),
          ("mep7CcmMac", 194),
          ("mep7CcmMeg", 195),
          ("mep7CcmMep", 196),
          ("mep7CcmPeriod", 197),
          ("mep7CcmRdi", 198),
          ("mep8NeMaxLoss", 199),
          ("mep8NeAvgLoss", 200),
          ("mep8FeMaxLoss", 201),
          ("mep8FeAvgLoss", 202),
          ("mep8MaxDM", 203),
          ("mep8AvgDM", 204),
          ("mep8MaxDMVar", 205),
          ("mep8AvgDMVar", 206),
          ("mep8CcmLoc", 207),
          ("mep8CcmMac", 208),
          ("mep8CcmMeg", 209),
          ("mep8CcmMep", 210),
          ("mep8CcmPeriod", 211),
          ("mep8CcmRdi", 212),
          ("mep9NeMaxLoss", 213),
          ("mep9NeAvgLoss", 214),
          ("mep9FeMaxLoss", 215),
          ("mep9FeAvgLoss", 216),
          ("mep9MaxDM", 217),
          ("mep9AvgDM", 218),
          ("mep9MaxDMVar", 219),
          ("mep9AvgDMVar", 220),
          ("mep9CcmLoc", 221),
          ("mep9CcmMac", 222),
          ("mep9CcmMeg", 223),
          ("mep9CcmMep", 224),
          ("mep9CcmPeriod", 225),
          ("mep9CcmRdi", 226),
          ("mep10NeMaxLoss", 227),
          ("mep10NeAvgLoss", 228),
          ("mep10FeMaxLoss", 229),
          ("mep10FeAvgLoss", 230),
          ("mep10MaxDM", 231),
          ("mep10AvgDM", 232),
          ("mep10MaxDMVar", 233),
          ("mep10AvgDMVar", 234),
          ("mep10CcmLoc", 235),
          ("mep10CcmMac", 236),
          ("mep10CcmMeg", 237),
          ("mep10CcmMep", 238),
          ("mep10CcmPeriod", 239),
          ("mep10CcmRdi", 240),
          ("rfc2544SvcAff", 241),
          ("rxLinkFltEth1", 242),
          ("rxLinkFltEth2", 243),
          ("rxLinkFltEth3", 244),
          ("rxLinkFltEth4", 245),
          ("rxLinkFltEth5", 246),
          ("rxLinkFltEth6", 247),
          ("rxLinkFltEth7", 248),
          ("rxLinkFltEth8", 249),
          ("rxLinkFltWan1", 250),
          ("rxLinkFltWan2", 251),
          ("rxDyingGaspEth1", 252),
          ("rxDyingGaspEth2", 253),
          ("rxDyingGaspEth3", 254),
          ("rxDyingGaspEth4", 255),
          ("rxDyingGaspEth5", 256),
          ("rxDyingGaspEth6", 257),
          ("rxDyingGaspEth7", 258),
          ("rxDyingGaspEth8", 259),
          ("rxDyingGaspWan1", 260),
          ("rxDyingGaspWan2", 261),
          ("rxCritEventEth1", 262),
          ("rxCritEventEth2", 263),
          ("rxCritEventEth3", 264),
          ("rxCritEventEth4", 265),
          ("rxCritEventEth5", 266),
          ("rxCritEventEth6", 267),
          ("rxCritEventEth7", 268),
          ("rxCritEventEth8", 269),
          ("rxCritEventWan1", 270),
          ("rxCritEventWan2", 271),
          ("loamOperDownEth1", 272),
          ("loamOperDownEth2", 273),
          ("loamOperDownEth3", 274),
          ("loamOperDownEth4", 275),
          ("loamOperDownEth5", 276),
          ("loamOperDownEth6", 277),
          ("loamOperDownEth7", 278),
          ("loamOperDownEth8", 279),
          ("loamOperDownWan1", 280),
          ("loamOperDownWan2", 281),
          ("sipCfgFileRetrieve", 282),
          ("sipCfgFileInvalid", 283))
    )



class AeCondStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )



class AeCondSeverityLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("info", 5),
          ("unknown", 6),
          ("clear", 7))
    )



class AeCondServiceAffecting(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )



class AeBriefText(TextualConvention, OctetString):
    status = "current"
    displayHint = "40a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class AeText(TextualConvention, OctetString):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class AeTime(TextualConvention, Integer32):
    status = "current"


class AeFsanSerialNumber(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12



class AeMfgSerialNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class AeRegistrationID(TextualConvention, OctetString):
    status = "current"
    displayHint = "10a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class AeOntState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("booting", 1),
          ("unregistered", 2),
          ("registered", 3))
    )



class AeSnmpVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("v2c", 2),
          ("v3", 3))
    )



class AeOntModelNum(TextualConvention, OctetString):
    status = "current"
    displayHint = "8a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )



class AeOntFirmwareVersion(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class AeOntRegistrationPeriod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )



class AeDeviceClass(TextualConvention, OctetString):
    status = "current"
    displayHint = "8a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )



class AeConfigMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("snmp", 2),
          ("tr69", 3),
          ("dynfile", 4))
    )



class AeConfigFilename(TextualConvention, OctetString):
    status = "current"
    displayHint = "80a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class AeConfigFileMarker(TextualConvention, OctetString):
    status = "current"
    displayHint = "80a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class AeConfigMIC(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class AeDeviceStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acquiredIp", 1),
          ("specificFile", 2),
          ("genericFile", 3),
          ("cachedFile", 4))
    )



class AeConfigStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 1),
          ("manufacturing", 2),
          ("noErrors", 3),
          ("withErrors", 4))
    )



class AePwe3AggInstance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )



class AePwe3T1Instance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class AePwe3BundleInstance(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class PerfCurrentCount(TextualConvention, Gauge32):
    status = "current"


class PerfInvalidFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ok", 1),
          ("pending", 2))
    )



class AeThresholdCrossingIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class AeThresholdCrossingPointer(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class AeVoiceSvcIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )



class AeVoipCfgState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1),
          ("initializing", 2),
          ("fault", 3),
          ("reserved1", 4),
          ("reserved2", 5),
          ("reserved3", 6),
          ("reserved4", 7),
          ("reserved5", 8),
          ("reserved6", 9),
          ("reserved7", 10),
          ("reserved8", 11),
          ("reserved9", 12),
          ("reserved10", 13),
          ("reserved11", 14),
          ("reserved12", 15),
          ("mac", 16),
          ("presence", 17),
          ("nohost", 18),
          ("static", 19),
          ("dhcpconfig", 20),
          ("dhcpacquire", 21),
          ("configpend", 22),
          ("tftpfail", 23),
          ("tftpfilenotfound", 24),
          ("proxyfail", 25),
          ("running", 26),
          ("enabled", 27),
          ("assnconnected", 28),
          ("disabled", 29),
          ("assndisconnected", 30))
    )



class AeVoipServerStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("registered", 1),
          ("insession", 2),
          ("failregicmp", 3),
          ("failregtcp", 4),
          ("failregauth", 5),
          ("failregtimeout", 6),
          ("failregserver", 7),
          ("failinviteicmp", 8),
          ("failinvitetcp", 9),
          ("failinviteauth", 10),
          ("failinvitetimeout", 11),
          ("failinviteserver", 12),
          ("notconfigured", 13),
          ("configdone", 14),
          ("oos", 15),
          ("rsip", 16),
          ("quarantine", 17),
          ("active", 18))
    )



class AeSipCallStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("idle", 1),
          ("dialing", 2),
          ("invite", 3),
          ("ringback", 4),
          ("busy", 5),
          ("ringing", 6),
          ("active", 7),
          ("hold", 8),
          ("disconnecting", 9),
          ("disconnected", 10))
    )



class AeHookState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("onHook", 0),
          ("offHook", 1))
    )



class AeVoipIpLineStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1),
          ("snd", 2),
          ("rec", 4),
          ("sndRec", 6),
          ("hold", 8),
          ("threeway", 16),
          ("callwait", 32))
    )



class AeRtpEncodeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ulaw", 0)
    )



class AeRtpPacketSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(80,
              160)
        )
    )
    namedValues = NamedValues(
        *(("tenMS", 80),
          ("twentyMS", 160))
    )



class AeClearAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("clear", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AE-TC",
    **{"AeEquipmentType": AeEquipmentType,
       "AeEquipmentInstance": AeEquipmentInstance,
       "AeAlarmType": AeAlarmType,
       "AeCondStatus": AeCondStatus,
       "AeCondSeverityLevel": AeCondSeverityLevel,
       "AeCondServiceAffecting": AeCondServiceAffecting,
       "AeBriefText": AeBriefText,
       "AeText": AeText,
       "AeTime": AeTime,
       "AeFsanSerialNumber": AeFsanSerialNumber,
       "AeMfgSerialNumber": AeMfgSerialNumber,
       "AeRegistrationID": AeRegistrationID,
       "AeOntState": AeOntState,
       "AeSnmpVersion": AeSnmpVersion,
       "AeOntModelNum": AeOntModelNum,
       "AeOntFirmwareVersion": AeOntFirmwareVersion,
       "AeOntRegistrationPeriod": AeOntRegistrationPeriod,
       "AeDeviceClass": AeDeviceClass,
       "AeConfigMethod": AeConfigMethod,
       "AeConfigFilename": AeConfigFilename,
       "AeConfigFileMarker": AeConfigFileMarker,
       "AeConfigMIC": AeConfigMIC,
       "AeDeviceStatus": AeDeviceStatus,
       "AeConfigStatus": AeConfigStatus,
       "AePwe3AggInstance": AePwe3AggInstance,
       "AePwe3T1Instance": AePwe3T1Instance,
       "AePwe3BundleInstance": AePwe3BundleInstance,
       "PerfCurrentCount": PerfCurrentCount,
       "PerfInvalidFlag": PerfInvalidFlag,
       "AeThresholdCrossingIndex": AeThresholdCrossingIndex,
       "AeThresholdCrossingPointer": AeThresholdCrossingPointer,
       "AeVoiceSvcIndex": AeVoiceSvcIndex,
       "AeVoipCfgState": AeVoipCfgState,
       "AeVoipServerStatus": AeVoipServerStatus,
       "AeSipCallStatus": AeSipCallStatus,
       "AeHookState": AeHookState,
       "AeVoipIpLineStatus": AeVoipIpLineStatus,
       "AeRtpEncodeType": AeRtpEncodeType,
       "AeRtpPacketSize": AeRtpPacketSize,
       "AeClearAction": AeClearAction}
)
