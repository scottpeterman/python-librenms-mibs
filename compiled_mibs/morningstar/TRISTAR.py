# SNMP MIB module (TRISTAR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\morningstar\TRISTAR
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:56 2025
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

(morningstar,) = mibBuilder.importSymbols(
    "MORNINGSTAR",
    "morningstar")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

tristar = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33333, 8)
)
if mibBuilder.loadTexts:
    tristar.setRevisions(
        ("2019-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SettingsSwitchesEnum(TextualConvention, Integer32):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("off-off-off-off-off-off-off-off", 0),
          ("on-off-off-off-off-off-off-off", 1),
          ("off-on-off-off-off-off-off-off", 2),
          ("on-on-off-off-off-off-off-off", 3),
          ("off-off-on-off-off-off-off-off", 4),
          ("on-off-on-off-off-off-off-off", 5),
          ("off-on-on-off-off-off-off-off", 6),
          ("on-on-on-off-off-off-off-off", 7),
          ("off-off-off-on-off-off-off-off", 8),
          ("on-off-off-on-off-off-off-off", 9),
          ("off-on-off-on-off-off-off-off", 10),
          ("on-on-off-on-off-off-off-off", 11),
          ("off-off-on-on-off-off-off-off", 12),
          ("on-off-on-on-off-off-off-off", 13),
          ("off-on-on-on-off-off-off-off", 14),
          ("on-on-on-on-off-off-off-off", 15),
          ("off-off-off-off-on-off-off-off", 16),
          ("on-off-off-off-on-off-off-off", 17),
          ("off-on-off-off-on-off-off-off", 18),
          ("on-on-off-off-on-off-off-off", 19),
          ("off-off-on-off-on-off-off-off", 20),
          ("on-off-on-off-on-off-off-off", 21),
          ("off-on-on-off-on-off-off-off", 22),
          ("on-on-on-off-on-off-off-off", 23),
          ("off-off-off-on-on-off-off-off", 24),
          ("on-off-off-on-on-off-off-off", 25),
          ("off-on-off-on-on-off-off-off", 26),
          ("on-on-off-on-on-off-off-off", 27),
          ("off-off-on-on-on-off-off-off", 28),
          ("on-off-on-on-on-off-off-off", 29),
          ("off-on-on-on-on-off-off-off", 30),
          ("on-on-on-on-on-off-off-off", 31),
          ("off-off-off-off-off-on-off-off", 32),
          ("on-off-off-off-off-on-off-off", 33),
          ("off-on-off-off-off-on-off-off", 34),
          ("on-on-off-off-off-on-off-off", 35),
          ("off-off-on-off-off-on-off-off", 36),
          ("on-off-on-off-off-on-off-off", 37),
          ("off-on-on-off-off-on-off-off", 38),
          ("on-on-on-off-off-on-off-off", 39),
          ("off-off-off-on-off-on-off-off", 40),
          ("on-off-off-on-off-on-off-off", 41),
          ("off-on-off-on-off-on-off-off", 42),
          ("on-on-off-on-off-on-off-off", 43),
          ("off-off-on-on-off-on-off-off", 44),
          ("on-off-on-on-off-on-off-off", 45),
          ("off-on-on-on-off-on-off-off", 46),
          ("on-on-on-on-off-on-off-off", 47),
          ("off-off-off-off-on-on-off-off", 48),
          ("on-off-off-off-on-on-off-off", 49),
          ("off-on-off-off-on-on-off-off", 50),
          ("on-on-off-off-on-on-off-off", 51),
          ("off-off-on-off-on-on-off-off", 52),
          ("on-off-on-off-on-on-off-off", 53),
          ("off-on-on-off-on-on-off-off", 54),
          ("on-on-on-off-on-on-off-off", 55),
          ("off-off-off-on-on-on-off-off", 56),
          ("on-off-off-on-on-on-off-off", 57),
          ("off-on-off-on-on-on-off-off", 58),
          ("on-on-off-on-on-on-off-off", 59),
          ("off-off-on-on-on-on-off-off", 60),
          ("on-off-on-on-on-on-off-off", 61),
          ("off-on-on-on-on-on-off-off", 62),
          ("on-on-on-on-on-on-off-off", 63),
          ("off-off-off-off-off-off-on-off", 64),
          ("on-off-off-off-off-off-on-off", 65),
          ("off-on-off-off-off-off-on-off", 66),
          ("on-on-off-off-off-off-on-off", 67),
          ("off-off-on-off-off-off-on-off", 68),
          ("on-off-on-off-off-off-on-off", 69),
          ("off-on-on-off-off-off-on-off", 70),
          ("on-on-on-off-off-off-on-off", 71),
          ("off-off-off-on-off-off-on-off", 72),
          ("on-off-off-on-off-off-on-off", 73),
          ("off-on-off-on-off-off-on-off", 74),
          ("on-on-off-on-off-off-on-off", 75),
          ("off-off-on-on-off-off-on-off", 76),
          ("on-off-on-on-off-off-on-off", 77),
          ("off-on-on-on-off-off-on-off", 78),
          ("on-on-on-on-off-off-on-off", 79),
          ("off-off-off-off-on-off-on-off", 80),
          ("on-off-off-off-on-off-on-off", 81),
          ("off-on-off-off-on-off-on-off", 82),
          ("on-on-off-off-on-off-on-off", 83),
          ("off-off-on-off-on-off-on-off", 84),
          ("on-off-on-off-on-off-on-off", 85),
          ("off-on-on-off-on-off-on-off", 86),
          ("on-on-on-off-on-off-on-off", 87),
          ("off-off-off-on-on-off-on-off", 88),
          ("on-off-off-on-on-off-on-off", 89),
          ("off-on-off-on-on-off-on-off", 90),
          ("on-on-off-on-on-off-on-off", 91),
          ("off-off-on-on-on-off-on-off", 92),
          ("on-off-on-on-on-off-on-off", 93),
          ("off-on-on-on-on-off-on-off", 94),
          ("on-on-on-on-on-off-on-off", 95),
          ("off-off-off-off-off-on-on-off", 96),
          ("on-off-off-off-off-on-on-off", 97),
          ("off-on-off-off-off-on-on-off", 98),
          ("on-on-off-off-off-on-on-off", 99),
          ("off-off-on-off-off-on-on-off", 100),
          ("on-off-on-off-off-on-on-off", 101),
          ("off-on-on-off-off-on-on-off", 102),
          ("on-on-on-off-off-on-on-off", 103),
          ("off-off-off-on-off-on-on-off", 104),
          ("on-off-off-on-off-on-on-off", 105),
          ("off-on-off-on-off-on-on-off", 106),
          ("on-on-off-on-off-on-on-off", 107),
          ("off-off-on-on-off-on-on-off", 108),
          ("on-off-on-on-off-on-on-off", 109),
          ("off-on-on-on-off-on-on-off", 110),
          ("on-on-on-on-off-on-on-off", 111),
          ("off-off-off-off-on-on-on-off", 112),
          ("on-off-off-off-on-on-on-off", 113),
          ("off-on-off-off-on-on-on-off", 114),
          ("on-on-off-off-on-on-on-off", 115),
          ("off-off-on-off-on-on-on-off", 116),
          ("on-off-on-off-on-on-on-off", 117),
          ("off-on-on-off-on-on-on-off", 118),
          ("on-on-on-off-on-on-on-off", 119),
          ("off-off-off-on-on-on-on-off", 120),
          ("on-off-off-on-on-on-on-off", 121),
          ("off-on-off-on-on-on-on-off", 122),
          ("on-on-off-on-on-on-on-off", 123),
          ("off-off-on-on-on-on-on-off", 124),
          ("on-off-on-on-on-on-on-off", 125),
          ("off-on-on-on-on-on-on-off", 126),
          ("on-on-on-on-on-on-on-off", 127),
          ("off-off-off-off-off-off-off-on", 128),
          ("on-off-off-off-off-off-off-on", 129),
          ("off-on-off-off-off-off-off-on", 130),
          ("on-on-off-off-off-off-off-on", 131),
          ("off-off-on-off-off-off-off-on", 132),
          ("on-off-on-off-off-off-off-on", 133),
          ("off-on-on-off-off-off-off-on", 134),
          ("on-on-on-off-off-off-off-on", 135),
          ("off-off-off-on-off-off-off-on", 136),
          ("on-off-off-on-off-off-off-on", 137),
          ("off-on-off-on-off-off-off-on", 138),
          ("on-on-off-on-off-off-off-on", 139),
          ("off-off-on-on-off-off-off-on", 140),
          ("on-off-on-on-off-off-off-on", 141),
          ("off-on-on-on-off-off-off-on", 142),
          ("on-on-on-on-off-off-off-on", 143),
          ("off-off-off-off-on-off-off-on", 144),
          ("on-off-off-off-on-off-off-on", 145),
          ("off-on-off-off-on-off-off-on", 146),
          ("on-on-off-off-on-off-off-on", 147),
          ("off-off-on-off-on-off-off-on", 148),
          ("on-off-on-off-on-off-off-on", 149),
          ("off-on-on-off-on-off-off-on", 150),
          ("on-on-on-off-on-off-off-on", 151),
          ("off-off-off-on-on-off-off-on", 152),
          ("on-off-off-on-on-off-off-on", 153),
          ("off-on-off-on-on-off-off-on", 154),
          ("on-on-off-on-on-off-off-on", 155),
          ("off-off-on-on-on-off-off-on", 156),
          ("on-off-on-on-on-off-off-on", 157),
          ("off-on-on-on-on-off-off-on", 158),
          ("on-on-on-on-on-off-off-on", 159),
          ("off-off-off-off-off-on-off-on", 160),
          ("on-off-off-off-off-on-off-on", 161),
          ("off-on-off-off-off-on-off-on", 162),
          ("on-on-off-off-off-on-off-on", 163),
          ("off-off-on-off-off-on-off-on", 164),
          ("on-off-on-off-off-on-off-on", 165),
          ("off-on-on-off-off-on-off-on", 166),
          ("on-on-on-off-off-on-off-on", 167),
          ("off-off-off-on-off-on-off-on", 168),
          ("on-off-off-on-off-on-off-on", 169),
          ("off-on-off-on-off-on-off-on", 170),
          ("on-on-off-on-off-on-off-on", 171),
          ("off-off-on-on-off-on-off-on", 172),
          ("on-off-on-on-off-on-off-on", 173),
          ("off-on-on-on-off-on-off-on", 174),
          ("on-on-on-on-off-on-off-on", 175),
          ("off-off-off-off-on-on-off-on", 176),
          ("on-off-off-off-on-on-off-on", 177),
          ("off-on-off-off-on-on-off-on", 178),
          ("on-on-off-off-on-on-off-on", 179),
          ("off-off-on-off-on-on-off-on", 180),
          ("on-off-on-off-on-on-off-on", 181),
          ("off-on-on-off-on-on-off-on", 182),
          ("on-on-on-off-on-on-off-on", 183),
          ("off-off-off-on-on-on-off-on", 184),
          ("on-off-off-on-on-on-off-on", 185),
          ("off-on-off-on-on-on-off-on", 186),
          ("on-on-off-on-on-on-off-on", 187),
          ("off-off-on-on-on-on-off-on", 188),
          ("on-off-on-on-on-on-off-on", 189),
          ("off-on-on-on-on-on-off-on", 190),
          ("on-on-on-on-on-on-off-on", 191),
          ("off-off-off-off-off-off-on-on", 192),
          ("on-off-off-off-off-off-on-on", 193),
          ("off-on-off-off-off-off-on-on", 194),
          ("on-on-off-off-off-off-on-on", 195),
          ("off-off-on-off-off-off-on-on", 196),
          ("on-off-on-off-off-off-on-on", 197),
          ("off-on-on-off-off-off-on-on", 198),
          ("on-on-on-off-off-off-on-on", 199),
          ("off-off-off-on-off-off-on-on", 200),
          ("on-off-off-on-off-off-on-on", 201),
          ("off-on-off-on-off-off-on-on", 202),
          ("on-on-off-on-off-off-on-on", 203),
          ("off-off-on-on-off-off-on-on", 204),
          ("on-off-on-on-off-off-on-on", 205),
          ("off-on-on-on-off-off-on-on", 206),
          ("on-on-on-on-off-off-on-on", 207),
          ("off-off-off-off-on-off-on-on", 208),
          ("on-off-off-off-on-off-on-on", 209),
          ("off-on-off-off-on-off-on-on", 210),
          ("on-on-off-off-on-off-on-on", 211),
          ("off-off-on-off-on-off-on-on", 212),
          ("on-off-on-off-on-off-on-on", 213),
          ("off-on-on-off-on-off-on-on", 214),
          ("on-on-on-off-on-off-on-on", 215),
          ("off-off-off-on-on-off-on-on", 216),
          ("on-off-off-on-on-off-on-on", 217),
          ("off-on-off-on-on-off-on-on", 218),
          ("on-on-off-on-on-off-on-on", 219),
          ("off-off-on-on-on-off-on-on", 220),
          ("on-off-on-on-on-off-on-on", 221),
          ("off-on-on-on-on-off-on-on", 222),
          ("on-on-on-on-on-off-on-on", 223),
          ("off-off-off-off-off-on-on-on", 224),
          ("on-off-off-off-off-on-on-on", 225),
          ("off-on-off-off-off-on-on-on", 226),
          ("on-on-off-off-off-on-on-on", 227),
          ("off-off-on-off-off-on-on-on", 228),
          ("on-off-on-off-off-on-on-on", 229),
          ("off-on-on-off-off-on-on-on", 230),
          ("on-on-on-off-off-on-on-on", 231),
          ("off-off-off-on-off-on-on-on", 232),
          ("on-off-off-on-off-on-on-on", 233),
          ("off-on-off-on-off-on-on-on", 234),
          ("on-on-off-on-off-on-on-on", 235),
          ("off-off-on-on-off-on-on-on", 236),
          ("on-off-on-on-off-on-on-on", 237),
          ("off-on-on-on-off-on-on-on", 238),
          ("on-on-on-on-off-on-on-on", 239),
          ("off-off-off-off-on-on-on-on", 240),
          ("on-off-off-off-on-on-on-on", 241),
          ("off-on-off-off-on-on-on-on", 242),
          ("on-on-off-off-on-on-on-on", 243),
          ("off-off-on-off-on-on-on-on", 244),
          ("on-off-on-off-on-on-on-on", 245),
          ("off-on-on-off-on-on-on-on", 246),
          ("on-on-on-off-on-on-on-on", 247),
          ("off-off-off-on-on-on-on-on", 248),
          ("on-off-off-on-on-on-on-on", 249),
          ("off-on-off-on-on-on-on-on", 250),
          ("on-on-off-on-on-on-on-on", 251),
          ("off-off-on-on-on-on-on-on", 252),
          ("on-off-on-on-on-on-on-on", 253),
          ("off-on-on-on-on-on-on-on", 254),
          ("on-on-on-on-on-on-on-on", 255))
    )



class ControlModeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("charge", 0),
          ("loadControl", 1),
          ("diversion", 2),
          ("lighting", 3))
    )



class ControlStateEnum(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("nightCheck", 1),
          ("disconnect", 2),
          ("night", 3),
          ("fault", 4),
          ("bulk", 5),
          ("absorption", 6),
          ("float", 7),
          ("equalize", 8))
    )



class LoadStateEnum(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("normal", 1),
          ("lvdWarning", 2),
          ("lvd", 3),
          ("fault", 4),
          ("disconnect", 5),
          ("lvdWarning1", 6),
          ("overrideLvd", 7),
          ("equalize", 8))
    )



class AlarmsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rtsOpen", 0),
          ("rtsShorted", 1),
          ("rtsDisconnected", 2),
          ("heatsinkTempSensorOpen", 3),
          ("heatsinkTempSensorShorted", 4),
          ("tristarHot", 5),
          ("currentLimit", 6),
          ("currentOffset", 7),
          ("batterySense", 8),
          ("batterySenseDisconnected", 9),
          ("uncalibrated", 10),
          ("rtsMiswire", 11),
          ("highVoltageDisconnect", 12),
          ("diversionLoadNearMax", 13),
          ("systemMiswire", 14),
          ("mosfetSOpen", 15),
          ("p12VoltageReferenceOff", 16),
          ("loadDisconnectState", 17),
          ("alarm19Undefined", 18),
          ("alarm20Undefined", 19),
          ("alarm21Undefined", 20),
          ("alarm22Undefined", 21),
          ("alarm23Undefined", 22),
          ("alarm24Undefined", 23))
    )


class FaultsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("externalShort", 0),
          ("overcurrent", 1),
          ("mosfetSShorted", 2),
          ("softwareFault", 3),
          ("highVoltageDisconnect", 4),
          ("tristarHot", 5),
          ("dipSwitchChange", 6),
          ("customSettingsEdit", 7),
          ("reset", 8),
          ("systemMiswire", 9),
          ("rtsShorted", 10),
          ("rtsDisconnected", 11),
          ("fault12Undefined", 12),
          ("fault13Undefined", 13),
          ("fault14Undefined", 14),
          ("fault15Undefined", 15))
    )


# MIB Managed Objects in the order of their OIDs



class _SubModel_Type(DisplayString):
    """Custom type subModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SubModel_Type.__name__ = "DisplayString"
_SubModel_Object = MibScalar
subModel = _SubModel_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 1),
    _SubModel_Type()
)
subModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subModel.setStatus("current")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _DeviceVersion_Type(DisplayString):
    """Custom type deviceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DeviceVersion_Type.__name__ = "DisplayString"
_DeviceVersion_Object = MibScalar
deviceVersion = _DeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 3),
    _DeviceVersion_Type()
)
deviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVersion.setStatus("current")
_BatteryVoltage_Type = Unsigned32
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 30),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")
_BatterySenseVoltage_Type = Unsigned32
_BatterySenseVoltage_Object = MibScalar
batterySenseVoltage = _BatterySenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 31),
    _BatterySenseVoltage_Type()
)
batterySenseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySenseVoltage.setStatus("current")
_ArrayloadVoltage_Type = Unsigned32
_ArrayloadVoltage_Object = MibScalar
arrayloadVoltage = _ArrayloadVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 32),
    _ArrayloadVoltage_Type()
)
arrayloadVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayloadVoltage.setStatus("current")
_ChargeCurrent_Type = Unsigned32
_ChargeCurrent_Object = MibScalar
chargeCurrent = _ChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 33),
    _ChargeCurrent_Type()
)
chargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeCurrent.setStatus("current")
_LoadCurrent_Type = Unsigned32
_LoadCurrent_Object = MibScalar
loadCurrent = _LoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 34),
    _LoadCurrent_Type()
)
loadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCurrent.setStatus("current")
_BatteryVoltageSlow_Type = Unsigned32
_BatteryVoltageSlow_Object = MibScalar
batteryVoltageSlow = _BatteryVoltageSlow_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 35),
    _BatteryVoltageSlow_Type()
)
batteryVoltageSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageSlow.setStatus("current")
_HeatsinkTemperature_Type = Integer32
_HeatsinkTemperature_Object = MibScalar
heatsinkTemperature = _HeatsinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 36),
    _HeatsinkTemperature_Type()
)
heatsinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatsinkTemperature.setStatus("current")
_BatteryTemperature_Type = Integer32
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 37),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("current")
_TargetVoltage_Type = Unsigned32
_TargetVoltage_Object = MibScalar
targetVoltage = _TargetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 38),
    _TargetVoltage_Type()
)
targetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetVoltage.setStatus("current")
_AhResettable_Type = Unsigned32
_AhResettable_Object = MibScalar
ahResettable = _AhResettable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 39),
    _AhResettable_Type()
)
ahResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahResettable.setStatus("current")
_AhTotal_Type = Unsigned32
_AhTotal_Object = MibScalar
ahTotal = _AhTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 40),
    _AhTotal_Type()
)
ahTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTotal.setStatus("current")
_Hourmeter_Type = Unsigned32
_Hourmeter_Object = MibScalar
hourmeter = _Hourmeter_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 41),
    _Hourmeter_Type()
)
hourmeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourmeter.setStatus("current")
_Alarms_Type = AlarmsBitfield
_Alarms_Object = MibScalar
alarms = _Alarms_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 42),
    _Alarms_Type()
)
alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarms.setStatus("current")
_Faults_Type = FaultsBitfield
_Faults_Object = MibScalar
faults = _Faults_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 43),
    _Faults_Type()
)
faults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faults.setStatus("current")
_SettingsSwitches_Type = SettingsSwitchesEnum
_SettingsSwitches_Object = MibScalar
settingsSwitches = _SettingsSwitches_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 44),
    _SettingsSwitches_Type()
)
settingsSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    settingsSwitches.setStatus("current")
_ControlMode_Type = ControlModeEnum
_ControlMode_Object = MibScalar
controlMode = _ControlMode_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 45),
    _ControlMode_Type()
)
controlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlMode.setStatus("current")
_ControlState_Type = ControlStateEnum
_ControlState_Object = MibScalar
controlState = _ControlState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 46),
    _ControlState_Type()
)
controlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlState.setStatus("current")
_LoadState_Type = LoadStateEnum
_LoadState_Object = MibScalar
loadState = _LoadState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 47),
    _LoadState_Type()
)
loadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadState.setStatus("current")
_PwmDutyCycle_Type = Unsigned32
_PwmDutyCycle_Object = MibScalar
pwmDutyCycle = _PwmDutyCycle_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 48),
    _PwmDutyCycle_Type()
)
pwmDutyCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwmDutyCycle.setStatus("current")
_KilowattHours_Type = Unsigned32
_KilowattHours_Object = MibScalar
kilowattHours = _KilowattHours_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 49),
    _KilowattHours_Type()
)
kilowattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kilowattHours.setStatus("current")
_MinimumBatteryVoltage_Type = Unsigned32
_MinimumBatteryVoltage_Object = MibScalar
minimumBatteryVoltage = _MinimumBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 50),
    _MinimumBatteryVoltage_Type()
)
minimumBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minimumBatteryVoltage.setStatus("current")
_MaximumBatteryVoltage_Type = Unsigned32
_MaximumBatteryVoltage_Object = MibScalar
maximumBatteryVoltage = _MaximumBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 8, 51),
    _MaximumBatteryVoltage_Type()
)
maximumBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumBatteryVoltage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRISTAR",
    **{"SettingsSwitchesEnum": SettingsSwitchesEnum,
       "ControlModeEnum": ControlModeEnum,
       "ControlStateEnum": ControlStateEnum,
       "LoadStateEnum": LoadStateEnum,
       "AlarmsBitfield": AlarmsBitfield,
       "FaultsBitfield": FaultsBitfield,
       "tristar": tristar,
       "subModel": subModel,
       "serialNumber": serialNumber,
       "deviceVersion": deviceVersion,
       "batteryVoltage": batteryVoltage,
       "batterySenseVoltage": batterySenseVoltage,
       "arrayloadVoltage": arrayloadVoltage,
       "chargeCurrent": chargeCurrent,
       "loadCurrent": loadCurrent,
       "batteryVoltageSlow": batteryVoltageSlow,
       "heatsinkTemperature": heatsinkTemperature,
       "batteryTemperature": batteryTemperature,
       "targetVoltage": targetVoltage,
       "ahResettable": ahResettable,
       "ahTotal": ahTotal,
       "hourmeter": hourmeter,
       "alarms": alarms,
       "faults": faults,
       "settingsSwitches": settingsSwitches,
       "controlMode": controlMode,
       "controlState": controlState,
       "loadState": loadState,
       "pwmDutyCycle": pwmDutyCycle,
       "kilowattHours": kilowattHours,
       "minimumBatteryVoltage": minimumBatteryVoltage,
       "maximumBatteryVoltage": maximumBatteryVoltage}
)
