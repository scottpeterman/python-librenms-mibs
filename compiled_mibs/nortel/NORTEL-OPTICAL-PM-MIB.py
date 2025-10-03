# SNMP MIB module (NORTEL-OPTICAL-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nortel\NORTEL-OPTICAL-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:18:07 2025
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

(nnOpticalGenericMIBs,) = mibBuilder.importSymbols(
    "NORTEL-OPTICAL-GENERIC-MIB",
    "nnOpticalGenericMIBs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nnOpticalPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1)
)
if mibBuilder.loadTexts:
    nnOpticalPmMIB.setRevisions(
        ("2005-08-16 00:00",
         "2006-04-12 00:00",
         "2006-07-12 00:00",
         "2007-05-21 00:00",
         "2008-02-07 00:00",
         "2008-03-25 00:00",
         "2008-04-02 00:00",
         "2008-08-27 00:00",
         "2009-03-18 00:00",
         "2009-06-15 00:00",
         "2010-06-18 00:00",
         "2010-12-31 00:00",
         "2011-01-18 00:00",
         "2012-06-26 00:00",
         "2012-10-18 00:00",
         "2012-11-06 00:00",
         "2013-02-26 00:00",
         "2013-06-23 00:00",
         "2014-03-14 00:00",
         "2014-05-14 00:00",
         "2015-11-24 00:00",
         "2015-12-03 00:00",
         "2016-01-05 00:00",
         "2017-01-31 00:00",
         "2017-08-16 00:00",
         "2018-04-05 00:00",
         "2019-06-11 00:00",
         "2019-07-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NnOpticalPmMonType(TextualConvention, Integer32):
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
              276)
        )
    )
    namedValues = NamedValues(
        *(("cvSectionRxNe", 1),
          ("esSectionRxNe", 2),
          ("sesSectionRxNe", 3),
          ("sefsSectionRxNe", 4),
          ("cvSectionTxNe", 5),
          ("esSectionTxNe", 6),
          ("sesSectionTxNe", 7),
          ("cvLineRxNe", 8),
          ("esLineRxNe", 9),
          ("sesLineRxNe", 10),
          ("uasLineRxNe", 11),
          ("fcLineRxNe", 12),
          ("cvLineTxNe", 13),
          ("esLineTxNe", 14),
          ("sesLineTxNe", 15),
          ("uasLineTxNe", 16),
          ("fcLineTxNe", 17),
          ("inframesEthRxNe", 18),
          ("fcserrEthRxNe", 19),
          ("frtoolongsEthRxNe", 20),
          ("frtooshortsEthRxNe", 21),
          ("outframesEthTxNe", 22),
          ("fcserrEthTxNe", 23),
          ("cvPCSRxNe", 24),
          ("esPCSRxNe", 25),
          ("sesPCSRxNe", 26),
          ("uasPCSRxNe", 27),
          ("cvPCSTxNe", 28),
          ("esPCSTxNe", 29),
          ("sesPCSTxNe", 30),
          ("uasPCSTxNe", 31),
          ("oprOCHRxNe", 32),
          ("oprnOCHRxNe", 33),
          ("optOCHTxNe", 34),
          ("optnOCHTxNe", 35),
          ("cvOTURxNe", 36),
          ("esOTURxNe", 37),
          ("sesOTURxNe", 38),
          ("sefsOTURxNe", 39),
          ("fecOTURxNe", 40),
          ("hccsOTURxNe", 41),
          ("pfbereOTURxNe", 42),
          ("prfberOTURxNe", 43),
          ("cvODURxNe", 44),
          ("esODURxNe", 45),
          ("sesODURxNe", 46),
          ("uasODURxNe", 47),
          ("fcODURxNe", 48),
          ("oprOTSRxNe", 49),
          ("optOTSTxNe", 50),
          ("orlOTSNaNe", 51),
          ("opinOTSNaNe", 52),
          ("grpopinOTSNaNe", 53),
          ("grpgainOTSNaNe", 54),
          ("opoutOTSNaNe", 55),
          ("grpoptOTSTxNe", 56),
          ("grpopoutOTSNaNe", 57),
          ("esEthRxNe", 58),
          ("sesEthRxNe", 59),
          ("uasEthRxNe", 60),
          ("dfrEthRxNe", 61),
          ("inframeserrEthRxNe", 62),
          ("inframesdiscdsEthRxNe", 63),
          ("esEthTxNe", 64),
          ("sesEthTxNe", 65),
          ("uasEthTxNe", 66),
          ("dfrEthTxNe", 67),
          ("outframeserrEthTxNe", 68),
          ("outframesdiscdsEthTxNe", 69),
          ("esWanRxNe", 70),
          ("sesWanRxNe", 71),
          ("uasWanRxNe", 72),
          ("inframesWanRxNe", 73),
          ("inframeserrWanRxNe", 74),
          ("outframesWanTxNe", 75),
          ("oprMinOTSRxNe", 76),
          ("oprMaxOTSRxNe", 77),
          ("oprAvgOTSRxNe", 78),
          ("optMinOTSTxNe", 79),
          ("optMaxOTSTxNe", 80),
          ("optAvgOTSTxNe", 81),
          ("orlMinOTSNaNe", 82),
          ("orlMaxOTSNaNe", 83),
          ("orlAvgOTSNaNe", 84),
          ("opinMinOTSNaNe", 85),
          ("opinMaxOTSNaNe", 86),
          ("opinAvgOTSNaNe", 87),
          ("grpopinMinOTSNaNe", 88),
          ("grpopinMaxOTSNaNe", 89),
          ("grpopinAvgOTSNaNe", 90),
          ("grpgainMinOTSNaNe", 91),
          ("grpgainMaxOTSNaNe", 92),
          ("grpgainAvgOTSNaNe", 93),
          ("opoutMinOTSNaNe", 94),
          ("opoutMaxOTSNaNe", 95),
          ("opoutAvgOTSNaNe", 96),
          ("grpoptMinOTSTxNe", 97),
          ("grpoptMaxOTSTxNe", 98),
          ("grpoptAvgOTSTxNe", 99),
          ("grpopoutMinOTSNaNe", 100),
          ("grpopoutMaxOTSNaNe", 101),
          ("grpopoutAvgOTSNaNe", 102),
          ("dfrWanRxNe", 103),
          ("pscwODURxNe", 104),
          ("pscpODURxNe", 105),
          ("psdODURxNe", 106),
          ("cvLineRxFe", 107),
          ("esLineRxFe", 108),
          ("sesLineRxFe", 109),
          ("uasLineRxFe", 110),
          ("fcLineRxFe", 111),
          ("cvOTUTxNe", 112),
          ("esOTUTxNe", 113),
          ("sesOTUTxNe", 114),
          ("cvODUTxNe", 115),
          ("esODUTxNe", 116),
          ("sesODUTxNe", 117),
          ("uasODUTxNe", 118),
          ("fcODUTxNe", 119),
          ("oproscOTSNaNe", 120),
          ("oproscMinOTSNaNe", 121),
          ("oproscMaxOTSNaNe", 122),
          ("oproscAvgOTSNaNe", 123),
          ("pscwLineRxNe", 124),
          ("pscpLineRxNe", 125),
          ("psdLineRxNe", 126),
          ("dropgainOTSNaNe", 127),
          ("dropgainMinOTSNaNe", 128),
          ("dropgainMaxOTSNaNe", 129),
          ("dropgainAvgOTSNaNe", 130),
          ("dgdMaxOCHRxNe", 131),
          ("dgdAvgOCHRxNe", 132),
          ("optMinOCHTxNe", 133),
          ("optMaxOCHTxNe", 134),
          ("optAvgOCHTxNe", 135),
          ("prfBerMaxOTURxNe", 136),
          ("oprLowOCHRxNe", 137),
          ("oprHighOCHRxNe", 138),
          ("oprnLowOCHRxNe", 139),
          ("oprnHighOCHRxNe", 140),
          ("optLowOCHTxNe", 141),
          ("optHighOCHTxNe", 142),
          ("optnLowOCHTxNe", 143),
          ("optnHighOCHTxNe", 144),
          ("cvOTURxFe", 145),
          ("esOTURxFe", 146),
          ("sesOTURxFe", 147),
          ("cvODURxFe", 148),
          ("esODURxFe", 149),
          ("sesODURxFe", 150),
          ("uasODURxFe", 151),
          ("fcODURxFe", 152),
          ("oprnOTSRxNe", 153),
          ("sefsSectionTxNe", 154),
          ("spanLossOCH", 155),
          ("spanLossMinOCH", 156),
          ("spanLossMaxOCH", 157),
          ("spanLossAvgOCH", 158),
          ("qMinOTU", 159),
          ("qMaxOTU", 160),
          ("qAvgOTU", 161),
          ("qStdevOTU", 162),
          ("oprMinOCHRxNe", 163),
          ("oprMaxOCHRxNe", 164),
          ("oprAvgOCHRxNe", 165),
          ("optOCHRxNe", 166),
          ("optMinOCHRxNe", 167),
          ("optMaxOCHRxNe", 168),
          ("optAvgOCHRxNe", 169),
          ("orlInOTSNaNe", 170),
          ("orlInMinOTSNaNe", 171),
          ("orlInMaxOTSNaNe", 172),
          ("orlInAvgOTSNaNe", 173),
          ("orlOutOTSNaNe", 174),
          ("orlOutMinOTSNaNe", 175),
          ("orlOutMaxOTSNaNe", 176),
          ("orlOutAvgOTSNaNe", 177),
          ("dmMinODURxNe", 178),
          ("dmMaxODURxNe", 179),
          ("dmAvgODURxNe", 180),
          ("pscwEthRxNe", 181),
          ("pscpEthRxNe", 182),
          ("psdEthRxNe", 183),
          ("remoteInframesEthRxNe", 184),
          ("remoteInframesErrEthRxNe", 185),
          ("remoteFcsErrEthRxNe", 186),
          ("remoteOutframesEthTxNe", 187),
          ("remoteOutframesDiscdsEthTxNe", 188),
          ("uncfecblkOtuRxNe", 189),
          ("iaeOtuRxNe", 190),
          ("iaeOtuRxFe", 191),
          ("esWanTxNe", 192),
          ("sesWanTxNe", 193),
          ("uasWanTxNe", 194),
          ("outframeserrWanTxNe", 195),
          ("cvODUTxFe", 196),
          ("esODUTxFe", 197),
          ("sesODUTxFe", 198),
          ("uasODUTxFe", 199),
          ("fcODUTxFe", 200),
          ("fecPMARxNe", 201),
          ("fecccwPMARxNe", 202),
          ("fecunccwPMARxNe", 203),
          ("hccsPMARxNe", 204),
          ("prfberAvgPMARxNe", 205),
          ("prfberMaxPMARxNe", 206),
          ("fecLane0PMARxNe", 207),
          ("prfberAvgLane0PMARxNe", 208),
          ("prfberMaxLane0cPMARxNe", 209),
          ("fecLane1PMARxNe", 210),
          ("prfberAvgLane1PMARxNe", 211),
          ("prfberMaxLane1cPMARxNe", 212),
          ("fecLane2PMARxNe", 213),
          ("prfberAvgLane2PMARxNe", 214),
          ("prfberMaxLane2PMARxNe", 215),
          ("fecLane3PMARxNe", 216),
          ("prfberAvgLane3PMARxNe", 217),
          ("prfberMaxLane3PMARxNe", 218),
          ("dgdMinOCHRxNe", 219),
          ("prfberPMARxNe", 220),
          ("oprOTSIRxNe", 221),
          ("optOTSITxNe", 222),
          ("oprnOTSIRxNe", 223),
          ("optnOTSITxNe", 224),
          ("oprAvgOTSIRxNe", 225),
          ("oprMinOTSIRxNe", 226),
          ("oprMaxOTSIRxNe", 227),
          ("optAvgOTSITxNe", 228),
          ("optMinOTSITxNe", 229),
          ("optMaxOTSITxNe", 230),
          ("dgdAvgOTSIRxNe", 231),
          ("dgdMaxOTSIRxNe", 232),
          ("pdlAvgOTSIRxNe", 233),
          ("pdlMaxOTSIRxNe", 234),
          ("hccsOTSIRxNe", 235),
          ("fecOTSIRxNe", 236),
          ("prfberOTSIRxNe", 237),
          ("prfbereOTSIRxNe", 238),
          ("prfberMaxOTSIRxNe", 239),
          ("qMinOTSIRxNe", 240),
          ("qMaxOTSIRxNe", 241),
          ("qAvgOTSIRxNe", 242),
          ("qstdevOTSIRxNe", 243),
          ("uncfecblkOTSIRxNe", 244),
          ("dmMinLRxNe", 245),
          ("dmMaxLRxNe", 246),
          ("dmAvgLRxNe", 247),
          ("hccsPCSRxNe", 248),
          ("prfBerPCSRxNe", 249),
          ("prfBerMaxPCSRxNe", 250),
          ("fecPCSRxNe", 251),
          ("fecCcuPCSRxNe", 252),
          ("fecUnCcuPCSRxNe", 253),
          ("osnrAvgOTSIRxNe", 254),
          ("osnrMinOTSIRxNe", 255),
          ("osnrMaxOTSIRxNe", 256),
          ("esnrAvgOTSIRxNe", 257),
          ("esnrMinOTSIRxNe", 258),
          ("esnrMaxOTSIRxNe", 259),
          ("cdAvgOTSIRxNe", 260),
          ("cdMinOTSIRxNe", 261),
          ("cdMaxOTSIRxNe", 262),
          ("pscwOTSRxNe", 263),
          ("pscpOTSRxNe", 264),
          ("psdOTSRxNe", 265),
          ("pdlAvgOCHRxNe", 266),
          ("pdlMaxOCHRxNe", 267),
          ("cdAvgOCHRxNe", 268),
          ("cdMinOCHRxNe", 269),
          ("cdMaxOCHRxNe", 270),
          ("csiMinOTSIRxNe", 271),
          ("csiMaxOTSIRxNe", 272),
          ("csiAvgOTSIRxNe", 273),
          ("snrExtMinOTSIRxNe", 274),
          ("snrExtMaxOTSIRxNe", 275),
          ("snrExtAvgOTSIRxNe", 276))
    )



class NnOpticalPmUnits(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dB", 2),
          ("dBm", 3),
          ("percent", 4),
          ("ber", 5),
          ("pS", 6))
    )



class NnOpticalPmValidity(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("complete", 2),
          ("partial", 3),
          ("adjusted", 4))
    )



# MIB Managed Objects in the order of their OIDs

_NnOpticalPmObjects_ObjectIdentity = ObjectIdentity
nnOpticalPmObjects = _NnOpticalPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1)
)
_NnOpticalPmRecent_ObjectIdentity = ObjectIdentity
nnOpticalPmRecent = _NnOpticalPmRecent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1)
)
_NnOpticalPmRecentTable_Object = MibTable
nnOpticalPmRecentTable = _NnOpticalPmRecentTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nnOpticalPmRecentTable.setStatus("current")
_NnOpticalPmRecentEntry_Object = MibTableRow
nnOpticalPmRecentEntry = _NnOpticalPmRecentEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1)
)
nnOpticalPmRecentEntry.setIndexNames(
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmRecentIfIndex"),
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmRecentMonType"),
)
if mibBuilder.loadTexts:
    nnOpticalPmRecentEntry.setStatus("current")
_NnOpticalPmRecentIfIndex_Type = Integer32
_NnOpticalPmRecentIfIndex_Object = MibTableColumn
nnOpticalPmRecentIfIndex = _NnOpticalPmRecentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 1),
    _NnOpticalPmRecentIfIndex_Type()
)
nnOpticalPmRecentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmRecentIfIndex.setStatus("current")
_NnOpticalPmRecentMonType_Type = NnOpticalPmMonType
_NnOpticalPmRecentMonType_Object = MibTableColumn
nnOpticalPmRecentMonType = _NnOpticalPmRecentMonType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 2),
    _NnOpticalPmRecentMonType_Type()
)
nnOpticalPmRecentMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmRecentMonType.setStatus("current")
_NnOpticalPmRecentIfIndexDescr_Type = SnmpAdminString
_NnOpticalPmRecentIfIndexDescr_Object = MibTableColumn
nnOpticalPmRecentIfIndexDescr = _NnOpticalPmRecentIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 3),
    _NnOpticalPmRecentIfIndexDescr_Type()
)
nnOpticalPmRecentIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmRecentIfIndexDescr.setStatus("current")
_NnOpticalPmRecentMonTypeDescr_Type = SnmpAdminString
_NnOpticalPmRecentMonTypeDescr_Object = MibTableColumn
nnOpticalPmRecentMonTypeDescr = _NnOpticalPmRecentMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 4),
    _NnOpticalPmRecentMonTypeDescr_Type()
)
nnOpticalPmRecentMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmRecentMonTypeDescr.setStatus("current")
_NnOpticalPmRecentUnits_Type = NnOpticalPmUnits
_NnOpticalPmRecentUnits_Object = MibTableColumn
nnOpticalPmRecentUnits = _NnOpticalPmRecentUnits_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 5),
    _NnOpticalPmRecentUnits_Type()
)
nnOpticalPmRecentUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmRecentUnits.setStatus("current")
_NnOpticalPmCurr15MinValue_Type = SnmpAdminString
_NnOpticalPmCurr15MinValue_Object = MibTableColumn
nnOpticalPmCurr15MinValue = _NnOpticalPmCurr15MinValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 6),
    _NnOpticalPmCurr15MinValue_Type()
)
nnOpticalPmCurr15MinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmCurr15MinValue.setStatus("current")
_NnOpticalPmCurr15MinValidity_Type = NnOpticalPmValidity
_NnOpticalPmCurr15MinValidity_Object = MibTableColumn
nnOpticalPmCurr15MinValidity = _NnOpticalPmCurr15MinValidity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 7),
    _NnOpticalPmCurr15MinValidity_Type()
)
nnOpticalPmCurr15MinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmCurr15MinValidity.setStatus("current")
_NnOpticalPmCurr15MinDateAndTime_Type = DateAndTime
_NnOpticalPmCurr15MinDateAndTime_Object = MibTableColumn
nnOpticalPmCurr15MinDateAndTime = _NnOpticalPmCurr15MinDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 8),
    _NnOpticalPmCurr15MinDateAndTime_Type()
)
nnOpticalPmCurr15MinDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmCurr15MinDateAndTime.setStatus("current")
_NnOpticalPmPrev15MinValue_Type = SnmpAdminString
_NnOpticalPmPrev15MinValue_Object = MibTableColumn
nnOpticalPmPrev15MinValue = _NnOpticalPmPrev15MinValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 9),
    _NnOpticalPmPrev15MinValue_Type()
)
nnOpticalPmPrev15MinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmPrev15MinValue.setStatus("current")
_NnOpticalPmPrev15MinValidity_Type = NnOpticalPmValidity
_NnOpticalPmPrev15MinValidity_Object = MibTableColumn
nnOpticalPmPrev15MinValidity = _NnOpticalPmPrev15MinValidity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 10),
    _NnOpticalPmPrev15MinValidity_Type()
)
nnOpticalPmPrev15MinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmPrev15MinValidity.setStatus("current")
_NnOpticalPmPrev15MinDateAndTime_Type = DateAndTime
_NnOpticalPmPrev15MinDateAndTime_Object = MibTableColumn
nnOpticalPmPrev15MinDateAndTime = _NnOpticalPmPrev15MinDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 11),
    _NnOpticalPmPrev15MinDateAndTime_Type()
)
nnOpticalPmPrev15MinDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmPrev15MinDateAndTime.setStatus("current")
_NnOpticalPmCurrDayValue_Type = SnmpAdminString
_NnOpticalPmCurrDayValue_Object = MibTableColumn
nnOpticalPmCurrDayValue = _NnOpticalPmCurrDayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 12),
    _NnOpticalPmCurrDayValue_Type()
)
nnOpticalPmCurrDayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmCurrDayValue.setStatus("current")
_NnOpticalPmCurrDayValidity_Type = NnOpticalPmValidity
_NnOpticalPmCurrDayValidity_Object = MibTableColumn
nnOpticalPmCurrDayValidity = _NnOpticalPmCurrDayValidity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 13),
    _NnOpticalPmCurrDayValidity_Type()
)
nnOpticalPmCurrDayValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmCurrDayValidity.setStatus("current")
_NnOpticalPmCurrDayDateAndTime_Type = DateAndTime
_NnOpticalPmCurrDayDateAndTime_Object = MibTableColumn
nnOpticalPmCurrDayDateAndTime = _NnOpticalPmCurrDayDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 14),
    _NnOpticalPmCurrDayDateAndTime_Type()
)
nnOpticalPmCurrDayDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmCurrDayDateAndTime.setStatus("current")
_NnOpticalPmPrevDayValue_Type = SnmpAdminString
_NnOpticalPmPrevDayValue_Object = MibTableColumn
nnOpticalPmPrevDayValue = _NnOpticalPmPrevDayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 15),
    _NnOpticalPmPrevDayValue_Type()
)
nnOpticalPmPrevDayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmPrevDayValue.setStatus("current")
_NnOpticalPmPrevDayValidity_Type = NnOpticalPmValidity
_NnOpticalPmPrevDayValidity_Object = MibTableColumn
nnOpticalPmPrevDayValidity = _NnOpticalPmPrevDayValidity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 16),
    _NnOpticalPmPrevDayValidity_Type()
)
nnOpticalPmPrevDayValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmPrevDayValidity.setStatus("current")
_NnOpticalPmPrevDayDateAndTime_Type = DateAndTime
_NnOpticalPmPrevDayDateAndTime_Object = MibTableColumn
nnOpticalPmPrevDayDateAndTime = _NnOpticalPmPrevDayDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 1, 1, 1, 17),
    _NnOpticalPmPrevDayDateAndTime_Type()
)
nnOpticalPmPrevDayDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmPrevDayDateAndTime.setStatus("current")
_NnOpticalPmUntimed_ObjectIdentity = ObjectIdentity
nnOpticalPmUntimed = _NnOpticalPmUntimed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2)
)
_NnOpticalPmUntTable_Object = MibTable
nnOpticalPmUntTable = _NnOpticalPmUntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nnOpticalPmUntTable.setStatus("current")
_NnOpticalPmUntEntry_Object = MibTableRow
nnOpticalPmUntEntry = _NnOpticalPmUntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1)
)
nnOpticalPmUntEntry.setIndexNames(
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmUntIfIndex"),
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmUntMonType"),
)
if mibBuilder.loadTexts:
    nnOpticalPmUntEntry.setStatus("current")
_NnOpticalPmUntIfIndex_Type = Integer32
_NnOpticalPmUntIfIndex_Object = MibTableColumn
nnOpticalPmUntIfIndex = _NnOpticalPmUntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 1),
    _NnOpticalPmUntIfIndex_Type()
)
nnOpticalPmUntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmUntIfIndex.setStatus("current")
_NnOpticalPmUntMonType_Type = NnOpticalPmMonType
_NnOpticalPmUntMonType_Object = MibTableColumn
nnOpticalPmUntMonType = _NnOpticalPmUntMonType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 2),
    _NnOpticalPmUntMonType_Type()
)
nnOpticalPmUntMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmUntMonType.setStatus("current")
_NnOpticalPmUntIfIndexDescr_Type = SnmpAdminString
_NnOpticalPmUntIfIndexDescr_Object = MibTableColumn
nnOpticalPmUntIfIndexDescr = _NnOpticalPmUntIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 3),
    _NnOpticalPmUntIfIndexDescr_Type()
)
nnOpticalPmUntIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmUntIfIndexDescr.setStatus("current")
_NnOpticalPmUntMonTypeDescr_Type = SnmpAdminString
_NnOpticalPmUntMonTypeDescr_Object = MibTableColumn
nnOpticalPmUntMonTypeDescr = _NnOpticalPmUntMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 4),
    _NnOpticalPmUntMonTypeDescr_Type()
)
nnOpticalPmUntMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmUntMonTypeDescr.setStatus("current")
_NnOpticalPmUntUnits_Type = NnOpticalPmUnits
_NnOpticalPmUntUnits_Object = MibTableColumn
nnOpticalPmUntUnits = _NnOpticalPmUntUnits_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 5),
    _NnOpticalPmUntUnits_Type()
)
nnOpticalPmUntUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmUntUnits.setStatus("current")
_NnOpticalPmUntValue_Type = SnmpAdminString
_NnOpticalPmUntValue_Object = MibTableColumn
nnOpticalPmUntValue = _NnOpticalPmUntValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 6),
    _NnOpticalPmUntValue_Type()
)
nnOpticalPmUntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmUntValue.setStatus("current")
_NnOpticalPmUntValidity_Type = NnOpticalPmValidity
_NnOpticalPmUntValidity_Object = MibTableColumn
nnOpticalPmUntValidity = _NnOpticalPmUntValidity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 7),
    _NnOpticalPmUntValidity_Type()
)
nnOpticalPmUntValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmUntValidity.setStatus("current")
_NnOpticalPmUntDateAndTime_Type = DateAndTime
_NnOpticalPmUntDateAndTime_Object = MibTableColumn
nnOpticalPmUntDateAndTime = _NnOpticalPmUntDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 2, 1, 1, 8),
    _NnOpticalPmUntDateAndTime_Type()
)
nnOpticalPmUntDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmUntDateAndTime.setStatus("current")
_NnOpticalPmBaseline_ObjectIdentity = ObjectIdentity
nnOpticalPmBaseline = _NnOpticalPmBaseline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3)
)
_NnOpticalPmBaslnTable_Object = MibTable
nnOpticalPmBaslnTable = _NnOpticalPmBaslnTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nnOpticalPmBaslnTable.setStatus("current")
_NnOpticalPmBaslnEntry_Object = MibTableRow
nnOpticalPmBaslnEntry = _NnOpticalPmBaslnEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1)
)
nnOpticalPmBaslnEntry.setIndexNames(
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmBaslnIfIndex"),
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmBaslnMonType"),
)
if mibBuilder.loadTexts:
    nnOpticalPmBaslnEntry.setStatus("current")
_NnOpticalPmBaslnIfIndex_Type = Integer32
_NnOpticalPmBaslnIfIndex_Object = MibTableColumn
nnOpticalPmBaslnIfIndex = _NnOpticalPmBaslnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 1),
    _NnOpticalPmBaslnIfIndex_Type()
)
nnOpticalPmBaslnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmBaslnIfIndex.setStatus("current")
_NnOpticalPmBaslnMonType_Type = NnOpticalPmMonType
_NnOpticalPmBaslnMonType_Object = MibTableColumn
nnOpticalPmBaslnMonType = _NnOpticalPmBaslnMonType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 2),
    _NnOpticalPmBaslnMonType_Type()
)
nnOpticalPmBaslnMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmBaslnMonType.setStatus("current")
_NnOpticalPmBaslnIfIndexDescr_Type = SnmpAdminString
_NnOpticalPmBaslnIfIndexDescr_Object = MibTableColumn
nnOpticalPmBaslnIfIndexDescr = _NnOpticalPmBaslnIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 3),
    _NnOpticalPmBaslnIfIndexDescr_Type()
)
nnOpticalPmBaslnIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmBaslnIfIndexDescr.setStatus("current")
_NnOpticalPmBaslnMonTypeDescr_Type = SnmpAdminString
_NnOpticalPmBaslnMonTypeDescr_Object = MibTableColumn
nnOpticalPmBaslnMonTypeDescr = _NnOpticalPmBaslnMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 4),
    _NnOpticalPmBaslnMonTypeDescr_Type()
)
nnOpticalPmBaslnMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmBaslnMonTypeDescr.setStatus("current")
_NnOpticalPmBaslnUnits_Type = NnOpticalPmUnits
_NnOpticalPmBaslnUnits_Object = MibTableColumn
nnOpticalPmBaslnUnits = _NnOpticalPmBaslnUnits_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 5),
    _NnOpticalPmBaslnUnits_Type()
)
nnOpticalPmBaslnUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmBaslnUnits.setStatus("current")
_NnOpticalPmBaslnValue_Type = SnmpAdminString
_NnOpticalPmBaslnValue_Object = MibTableColumn
nnOpticalPmBaslnValue = _NnOpticalPmBaslnValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 6),
    _NnOpticalPmBaslnValue_Type()
)
nnOpticalPmBaslnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmBaslnValue.setStatus("current")
_NnOpticalPmBaslnValidity_Type = NnOpticalPmValidity
_NnOpticalPmBaslnValidity_Object = MibTableColumn
nnOpticalPmBaslnValidity = _NnOpticalPmBaslnValidity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 7),
    _NnOpticalPmBaslnValidity_Type()
)
nnOpticalPmBaslnValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmBaslnValidity.setStatus("current")
_NnOpticalPmBaslnDateAndTime_Type = DateAndTime
_NnOpticalPmBaslnDateAndTime_Object = MibTableColumn
nnOpticalPmBaslnDateAndTime = _NnOpticalPmBaslnDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 3, 1, 1, 8),
    _NnOpticalPmBaslnDateAndTime_Type()
)
nnOpticalPmBaslnDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmBaslnDateAndTime.setStatus("current")
_NnOpticalPmTimed_ObjectIdentity = ObjectIdentity
nnOpticalPmTimed = _NnOpticalPmTimed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4)
)
_NnOpticalPm15Min_ObjectIdentity = ObjectIdentity
nnOpticalPm15Min = _NnOpticalPm15Min_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1)
)
_NnOpticalPm15MinTable_Object = MibTable
nnOpticalPm15MinTable = _NnOpticalPm15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    nnOpticalPm15MinTable.setStatus("current")
_NnOpticalPm15MinEntry_Object = MibTableRow
nnOpticalPm15MinEntry = _NnOpticalPm15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1)
)
nnOpticalPm15MinEntry.setIndexNames(
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPm15MinIfIndex"),
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPm15MinIntIndex"),
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPm15MinMonType"),
)
if mibBuilder.loadTexts:
    nnOpticalPm15MinEntry.setStatus("current")
_NnOpticalPm15MinIfIndex_Type = Integer32
_NnOpticalPm15MinIfIndex_Object = MibTableColumn
nnOpticalPm15MinIfIndex = _NnOpticalPm15MinIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 1),
    _NnOpticalPm15MinIfIndex_Type()
)
nnOpticalPm15MinIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinIfIndex.setStatus("current")
_NnOpticalPm15MinIntIndex_Type = Integer32
_NnOpticalPm15MinIntIndex_Object = MibTableColumn
nnOpticalPm15MinIntIndex = _NnOpticalPm15MinIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 2),
    _NnOpticalPm15MinIntIndex_Type()
)
nnOpticalPm15MinIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinIntIndex.setStatus("current")
_NnOpticalPm15MinMonType_Type = NnOpticalPmMonType
_NnOpticalPm15MinMonType_Object = MibTableColumn
nnOpticalPm15MinMonType = _NnOpticalPm15MinMonType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 3),
    _NnOpticalPm15MinMonType_Type()
)
nnOpticalPm15MinMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinMonType.setStatus("current")
_NnOpticalPm15MinIfIndexDescr_Type = SnmpAdminString
_NnOpticalPm15MinIfIndexDescr_Object = MibTableColumn
nnOpticalPm15MinIfIndexDescr = _NnOpticalPm15MinIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 4),
    _NnOpticalPm15MinIfIndexDescr_Type()
)
nnOpticalPm15MinIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinIfIndexDescr.setStatus("current")
_NnOpticalPm15MinMonTypeDescr_Type = SnmpAdminString
_NnOpticalPm15MinMonTypeDescr_Object = MibTableColumn
nnOpticalPm15MinMonTypeDescr = _NnOpticalPm15MinMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 5),
    _NnOpticalPm15MinMonTypeDescr_Type()
)
nnOpticalPm15MinMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinMonTypeDescr.setStatus("current")
_NnOpticalPm15MinUnits_Type = NnOpticalPmUnits
_NnOpticalPm15MinUnits_Object = MibTableColumn
nnOpticalPm15MinUnits = _NnOpticalPm15MinUnits_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 6),
    _NnOpticalPm15MinUnits_Type()
)
nnOpticalPm15MinUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinUnits.setStatus("current")
_NnOpticalPm15MinValue_Type = SnmpAdminString
_NnOpticalPm15MinValue_Object = MibTableColumn
nnOpticalPm15MinValue = _NnOpticalPm15MinValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 7),
    _NnOpticalPm15MinValue_Type()
)
nnOpticalPm15MinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinValue.setStatus("current")
_NnOpticalPm15MinValidity_Type = NnOpticalPmValidity
_NnOpticalPm15MinValidity_Object = MibTableColumn
nnOpticalPm15MinValidity = _NnOpticalPm15MinValidity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 8),
    _NnOpticalPm15MinValidity_Type()
)
nnOpticalPm15MinValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinValidity.setStatus("current")
_NnOpticalPm15MinDateAndTime_Type = DateAndTime
_NnOpticalPm15MinDateAndTime_Object = MibTableColumn
nnOpticalPm15MinDateAndTime = _NnOpticalPm15MinDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 1, 1, 1, 9),
    _NnOpticalPm15MinDateAndTime_Type()
)
nnOpticalPm15MinDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPm15MinDateAndTime.setStatus("current")
_NnOpticalPmDay_ObjectIdentity = ObjectIdentity
nnOpticalPmDay = _NnOpticalPmDay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2)
)
_NnOpticalPmDayTable_Object = MibTable
nnOpticalPmDayTable = _NnOpticalPmDayTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nnOpticalPmDayTable.setStatus("current")
_NnOpticalPmDayEntry_Object = MibTableRow
nnOpticalPmDayEntry = _NnOpticalPmDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1)
)
nnOpticalPmDayEntry.setIndexNames(
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmDayIfIndex"),
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmDayIntIndex"),
    (0, "NORTEL-OPTICAL-PM-MIB", "nnOpticalPmDayMonType"),
)
if mibBuilder.loadTexts:
    nnOpticalPmDayEntry.setStatus("current")
_NnOpticalPmDayIfIndex_Type = Integer32
_NnOpticalPmDayIfIndex_Object = MibTableColumn
nnOpticalPmDayIfIndex = _NnOpticalPmDayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 1),
    _NnOpticalPmDayIfIndex_Type()
)
nnOpticalPmDayIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayIfIndex.setStatus("current")
_NnOpticalPmDayIntIndex_Type = Integer32
_NnOpticalPmDayIntIndex_Object = MibTableColumn
nnOpticalPmDayIntIndex = _NnOpticalPmDayIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 2),
    _NnOpticalPmDayIntIndex_Type()
)
nnOpticalPmDayIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayIntIndex.setStatus("current")
_NnOpticalPmDayMonType_Type = NnOpticalPmMonType
_NnOpticalPmDayMonType_Object = MibTableColumn
nnOpticalPmDayMonType = _NnOpticalPmDayMonType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 3),
    _NnOpticalPmDayMonType_Type()
)
nnOpticalPmDayMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayMonType.setStatus("current")
_NnOpticalPmDayIfIndexDescr_Type = SnmpAdminString
_NnOpticalPmDayIfIndexDescr_Object = MibTableColumn
nnOpticalPmDayIfIndexDescr = _NnOpticalPmDayIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 4),
    _NnOpticalPmDayIfIndexDescr_Type()
)
nnOpticalPmDayIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayIfIndexDescr.setStatus("current")
_NnOpticalPmDayMonTypeDescr_Type = SnmpAdminString
_NnOpticalPmDayMonTypeDescr_Object = MibTableColumn
nnOpticalPmDayMonTypeDescr = _NnOpticalPmDayMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 5),
    _NnOpticalPmDayMonTypeDescr_Type()
)
nnOpticalPmDayMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayMonTypeDescr.setStatus("current")
_NnOpticalPmDayUnits_Type = NnOpticalPmUnits
_NnOpticalPmDayUnits_Object = MibTableColumn
nnOpticalPmDayUnits = _NnOpticalPmDayUnits_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 6),
    _NnOpticalPmDayUnits_Type()
)
nnOpticalPmDayUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayUnits.setStatus("current")
_NnOpticalPmDayValue_Type = SnmpAdminString
_NnOpticalPmDayValue_Object = MibTableColumn
nnOpticalPmDayValue = _NnOpticalPmDayValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 7),
    _NnOpticalPmDayValue_Type()
)
nnOpticalPmDayValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayValue.setStatus("current")
_NnOpticalPmDayValidity_Type = NnOpticalPmValidity
_NnOpticalPmDayValidity_Object = MibTableColumn
nnOpticalPmDayValidity = _NnOpticalPmDayValidity_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 8),
    _NnOpticalPmDayValidity_Type()
)
nnOpticalPmDayValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayValidity.setStatus("current")
_NnOpticalPmDayDateAndTime_Type = DateAndTime
_NnOpticalPmDayDateAndTime_Object = MibTableColumn
nnOpticalPmDayDateAndTime = _NnOpticalPmDayDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 10, 1, 1, 4, 2, 1, 1, 9),
    _NnOpticalPmDayDateAndTime_Type()
)
nnOpticalPmDayDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnOpticalPmDayDateAndTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-OPTICAL-PM-MIB",
    **{"NnOpticalPmMonType": NnOpticalPmMonType,
       "NnOpticalPmUnits": NnOpticalPmUnits,
       "NnOpticalPmValidity": NnOpticalPmValidity,
       "nnOpticalPmMIB": nnOpticalPmMIB,
       "nnOpticalPmObjects": nnOpticalPmObjects,
       "nnOpticalPmRecent": nnOpticalPmRecent,
       "nnOpticalPmRecentTable": nnOpticalPmRecentTable,
       "nnOpticalPmRecentEntry": nnOpticalPmRecentEntry,
       "nnOpticalPmRecentIfIndex": nnOpticalPmRecentIfIndex,
       "nnOpticalPmRecentMonType": nnOpticalPmRecentMonType,
       "nnOpticalPmRecentIfIndexDescr": nnOpticalPmRecentIfIndexDescr,
       "nnOpticalPmRecentMonTypeDescr": nnOpticalPmRecentMonTypeDescr,
       "nnOpticalPmRecentUnits": nnOpticalPmRecentUnits,
       "nnOpticalPmCurr15MinValue": nnOpticalPmCurr15MinValue,
       "nnOpticalPmCurr15MinValidity": nnOpticalPmCurr15MinValidity,
       "nnOpticalPmCurr15MinDateAndTime": nnOpticalPmCurr15MinDateAndTime,
       "nnOpticalPmPrev15MinValue": nnOpticalPmPrev15MinValue,
       "nnOpticalPmPrev15MinValidity": nnOpticalPmPrev15MinValidity,
       "nnOpticalPmPrev15MinDateAndTime": nnOpticalPmPrev15MinDateAndTime,
       "nnOpticalPmCurrDayValue": nnOpticalPmCurrDayValue,
       "nnOpticalPmCurrDayValidity": nnOpticalPmCurrDayValidity,
       "nnOpticalPmCurrDayDateAndTime": nnOpticalPmCurrDayDateAndTime,
       "nnOpticalPmPrevDayValue": nnOpticalPmPrevDayValue,
       "nnOpticalPmPrevDayValidity": nnOpticalPmPrevDayValidity,
       "nnOpticalPmPrevDayDateAndTime": nnOpticalPmPrevDayDateAndTime,
       "nnOpticalPmUntimed": nnOpticalPmUntimed,
       "nnOpticalPmUntTable": nnOpticalPmUntTable,
       "nnOpticalPmUntEntry": nnOpticalPmUntEntry,
       "nnOpticalPmUntIfIndex": nnOpticalPmUntIfIndex,
       "nnOpticalPmUntMonType": nnOpticalPmUntMonType,
       "nnOpticalPmUntIfIndexDescr": nnOpticalPmUntIfIndexDescr,
       "nnOpticalPmUntMonTypeDescr": nnOpticalPmUntMonTypeDescr,
       "nnOpticalPmUntUnits": nnOpticalPmUntUnits,
       "nnOpticalPmUntValue": nnOpticalPmUntValue,
       "nnOpticalPmUntValidity": nnOpticalPmUntValidity,
       "nnOpticalPmUntDateAndTime": nnOpticalPmUntDateAndTime,
       "nnOpticalPmBaseline": nnOpticalPmBaseline,
       "nnOpticalPmBaslnTable": nnOpticalPmBaslnTable,
       "nnOpticalPmBaslnEntry": nnOpticalPmBaslnEntry,
       "nnOpticalPmBaslnIfIndex": nnOpticalPmBaslnIfIndex,
       "nnOpticalPmBaslnMonType": nnOpticalPmBaslnMonType,
       "nnOpticalPmBaslnIfIndexDescr": nnOpticalPmBaslnIfIndexDescr,
       "nnOpticalPmBaslnMonTypeDescr": nnOpticalPmBaslnMonTypeDescr,
       "nnOpticalPmBaslnUnits": nnOpticalPmBaslnUnits,
       "nnOpticalPmBaslnValue": nnOpticalPmBaslnValue,
       "nnOpticalPmBaslnValidity": nnOpticalPmBaslnValidity,
       "nnOpticalPmBaslnDateAndTime": nnOpticalPmBaslnDateAndTime,
       "nnOpticalPmTimed": nnOpticalPmTimed,
       "nnOpticalPm15Min": nnOpticalPm15Min,
       "nnOpticalPm15MinTable": nnOpticalPm15MinTable,
       "nnOpticalPm15MinEntry": nnOpticalPm15MinEntry,
       "nnOpticalPm15MinIfIndex": nnOpticalPm15MinIfIndex,
       "nnOpticalPm15MinIntIndex": nnOpticalPm15MinIntIndex,
       "nnOpticalPm15MinMonType": nnOpticalPm15MinMonType,
       "nnOpticalPm15MinIfIndexDescr": nnOpticalPm15MinIfIndexDescr,
       "nnOpticalPm15MinMonTypeDescr": nnOpticalPm15MinMonTypeDescr,
       "nnOpticalPm15MinUnits": nnOpticalPm15MinUnits,
       "nnOpticalPm15MinValue": nnOpticalPm15MinValue,
       "nnOpticalPm15MinValidity": nnOpticalPm15MinValidity,
       "nnOpticalPm15MinDateAndTime": nnOpticalPm15MinDateAndTime,
       "nnOpticalPmDay": nnOpticalPmDay,
       "nnOpticalPmDayTable": nnOpticalPmDayTable,
       "nnOpticalPmDayEntry": nnOpticalPmDayEntry,
       "nnOpticalPmDayIfIndex": nnOpticalPmDayIfIndex,
       "nnOpticalPmDayIntIndex": nnOpticalPmDayIntIndex,
       "nnOpticalPmDayMonType": nnOpticalPmDayMonType,
       "nnOpticalPmDayIfIndexDescr": nnOpticalPmDayIfIndexDescr,
       "nnOpticalPmDayMonTypeDescr": nnOpticalPmDayMonTypeDescr,
       "nnOpticalPmDayUnits": nnOpticalPmDayUnits,
       "nnOpticalPmDayValue": nnOpticalPmDayValue,
       "nnOpticalPmDayValidity": nnOpticalPmDayValidity,
       "nnOpticalPmDayDateAndTime": nnOpticalPmDayDateAndTime}
)
