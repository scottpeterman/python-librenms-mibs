# SNMP MIB module (PROSTAR-MPPT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\morningstar\PROSTAR-MPPT
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:52 2025
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

prostarMppt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33333, 5)
)
if mibBuilder.loadTexts:
    prostarMppt.setRevisions(
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
          ("bulkMppt", 5),
          ("absorption", 6),
          ("float", 7),
          ("equalize", 8),
          ("slave", 9),
          ("fixed", 10))
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
          ("normalOff", 6),
          ("override", 7),
          ("notUsed", 8))
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("ledStart", 0),
          ("ledStart2", 1),
          ("ledBranch", 2),
          ("equalizeFastGreen", 3),
          ("floatSlowGreen", 4),
          ("absorptionFlashingGreen", 5),
          ("green", 6),
          ("green-yellow", 7),
          ("yellow", 8),
          ("yellow-red", 9),
          ("flashingRed", 10),
          ("red", 11),
          ("r-y-gError", 12),
          ("ry-gError", 13),
          ("rg-yError", 14),
          ("r-yError", 15),
          ("r-gError", 16),
          ("ry-gyError", 17),
          ("gyrFlashingError", 18),
          ("gyrX2", 19),
          ("ledOff", 20))
    )



class ArrayFaultsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("overcurrent", 0),
          ("mosfetSShorted", 1),
          ("software", 2),
          ("batteryHvd", 3),
          ("arrayHvd", 4),
          ("customSettingsEdit", 5),
          ("rtsShorted", 6),
          ("rtsNoLongerValid", 7),
          ("localTempSensorDamaged", 8),
          ("batteryLowVoltageDisconnect", 9),
          ("slaveTimeout", 10),
          ("dipSwitchChanged", 11),
          ("fault13Undefined", 12),
          ("fault14Undefined", 13),
          ("fault15Undefined", 14),
          ("fault16Undefined", 15))
    )


class LoadFaultsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("externalShortCircuit", 0),
          ("overcurrent", 1),
          ("mosfetShorted", 2),
          ("software", 3),
          ("loadHvd", 4),
          ("highTempDisconnect", 5),
          ("dipSwitchChanged", 6),
          ("customSettingsEdit", 7))
    )


class AlarmsBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rtsOpen", 0),
          ("rtsShorted", 1),
          ("rtsDisconnected", 2),
          ("heatsinkTempSensorOpen", 3),
          ("heatsinkTempSensorShorted", 4),
          ("heatsinkTempLimit", 5),
          ("inductorTempSensorOpen", 6),
          ("inductorTempSensorShorted", 7),
          ("inductorTempLimit", 8),
          ("currentLimit", 9),
          ("currentMeasurementError", 10),
          ("batterySenseOutOfRange", 11),
          ("batterySenseDisconnected", 12),
          ("uncalibrated", 13),
          ("tb5v", 14),
          ("fp10SupplyOutOfRange", 15),
          ("unused", 16),
          ("mosfetOpen", 17),
          ("arrayCurrentOffset", 18),
          ("loadCurrentOffset", 19),
          ("p33SupplyOutOfRange", 20),
          ("p12SupplyOutOfRange", 21),
          ("hightInputVoltageLimit", 22),
          ("controllerReset", 23),
          ("loadLvd", 24),
          ("logTimeout", 25),
          ("eepromAccessFailure", 26))
    )


class ArrayFaultsDailyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("overcurrent", 0),
          ("mosfetSShorted", 1),
          ("software", 2),
          ("batteryHvd", 3),
          ("arrayHvd", 4),
          ("customSettingsEdit", 5),
          ("rtsShorted", 6),
          ("rtsNoLongerValid", 7),
          ("localTempSensorDamaged", 8),
          ("batteryLowVoltageDisconnect", 9),
          ("slaveTimeout", 10),
          ("dipSwitchChanged", 11),
          ("fault13Undefined", 12),
          ("fault14Undefined", 13),
          ("fault15Undefined", 14),
          ("fault16Undefined", 15))
    )


class LoadFaultsDailyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("externalShortCircuit", 0),
          ("overcurrent", 1),
          ("mosfetShorted", 2),
          ("software", 3),
          ("loadHvd", 4),
          ("highTempDisconnect", 5),
          ("dipSwitchChanged", 6),
          ("customSettingsEdit", 7))
    )


class AlarmsDailyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rtsOpen", 0),
          ("rtsShorted", 1),
          ("rtsDisconnected", 2),
          ("heatsinkTempSensorOpen", 3),
          ("heatsinkTempSensorShorted", 4),
          ("heatsinkTempLimit", 5),
          ("inductorTempSensorOpen", 6),
          ("inductorTempSensorShorted", 7),
          ("inductorTempLimit", 8),
          ("currentLimit", 9),
          ("currentMeasurementError", 10),
          ("batterySenseOutOfRange", 11),
          ("batterySenseDisconnected", 12),
          ("uncalibrated", 13),
          ("tb5v", 14),
          ("fp10SupplyOutOfRange", 15),
          ("unused", 16),
          ("mosfetOpen", 17),
          ("arrayCurrentOffset", 18),
          ("loadCurrentOffset", 19),
          ("p33SupplyOutOfRange", 20),
          ("p12SupplyOutOfRange", 21),
          ("hightInputVoltageLimit", 22),
          ("controllerReset", 23),
          ("loadLvd", 24),
          ("logTimeout", 25),
          ("eepromAccessFailure", 26))
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
    (1, 3, 6, 1, 4, 1, 33333, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 33333, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 33333, 5, 3),
    _DeviceVersion_Type()
)
deviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVersion.setStatus("current")


class _BatteryTerminalVoltage_Type(DisplayString):
    """Custom type batteryTerminalVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTerminalVoltage_Type.__name__ = "DisplayString"
_BatteryTerminalVoltage_Object = MibScalar
batteryTerminalVoltage = _BatteryTerminalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 30),
    _BatteryTerminalVoltage_Type()
)
batteryTerminalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTerminalVoltage.setStatus("current")


class _ArrayVoltage_Type(DisplayString):
    """Custom type arrayVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVoltage_Type.__name__ = "DisplayString"
_ArrayVoltage_Object = MibScalar
arrayVoltage = _ArrayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 31),
    _ArrayVoltage_Type()
)
arrayVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVoltage.setStatus("current")


class _LoadVoltage_Type(DisplayString):
    """Custom type loadVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadVoltage_Type.__name__ = "DisplayString"
_LoadVoltage_Object = MibScalar
loadVoltage = _LoadVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 32),
    _LoadVoltage_Type()
)
loadVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadVoltage.setStatus("current")


class _ChargeCurrent_Type(DisplayString):
    """Custom type chargeCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChargeCurrent_Type.__name__ = "DisplayString"
_ChargeCurrent_Object = MibScalar
chargeCurrent = _ChargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 33),
    _ChargeCurrent_Type()
)
chargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeCurrent.setStatus("current")


class _LoadCurrent_Type(DisplayString):
    """Custom type loadCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadCurrent_Type.__name__ = "DisplayString"
_LoadCurrent_Object = MibScalar
loadCurrent = _LoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 34),
    _LoadCurrent_Type()
)
loadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCurrent.setStatus("current")


class _BatteryCurrentNet_Type(DisplayString):
    """Custom type batteryCurrentNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryCurrentNet_Type.__name__ = "DisplayString"
_BatteryCurrentNet_Object = MibScalar
batteryCurrentNet = _BatteryCurrentNet_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 35),
    _BatteryCurrentNet_Type()
)
batteryCurrentNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentNet.setStatus("current")


class _BatterySenseVoltage_Type(DisplayString):
    """Custom type batterySenseVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatterySenseVoltage_Type.__name__ = "DisplayString"
_BatterySenseVoltage_Object = MibScalar
batterySenseVoltage = _BatterySenseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 36),
    _BatterySenseVoltage_Type()
)
batterySenseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySenseVoltage.setStatus("current")


class _MeterbusVoltage_Type(DisplayString):
    """Custom type meterbusVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MeterbusVoltage_Type.__name__ = "DisplayString"
_MeterbusVoltage_Object = MibScalar
meterbusVoltage = _MeterbusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 37),
    _MeterbusVoltage_Type()
)
meterbusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meterbusVoltage.setStatus("current")


class _HeatsinkTemperature_Type(DisplayString):
    """Custom type heatsinkTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HeatsinkTemperature_Type.__name__ = "DisplayString"
_HeatsinkTemperature_Object = MibScalar
heatsinkTemperature = _HeatsinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 38),
    _HeatsinkTemperature_Type()
)
heatsinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatsinkTemperature.setStatus("current")


class _BatteryTemperature_Type(DisplayString):
    """Custom type batteryTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTemperature_Type.__name__ = "DisplayString"
_BatteryTemperature_Object = MibScalar
batteryTemperature = _BatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 39),
    _BatteryTemperature_Type()
)
batteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperature.setStatus("current")


class _AmbientTemperature_Type(DisplayString):
    """Custom type ambientTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AmbientTemperature_Type.__name__ = "DisplayString"
_AmbientTemperature_Object = MibScalar
ambientTemperature = _AmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 40),
    _AmbientTemperature_Type()
)
ambientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientTemperature.setStatus("current")


class _RtsTemperature_Type(DisplayString):
    """Custom type rtsTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RtsTemperature_Type.__name__ = "DisplayString"
_RtsTemperature_Object = MibScalar
rtsTemperature = _RtsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 41),
    _RtsTemperature_Type()
)
rtsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsTemperature.setStatus("current")


class _UInductorTemperature_Type(DisplayString):
    """Custom type uInductorTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UInductorTemperature_Type.__name__ = "DisplayString"
_UInductorTemperature_Object = MibScalar
uInductorTemperature = _UInductorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 42),
    _UInductorTemperature_Type()
)
uInductorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uInductorTemperature.setStatus("current")


class _VInductorTemperature_Type(DisplayString):
    """Custom type vInductorTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VInductorTemperature_Type.__name__ = "DisplayString"
_VInductorTemperature_Object = MibScalar
vInductorTemperature = _VInductorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 43),
    _VInductorTemperature_Type()
)
vInductorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vInductorTemperature.setStatus("current")


class _WInductorTemperature_Type(DisplayString):
    """Custom type wInductorTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WInductorTemperature_Type.__name__ = "DisplayString"
_WInductorTemperature_Object = MibScalar
wInductorTemperature = _WInductorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 44),
    _WInductorTemperature_Type()
)
wInductorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wInductorTemperature.setStatus("current")
_ChargeState_Type = ChargeStateEnum
_ChargeState_Object = MibScalar
chargeState = _ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 45),
    _ChargeState_Type()
)
chargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeState.setStatus("current")
_ArrayFaults_Type = ArrayFaultsBitfield
_ArrayFaults_Object = MibScalar
arrayFaults = _ArrayFaults_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 46),
    _ArrayFaults_Type()
)
arrayFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayFaults.setStatus("current")


class _BatteryVoltageSlow_Type(DisplayString):
    """Custom type batteryVoltageSlow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryVoltageSlow_Type.__name__ = "DisplayString"
_BatteryVoltageSlow_Object = MibScalar
batteryVoltageSlow = _BatteryVoltageSlow_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 47),
    _BatteryVoltageSlow_Type()
)
batteryVoltageSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageSlow.setStatus("current")


class _TargetVoltage_Type(DisplayString):
    """Custom type targetVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TargetVoltage_Type.__name__ = "DisplayString"
_TargetVoltage_Object = MibScalar
targetVoltage = _TargetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 48),
    _TargetVoltage_Type()
)
targetVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetVoltage.setStatus("current")
_AhChargeResettable_Type = Unsigned32
_AhChargeResettable_Object = MibScalar
ahChargeResettable = _AhChargeResettable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 49),
    _AhChargeResettable_Type()
)
ahChargeResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahChargeResettable.setStatus("current")
_AhChargeTotal_Type = Unsigned32
_AhChargeTotal_Object = MibScalar
ahChargeTotal = _AhChargeTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 50),
    _AhChargeTotal_Type()
)
ahChargeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahChargeTotal.setStatus("current")


class _KwhChargeResettable_Type(DisplayString):
    """Custom type kwhChargeResettable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_KwhChargeResettable_Type.__name__ = "DisplayString"
_KwhChargeResettable_Object = MibScalar
kwhChargeResettable = _KwhChargeResettable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 51),
    _KwhChargeResettable_Type()
)
kwhChargeResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kwhChargeResettable.setStatus("current")


class _KwhChargeTotal_Type(DisplayString):
    """Custom type kwhChargeTotal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_KwhChargeTotal_Type.__name__ = "DisplayString"
_KwhChargeTotal_Object = MibScalar
kwhChargeTotal = _KwhChargeTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 52),
    _KwhChargeTotal_Type()
)
kwhChargeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kwhChargeTotal.setStatus("current")
_LoadState_Type = LoadStateEnum
_LoadState_Object = MibScalar
loadState = _LoadState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 53),
    _LoadState_Type()
)
loadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadState.setStatus("current")
_LoadFaults_Type = LoadFaultsBitfield
_LoadFaults_Object = MibScalar
loadFaults = _LoadFaults_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 54),
    _LoadFaults_Type()
)
loadFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFaults.setStatus("current")


class _LvdSetpoint_Type(DisplayString):
    """Custom type lvdSetpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LvdSetpoint_Type.__name__ = "DisplayString"
_LvdSetpoint_Object = MibScalar
lvdSetpoint = _LvdSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 55),
    _LvdSetpoint_Type()
)
lvdSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lvdSetpoint.setStatus("current")
_AhLoadResettable_Type = Unsigned32
_AhLoadResettable_Object = MibScalar
ahLoadResettable = _AhLoadResettable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 56),
    _AhLoadResettable_Type()
)
ahLoadResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLoadResettable.setStatus("current")
_AhLoadTotal_Type = Unsigned32
_AhLoadTotal_Object = MibScalar
ahLoadTotal = _AhLoadTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 57),
    _AhLoadTotal_Type()
)
ahLoadTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLoadTotal.setStatus("current")
_Hourmeter_Type = Unsigned32
_Hourmeter_Object = MibScalar
hourmeter = _Hourmeter_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 58),
    _Hourmeter_Type()
)
hourmeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourmeter.setStatus("current")
_Alarms_Type = AlarmsBitfield
_Alarms_Object = MibScalar
alarms = _Alarms_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 59),
    _Alarms_Type()
)
alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarms.setStatus("current")
_SettingsSwitches_Type = SettingsSwitchesEnum
_SettingsSwitches_Object = MibScalar
settingsSwitches = _SettingsSwitches_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 60),
    _SettingsSwitches_Type()
)
settingsSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    settingsSwitches.setStatus("current")
_LedState_Type = LedStateEnum
_LedState_Object = MibScalar
ledState = _LedState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 61),
    _LedState_Type()
)
ledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledState.setStatus("current")


class _ArrayPower_Type(DisplayString):
    """Custom type arrayPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayPower_Type.__name__ = "DisplayString"
_ArrayPower_Object = MibScalar
arrayPower = _ArrayPower_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 62),
    _ArrayPower_Type()
)
arrayPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayPower.setStatus("current")


class _ArrayVmp_Type(DisplayString):
    """Custom type arrayVmp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVmp_Type.__name__ = "DisplayString"
_ArrayVmp_Object = MibScalar
arrayVmp = _ArrayVmp_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 63),
    _ArrayVmp_Type()
)
arrayVmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVmp.setStatus("current")


class _ArrayMaxPowerSweep_Type(DisplayString):
    """Custom type arrayMaxPowerSweep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayMaxPowerSweep_Type.__name__ = "DisplayString"
_ArrayMaxPowerSweep_Object = MibScalar
arrayMaxPowerSweep = _ArrayMaxPowerSweep_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 64),
    _ArrayMaxPowerSweep_Type()
)
arrayMaxPowerSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayMaxPowerSweep.setStatus("current")


class _ArrayVoc_Type(DisplayString):
    """Custom type arrayVoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVoc_Type.__name__ = "DisplayString"
_ArrayVoc_Object = MibScalar
arrayVoc = _ArrayVoc_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 65),
    _ArrayVoc_Type()
)
arrayVoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVoc.setStatus("current")


class _VbMinDaily_Type(DisplayString):
    """Custom type vbMinDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VbMinDaily_Type.__name__ = "DisplayString"
_VbMinDaily_Object = MibScalar
vbMinDaily = _VbMinDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 66),
    _VbMinDaily_Type()
)
vbMinDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbMinDaily.setStatus("current")


class _VbMaxDaily_Type(DisplayString):
    """Custom type vbMaxDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VbMaxDaily_Type.__name__ = "DisplayString"
_VbMaxDaily_Object = MibScalar
vbMaxDaily = _VbMaxDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 67),
    _VbMaxDaily_Type()
)
vbMaxDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbMaxDaily.setStatus("current")


class _AhChargeDaily_Type(DisplayString):
    """Custom type ahChargeDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AhChargeDaily_Type.__name__ = "DisplayString"
_AhChargeDaily_Object = MibScalar
ahChargeDaily = _AhChargeDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 68),
    _AhChargeDaily_Type()
)
ahChargeDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahChargeDaily.setStatus("current")


class _AhLoadDaily_Type(DisplayString):
    """Custom type ahLoadDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AhLoadDaily_Type.__name__ = "DisplayString"
_AhLoadDaily_Object = MibScalar
ahLoadDaily = _AhLoadDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 69),
    _AhLoadDaily_Type()
)
ahLoadDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLoadDaily.setStatus("current")
_ArrayFaultsDaily_Type = ArrayFaultsDailyBitfield
_ArrayFaultsDaily_Object = MibScalar
arrayFaultsDaily = _ArrayFaultsDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 70),
    _ArrayFaultsDaily_Type()
)
arrayFaultsDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayFaultsDaily.setStatus("current")
_LoadFaultsDaily_Type = LoadFaultsDailyBitfield
_LoadFaultsDaily_Object = MibScalar
loadFaultsDaily = _LoadFaultsDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 71),
    _LoadFaultsDaily_Type()
)
loadFaultsDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFaultsDaily.setStatus("current")
_AlarmsDaily_Type = AlarmsDailyBitfield
_AlarmsDaily_Object = MibScalar
alarmsDaily = _AlarmsDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 72),
    _AlarmsDaily_Type()
)
alarmsDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmsDaily.setStatus("current")


class _ArrayVoltageMaxDaily_Type(DisplayString):
    """Custom type arrayVoltageMaxDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVoltageMaxDaily_Type.__name__ = "DisplayString"
_ArrayVoltageMaxDaily_Object = MibScalar
arrayVoltageMaxDaily = _ArrayVoltageMaxDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 73),
    _ArrayVoltageMaxDaily_Type()
)
arrayVoltageMaxDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVoltageMaxDaily.setStatus("current")


class _ArrayVoltageFixed_Type(DisplayString):
    """Custom type arrayVoltageFixed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVoltageFixed_Type.__name__ = "DisplayString"
_ArrayVoltageFixed_Object = MibScalar
arrayVoltageFixed = _ArrayVoltageFixed_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 74),
    _ArrayVoltageFixed_Type()
)
arrayVoltageFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVoltageFixed.setStatus("current")


class _ArrayVocFixed_Type(DisplayString):
    """Custom type arrayVocFixed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrayVocFixed_Type.__name__ = "DisplayString"
_ArrayVocFixed_Object = MibScalar
arrayVocFixed = _ArrayVocFixed_Object(
    (1, 3, 6, 1, 4, 1, 33333, 5, 75),
    _ArrayVocFixed_Type()
)
arrayVocFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayVocFixed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROSTAR-MPPT",
    **{"ChargeStateEnum": ChargeStateEnum,
       "LoadStateEnum": LoadStateEnum,
       "SettingsSwitchesEnum": SettingsSwitchesEnum,
       "LedStateEnum": LedStateEnum,
       "ArrayFaultsBitfield": ArrayFaultsBitfield,
       "LoadFaultsBitfield": LoadFaultsBitfield,
       "AlarmsBitfield": AlarmsBitfield,
       "ArrayFaultsDailyBitfield": ArrayFaultsDailyBitfield,
       "LoadFaultsDailyBitfield": LoadFaultsDailyBitfield,
       "AlarmsDailyBitfield": AlarmsDailyBitfield,
       "prostarMppt": prostarMppt,
       "subModel": subModel,
       "serialNumber": serialNumber,
       "deviceVersion": deviceVersion,
       "batteryTerminalVoltage": batteryTerminalVoltage,
       "arrayVoltage": arrayVoltage,
       "loadVoltage": loadVoltage,
       "chargeCurrent": chargeCurrent,
       "loadCurrent": loadCurrent,
       "batteryCurrentNet": batteryCurrentNet,
       "batterySenseVoltage": batterySenseVoltage,
       "meterbusVoltage": meterbusVoltage,
       "heatsinkTemperature": heatsinkTemperature,
       "batteryTemperature": batteryTemperature,
       "ambientTemperature": ambientTemperature,
       "rtsTemperature": rtsTemperature,
       "uInductorTemperature": uInductorTemperature,
       "vInductorTemperature": vInductorTemperature,
       "wInductorTemperature": wInductorTemperature,
       "chargeState": chargeState,
       "arrayFaults": arrayFaults,
       "batteryVoltageSlow": batteryVoltageSlow,
       "targetVoltage": targetVoltage,
       "ahChargeResettable": ahChargeResettable,
       "ahChargeTotal": ahChargeTotal,
       "kwhChargeResettable": kwhChargeResettable,
       "kwhChargeTotal": kwhChargeTotal,
       "loadState": loadState,
       "loadFaults": loadFaults,
       "lvdSetpoint": lvdSetpoint,
       "ahLoadResettable": ahLoadResettable,
       "ahLoadTotal": ahLoadTotal,
       "hourmeter": hourmeter,
       "alarms": alarms,
       "settingsSwitches": settingsSwitches,
       "ledState": ledState,
       "arrayPower": arrayPower,
       "arrayVmp": arrayVmp,
       "arrayMaxPowerSweep": arrayMaxPowerSweep,
       "arrayVoc": arrayVoc,
       "vbMinDaily": vbMinDaily,
       "vbMaxDaily": vbMaxDaily,
       "ahChargeDaily": ahChargeDaily,
       "ahLoadDaily": ahLoadDaily,
       "arrayFaultsDaily": arrayFaultsDaily,
       "loadFaultsDaily": loadFaultsDaily,
       "alarmsDaily": alarmsDaily,
       "arrayVoltageMaxDaily": arrayVoltageMaxDaily,
       "arrayVoltageFixed": arrayVoltageFixed,
       "arrayVocFixed": arrayVocFixed}
)
