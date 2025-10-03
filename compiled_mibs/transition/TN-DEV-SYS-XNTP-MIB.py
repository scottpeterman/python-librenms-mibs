# SNMP MIB module (TN-DEV-SYS-XNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DEV-SYS-XNTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:11 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnDevMgmt,) = mibBuilder.importSymbols(
    "TN-MGMT-MIB",
    "tnDevMgmt")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDevSysxNTP_ObjectIdentity = ObjectIdentity
tnDevSysxNTP = _TnDevSysxNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11)
)
_TnxNTPClientMgmtTable_Object = MibTable
tnxNTPClientMgmtTable = _TnxNTPClientMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tnxNTPClientMgmtTable.setStatus("current")
_TnxNTPClientMgmtEntry_Object = MibTableRow
tnxNTPClientMgmtEntry = _TnxNTPClientMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1)
)
tnxNTPClientMgmtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnxNTPClientMgmtEntry.setStatus("current")


class _TnxNTPClientStatus_Type(Integer32):
    """Custom type tnxNTPClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_TnxNTPClientStatus_Type.__name__ = "Integer32"
_TnxNTPClientStatus_Object = MibTableColumn
tnxNTPClientStatus = _TnxNTPClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1, 1),
    _TnxNTPClientStatus_Type()
)
tnxNTPClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPClientStatus.setStatus("current")


class _TnxNTPDaylightSavingTime_Type(Integer32):
    """Custom type tnxNTPDaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnxNTPDaylightSavingTime_Type.__name__ = "Integer32"
_TnxNTPDaylightSavingTime_Object = MibTableColumn
tnxNTPDaylightSavingTime = _TnxNTPDaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1, 2),
    _TnxNTPDaylightSavingTime_Type()
)
tnxNTPDaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPDaylightSavingTime.setStatus("current")


class _TnxNTPUTCTimezone_Type(Integer32):
    """Custom type tnxNTPUTCTimezone based on Integer32"""
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
              63)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("gmt-negative-12-00-Eniwetok-Kwajalein", 1),
          ("gmt-negative-11-00-Midway-Island-Samoa", 2),
          ("gmt-negative-10-00-Hawaii", 3),
          ("gmt-negative-09-00-Alaska", 4),
          ("gmt-negative-08-00-Pacific-Time-US-and-Canada-Tijuana", 5),
          ("gmt-negative-07-00-Arizona", 6),
          ("gmt-negative-07-00-Mountain-Time-US-and-Canada", 7),
          ("gmt-negative-06-00-Central-Time-US-and-Canada", 8),
          ("gmt-negative-06-00-Mexico-City-Tegucigalpa", 9),
          ("gmt-negative-06-00-Saskatchewan", 10),
          ("gmt-negative-05-00-Bogota-Lima-Quito", 11),
          ("gmt-negative-05-00-Eastern-Time-US-and-Canada", 12),
          ("gmt-negative-05-00-Indiana-East", 13),
          ("gmt-negative-04-00-Atlantic-Time-Canada", 14),
          ("gmt-negative-04-00-Caracas-La-Paz", 15),
          ("gmt-negative-04-00-Santiago", 16),
          ("gmt-negative-03-30-Newfoundland", 17),
          ("gmt-negative-03-00-Brasilia", 18),
          ("gmt-negative-03-00-Buenos-Aires-Georgetown", 19),
          ("gmt-negative-02-00-Mid-Atlantic", 20),
          ("gmt-negative-01-00-Azores-Cape-Verde-Is", 21),
          ("gmt-Casablanca-Monrovia", 22),
          ("gmt-Greenwich-Mean-Time-Dublin-Edinburgh-Lisbon-London", 23),
          ("gmt-positive-01-00-Amsterdam-Berlin-Bern-Rome-Stockholm-Vienna", 24),
          ("gmt-positive-01-00-Belgrade-Bratislava-Budapest-Ljubljana-Prague", 25),
          ("gmt-positive-01-00-Brussels-Copenhagen-Madrid-Paris-Vilnius", 26),
          ("gmt-positive-01-00-Sarajevo-Skopje-Sofija-Warsaw-Zagreb", 27),
          ("gmt-positive-02-00-Athens-Istanbul-Minsk", 28),
          ("gmt-positive-02-00-Bucharest", 29),
          ("gmt-positive-02-00-Cairo", 30),
          ("gmt-positive-02-00-Harare-Pretoria", 31),
          ("gmt-positive-02-00-Helsinki-Riga-Tallinn", 32),
          ("gmt-positive-02-00-Jerusalem", 33),
          ("gmt-positive-03-00-Baghdad-Kuwait-Riyadh", 34),
          ("gmt-positive-03-00-Moscow-St-Petersburg-Volgograd", 35),
          ("gmt-positive-03-00-Mairobi", 36),
          ("gmt-positive-03-30-Tehran", 37),
          ("gmt-positive-04-00-Abu-Dhabi-Muscat", 38),
          ("gmt-positive-04-00-Baku-Tbilisi", 39),
          ("gmt-positive-04-30-Kabul", 40),
          ("gmt-positive-05-00-Ekaterinburg", 41),
          ("gmt-positive-05-00-Islamabad-Karachi-Tashkent", 42),
          ("gmt-positive-05-30-Bombay-Calcutta-Madras-New-Delhi", 43),
          ("gmt-positive-06-00-Astana-Almaty-Dhaka", 44),
          ("gmt-positive-06-00-Colombo", 45),
          ("gmt-positive-07-00-Bangkok-Hanoi-Jakarta", 46),
          ("gmt-positive-08-00-Beijing-Chongqing-Hong-Kong-Urumqi", 47),
          ("gmt-positive-08-00-Perth", 48),
          ("gmt-positive-08-00-Singapore", 49),
          ("gmt-positive-08-00-Taipei", 50),
          ("gmt-positive-09-00-Osaka-Sapporo-Tokyo", 51),
          ("gmt-positive-09-00-Seoul", 52),
          ("gmt-positive-09-00-Yakutsk", 53),
          ("gmt-positive-09-30-Adelaide", 54),
          ("gmt-positive-09-30-Darwin", 55),
          ("gmt-positive-10-00-Brisbane", 56),
          ("gmt-positive-10-00-Canberra-Melbourne-Sydney", 57),
          ("gmt-positive-10-00-Guam-Port-Moresby", 58),
          ("gmt-positive-10-00-Hobart", 59),
          ("gmt-positive-10-00-Vladivostok", 60),
          ("gmt-positive-11-00-Magadan-Solomon-Is-New-Caledonia", 61),
          ("gmt-positive-12-00-Auckland-Wllington", 62),
          ("gmt-positive-12-00-Fiji-Kamchatka-Marshall-Is", 63))
    )


_TnxNTPUTCTimezone_Type.__name__ = "Integer32"
_TnxNTPUTCTimezone_Object = MibTableColumn
tnxNTPUTCTimezone = _TnxNTPUTCTimezone_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1, 3),
    _TnxNTPUTCTimezone_Type()
)
tnxNTPUTCTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPUTCTimezone.setStatus("current")


class _TnxNTPDeviceTimer_Type(DisplayString):
    """Custom type tnxNTPDeviceTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnxNTPDeviceTimer_Type.__name__ = "DisplayString"
_TnxNTPDeviceTimer_Object = MibTableColumn
tnxNTPDeviceTimer = _TnxNTPDeviceTimer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1, 4),
    _TnxNTPDeviceTimer_Type()
)
tnxNTPDeviceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPDeviceTimer.setStatus("current")


class _TnxNTPDaylightSavingPeriodStart_Type(DisplayString):
    """Custom type tnxNTPDaylightSavingPeriodStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnxNTPDaylightSavingPeriodStart_Type.__name__ = "DisplayString"
_TnxNTPDaylightSavingPeriodStart_Object = MibTableColumn
tnxNTPDaylightSavingPeriodStart = _TnxNTPDaylightSavingPeriodStart_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1, 5),
    _TnxNTPDaylightSavingPeriodStart_Type()
)
tnxNTPDaylightSavingPeriodStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPDaylightSavingPeriodStart.setStatus("current")


class _TnxNTPDaylightSavingPeriodEnd_Type(DisplayString):
    """Custom type tnxNTPDaylightSavingPeriodEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnxNTPDaylightSavingPeriodEnd_Type.__name__ = "DisplayString"
_TnxNTPDaylightSavingPeriodEnd_Object = MibTableColumn
tnxNTPDaylightSavingPeriodEnd = _TnxNTPDaylightSavingPeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1, 6),
    _TnxNTPDaylightSavingPeriodEnd_Type()
)
tnxNTPDaylightSavingPeriodEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPDaylightSavingPeriodEnd.setStatus("current")
_TnxNTPDaylightSavingOffset_Type = Integer32
_TnxNTPDaylightSavingOffset_Object = MibTableColumn
tnxNTPDaylightSavingOffset = _TnxNTPDaylightSavingOffset_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1, 7),
    _TnxNTPDaylightSavingOffset_Type()
)
tnxNTPDaylightSavingOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPDaylightSavingOffset.setStatus("current")


class _TnxNTPDaylightSavingTimeMode_Type(Integer32):
    """Custom type tnxNTPDaylightSavingTimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("recurring", 1),
          ("nonrecurring", 2))
    )


_TnxNTPDaylightSavingTimeMode_Type.__name__ = "Integer32"
_TnxNTPDaylightSavingTimeMode_Object = MibTableColumn
tnxNTPDaylightSavingTimeMode = _TnxNTPDaylightSavingTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 1, 1, 8),
    _TnxNTPDaylightSavingTimeMode_Type()
)
tnxNTPDaylightSavingTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPDaylightSavingTimeMode.setStatus("current")
_TnxNTPServerTable_Object = MibTable
tnxNTPServerTable = _TnxNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    tnxNTPServerTable.setStatus("current")
_TnxNTPServerEntry_Object = MibTableRow
tnxNTPServerEntry = _TnxNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 2, 1)
)
tnxNTPServerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-DEV-SYS-XNTP-MIB", "tnxNTPServerIndex"),
)
if mibBuilder.loadTexts:
    tnxNTPServerEntry.setStatus("current")
_TnxNTPServerIndex_Type = Integer32
_TnxNTPServerIndex_Object = MibTableColumn
tnxNTPServerIndex = _TnxNTPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 2, 1, 1),
    _TnxNTPServerIndex_Type()
)
tnxNTPServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnxNTPServerIndex.setStatus("current")
_TnxNTPServerIPAddrType_Type = InetAddressType
_TnxNTPServerIPAddrType_Object = MibTableColumn
tnxNTPServerIPAddrType = _TnxNTPServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 2, 1, 2),
    _TnxNTPServerIPAddrType_Type()
)
tnxNTPServerIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPServerIPAddrType.setStatus("current")
_TnxNTPServerIPAddr_Type = InetAddress
_TnxNTPServerIPAddr_Object = MibTableColumn
tnxNTPServerIPAddr = _TnxNTPServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 2, 1, 3),
    _TnxNTPServerIPAddr_Type()
)
tnxNTPServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnxNTPServerIPAddr.setStatus("current")
_TnxNTPServerStatus_Type = RowStatus
_TnxNTPServerStatus_Object = MibTableColumn
tnxNTPServerStatus = _TnxNTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 3, 1, 1, 11, 2, 1, 4),
    _TnxNTPServerStatus_Type()
)
tnxNTPServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnxNTPServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DEV-SYS-XNTP-MIB",
    **{"tnDevSysxNTP": tnDevSysxNTP,
       "tnxNTPClientMgmtTable": tnxNTPClientMgmtTable,
       "tnxNTPClientMgmtEntry": tnxNTPClientMgmtEntry,
       "tnxNTPClientStatus": tnxNTPClientStatus,
       "tnxNTPDaylightSavingTime": tnxNTPDaylightSavingTime,
       "tnxNTPUTCTimezone": tnxNTPUTCTimezone,
       "tnxNTPDeviceTimer": tnxNTPDeviceTimer,
       "tnxNTPDaylightSavingPeriodStart": tnxNTPDaylightSavingPeriodStart,
       "tnxNTPDaylightSavingPeriodEnd": tnxNTPDaylightSavingPeriodEnd,
       "tnxNTPDaylightSavingOffset": tnxNTPDaylightSavingOffset,
       "tnxNTPDaylightSavingTimeMode": tnxNTPDaylightSavingTimeMode,
       "tnxNTPServerTable": tnxNTPServerTable,
       "tnxNTPServerEntry": tnxNTPServerEntry,
       "tnxNTPServerIndex": tnxNTPServerIndex,
       "tnxNTPServerIPAddrType": tnxNTPServerIPAddrType,
       "tnxNTPServerIPAddr": tnxNTPServerIPAddr,
       "tnxNTPServerStatus": tnxNTPServerStatus}
)
