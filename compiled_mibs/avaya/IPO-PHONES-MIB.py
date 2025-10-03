# SNMP MIB module (IPO-PHONES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avaya\IPO-PHONES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:06 2025
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

(IndexInteger,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexInteger")

(ipoGTEventDateTime,
 ipoGTEventDevID,
 ipoGTEventEntityName,
 ipoGTEventSeverity,
 ipoGTEventStdSeverity,
 ipoGenMibs) = mibBuilder.importSymbols(
    "IPO-MIB",
    "ipoGTEventDateTime",
    "ipoGTEventDevID",
    "ipoGTEventEntityName",
    "ipoGTEventSeverity",
    "ipoGTEventStdSeverity",
    "ipoGenMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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

ipoPhonesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipoPhonesMIB.setRevisions(
        ("2011-02-09 15:21",
         "2009-02-18 13:09",
         "2008-06-12 15:06",
         "2008-04-17 16:30",
         "2007-03-28 12:09",
         "2007-02-24 12:09",
         "2006-06-29 00:00",
         "2006-01-31 00:00",
         "2005-11-22 00:00",
         "2005-07-21 10:50",
         "2005-07-21 10:30",
         "2005-03-04 00:00",
         "2005-01-06 00:00",
         "2004-12-20 00:00",
         "2004-03-03 00:00",
         "2003-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PhoneType(TextualConvention, Integer32):
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
              170)
        )
    )
    namedValues = NamedValues(
        *(("noPhone", 1),
          ("genericPhone", 2),
          ("potPhone", 3),
          ("dtPhone", 4),
          ("a4406Dplus", 5),
          ("a4412Dplus", 6),
          ("a4424Dplus", 7),
          ("a4424LDplus", 8),
          ("a9040TransTalk", 9),
          ("a6408Dplus", 10),
          ("a6416Dplus", 11),
          ("a6424Dplus", 12),
          ("a4606ip", 13),
          ("a4612ip", 14),
          ("a4624ip", 15),
          ("a4620ip", 16),
          ("a4602ip", 17),
          ("a2420", 18),
          ("a2010dt", 19),
          ("a2020dt", 20),
          ("a2030dt", 21),
          ("a2050dt", 22),
          ("act5", 23),
          ("att3", 24),
          ("att5", 25),
          ("a5420", 26),
          ("a5410", 27),
          ("a4601ip", 28),
          ("a4610ip", 29),
          ("ablf", 30),
          ("a2402", 31),
          ("a2410", 32),
          ("a5610ip", 33),
          ("a5620ip", 34),
          ("softIPPhone", 35),
          ("a5601ip", 36),
          ("a5602ip", 37),
          ("a4621ip", 38),
          ("a5621ip", 39),
          ("a4625ip", 40),
          ("a5402", 41),
          ("h323Phone", 42),
          ("sipPhone", 43),
          ("t3Compact", 44),
          ("t3Classic", 45),
          ("t3Comfort", 46),
          ("t3Phone", 47),
          ("t3compactIP", 48),
          ("t3classicIP", 49),
          ("t3comfortIP", 50),
          ("avayaSip", 51),
          ("admmPhone", 52),
          ("a9620ip", 53),
          ("a9630ip", 54),
          ("telecommuter", 55),
          ("mobiletwin", 56),
          ("a9640ip", 57),
          ("a9650ip", 58),
          ("a9610ip", 59),
          ("a1603ip", 60),
          ("a1608ip", 61),
          ("a1616ip", 62),
          ("a1703ip", 63),
          ("a1708ip", 64),
          ("a1716ip", 65),
          ("s60Sip", 66),
          ("sp320Sip", 67),
          ("sp601Sip", 68),
          ("a10ataSip", 69),
          ("pmataSip", 70),
          ("ip22Sip", 71),
          ("ip24Sip", 72),
          ("gxp2000Sip", 73),
          ("gxp2020Sip", 74),
          ("eyebeamSip", 75),
          ("a1403", 76),
          ("a1408", 77),
          ("a1416", 78),
          ("a1450", 79),
          ("ip28Sip", 80),
          ("phoneManagerIP", 81),
          ("a1503", 82),
          ("a1508", 83),
          ("a1516", 84),
          ("a1550", 85),
          ("a1603Lip", 86),
          ("a1608Lip", 87),
          ("a1616Lip", 88),
          ("softPhoneSip", 89),
          ("etr34d", 90),
          ("etr18d", 91),
          ("etr6d", 92),
          ("etr34", 93),
          ("etr18", 94),
          ("etr6", 95),
          ("etrpots", 96),
          ("doorphone1", 97),
          ("doorphone2", 98),
          ("bstT7316e", 99),
          ("a9620Sip", 100),
          ("a9630Sip", 101),
          ("a9640Sip", 102),
          ("a9650Sip", 103),
          ("a96xxSip", 104),
          ("a1603Sip", 105),
          ("a9404", 106),
          ("a9408", 107),
          ("a9504", 108),
          ("a9508", 109),
          ("a9608ip", 110),
          ("a9611ip", 111),
          ("a9621ip", 112),
          ("a9641ip", 113),
          ("a3720Admm", 114),
          ("a3725Admm", 115),
          ("a1010Sip", 116),
          ("a1040Sip", 117),
          ("a1120ESip", 118),
          ("a1140ESip", 119),
          ("a1220Sip", 120),
          ("a1230Sip", 121),
          ("a1692Sip", 122),
          ("pvvxSip", 123),
          ("gxv3140Sip", 124),
          ("a3740Admm", 125),
          ("a3749Admm", 126),
          ("bstT7316", 127),
          ("bstT7208", 128),
          ("bstM7208", 129),
          ("bstM7310", 130),
          ("bstM7310blf", 131),
          ("bstM7324", 132),
          ("bstM7100", 133),
          ("bstT7100", 134),
          ("bstT7000", 135),
          ("bstDectA", 136),
          ("bstDectB", 137),
          ("bstDectC", 138),
          ("bstDoorphone", 139),
          ("bstT7406", 140),
          ("bstT7406E", 141),
          ("bstM7310N", 142),
          ("bstAcu", 143),
          ("bstM7100N", 144),
          ("bstM7324N", 145),
          ("bstM7208N", 146),
          ("aB179Sip", 147),
          ("bstAta", 148),
          ("aA175Sip", 149),
          ("aOneXSip", 150),
          ("aFlareSip", 151),
          ("aD100", 152),
          ("aRadvisionXT1000", 153),
          ("aRadvisionXT1200", 154),
          ("aRadvisionXT4000", 155),
          ("aRadvisionXT4200", 156),
          ("aRadvisionXT5000", 157),
          ("aRadvisionXTPiccolo", 158),
          ("aRadvisionScopiaMCU", 159),
          ("aRadvisionScopiaVC240", 160),
          ("aOneXSipMobile", 161),
          ("aACCSServer", 162),
          ("aCIEServer", 163),
          ("aE129SIP", 164),
          ("aE159SIP", 165),
          ("aE169SIP", 166),
          ("aOneXMsiSIP", 167),
          ("aRadvisionXT240", 168),
          ("aWebRTCSIP", 169),
          ("softPhoneSipMac", 170))
    )



# MIB Managed Objects in the order of their OIDs

_IpoPhonesMibNotifications_ObjectIdentity = ObjectIdentity
ipoPhonesMibNotifications = _IpoPhonesMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0)
)
_IpoPhonesMibObjects_ObjectIdentity = ObjectIdentity
ipoPhonesMibObjects = _IpoPhonesMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1)
)
_IpoPhones_ObjectIdentity = ObjectIdentity
ipoPhones = _IpoPhones_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1)
)
_IpoPhonesNumber_Type = Integer32
_IpoPhonesNumber_Object = MibScalar
ipoPhonesNumber = _IpoPhonesNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 1),
    _IpoPhonesNumber_Type()
)
ipoPhonesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesNumber.setStatus("current")
_IpoPhonesTable_Object = MibTable
ipoPhonesTable = _IpoPhonesTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipoPhonesTable.setStatus("current")
_IpoPhonesEntry_Object = MibTableRow
ipoPhonesEntry = _IpoPhonesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1)
)
ipoPhonesEntry.setIndexNames(
    (0, "IPO-PHONES-MIB", "ipoPhonesIndex"),
)
if mibBuilder.loadTexts:
    ipoPhonesEntry.setStatus("current")
_IpoPhonesIndex_Type = IndexInteger
_IpoPhonesIndex_Object = MibTableColumn
ipoPhonesIndex = _IpoPhonesIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1),
    _IpoPhonesIndex_Type()
)
ipoPhonesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesIndex.setStatus("current")
_IpoPhonesExtID_Type = Integer32
_IpoPhonesExtID_Object = MibTableColumn
ipoPhonesExtID = _IpoPhonesExtID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2),
    _IpoPhonesExtID_Type()
)
ipoPhonesExtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesExtID.setStatus("current")
_IpoPhonesExtNumber_Type = Integer32
_IpoPhonesExtNumber_Object = MibTableColumn
ipoPhonesExtNumber = _IpoPhonesExtNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 3),
    _IpoPhonesExtNumber_Type()
)
ipoPhonesExtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesExtNumber.setStatus("current")


class _IpoPhonesUserShort_Type(DisplayString):
    """Custom type ipoPhonesUserShort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IpoPhonesUserShort_Type.__name__ = "DisplayString"
_IpoPhonesUserShort_Object = MibTableColumn
ipoPhonesUserShort = _IpoPhonesUserShort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 4),
    _IpoPhonesUserShort_Type()
)
ipoPhonesUserShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesUserShort.setStatus("current")


class _IpoPhonesUserLong_Type(DisplayString):
    """Custom type ipoPhonesUserLong based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpoPhonesUserLong_Type.__name__ = "DisplayString"
_IpoPhonesUserLong_Object = MibTableColumn
ipoPhonesUserLong = _IpoPhonesUserLong_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 5),
    _IpoPhonesUserLong_Type()
)
ipoPhonesUserLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesUserLong.setStatus("current")
_IpoPhonesType_Type = PhoneType
_IpoPhonesType_Object = MibTableColumn
ipoPhonesType = _IpoPhonesType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 6),
    _IpoPhonesType_Type()
)
ipoPhonesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesType.setStatus("current")
_IpoPhonesPort_Type = Unsigned32
_IpoPhonesPort_Object = MibTableColumn
ipoPhonesPort = _IpoPhonesPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 7),
    _IpoPhonesPort_Type()
)
ipoPhonesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesPort.setStatus("current")
_IpoPhonesPortNumber_Type = Unsigned32
_IpoPhonesPortNumber_Object = MibTableColumn
ipoPhonesPortNumber = _IpoPhonesPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 8),
    _IpoPhonesPortNumber_Type()
)
ipoPhonesPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesPortNumber.setStatus("current")
_IpoPhonesModuleNumber_Type = Unsigned32
_IpoPhonesModuleNumber_Object = MibTableColumn
ipoPhonesModuleNumber = _IpoPhonesModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 9),
    _IpoPhonesModuleNumber_Type()
)
ipoPhonesModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesModuleNumber.setStatus("current")
_IpoPhonesIPAddress_Type = IpAddress
_IpoPhonesIPAddress_Object = MibTableColumn
ipoPhonesIPAddress = _IpoPhonesIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 10),
    _IpoPhonesIPAddress_Type()
)
ipoPhonesIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesIPAddress.setStatus("current")
_IpoPhonesPhysAddress_Type = PhysAddress
_IpoPhonesPhysAddress_Object = MibTableColumn
ipoPhonesPhysAddress = _IpoPhonesPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 1, 1, 2, 1, 11),
    _IpoPhonesPhysAddress_Type()
)
ipoPhonesPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipoPhonesPhysAddress.setStatus("current")
_IpoPhonesConformance_ObjectIdentity = ObjectIdentity
ipoPhonesConformance = _IpoPhonesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2)
)
_IpoPhonesCompliances_ObjectIdentity = ObjectIdentity
ipoPhonesCompliances = _IpoPhonesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1)
)
_IpoPhonesGroups_ObjectIdentity = ObjectIdentity
ipoPhonesGroups = _IpoPhonesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2)
)

# Managed Objects groups

ipoPhonesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 1)
)
ipoPhonesGroup.setObjects(
      *(("IPO-PHONES-MIB", "ipoPhonesNumber"),
        ("IPO-PHONES-MIB", "ipoPhonesIndex"),
        ("IPO-PHONES-MIB", "ipoPhonesExtID"),
        ("IPO-PHONES-MIB", "ipoPhonesExtNumber"),
        ("IPO-PHONES-MIB", "ipoPhonesUserShort"),
        ("IPO-PHONES-MIB", "ipoPhonesUserLong"),
        ("IPO-PHONES-MIB", "ipoPhonesType"),
        ("IPO-PHONES-MIB", "ipoPhonesPort"))
)
if mibBuilder.loadTexts:
    ipoPhonesGroup.setStatus("current")

ipoPhones2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 4)
)
ipoPhones2Group.setObjects(
      *(("IPO-PHONES-MIB", "ipoPhonesPortNumber"),
        ("IPO-PHONES-MIB", "ipoPhonesModuleNumber"),
        ("IPO-PHONES-MIB", "ipoPhonesIPAddress"),
        ("IPO-PHONES-MIB", "ipoPhonesPhysAddress"))
)
if mibBuilder.loadTexts:
    ipoPhones2Group.setStatus("current")


# Notification objects

ipoPhonesChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0, 1)
)
ipoPhonesChangeEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-PHONES-MIB", "ipoPhonesExtID"),
        ("IPO-PHONES-MIB", "ipoPhonesType"),
        ("IPO-PHONES-MIB", "ipoPhonesPort"))
)
if mibBuilder.loadTexts:
    ipoPhonesChangeEvent.setStatus(
        "deprecated"
    )

ipoPhonesChangeSvcEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 0, 2)
)
ipoPhonesChangeSvcEvent.setObjects(
      *(("IPO-MIB", "ipoGTEventStdSeverity"),
        ("IPO-MIB", "ipoGTEventDateTime"),
        ("IPO-MIB", "ipoGTEventDevID"),
        ("SNMPv2-MIB", "sysDescr"),
        ("IPO-PHONES-MIB", "ipoPhonesExtID"),
        ("IPO-PHONES-MIB", "ipoPhonesType"),
        ("IPO-PHONES-MIB", "ipoPhonesPort"),
        ("IPO-MIB", "ipoGTEventEntityName"))
)
if mibBuilder.loadTexts:
    ipoPhonesChangeSvcEvent.setStatus(
        "current"
    )


# Notifications groups

ipoPhonesNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 2)
)
ipoPhonesNotificationsGroup.setObjects(
    ("IPO-PHONES-MIB", "ipoPhonesChangeEvent")
)
if mibBuilder.loadTexts:
    ipoPhonesNotificationsGroup.setStatus(
        "deprecated"
    )

ipoPhonesv2NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 2, 3)
)
ipoPhonesv2NotificationsGroup.setObjects(
    ("IPO-PHONES-MIB", "ipoPhonesChangeSvcEvent")
)
if mibBuilder.loadTexts:
    ipoPhonesv2NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ipoPhonesCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 1)
)
ipoPhonesCompliance.setObjects(
      *(("IPO-PHONES-MIB", "ipoPhonesGroup"),
        ("IPO-PHONES-MIB", "ipoPhonesNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipoPhonesCompliance.setStatus(
        "deprecated"
    )

ipoPhonesv2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 2)
)
ipoPhonesv2Compliance.setObjects(
      *(("IPO-PHONES-MIB", "ipoPhonesGroup"),
        ("IPO-PHONES-MIB", "ipoPhonesv2NotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipoPhonesv2Compliance.setStatus(
        "deprecated"
    )

ipoPhonesv3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 2, 1, 1, 1, 2, 1, 3)
)
ipoPhonesv3Compliance.setObjects(
      *(("IPO-PHONES-MIB", "ipoPhonesGroup"),
        ("IPO-PHONES-MIB", "ipoPhones2Group"),
        ("IPO-PHONES-MIB", "ipoPhonesv2NotificationsGroup"))
)
if mibBuilder.loadTexts:
    ipoPhonesv3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPO-PHONES-MIB",
    **{"PhoneType": PhoneType,
       "ipoPhonesMIB": ipoPhonesMIB,
       "ipoPhonesMibNotifications": ipoPhonesMibNotifications,
       "ipoPhonesChangeEvent": ipoPhonesChangeEvent,
       "ipoPhonesChangeSvcEvent": ipoPhonesChangeSvcEvent,
       "ipoPhonesMibObjects": ipoPhonesMibObjects,
       "ipoPhones": ipoPhones,
       "ipoPhonesNumber": ipoPhonesNumber,
       "ipoPhonesTable": ipoPhonesTable,
       "ipoPhonesEntry": ipoPhonesEntry,
       "ipoPhonesIndex": ipoPhonesIndex,
       "ipoPhonesExtID": ipoPhonesExtID,
       "ipoPhonesExtNumber": ipoPhonesExtNumber,
       "ipoPhonesUserShort": ipoPhonesUserShort,
       "ipoPhonesUserLong": ipoPhonesUserLong,
       "ipoPhonesType": ipoPhonesType,
       "ipoPhonesPort": ipoPhonesPort,
       "ipoPhonesPortNumber": ipoPhonesPortNumber,
       "ipoPhonesModuleNumber": ipoPhonesModuleNumber,
       "ipoPhonesIPAddress": ipoPhonesIPAddress,
       "ipoPhonesPhysAddress": ipoPhonesPhysAddress,
       "ipoPhonesConformance": ipoPhonesConformance,
       "ipoPhonesCompliances": ipoPhonesCompliances,
       "ipoPhonesCompliance": ipoPhonesCompliance,
       "ipoPhonesv2Compliance": ipoPhonesv2Compliance,
       "ipoPhonesv3Compliance": ipoPhonesv3Compliance,
       "ipoPhonesGroups": ipoPhonesGroups,
       "ipoPhonesGroup": ipoPhonesGroup,
       "ipoPhonesNotificationsGroup": ipoPhonesNotificationsGroup,
       "ipoPhonesv2NotificationsGroup": ipoPhonesv2NotificationsGroup,
       "ipoPhones2Group": ipoPhones2Group}
)
