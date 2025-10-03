# SNMP MIB module (TRISTAR-MPPT-600V) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\morningstar\TRISTAR-MPPT-600V
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:58 2025
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

tristarmppt600v = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33333, 7)
)
if mibBuilder.loadTexts:
    tristarmppt600v.setRevisions(
        ("2019-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChargeStateEnum(TextualConvention, Integer32):
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
        *(("start", 0),
          ("nightCheck", 1),
          ("disconnect", 2),
          ("night", 3),
          ("fault", 4),
          ("mppt", 5),
          ("absorption", 6),
          ("float", 7),
          ("equalize", 8),
          ("slave", 9),
          ("fixed", 10))
    )



class LedStateEnum(TextualConvention, Integer32):
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
              11,
              12,
              13,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ledStart", 0),
          ("ledStart2", 1),
          ("ledBranch", 2),
          ("greenFlashingFast", 3),
          ("greenFlashingSlow", 4),
          ("greenFlashing", 5),
          ("green", 6),
          ("greenYellow", 7),
          ("yellow", 8),
          ("yellowRed", 9),
          ("red", 11),
          ("r-y-gSequencing", 12),
          ("r-y-GSequencing", 13),
          ("r-GSequencing", 16),
          ("r-y-Y-gSequencing", 17),
          ("g-y-rFlashing", 18),
          ("g-y-rFlashing1", 19))
    )



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



class FaultsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("overcurrent", 0),
          ("fetShort", 1),
          ("softwareFault", 2),
          ("batteryHvd", 3),
          ("arrayHvd", 4),
          ("dipSwitchChange", 5),
          ("customSettingsEdit", 6),
          ("rtsShorted", 7),
          ("rtsDisconnected", 8),
          ("eepromRetryLimit", 9),
          ("controllerWasReset", 10),
          ("chargeSlaveControlTimeout", 11),
          ("rs232SerialToMeterBridge", 12),
          ("batteryLvd", 13),
          ("fault14Undefined", 14),
          ("powerboardCommunicationFault", 15),
          ("fault16Software", 16),
          ("fault17Software", 17),
          ("fault18Software", 18),
          ("fault19Software", 19),
          ("fault20Software", 20),
          ("fault21Software", 21),
          ("fpgaVersion", 22),
          ("currentSensorReferenceOutOfRange", 23),
          ("ia-refSlaveModeTimeout", 24),
          ("blockbusBoot", 25),
          ("hscommMaster", 26),
          ("hscomm", 27),
          ("slave", 28),
          ("fault29Undefined", 29),
          ("fault30Undefined", 30),
          ("fault31Undefined", 31))
    )


class FaultsDailyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("overcurrent", 0),
          ("fetShort", 1),
          ("softwareFault", 2),
          ("batteryHvd", 3),
          ("arrayHvd", 4),
          ("dipSwitchChange", 5),
          ("customSettingsEdit", 6),
          ("rtsShorted", 7),
          ("rtsDisconnected", 8),
          ("eepromRetryLimit", 9),
          ("controllerWasReset", 10),
          ("chargeSlaveControlTimeout", 11),
          ("rs232SerialToMeterBridge", 12),
          ("batteryLvd", 13),
          ("fault14Undefined", 14),
          ("powerboardCommunicationFault", 15),
          ("fault16Software", 16),
          ("fault17Software", 17),
          ("fault18Software", 18),
          ("fault19Software", 19),
          ("fault20Software", 20),
          ("fault21Software", 21),
          ("fpgaVersion", 22),
          ("currentSensorReferenceOutOfRange", 23),
          ("ia-refSlaveModeTimeout", 24),
          ("blockbusBoot", 25),
          ("hscommMaster", 26),
          ("hscomm", 27),
          ("slave", 28),
          ("fault29Undefined", 29),
          ("fault30Undefined", 30),
          ("fault31Undefined", 31))
    )


class AlarmsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rtsOpen", 0),
          ("rtsShorted", 1),
          ("rtsDisconnected", 2),
          ("heatsinkTempSensorOpen", 3),
          ("heatsinkTempSensorShorted", 4),
          ("highTemperatureCurrentLimit", 5),
          ("currentLimit", 6),
          ("currentOffset", 7),
          ("batterySense", 8),
          ("batterySenseDisconnected", 9),
          ("uncalibrated", 10),
          ("rtsMiswire", 11),
          ("highVoltageDisconnect", 12),
          ("undefined", 13),
          ("systemMiswire", 14),
          ("mosfetSOpen", 15),
          ("p12VoltageOutOfRange", 16),
          ("highArrayVCurrentLimit", 17),
          ("maxAdcValueReached", 18),
          ("controllerWasReset", 19),
          ("alarm21Internal", 20),
          ("p3VoltageOutOfRange", 21),
          ("derateLimit", 22),
          ("arrayCurrentOffset", 23),
          ("ee-i2cRetryLimit", 24),
          ("ethernetAlarm", 25),
          ("lvd", 26),
          ("software", 27),
          ("fp12VoltageOutOfRange", 28),
          ("extflashFault", 29),
          ("slaveControlFault", 30),
          ("alarm32Undefined", 31))
    )


class AlarmsDailyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rtsOpen", 0),
          ("rtsShorted", 1),
          ("rtsDisconnected", 2),
          ("heatsinkTempSensorOpen", 3),
          ("heatsinkTempSensorShorted", 4),
          ("highTemperatureCurrentLimit", 5),
          ("currentLimit", 6),
          ("currentOffset", 7),
          ("batterySense", 8),
          ("batterySenseDisconnected", 9),
          ("uncalibrated", 10),
          ("rtsMiswire", 11),
          ("highVoltageDisconnect", 12),
          ("undefined", 13),
          ("systemMiswire", 14),
          ("mosfetSOpen", 15),
          ("p12VoltageOutOfRange", 16),
          ("highArrayVCurrentLimit", 17),
          ("maxAdcValueReached", 18),
          ("controllerWasReset", 19),
          ("alarm21Internal", 20),
          ("p3VoltageOutOfRange", 21),
          ("derateLimit", 22),
          ("arrayCurrentOffset", 23),
          ("ee-i2cRetryLimit", 24),
          ("ethernetAlarm", 25),
          ("lvd", 26),
          ("software", 27),
          ("fp12VoltageOutOfRange", 28),
          ("extflashFault", 29),
          ("slaveControlFault", 30),
          ("alarm32Undefined", 31))
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
    (1, 3, 6, 1, 4, 1, 33333, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 33333, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 33333, 7, 3),
    _DeviceVersion_Type()
)
deviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVersion.setStatus("current")


class _ArrayVoltage_Type(DisplayString):
    """Custom type arrayVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVoltage_Type.__name__ = "DisplayString"
_ArrayVoltage_Object = MibScalar
arrayVoltage = _ArrayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 30),
    _ArrayVoltage_Type()
)
arrayVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVoltage.setStatus("current")


class _ArrayCurrent_Type(DisplayString):
    """Custom type arrayCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayCurrent_Type.__name__ = "DisplayString"
_ArrayCurrent_Object = MibScalar
arrayCurrent = _ArrayCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 31),
    _ArrayCurrent_Type()
)
arrayCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayCurrent.setStatus("current")


class _InputPower_Type(DisplayString):
    """Custom type inputPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputPower_Type.__name__ = "DisplayString"
_InputPower_Object = MibScalar
inputPower = _InputPower_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 32),
    _InputPower_Type()
)
inputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputPower.setStatus("current")


class _ArrayPmaxLastSweep_Type(DisplayString):
    """Custom type arrayPmaxLastSweep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayPmaxLastSweep_Type.__name__ = "DisplayString"
_ArrayPmaxLastSweep_Object = MibScalar
arrayPmaxLastSweep = _ArrayPmaxLastSweep_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 33),
    _ArrayPmaxLastSweep_Type()
)
arrayPmaxLastSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayPmaxLastSweep.setStatus("current")


class _ArrayVmpLastSweep_Type(DisplayString):
    """Custom type arrayVmpLastSweep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVmpLastSweep_Type.__name__ = "DisplayString"
_ArrayVmpLastSweep_Object = MibScalar
arrayVmpLastSweep = _ArrayVmpLastSweep_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 34),
    _ArrayVmpLastSweep_Type()
)
arrayVmpLastSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVmpLastSweep.setStatus("current")


class _ArrayVocLastSweep_Type(DisplayString):
    """Custom type arrayVocLastSweep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVocLastSweep_Type.__name__ = "DisplayString"
_ArrayVocLastSweep_Object = MibScalar
arrayVocLastSweep = _ArrayVocLastSweep_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 35),
    _ArrayVocLastSweep_Type()
)
arrayVocLastSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVocLastSweep.setStatus("current")


class _BatteryVoltage_Type(DisplayString):
    """Custom type batteryVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryVoltage_Type.__name__ = "DisplayString"
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 36),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("current")


class _BatteryVoltageSlow_Type(DisplayString):
    """Custom type batteryVoltageSlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryVoltageSlow_Type.__name__ = "DisplayString"
_BatteryVoltageSlow_Object = MibScalar
batteryVoltageSlow = _BatteryVoltageSlow_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 37),
    _BatteryVoltageSlow_Type()
)
batteryVoltageSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageSlow.setStatus("current")


class _BatteryTerminalVoltage_Type(DisplayString):
    """Custom type batteryTerminalVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTerminalVoltage_Type.__name__ = "DisplayString"
_BatteryTerminalVoltage_Object = MibScalar
batteryTerminalVoltage = _BatteryTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 38),
    _BatteryTerminalVoltage_Type()
)
batteryTerminalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTerminalVoltage.setStatus("current")


class _BatterySenseVoltage_Type(DisplayString):
    """Custom type batterySenseVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatterySenseVoltage_Type.__name__ = "DisplayString"
_BatterySenseVoltage_Object = MibScalar
batterySenseVoltage = _BatterySenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 39),
    _BatterySenseVoltage_Type()
)
batterySenseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySenseVoltage.setStatus("current")


class _MinBatteryVoltageSlow_Type(DisplayString):
    """Custom type minBatteryVoltageSlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MinBatteryVoltageSlow_Type.__name__ = "DisplayString"
_MinBatteryVoltageSlow_Object = MibScalar
minBatteryVoltageSlow = _MinBatteryVoltageSlow_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 40),
    _MinBatteryVoltageSlow_Type()
)
minBatteryVoltageSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minBatteryVoltageSlow.setStatus("current")


class _MaxBatteryVoltageSlow_Type(DisplayString):
    """Custom type maxBatteryVoltageSlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MaxBatteryVoltageSlow_Type.__name__ = "DisplayString"
_MaxBatteryVoltageSlow_Object = MibScalar
maxBatteryVoltageSlow = _MaxBatteryVoltageSlow_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 41),
    _MaxBatteryVoltageSlow_Type()
)
maxBatteryVoltageSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBatteryVoltageSlow.setStatus("current")


class _BatteryCurrent_Type(DisplayString):
    """Custom type batteryCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryCurrent_Type.__name__ = "DisplayString"
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 42),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("current")


class _BatteryCurrentSlow_Type(DisplayString):
    """Custom type batteryCurrentSlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryCurrentSlow_Type.__name__ = "DisplayString"
_BatteryCurrentSlow_Object = MibScalar
batteryCurrentSlow = _BatteryCurrentSlow_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 43),
    _BatteryCurrentSlow_Type()
)
batteryCurrentSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentSlow.setStatus("current")


class _OutputPower_Type(DisplayString):
    """Custom type outputPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OutputPower_Type.__name__ = "DisplayString"
_OutputPower_Object = MibScalar
outputPower = _OutputPower_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 44),
    _OutputPower_Type()
)
outputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputPower.setStatus("current")


class _TargetRegulationVoltage_Type(DisplayString):
    """Custom type targetRegulationVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TargetRegulationVoltage_Type.__name__ = "DisplayString"
_TargetRegulationVoltage_Object = MibScalar
targetRegulationVoltage = _TargetRegulationVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 45),
    _TargetRegulationVoltage_Type()
)
targetRegulationVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetRegulationVoltage.setStatus("current")
_ChargeState_Type = ChargeStateEnum
_ChargeState_Object = MibScalar
chargeState = _ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 46),
    _ChargeState_Type()
)
chargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeState.setStatus("current")


class _RtsTemperature_Type(DisplayString):
    """Custom type rtsTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RtsTemperature_Type.__name__ = "DisplayString"
_RtsTemperature_Object = MibScalar
rtsTemperature = _RtsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 47),
    _RtsTemperature_Type()
)
rtsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsTemperature.setStatus("current")


class _BatteryTemperature_Type(DisplayString):
    """Custom type batteryTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTemperature_Type.__name__ = "DisplayString"
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 48),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("current")


class _HeatsinkTemperature_Type(DisplayString):
    """Custom type heatsinkTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HeatsinkTemperature_Type.__name__ = "DisplayString"
_HeatsinkTemperature_Object = MibScalar
heatsinkTemperature = _HeatsinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 49),
    _HeatsinkTemperature_Type()
)
heatsinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatsinkTemperature.setStatus("current")


class _AhChargeResetable_Type(DisplayString):
    """Custom type ahChargeResetable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AhChargeResetable_Type.__name__ = "DisplayString"
_AhChargeResetable_Object = MibScalar
ahChargeResetable = _AhChargeResetable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 50),
    _AhChargeResetable_Type()
)
ahChargeResetable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahChargeResetable.setStatus("current")


class _AhChargeTotal_Type(DisplayString):
    """Custom type ahChargeTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AhChargeTotal_Type.__name__ = "DisplayString"
_AhChargeTotal_Object = MibScalar
ahChargeTotal = _AhChargeTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 51),
    _AhChargeTotal_Type()
)
ahChargeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahChargeTotal.setStatus("current")


class _KwhChargeResetable_Type(DisplayString):
    """Custom type kwhChargeResetable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_KwhChargeResetable_Type.__name__ = "DisplayString"
_KwhChargeResetable_Object = MibScalar
kwhChargeResetable = _KwhChargeResetable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 52),
    _KwhChargeResetable_Type()
)
kwhChargeResetable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kwhChargeResetable.setStatus("current")


class _KwhChargeTotal_Type(DisplayString):
    """Custom type kwhChargeTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_KwhChargeTotal_Type.__name__ = "DisplayString"
_KwhChargeTotal_Object = MibScalar
kwhChargeTotal = _KwhChargeTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 53),
    _KwhChargeTotal_Type()
)
kwhChargeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kwhChargeTotal.setStatus("current")
_LedState_Type = LedStateEnum
_LedState_Object = MibScalar
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 54),
    _LedState_Type()
)
ledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledState.setStatus("current")
_Faults_Type = FaultsBitfield
_Faults_Object = MibScalar
faults = _Faults_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 55),
    _Faults_Type()
)
faults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faults.setStatus("current")
_FaultsDaily_Type = FaultsDailyBitfield
_FaultsDaily_Object = MibScalar
faultsDaily = _FaultsDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 56),
    _FaultsDaily_Type()
)
faultsDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultsDaily.setStatus("current")
_Alarms_Type = AlarmsBitfield
_Alarms_Object = MibScalar
alarms = _Alarms_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 57),
    _Alarms_Type()
)
alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarms.setStatus("current")
_AlarmsDaily_Type = AlarmsDailyBitfield
_AlarmsDaily_Object = MibScalar
alarmsDaily = _AlarmsDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 58),
    _AlarmsDaily_Type()
)
alarmsDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmsDaily.setStatus("current")
_Hourmeter_Type = Unsigned32
_Hourmeter_Object = MibScalar
hourmeter = _Hourmeter_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 59),
    _Hourmeter_Type()
)
hourmeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourmeter.setStatus("current")
_SettingsSwitches_Type = SettingsSwitchesEnum
_SettingsSwitches_Object = MibScalar
settingsSwitches = _SettingsSwitches_Object(
    (1, 3, 6, 1, 4, 1, 33333, 7, 60),
    _SettingsSwitches_Type()
)
settingsSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    settingsSwitches.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRISTAR-MPPT-600V",
    **{"ChargeStateEnum": ChargeStateEnum,
       "LedStateEnum": LedStateEnum,
       "SettingsSwitchesEnum": SettingsSwitchesEnum,
       "FaultsBitfield": FaultsBitfield,
       "FaultsDailyBitfield": FaultsDailyBitfield,
       "AlarmsBitfield": AlarmsBitfield,
       "AlarmsDailyBitfield": AlarmsDailyBitfield,
       "tristarmppt600v": tristarmppt600v,
       "subModel": subModel,
       "serialNumber": serialNumber,
       "deviceVersion": deviceVersion,
       "arrayVoltage": arrayVoltage,
       "arrayCurrent": arrayCurrent,
       "inputPower": inputPower,
       "arrayPmaxLastSweep": arrayPmaxLastSweep,
       "arrayVmpLastSweep": arrayVmpLastSweep,
       "arrayVocLastSweep": arrayVocLastSweep,
       "batteryVoltage": batteryVoltage,
       "batteryVoltageSlow": batteryVoltageSlow,
       "batteryTerminalVoltage": batteryTerminalVoltage,
       "batterySenseVoltage": batterySenseVoltage,
       "minBatteryVoltageSlow": minBatteryVoltageSlow,
       "maxBatteryVoltageSlow": maxBatteryVoltageSlow,
       "batteryCurrent": batteryCurrent,
       "batteryCurrentSlow": batteryCurrentSlow,
       "outputPower": outputPower,
       "targetRegulationVoltage": targetRegulationVoltage,
       "chargeState": chargeState,
       "rtsTemperature": rtsTemperature,
       "batteryTemperature": batteryTemperature,
       "heatsinkTemperature": heatsinkTemperature,
       "ahChargeResetable": ahChargeResetable,
       "ahChargeTotal": ahChargeTotal,
       "kwhChargeResetable": kwhChargeResetable,
       "kwhChargeTotal": kwhChargeTotal,
       "ledState": ledState,
       "faults": faults,
       "faultsDaily": faultsDaily,
       "alarms": alarms,
       "alarmsDaily": alarmsDaily,
       "hourmeter": hourmeter,
       "settingsSwitches": settingsSwitches}
)
