# SNMP MIB module (MOXA-AWK4131A-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-AWK4131A-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:59 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

awk4131A = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_IndustrialWirelessLan_ObjectIdentity = ObjectIdentity
industrialWirelessLan = _IndustrialWirelessLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15)
)
_AwkTraps_ObjectIdentity = ObjectIdentity
awkTraps = _AwkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 0)
)
_SwMgmt_ObjectIdentity = ObjectIdentity
swMgmt = _SwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1)
)
_Overview_ObjectIdentity = ObjectIdentity
overview = _Overview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1)
)
_OverviewModelName_Type = DisplayString
_OverviewModelName_Object = MibScalar
overviewModelName = _OverviewModelName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 1),
    _OverviewModelName_Type()
)
overviewModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overviewModelName.setStatus("current")
_OverviewDeviceName_Type = DisplayString
_OverviewDeviceName_Object = MibScalar
overviewDeviceName = _OverviewDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 2),
    _OverviewDeviceName_Type()
)
overviewDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overviewDeviceName.setStatus("current")
_OverviewSerialNumber_Type = DisplayString
_OverviewSerialNumber_Object = MibScalar
overviewSerialNumber = _OverviewSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 3),
    _OverviewSerialNumber_Type()
)
overviewSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overviewSerialNumber.setStatus("current")
_OverviewUpTime_Type = DisplayString
_OverviewUpTime_Object = MibScalar
overviewUpTime = _OverviewUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 4),
    _OverviewUpTime_Type()
)
overviewUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overviewUpTime.setStatus("current")
_OverviewFirmwareVersion_Type = DisplayString
_OverviewFirmwareVersion_Object = MibScalar
overviewFirmwareVersion = _OverviewFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 5),
    _OverviewFirmwareVersion_Type()
)
overviewFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overviewFirmwareVersion.setStatus("current")
_OverviewMacAddress_Type = DisplayString
_OverviewMacAddress_Object = MibScalar
overviewMacAddress = _OverviewMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 6),
    _OverviewMacAddress_Type()
)
overviewMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overviewMacAddress.setStatus("current")
_OverviewDeviceLocation_Type = DisplayString
_OverviewDeviceLocation_Object = MibScalar
overviewDeviceLocation = _OverviewDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 9),
    _OverviewDeviceLocation_Type()
)
overviewDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overviewDeviceLocation.setStatus("current")
_OverviewDeviceDescription_Type = DisplayString
_OverviewDeviceDescription_Object = MibScalar
overviewDeviceDescription = _OverviewDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 10),
    _OverviewDeviceDescription_Type()
)
overviewDeviceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overviewDeviceDescription.setStatus("current")
_OverviewDeviceContactInfo_Type = DisplayString
_OverviewDeviceContactInfo_Object = MibScalar
overviewDeviceContactInfo = _OverviewDeviceContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 11),
    _OverviewDeviceContactInfo_Type()
)
overviewDeviceContactInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overviewDeviceContactInfo.setStatus("current")
_OverviewWebLoginMessage_Type = DisplayString
_OverviewWebLoginMessage_Object = MibScalar
overviewWebLoginMessage = _OverviewWebLoginMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 30),
    _OverviewWebLoginMessage_Type()
)
overviewWebLoginMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overviewWebLoginMessage.setStatus("current")
_OverviewWebLoginFailMessage_Type = DisplayString
_OverviewWebLoginFailMessage_Object = MibScalar
overviewWebLoginFailMessage = _OverviewWebLoginFailMessage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 1, 31),
    _OverviewWebLoginFailMessage_Type()
)
overviewWebLoginFailMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overviewWebLoginFailMessage.setStatus("current")
_Basic_ObjectIdentity = ObjectIdentity
basic = _Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3)
)
_NetDev_ObjectIdentity = ObjectIdentity
netDev = _NetDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1)
)


class _NetDevDhcpEnable_Type(Integer32):
    """Custom type netDevDhcpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_NetDevDhcpEnable_Type.__name__ = "Integer32"
_NetDevDhcpEnable_Object = MibScalar
netDevDhcpEnable = _NetDevDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1, 1),
    _NetDevDhcpEnable_Type()
)
netDevDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevDhcpEnable.setStatus("current")
_NetDevIpV4Addr_Type = IpAddress
_NetDevIpV4Addr_Object = MibScalar
netDevIpV4Addr = _NetDevIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1, 2),
    _NetDevIpV4Addr_Type()
)
netDevIpV4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevIpV4Addr.setStatus("current")
_NetDevIpV4Mask_Type = IpAddress
_NetDevIpV4Mask_Object = MibScalar
netDevIpV4Mask = _NetDevIpV4Mask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1, 3),
    _NetDevIpV4Mask_Type()
)
netDevIpV4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevIpV4Mask.setStatus("current")
_NetDevIpV4Gateway_Type = IpAddress
_NetDevIpV4Gateway_Object = MibScalar
netDevIpV4Gateway = _NetDevIpV4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1, 4),
    _NetDevIpV4Gateway_Type()
)
netDevIpV4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevIpV4Gateway.setStatus("current")
_NetDevIpV4DnsTable_Object = MibTable
netDevIpV4DnsTable = _NetDevIpV4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    netDevIpV4DnsTable.setStatus("current")
_NetDevIpV4DnsEntry_Object = MibTableRow
netDevIpV4DnsEntry = _NetDevIpV4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1, 5, 1)
)
netDevIpV4DnsEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "netDevIpV4DnsIndex"),
)
if mibBuilder.loadTexts:
    netDevIpV4DnsEntry.setStatus("current")


class _NetDevIpV4DnsIndex_Type(Integer32):
    """Custom type netDevIpV4DnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NetDevIpV4DnsIndex_Type.__name__ = "Integer32"
_NetDevIpV4DnsIndex_Object = MibTableColumn
netDevIpV4DnsIndex = _NetDevIpV4DnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1, 5, 1, 1),
    _NetDevIpV4DnsIndex_Type()
)
netDevIpV4DnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netDevIpV4DnsIndex.setStatus("current")
_NetDevIpV4DnsData_Type = IpAddress
_NetDevIpV4DnsData_Object = MibTableColumn
netDevIpV4DnsData = _NetDevIpV4DnsData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 1, 5, 1, 2),
    _NetDevIpV4DnsData_Type()
)
netDevIpV4DnsData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevIpV4DnsData.setStatus("current")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2)
)
_TimeNow_Type = Integer32
_TimeNow_Object = MibScalar
timeNow = _TimeNow_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 1),
    _TimeNow_Type()
)
timeNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNow.setStatus("current")


class _TimeTimeZone_Type(Integer32):
    """Custom type timeTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_TimeTimeZone_Type.__name__ = "Integer32"
_TimeTimeZone_Object = MibScalar
timeTimeZone = _TimeTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 2),
    _TimeTimeZone_Type()
)
timeTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeTimeZone.setStatus("current")
_TimeTimeServerTable_Object = MibTable
timeTimeServerTable = _TimeTimeServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    timeTimeServerTable.setStatus("current")
_TimeTimeServerEntry_Object = MibTableRow
timeTimeServerEntry = _TimeTimeServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 3, 1)
)
timeTimeServerEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "timeTimeServerIndex"),
)
if mibBuilder.loadTexts:
    timeTimeServerEntry.setStatus("current")


class _TimeTimeServerIndex_Type(Integer32):
    """Custom type timeTimeServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TimeTimeServerIndex_Type.__name__ = "Integer32"
_TimeTimeServerIndex_Object = MibTableColumn
timeTimeServerIndex = _TimeTimeServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 3, 1, 1),
    _TimeTimeServerIndex_Type()
)
timeTimeServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeTimeServerIndex.setStatus("current")
_TimeTimeServerData_Type = DisplayString
_TimeTimeServerData_Object = MibTableColumn
timeTimeServerData = _TimeTimeServerData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 3, 1, 2),
    _TimeTimeServerData_Type()
)
timeTimeServerData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeTimeServerData.setStatus("current")


class _TimeQueryPeriod_Type(Integer32):
    """Custom type timeQueryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 9999),
    )


_TimeQueryPeriod_Type.__name__ = "Integer32"
_TimeQueryPeriod_Object = MibScalar
timeQueryPeriod = _TimeQueryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 4),
    _TimeQueryPeriod_Type()
)
timeQueryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeQueryPeriod.setStatus("current")


class _TimeDaylightSavingEnable_Type(Integer32):
    """Custom type timeDaylightSavingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TimeDaylightSavingEnable_Type.__name__ = "Integer32"
_TimeDaylightSavingEnable_Object = MibScalar
timeDaylightSavingEnable = _TimeDaylightSavingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 5),
    _TimeDaylightSavingEnable_Type()
)
timeDaylightSavingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingEnable.setStatus("current")


class _TimeDaylightSavingStartMonth_Type(Integer32):
    """Custom type timeDaylightSavingStartMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("january", 1),
          ("february", 2),
          ("march", 3),
          ("april", 4),
          ("may", 5),
          ("june", 6),
          ("july", 7),
          ("augest", 8),
          ("september", 9),
          ("october", 10),
          ("november", 11),
          ("december", 12))
    )


_TimeDaylightSavingStartMonth_Type.__name__ = "Integer32"
_TimeDaylightSavingStartMonth_Object = MibScalar
timeDaylightSavingStartMonth = _TimeDaylightSavingStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 6),
    _TimeDaylightSavingStartMonth_Type()
)
timeDaylightSavingStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStartMonth.setStatus("current")


class _TimeDaylightSavingStartWeekIndex_Type(Integer32):
    """Custom type timeDaylightSavingStartWeekIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_TimeDaylightSavingStartWeekIndex_Type.__name__ = "Integer32"
_TimeDaylightSavingStartWeekIndex_Object = MibScalar
timeDaylightSavingStartWeekIndex = _TimeDaylightSavingStartWeekIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 7),
    _TimeDaylightSavingStartWeekIndex_Type()
)
timeDaylightSavingStartWeekIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStartWeekIndex.setStatus("current")


class _TimeDaylightSavingStartWeekday_Type(Integer32):
    """Custom type timeDaylightSavingStartWeekday based on Integer32"""
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
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_TimeDaylightSavingStartWeekday_Type.__name__ = "Integer32"
_TimeDaylightSavingStartWeekday_Object = MibScalar
timeDaylightSavingStartWeekday = _TimeDaylightSavingStartWeekday_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 8),
    _TimeDaylightSavingStartWeekday_Type()
)
timeDaylightSavingStartWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStartWeekday.setStatus("current")


class _TimeDaylightSavingStartHour_Type(Integer32):
    """Custom type timeDaylightSavingStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeDaylightSavingStartHour_Type.__name__ = "Integer32"
_TimeDaylightSavingStartHour_Object = MibScalar
timeDaylightSavingStartHour = _TimeDaylightSavingStartHour_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 9),
    _TimeDaylightSavingStartHour_Type()
)
timeDaylightSavingStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStartHour.setStatus("current")


class _TimeDaylightSavingStartMin_Type(Integer32):
    """Custom type timeDaylightSavingStartMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeDaylightSavingStartMin_Type.__name__ = "Integer32"
_TimeDaylightSavingStartMin_Object = MibScalar
timeDaylightSavingStartMin = _TimeDaylightSavingStartMin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 10),
    _TimeDaylightSavingStartMin_Type()
)
timeDaylightSavingStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStartMin.setStatus("current")


class _TimeDaylightSavingStopMonth_Type(Integer32):
    """Custom type timeDaylightSavingStopMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("january", 1),
          ("february", 2),
          ("march", 3),
          ("april", 4),
          ("may", 5),
          ("june", 6),
          ("july", 7),
          ("augest", 8),
          ("september", 9),
          ("october", 10),
          ("november", 11),
          ("december", 12))
    )


_TimeDaylightSavingStopMonth_Type.__name__ = "Integer32"
_TimeDaylightSavingStopMonth_Object = MibScalar
timeDaylightSavingStopMonth = _TimeDaylightSavingStopMonth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 11),
    _TimeDaylightSavingStopMonth_Type()
)
timeDaylightSavingStopMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStopMonth.setStatus("current")


class _TimeDaylightSavingStopWeekIndex_Type(Integer32):
    """Custom type timeDaylightSavingStopWeekIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3),
          ("fourth", 4),
          ("last", 5))
    )


_TimeDaylightSavingStopWeekIndex_Type.__name__ = "Integer32"
_TimeDaylightSavingStopWeekIndex_Object = MibScalar
timeDaylightSavingStopWeekIndex = _TimeDaylightSavingStopWeekIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 12),
    _TimeDaylightSavingStopWeekIndex_Type()
)
timeDaylightSavingStopWeekIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStopWeekIndex.setStatus("current")


class _TimeDaylightSavingStopWeekday_Type(Integer32):
    """Custom type timeDaylightSavingStopWeekday based on Integer32"""
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
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_TimeDaylightSavingStopWeekday_Type.__name__ = "Integer32"
_TimeDaylightSavingStopWeekday_Object = MibScalar
timeDaylightSavingStopWeekday = _TimeDaylightSavingStopWeekday_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 13),
    _TimeDaylightSavingStopWeekday_Type()
)
timeDaylightSavingStopWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStopWeekday.setStatus("current")


class _TimeDaylightSavingStophour_Type(Integer32):
    """Custom type timeDaylightSavingStophour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_TimeDaylightSavingStophour_Type.__name__ = "Integer32"
_TimeDaylightSavingStophour_Object = MibScalar
timeDaylightSavingStophour = _TimeDaylightSavingStophour_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 14),
    _TimeDaylightSavingStophour_Type()
)
timeDaylightSavingStophour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStophour.setStatus("current")


class _TimeDaylightSavingStopMin_Type(Integer32):
    """Custom type timeDaylightSavingStopMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_TimeDaylightSavingStopMin_Type.__name__ = "Integer32"
_TimeDaylightSavingStopMin_Object = MibScalar
timeDaylightSavingStopMin = _TimeDaylightSavingStopMin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 15),
    _TimeDaylightSavingStopMin_Type()
)
timeDaylightSavingStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingStopMin.setStatus("current")


class _TimeDaylightSavingTimeOffset_Type(Integer32):
    """Custom type timeDaylightSavingTimeOffset based on Integer32"""
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
        *(("plus30min", 1),
          ("plus60min", 2),
          ("plus90min", 3),
          ("plus120min", 4))
    )


_TimeDaylightSavingTimeOffset_Type.__name__ = "Integer32"
_TimeDaylightSavingTimeOffset_Object = MibScalar
timeDaylightSavingTimeOffset = _TimeDaylightSavingTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 16),
    _TimeDaylightSavingTimeOffset_Type()
)
timeDaylightSavingTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeDaylightSavingTimeOffset.setStatus("current")


class _TimeNtpOption_Type(Integer32):
    """Custom type timeNtpOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sntp", 1)
    )


_TimeNtpOption_Type.__name__ = "Integer32"
_TimeNtpOption_Object = MibScalar
timeNtpOption = _TimeNtpOption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 2, 17),
    _TimeNtpOption_Type()
)
timeNtpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeNtpOption.setStatus("current")
_NetDevWlan_ObjectIdentity = ObjectIdentity
netDevWlan = _NetDevWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3)
)


class _NetDevWlanDhcpEnable_Type(Integer32):
    """Custom type netDevWlanDhcpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_NetDevWlanDhcpEnable_Type.__name__ = "Integer32"
_NetDevWlanDhcpEnable_Object = MibScalar
netDevWlanDhcpEnable = _NetDevWlanDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3, 1),
    _NetDevWlanDhcpEnable_Type()
)
netDevWlanDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevWlanDhcpEnable.setStatus("current")
_NetDevWlanIpV4Addr_Type = IpAddress
_NetDevWlanIpV4Addr_Object = MibScalar
netDevWlanIpV4Addr = _NetDevWlanIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3, 2),
    _NetDevWlanIpV4Addr_Type()
)
netDevWlanIpV4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevWlanIpV4Addr.setStatus("current")
_NetDevWlanIpV4Mask_Type = IpAddress
_NetDevWlanIpV4Mask_Object = MibScalar
netDevWlanIpV4Mask = _NetDevWlanIpV4Mask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3, 3),
    _NetDevWlanIpV4Mask_Type()
)
netDevWlanIpV4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevWlanIpV4Mask.setStatus("current")
_NetDevWlanIpV4Gateway_Type = IpAddress
_NetDevWlanIpV4Gateway_Object = MibScalar
netDevWlanIpV4Gateway = _NetDevWlanIpV4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3, 4),
    _NetDevWlanIpV4Gateway_Type()
)
netDevWlanIpV4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevWlanIpV4Gateway.setStatus("current")
_NetDevWlanIpV4DnsTable_Object = MibTable
netDevWlanIpV4DnsTable = _NetDevWlanIpV4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    netDevWlanIpV4DnsTable.setStatus("current")
_NetDevWlanIpV4DnsEntry_Object = MibTableRow
netDevWlanIpV4DnsEntry = _NetDevWlanIpV4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3, 5, 1)
)
netDevWlanIpV4DnsEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "netDevWlanIpV4DnsIndex"),
)
if mibBuilder.loadTexts:
    netDevWlanIpV4DnsEntry.setStatus("current")


class _NetDevWlanIpV4DnsIndex_Type(Integer32):
    """Custom type netDevWlanIpV4DnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NetDevWlanIpV4DnsIndex_Type.__name__ = "Integer32"
_NetDevWlanIpV4DnsIndex_Object = MibTableColumn
netDevWlanIpV4DnsIndex = _NetDevWlanIpV4DnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3, 5, 1, 1),
    _NetDevWlanIpV4DnsIndex_Type()
)
netDevWlanIpV4DnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netDevWlanIpV4DnsIndex.setStatus("current")
_NetDevWlanIpV4DnsData_Type = IpAddress
_NetDevWlanIpV4DnsData_Object = MibTableColumn
netDevWlanIpV4DnsData = _NetDevWlanIpV4DnsData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 3, 5, 1, 2),
    _NetDevWlanIpV4DnsData_Type()
)
netDevWlanIpV4DnsData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevWlanIpV4DnsData.setStatus("current")
_NetDevLan_ObjectIdentity = ObjectIdentity
netDevLan = _NetDevLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 4)
)


class _NetDevLanDhcpEnable_Type(Integer32):
    """Custom type netDevLanDhcpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_NetDevLanDhcpEnable_Type.__name__ = "Integer32"
_NetDevLanDhcpEnable_Object = MibScalar
netDevLanDhcpEnable = _NetDevLanDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 4, 1),
    _NetDevLanDhcpEnable_Type()
)
netDevLanDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevLanDhcpEnable.setStatus("current")
_NetDevLanIpV4Addr_Type = IpAddress
_NetDevLanIpV4Addr_Object = MibScalar
netDevLanIpV4Addr = _NetDevLanIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 4, 2),
    _NetDevLanIpV4Addr_Type()
)
netDevLanIpV4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevLanIpV4Addr.setStatus("current")
_NetDevLanIpV4Mask_Type = IpAddress
_NetDevLanIpV4Mask_Object = MibScalar
netDevLanIpV4Mask = _NetDevLanIpV4Mask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 3, 4, 3),
    _NetDevLanIpV4Mask_Type()
)
netDevLanIpV4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDevLanIpV4Mask.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5)
)
_DevTable_Object = MibTable
devTable = _DevTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1)
)
if mibBuilder.loadTexts:
    devTable.setStatus("current")
_DevEntry_Object = MibTableRow
devEntry = _DevEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1)
)
devEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "devIndex"),
)
if mibBuilder.loadTexts:
    devEntry.setStatus("current")


class _DevIndex_Type(Integer32):
    """Custom type devIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DevIndex_Type.__name__ = "Integer32"
_DevIndex_Object = MibTableColumn
devIndex = _DevIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 1),
    _DevIndex_Type()
)
devIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIndex.setStatus("current")
_DevChannelA_Type = Integer32
_DevChannelA_Object = MibTableColumn
devChannelA = _DevChannelA_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 2),
    _DevChannelA_Type()
)
devChannelA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devChannelA.setStatus("current")
_DevChannelB_Type = Integer32
_DevChannelB_Object = MibTableColumn
devChannelB = _DevChannelB_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 3),
    _DevChannelB_Type()
)
devChannelB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devChannelB.setStatus("current")
_DevChannelG_Type = Integer32
_DevChannelG_Object = MibTableColumn
devChannelG = _DevChannelG_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 4),
    _DevChannelG_Type()
)
devChannelG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devChannelG.setStatus("current")
_DevChannelListA_Type = DisplayString
_DevChannelListA_Object = MibTableColumn
devChannelListA = _DevChannelListA_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 5),
    _DevChannelListA_Type()
)
devChannelListA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devChannelListA.setStatus("current")
_DevChannelListB_Type = DisplayString
_DevChannelListB_Object = MibTableColumn
devChannelListB = _DevChannelListB_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 6),
    _DevChannelListB_Type()
)
devChannelListB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devChannelListB.setStatus("current")
_DevChannelListG_Type = DisplayString
_DevChannelListG_Object = MibTableColumn
devChannelListG = _DevChannelListG_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 7),
    _DevChannelListG_Type()
)
devChannelListG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devChannelListG.setStatus("current")


class _DevRfType_Type(Integer32):
    """Custom type devRfType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bg", 1),
          ("a", 2),
          ("b", 3),
          ("g", 4),
          ("gn", 5),
          ("bgn", 6),
          ("an", 7),
          ("n24GHz", 8),
          ("n5GHz", 9))
    )


_DevRfType_Type.__name__ = "Integer32"
_DevRfType_Object = MibTableColumn
devRfType = _DevRfType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 8),
    _DevRfType_Type()
)
devRfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRfType.setStatus("current")
_DevCountryCode_Type = DisplayString
_DevCountryCode_Object = MibTableColumn
devCountryCode = _DevCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 9),
    _DevCountryCode_Type()
)
devCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devCountryCode.setStatus("current")


class _DevTXrateA_Type(Integer32):
    """Custom type devTXrateA based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate6M", 2),
          ("rate9M", 3),
          ("rate12M", 4),
          ("rate18M", 5),
          ("rate24M", 6),
          ("rate36M", 7),
          ("rate48M", 8),
          ("rate54M", 9))
    )


_DevTXrateA_Type.__name__ = "Integer32"
_DevTXrateA_Object = MibTableColumn
devTXrateA = _DevTXrateA_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 10),
    _DevTXrateA_Type()
)
devTXrateA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTXrateA.setStatus("current")


class _DevTXrateB_Type(Integer32):
    """Custom type devTXrateB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate1M", 2),
          ("rate2M", 3),
          ("rate5-5M", 4),
          ("rate11M", 5))
    )


_DevTXrateB_Type.__name__ = "Integer32"
_DevTXrateB_Object = MibTableColumn
devTXrateB = _DevTXrateB_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 11),
    _DevTXrateB_Type()
)
devTXrateB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTXrateB.setStatus("current")


class _DevTXrateG_Type(Integer32):
    """Custom type devTXrateG based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate6M", 2),
          ("rate9M", 3),
          ("rate12M", 4),
          ("rate18M", 5),
          ("rate24M", 6),
          ("rate36M", 7),
          ("rate48M", 8),
          ("rate54M", 9))
    )


_DevTXrateG_Type.__name__ = "Integer32"
_DevTXrateG_Object = MibTableColumn
devTXrateG = _DevTXrateG_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 12),
    _DevTXrateG_Type()
)
devTXrateG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTXrateG.setStatus("current")


class _DevTXrateBG_Type(Integer32):
    """Custom type devTXrateBG based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate1M", 2),
          ("rate2M", 3),
          ("rate5-5M", 4),
          ("rate6M", 5),
          ("rate9M", 6),
          ("rate11M", 7),
          ("rate12M", 8),
          ("rate18M", 9),
          ("rate24M", 10),
          ("rate36M", 11),
          ("rate48M", 12),
          ("rate54M", 13))
    )


_DevTXrateBG_Type.__name__ = "Integer32"
_DevTXrateBG_Object = MibTableColumn
devTXrateBG = _DevTXrateBG_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 13),
    _DevTXrateBG_Type()
)
devTXrateBG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTXrateBG.setStatus("current")


class _DevBeaconInterval_Type(Integer32):
    """Custom type devBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 1000),
    )


_DevBeaconInterval_Type.__name__ = "Integer32"
_DevBeaconInterval_Object = MibTableColumn
devBeaconInterval = _DevBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 15),
    _DevBeaconInterval_Type()
)
devBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devBeaconInterval.setStatus("current")


class _DevDTIMinterval_Type(Integer32):
    """Custom type devDTIMinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DevDTIMinterval_Type.__name__ = "Integer32"
_DevDTIMinterval_Object = MibTableColumn
devDTIMinterval = _DevDTIMinterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 16),
    _DevDTIMinterval_Type()
)
devDTIMinterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDTIMinterval.setStatus("current")


class _DevFragThresh_Type(Integer32):
    """Custom type devFragThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_DevFragThresh_Type.__name__ = "Integer32"
_DevFragThresh_Object = MibTableColumn
devFragThresh = _DevFragThresh_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 17),
    _DevFragThresh_Type()
)
devFragThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFragThresh.setStatus("current")


class _DevRtsthreshold_Type(Integer32):
    """Custom type devRtsthreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 2346),
    )


_DevRtsthreshold_Type.__name__ = "Integer32"
_DevRtsthreshold_Object = MibTableColumn
devRtsthreshold = _DevRtsthreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 18),
    _DevRtsthreshold_Type()
)
devRtsthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRtsthreshold.setStatus("current")


class _DevTxRange_Type(Integer32):
    """Custom type devTxRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 11000),
    )


_DevTxRange_Type.__name__ = "Integer32"
_DevTxRange_Object = MibTableColumn
devTxRange = _DevTxRange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 19),
    _DevTxRange_Type()
)
devTxRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTxRange.setStatus("current")


class _DevTxAntenna_Type(Integer32):
    """Custom type devTxAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainAntenna", 1),
          ("auxAntenna", 2),
          ("diversityAntenna", 3))
    )


_DevTxAntenna_Type.__name__ = "Integer32"
_DevTxAntenna_Object = MibTableColumn
devTxAntenna = _DevTxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 21),
    _DevTxAntenna_Type()
)
devTxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTxAntenna.setStatus("current")


class _DevWMMenable_Type(Integer32):
    """Custom type devWMMenable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DevWMMenable_Type.__name__ = "Integer32"
_DevWMMenable_Object = MibTableColumn
devWMMenable = _DevWMMenable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 23),
    _DevWMMenable_Type()
)
devWMMenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devWMMenable.setStatus("current")


class _DevOperationmode_Type(Integer32):
    """Custom type devOperationmode based on Integer32"""
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
        *(("client", 1),
          ("ap", 2),
          ("sniffer", 3),
          ("master", 4),
          ("slave", 5),
          ("clientRouter", 6))
    )


_DevOperationmode_Type.__name__ = "Integer32"
_DevOperationmode_Object = MibTableColumn
devOperationmode = _DevOperationmode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 24),
    _DevOperationmode_Type()
)
devOperationmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devOperationmode.setStatus("current")


class _DevChannelWidth_Type(Integer32):
    """Custom type devChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("width20MHz", 1),
          ("width40MHz", 2))
    )


_DevChannelWidth_Type.__name__ = "Integer32"
_DevChannelWidth_Object = MibTableColumn
devChannelWidth = _DevChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 25),
    _DevChannelWidth_Type()
)
devChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devChannelWidth.setStatus("current")
_DevChannelN24GHz_Type = Integer32
_DevChannelN24GHz_Object = MibTableColumn
devChannelN24GHz = _DevChannelN24GHz_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 26),
    _DevChannelN24GHz_Type()
)
devChannelN24GHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devChannelN24GHz.setStatus("current")
_DevChannelN5GHz_Type = Integer32
_DevChannelN5GHz_Object = MibTableColumn
devChannelN5GHz = _DevChannelN5GHz_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 27),
    _DevChannelN5GHz_Type()
)
devChannelN5GHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devChannelN5GHz.setStatus("current")


class _DevTxRateN_Type(Integer32):
    """Custom type devTxRateN based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rateMCS0", 2),
          ("rateMCS1", 3),
          ("rateMCS2", 4),
          ("rateMCS3", 5),
          ("rateMCS4", 6),
          ("rateMCS5", 7),
          ("rateMCS6", 8),
          ("rateMCS7", 9),
          ("rateMCS8", 10),
          ("rateMCS9", 11),
          ("rateMCS10", 12),
          ("rateMCS11", 13),
          ("rateMCS12", 14),
          ("rateMCS13", 15),
          ("rateMCS14", 16),
          ("rateMCS15", 17))
    )


_DevTxRateN_Type.__name__ = "Integer32"
_DevTxRateN_Object = MibTableColumn
devTxRateN = _DevTxRateN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 28),
    _DevTxRateN_Type()
)
devTxRateN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTxRateN.setStatus("current")


class _DevMulticastRateA_Type(Integer32):
    """Custom type devMulticastRateA based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate6M", 2),
          ("rate9M", 3),
          ("rate12M", 4),
          ("rate18M", 5),
          ("rate24M", 6),
          ("rate36M", 7),
          ("rate48M", 8),
          ("rate54M", 9))
    )


_DevMulticastRateA_Type.__name__ = "Integer32"
_DevMulticastRateA_Object = MibTableColumn
devMulticastRateA = _DevMulticastRateA_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 30),
    _DevMulticastRateA_Type()
)
devMulticastRateA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMulticastRateA.setStatus("current")


class _DevMulticastRateB_Type(Integer32):
    """Custom type devMulticastRateB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate1M", 2),
          ("rate2M", 3),
          ("rate5-5M", 4),
          ("rate11M", 5))
    )


_DevMulticastRateB_Type.__name__ = "Integer32"
_DevMulticastRateB_Object = MibTableColumn
devMulticastRateB = _DevMulticastRateB_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 31),
    _DevMulticastRateB_Type()
)
devMulticastRateB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMulticastRateB.setStatus("current")


class _DevMulticastRateG_Type(Integer32):
    """Custom type devMulticastRateG based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate6M", 2),
          ("rate9M", 3),
          ("rate12M", 4),
          ("rate18M", 5),
          ("rate24M", 6),
          ("rate36M", 7),
          ("rate48M", 8),
          ("rate54M", 9))
    )


_DevMulticastRateG_Type.__name__ = "Integer32"
_DevMulticastRateG_Object = MibTableColumn
devMulticastRateG = _DevMulticastRateG_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 32),
    _DevMulticastRateG_Type()
)
devMulticastRateG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMulticastRateG.setStatus("current")


class _DevMulticastRateBG_Type(Integer32):
    """Custom type devMulticastRateBG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate1M", 2),
          ("rate2M", 3),
          ("rate5-5M", 4),
          ("rate11M", 5))
    )


_DevMulticastRateBG_Type.__name__ = "Integer32"
_DevMulticastRateBG_Object = MibTableColumn
devMulticastRateBG = _DevMulticastRateBG_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 33),
    _DevMulticastRateBG_Type()
)
devMulticastRateBG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMulticastRateBG.setStatus("current")


class _DevMulticastRateBGN_Type(Integer32):
    """Custom type devMulticastRateBGN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate1M", 2),
          ("rate2M", 3),
          ("rate5-5M", 4),
          ("rate11M", 5))
    )


_DevMulticastRateBGN_Type.__name__ = "Integer32"
_DevMulticastRateBGN_Object = MibTableColumn
devMulticastRateBGN = _DevMulticastRateBGN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 34),
    _DevMulticastRateBGN_Type()
)
devMulticastRateBGN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMulticastRateBGN.setStatus("current")


class _DevMulticastRateAN_Type(Integer32):
    """Custom type devMulticastRateAN based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rate6M", 2),
          ("rate9M", 3),
          ("rate12M", 4),
          ("rate18M", 5),
          ("rate24M", 6),
          ("rate36M", 7),
          ("rate48M", 8),
          ("rate54M", 9))
    )


_DevMulticastRateAN_Type.__name__ = "Integer32"
_DevMulticastRateAN_Object = MibTableColumn
devMulticastRateAN = _DevMulticastRateAN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 35),
    _DevMulticastRateAN_Type()
)
devMulticastRateAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMulticastRateAN.setStatus("current")


class _DevMulticastRateN_Type(Integer32):
    """Custom type devMulticastRateN based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("rateAuto", 1),
          ("rateMCS0", 2),
          ("rateMCS1", 3),
          ("rateMCS2", 4),
          ("rateMCS3", 5),
          ("rateMCS4", 6),
          ("rateMCS5", 7),
          ("rateMCS6", 8),
          ("rateMCS7", 9),
          ("rateMCS8", 10),
          ("rateMCS9", 11),
          ("rateMCS10", 12),
          ("rateMCS11", 13),
          ("rateMCS12", 14),
          ("rateMCS13", 15),
          ("rateMCS14", 16),
          ("rateMCS15", 17))
    )


_DevMulticastRateN_Type.__name__ = "Integer32"
_DevMulticastRateN_Object = MibTableColumn
devMulticastRateN = _DevMulticastRateN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 36),
    _DevMulticastRateN_Type()
)
devMulticastRateN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMulticastRateN.setStatus("current")


class _DevTxPowerdBm_Type(Integer32):
    """Custom type devTxPowerdBm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_DevTxPowerdBm_Type.__name__ = "Integer32"
_DevTxPowerdBm_Object = MibTableColumn
devTxPowerdBm = _DevTxPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 41),
    _DevTxPowerdBm_Type()
)
devTxPowerdBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTxPowerdBm.setStatus("current")


class _DevMacClone_Type(Integer32):
    """Custom type devMacClone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DevMacClone_Type.__name__ = "Integer32"
_DevMacClone_Object = MibTableColumn
devMacClone = _DevMacClone_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 42),
    _DevMacClone_Type()
)
devMacClone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMacClone.setStatus("current")


class _DevTXrateMin_Type(Integer32):
    """Custom type devTXrateMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_DevTXrateMin_Type.__name__ = "Integer32"
_DevTXrateMin_Object = MibTableColumn
devTXrateMin = _DevTXrateMin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 58),
    _DevTXrateMin_Type()
)
devTXrateMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTXrateMin.setStatus("current")


class _DevInactiveTimeout_Type(Integer32):
    """Custom type devInactiveTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 240),
    )


_DevInactiveTimeout_Type.__name__ = "Integer32"
_DevInactiveTimeout_Object = MibTableColumn
devInactiveTimeout = _DevInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 59),
    _DevInactiveTimeout_Type()
)
devInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInactiveTimeout.setStatus("current")


class _DevProxyArp_Type(Integer32):
    """Custom type devProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DevProxyArp_Type.__name__ = "Integer32"
_DevProxyArp_Object = MibTableColumn
devProxyArp = _DevProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 60),
    _DevProxyArp_Type()
)
devProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devProxyArp.setStatus("current")


class _DevMacCloneMethod_Type(Integer32):
    """Custom type devMacCloneMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("static", 2))
    )


_DevMacCloneMethod_Type.__name__ = "Integer32"
_DevMacCloneMethod_Object = MibTableColumn
devMacCloneMethod = _DevMacCloneMethod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 63),
    _DevMacCloneMethod_Type()
)
devMacCloneMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMacCloneMethod.setStatus("current")
_DevMacCloneStaticMac_Type = DisplayString
_DevMacCloneStaticMac_Object = MibTableColumn
devMacCloneStaticMac = _DevMacCloneStaticMac_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 64),
    _DevMacCloneStaticMac_Type()
)
devMacCloneStaticMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devMacCloneStaticMac.setStatus("current")


class _DevRemoteConnCheckEnable_Type(Integer32):
    """Custom type devRemoteConnCheckEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DevRemoteConnCheckEnable_Type.__name__ = "Integer32"
_DevRemoteConnCheckEnable_Object = MibTableColumn
devRemoteConnCheckEnable = _DevRemoteConnCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 106),
    _DevRemoteConnCheckEnable_Type()
)
devRemoteConnCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckEnable.setStatus("current")


class _DevRemoteConnCheckReconnWLAN_Type(Integer32):
    """Custom type devRemoteConnCheckReconnWLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DevRemoteConnCheckReconnWLAN_Type.__name__ = "Integer32"
_DevRemoteConnCheckReconnWLAN_Object = MibTableColumn
devRemoteConnCheckReconnWLAN = _DevRemoteConnCheckReconnWLAN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 107),
    _DevRemoteConnCheckReconnWLAN_Type()
)
devRemoteConnCheckReconnWLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckReconnWLAN.setStatus("current")


class _DevRemoteConnCheckRebootDevice_Type(Integer32):
    """Custom type devRemoteConnCheckRebootDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DevRemoteConnCheckRebootDevice_Type.__name__ = "Integer32"
_DevRemoteConnCheckRebootDevice_Object = MibTableColumn
devRemoteConnCheckRebootDevice = _DevRemoteConnCheckRebootDevice_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 108),
    _DevRemoteConnCheckRebootDevice_Type()
)
devRemoteConnCheckRebootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckRebootDevice.setStatus("current")
_DevRemoteConnCheckRemoteHost_Type = IpAddress
_DevRemoteConnCheckRemoteHost_Object = MibTableColumn
devRemoteConnCheckRemoteHost = _DevRemoteConnCheckRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 109),
    _DevRemoteConnCheckRemoteHost_Type()
)
devRemoteConnCheckRemoteHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckRemoteHost.setStatus("current")


class _DevRemoteConnCheckCheckInterval_Type(Integer32):
    """Custom type devRemoteConnCheckCheckInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_DevRemoteConnCheckCheckInterval_Type.__name__ = "Integer32"
_DevRemoteConnCheckCheckInterval_Object = MibTableColumn
devRemoteConnCheckCheckInterval = _DevRemoteConnCheckCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 110),
    _DevRemoteConnCheckCheckInterval_Type()
)
devRemoteConnCheckCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckCheckInterval.setStatus("current")


class _DevRemoteConnCheckCheckTimeout_Type(Integer32):
    """Custom type devRemoteConnCheckCheckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_DevRemoteConnCheckCheckTimeout_Type.__name__ = "Integer32"
_DevRemoteConnCheckCheckTimeout_Object = MibTableColumn
devRemoteConnCheckCheckTimeout = _DevRemoteConnCheckCheckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 111),
    _DevRemoteConnCheckCheckTimeout_Type()
)
devRemoteConnCheckCheckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckCheckTimeout.setStatus("current")


class _DevRemoteConnCheckRetryCount_Type(Integer32):
    """Custom type devRemoteConnCheckRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DevRemoteConnCheckRetryCount_Type.__name__ = "Integer32"
_DevRemoteConnCheckRetryCount_Object = MibTableColumn
devRemoteConnCheckRetryCount = _DevRemoteConnCheckRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 112),
    _DevRemoteConnCheckRetryCount_Type()
)
devRemoteConnCheckRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckRetryCount.setStatus("current")


class _DevRemoteConnCheckRetryInterval_Type(Integer32):
    """Custom type devRemoteConnCheckRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_DevRemoteConnCheckRetryInterval_Type.__name__ = "Integer32"
_DevRemoteConnCheckRetryInterval_Object = MibTableColumn
devRemoteConnCheckRetryInterval = _DevRemoteConnCheckRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 113),
    _DevRemoteConnCheckRetryInterval_Type()
)
devRemoteConnCheckRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckRetryInterval.setStatus("current")


class _DevRemoteConnCheckRebootCount_Type(Integer32):
    """Custom type devRemoteConnCheckRebootCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DevRemoteConnCheckRebootCount_Type.__name__ = "Integer32"
_DevRemoteConnCheckRebootCount_Object = MibTableColumn
devRemoteConnCheckRebootCount = _DevRemoteConnCheckRebootCount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 1, 1, 114),
    _DevRemoteConnCheckRebootCount_Type()
)
devRemoteConnCheckRebootCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devRemoteConnCheckRebootCount.setStatus("current")
_VapTable_Object = MibTable
vapTable = _VapTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3)
)
if mibBuilder.loadTexts:
    vapTable.setStatus("current")
_VapEntry_Object = MibTableRow
vapEntry = _VapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1)
)
vapEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "vapIndex"),
)
if mibBuilder.loadTexts:
    vapEntry.setStatus("current")


class _VapIndex_Type(Integer32):
    """Custom type vapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_VapIndex_Type.__name__ = "Integer32"
_VapIndex_Object = MibTableColumn
vapIndex = _VapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 1),
    _VapIndex_Type()
)
vapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapIndex.setStatus("current")
_VapSSID_Type = DisplayString
_VapSSID_Object = MibTableColumn
vapSSID = _VapSSID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 2),
    _VapSSID_Type()
)
vapSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapSSID.setStatus("current")
_VapSignalLV_Type = DisplayString
_VapSignalLV_Object = MibTableColumn
vapSignalLV = _VapSignalLV_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 3),
    _VapSignalLV_Type()
)
vapSignalLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapSignalLV.setStatus("current")


class _VapSsidBroadcast_Type(Integer32):
    """Custom type vapSsidBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapSsidBroadcast_Type.__name__ = "Integer32"
_VapSsidBroadcast_Object = MibTableColumn
vapSsidBroadcast = _VapSsidBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 4),
    _VapSsidBroadcast_Type()
)
vapSsidBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapSsidBroadcast.setStatus("current")


class _VapWdsEnable_Type(Integer32):
    """Custom type vapWdsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapWdsEnable_Type.__name__ = "Integer32"
_VapWdsEnable_Object = MibTableColumn
vapWdsEnable = _VapWdsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 5),
    _VapWdsEnable_Type()
)
vapWdsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWdsEnable.setStatus("current")


class _VapAPfunctionality_Type(Integer32):
    """Custom type vapAPfunctionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapAPfunctionality_Type.__name__ = "Integer32"
_VapAPfunctionality_Object = MibTableColumn
vapAPfunctionality = _VapAPfunctionality_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 6),
    _VapAPfunctionality_Type()
)
vapAPfunctionality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapAPfunctionality.setStatus("current")


class _VapAuthType_Type(Integer32):
    """Custom type vapAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("wep", 2),
          ("wpa", 3),
          ("wpa2", 4),
          ("wpa-wpa2-mix", 5))
    )


_VapAuthType_Type.__name__ = "Integer32"
_VapAuthType_Object = MibTableColumn
vapAuthType = _VapAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 7),
    _VapAuthType_Type()
)
vapAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapAuthType.setStatus("current")


class _VapWEPauth_Type(Integer32):
    """Custom type vapWEPauth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("share", 2))
    )


_VapWEPauth_Type.__name__ = "Integer32"
_VapWEPauth_Object = MibTableColumn
vapWEPauth = _VapWEPauth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 8),
    _VapWEPauth_Type()
)
vapWEPauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWEPauth.setStatus("current")


class _VapWEPtype_Type(Integer32):
    """Custom type vapWEPtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2))
    )


_VapWEPtype_Type.__name__ = "Integer32"
_VapWEPtype_Object = MibTableColumn
vapWEPtype = _VapWEPtype_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 9),
    _VapWEPtype_Type()
)
vapWEPtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWEPtype.setStatus("current")


class _VapWEPlen_Type(Integer32):
    """Custom type vapWEPlen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wep64", 1),
          ("wep128", 2))
    )


_VapWEPlen_Type.__name__ = "Integer32"
_VapWEPlen_Object = MibTableColumn
vapWEPlen = _VapWEPlen_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 10),
    _VapWEPlen_Type()
)
vapWEPlen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWEPlen.setStatus("current")


class _VapWEPkeyIndex_Type(Integer32):
    """Custom type vapWEPkeyIndex based on Integer32"""
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
        *(("key1", 1),
          ("key2", 2),
          ("key3", 3),
          ("key4", 4))
    )


_VapWEPkeyIndex_Type.__name__ = "Integer32"
_VapWEPkeyIndex_Object = MibTableColumn
vapWEPkeyIndex = _VapWEPkeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 11),
    _VapWEPkeyIndex_Type()
)
vapWEPkeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWEPkeyIndex.setStatus("current")


class _VapWPAtype_Type(Integer32):
    """Custom type vapWPAtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("personal", 1),
          ("enterprise", 2))
    )


_VapWPAtype_Type.__name__ = "Integer32"
_VapWPAtype_Object = MibTableColumn
vapWPAtype = _VapWPAtype_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 16),
    _VapWPAtype_Type()
)
vapWPAtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWPAtype.setStatus("current")


class _VapEapolVer_Type(Integer32):
    """Custom type vapEapolVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VapEapolVer_Type.__name__ = "Integer32"
_VapEapolVer_Object = MibTableColumn
vapEapolVer = _VapEapolVer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 17),
    _VapEapolVer_Type()
)
vapEapolVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapEapolVer.setStatus("current")


class _VapWpaEncrypt_Type(Integer32):
    """Custom type vapWpaEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("mixed", 3))
    )


_VapWpaEncrypt_Type.__name__ = "Integer32"
_VapWpaEncrypt_Object = MibTableColumn
vapWpaEncrypt = _VapWpaEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 18),
    _VapWpaEncrypt_Type()
)
vapWpaEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapWpaEncrypt.setStatus("current")
_Vap1stAuthServerIPv4Addr_Type = IpAddress
_Vap1stAuthServerIPv4Addr_Object = MibTableColumn
vap1stAuthServerIPv4Addr = _Vap1stAuthServerIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 20),
    _Vap1stAuthServerIPv4Addr_Type()
)
vap1stAuthServerIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vap1stAuthServerIPv4Addr.setStatus("current")


class _Vap1stAuthServerPort_Type(Integer32):
    """Custom type vap1stAuthServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Vap1stAuthServerPort_Type.__name__ = "Integer32"
_Vap1stAuthServerPort_Object = MibTableColumn
vap1stAuthServerPort = _Vap1stAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 21),
    _Vap1stAuthServerPort_Type()
)
vap1stAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vap1stAuthServerPort.setStatus("current")
_Vap2ndAuthServerIPv4Addr_Type = IpAddress
_Vap2ndAuthServerIPv4Addr_Object = MibTableColumn
vap2ndAuthServerIPv4Addr = _Vap2ndAuthServerIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 23),
    _Vap2ndAuthServerIPv4Addr_Type()
)
vap2ndAuthServerIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vap2ndAuthServerIPv4Addr.setStatus("current")


class _Vap2ndAuthServerPort_Type(Integer32):
    """Custom type vap2ndAuthServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Vap2ndAuthServerPort_Type.__name__ = "Integer32"
_Vap2ndAuthServerPort_Object = MibTableColumn
vap2ndAuthServerPort = _Vap2ndAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 24),
    _Vap2ndAuthServerPort_Type()
)
vap2ndAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vap2ndAuthServerPort.setStatus("current")
_VapCertInfo_Type = DisplayString
_VapCertInfo_Object = MibTableColumn
vapCertInfo = _VapCertInfo_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 26),
    _VapCertInfo_Type()
)
vapCertInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapCertInfo.setStatus("current")


class _VapEapProto_Type(Integer32):
    """Custom type vapEapProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tls", 1),
          ("ttls", 2),
          ("peap", 3))
    )


_VapEapProto_Type.__name__ = "Integer32"
_VapEapProto_Object = MibTableColumn
vapEapProto = _VapEapProto_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 27),
    _VapEapProto_Type()
)
vapEapProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapEapProto.setStatus("current")
_VapEAPanonymous_Type = DisplayString
_VapEAPanonymous_Object = MibTableColumn
vapEAPanonymous = _VapEAPanonymous_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 28),
    _VapEAPanonymous_Type()
)
vapEAPanonymous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapEAPanonymous.setStatus("current")


class _VapTtlsInner_Type(Integer32):
    """Custom type vapTtlsInner based on Integer32"""
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
        *(("pap", 1),
          ("chap", 2),
          ("ms-chap", 3),
          ("ms-chapV2", 4))
    )


_VapTtlsInner_Type.__name__ = "Integer32"
_VapTtlsInner_Object = MibTableColumn
vapTtlsInner = _VapTtlsInner_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 29),
    _VapTtlsInner_Type()
)
vapTtlsInner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapTtlsInner.setStatus("current")


class _VapPeapInner_Type(Integer32):
    """Custom type vapPeapInner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ms-chapV2", 1)
    )


_VapPeapInner_Type.__name__ = "Integer32"
_VapPeapInner_Object = MibTableColumn
vapPeapInner = _VapPeapInner_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 30),
    _VapPeapInner_Type()
)
vapPeapInner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapPeapInner.setStatus("current")
_VapEapUser_Type = DisplayString
_VapEapUser_Object = MibTableColumn
vapEapUser = _VapEapUser_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 31),
    _VapEapUser_Type()
)
vapEapUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapEapUser.setStatus("current")


class _VapRekey_Type(Integer32):
    """Custom type vapRekey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_VapRekey_Type.__name__ = "Integer32"
_VapRekey_Object = MibTableColumn
vapRekey = _VapRekey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 33),
    _VapRekey_Type()
)
vapRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapRekey.setStatus("current")
_VapBssidClient_Type = DisplayString
_VapBssidClient_Object = MibTableColumn
vapBssidClient = _VapBssidClient_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 34),
    _VapBssidClient_Type()
)
vapBssidClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vapBssidClient.setStatus("current")


class _VapClientIsolation_Type(Integer32):
    """Custom type vapClientIsolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noIsolation", 1),
          ("isolatedWithinTheSameAP", 2),
          ("isolatedWithinTheSameSubnet", 3))
    )


_VapClientIsolation_Type.__name__ = "Integer32"
_VapClientIsolation_Object = MibTableColumn
vapClientIsolation = _VapClientIsolation_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 38),
    _VapClientIsolation_Type()
)
vapClientIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClientIsolation.setStatus("current")
_VapClientIsolationGateway_Type = IpAddress
_VapClientIsolationGateway_Object = MibTableColumn
vapClientIsolationGateway = _VapClientIsolationGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 39),
    _VapClientIsolationGateway_Type()
)
vapClientIsolationGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClientIsolationGateway.setStatus("current")
_VapClientIsolationNetMask_Type = IpAddress
_VapClientIsolationNetMask_Object = MibTableColumn
vapClientIsolationNetMask = _VapClientIsolationNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 40),
    _VapClientIsolationNetMask_Type()
)
vapClientIsolationNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClientIsolationNetMask.setStatus("current")


class _VapMgmtEncryption_Type(Integer32):
    """Custom type vapMgmtEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapMgmtEncryption_Type.__name__ = "Integer32"
_VapMgmtEncryption_Object = MibTableColumn
vapMgmtEncryption = _VapMgmtEncryption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 41),
    _VapMgmtEncryption_Type()
)
vapMgmtEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapMgmtEncryption.setStatus("current")


class _VapAerolink_ap_Type(Integer32):
    """Custom type vapAerolink_ap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapAerolink_ap_Type.__name__ = "Integer32"
_VapAerolink_ap_Object = MibTableColumn
vapAerolink_ap = _VapAerolink_ap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 43),
    _VapAerolink_ap_Type()
)
vapAerolink_ap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapAerolink_ap.setStatus("current")


class _VapClientIsolationSubnetType_Type(Integer32):
    """Custom type vapClientIsolationSubnetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_VapClientIsolationSubnetType_Type.__name__ = "Integer32"
_VapClientIsolationSubnetType_Object = MibTableColumn
vapClientIsolationSubnetType = _VapClientIsolationSubnetType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 201),
    _VapClientIsolationSubnetType_Type()
)
vapClientIsolationSubnetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClientIsolationSubnetType.setStatus("current")


class _VapClntIsoEnableRule1_Type(Integer32):
    """Custom type vapClntIsoEnableRule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapClntIsoEnableRule1_Type.__name__ = "Integer32"
_VapClntIsoEnableRule1_Object = MibTableColumn
vapClntIsoEnableRule1 = _VapClntIsoEnableRule1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 211),
    _VapClntIsoEnableRule1_Type()
)
vapClntIsoEnableRule1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoEnableRule1.setStatus("current")
_VapClntIsoHostRule1_Type = DisplayString
_VapClntIsoHostRule1_Object = MibTableColumn
vapClntIsoHostRule1 = _VapClntIsoHostRule1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 212),
    _VapClntIsoHostRule1_Type()
)
vapClntIsoHostRule1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoHostRule1.setStatus("current")
_VapClntIsoNetmaskRule1_Type = IpAddress
_VapClntIsoNetmaskRule1_Object = MibTableColumn
vapClntIsoNetmaskRule1 = _VapClntIsoNetmaskRule1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 213),
    _VapClntIsoNetmaskRule1_Type()
)
vapClntIsoNetmaskRule1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoNetmaskRule1.setStatus("current")


class _VapClntIsoProtoRule1_Type(Integer32):
    """Custom type vapClntIsoProtoRule1 based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_VapClntIsoProtoRule1_Type.__name__ = "Integer32"
_VapClntIsoProtoRule1_Object = MibTableColumn
vapClntIsoProtoRule1 = _VapClntIsoProtoRule1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 214),
    _VapClntIsoProtoRule1_Type()
)
vapClntIsoProtoRule1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoProtoRule1.setStatus("current")


class _VapClntIsoPortStartRule1_Type(Integer32):
    """Custom type vapClntIsoPortStartRule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortStartRule1_Type.__name__ = "Integer32"
_VapClntIsoPortStartRule1_Object = MibTableColumn
vapClntIsoPortStartRule1 = _VapClntIsoPortStartRule1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 215),
    _VapClntIsoPortStartRule1_Type()
)
vapClntIsoPortStartRule1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortStartRule1.setStatus("current")


class _VapClntIsoPortEndRule1_Type(Integer32):
    """Custom type vapClntIsoPortEndRule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortEndRule1_Type.__name__ = "Integer32"
_VapClntIsoPortEndRule1_Object = MibTableColumn
vapClntIsoPortEndRule1 = _VapClntIsoPortEndRule1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 216),
    _VapClntIsoPortEndRule1_Type()
)
vapClntIsoPortEndRule1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortEndRule1.setStatus("current")


class _VapClntIsoEnableRule2_Type(Integer32):
    """Custom type vapClntIsoEnableRule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapClntIsoEnableRule2_Type.__name__ = "Integer32"
_VapClntIsoEnableRule2_Object = MibTableColumn
vapClntIsoEnableRule2 = _VapClntIsoEnableRule2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 221),
    _VapClntIsoEnableRule2_Type()
)
vapClntIsoEnableRule2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoEnableRule2.setStatus("current")
_VapClntIsoHostRule2_Type = DisplayString
_VapClntIsoHostRule2_Object = MibTableColumn
vapClntIsoHostRule2 = _VapClntIsoHostRule2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 222),
    _VapClntIsoHostRule2_Type()
)
vapClntIsoHostRule2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoHostRule2.setStatus("current")
_VapClntIsoNetmaskRule2_Type = IpAddress
_VapClntIsoNetmaskRule2_Object = MibTableColumn
vapClntIsoNetmaskRule2 = _VapClntIsoNetmaskRule2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 223),
    _VapClntIsoNetmaskRule2_Type()
)
vapClntIsoNetmaskRule2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoNetmaskRule2.setStatus("current")


class _VapClntIsoProtoRule2_Type(Integer32):
    """Custom type vapClntIsoProtoRule2 based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_VapClntIsoProtoRule2_Type.__name__ = "Integer32"
_VapClntIsoProtoRule2_Object = MibTableColumn
vapClntIsoProtoRule2 = _VapClntIsoProtoRule2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 224),
    _VapClntIsoProtoRule2_Type()
)
vapClntIsoProtoRule2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoProtoRule2.setStatus("current")


class _VapClntIsoPortStartRule2_Type(Integer32):
    """Custom type vapClntIsoPortStartRule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortStartRule2_Type.__name__ = "Integer32"
_VapClntIsoPortStartRule2_Object = MibTableColumn
vapClntIsoPortStartRule2 = _VapClntIsoPortStartRule2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 225),
    _VapClntIsoPortStartRule2_Type()
)
vapClntIsoPortStartRule2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortStartRule2.setStatus("current")


class _VapClntIsoPortEndRule2_Type(Integer32):
    """Custom type vapClntIsoPortEndRule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortEndRule2_Type.__name__ = "Integer32"
_VapClntIsoPortEndRule2_Object = MibTableColumn
vapClntIsoPortEndRule2 = _VapClntIsoPortEndRule2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 226),
    _VapClntIsoPortEndRule2_Type()
)
vapClntIsoPortEndRule2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortEndRule2.setStatus("current")


class _VapClntIsoEnableRule3_Type(Integer32):
    """Custom type vapClntIsoEnableRule3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapClntIsoEnableRule3_Type.__name__ = "Integer32"
_VapClntIsoEnableRule3_Object = MibTableColumn
vapClntIsoEnableRule3 = _VapClntIsoEnableRule3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 231),
    _VapClntIsoEnableRule3_Type()
)
vapClntIsoEnableRule3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoEnableRule3.setStatus("current")
_VapClntIsoHostRule3_Type = DisplayString
_VapClntIsoHostRule3_Object = MibTableColumn
vapClntIsoHostRule3 = _VapClntIsoHostRule3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 232),
    _VapClntIsoHostRule3_Type()
)
vapClntIsoHostRule3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoHostRule3.setStatus("current")
_VapClntIsoNetmaskRule3_Type = IpAddress
_VapClntIsoNetmaskRule3_Object = MibTableColumn
vapClntIsoNetmaskRule3 = _VapClntIsoNetmaskRule3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 233),
    _VapClntIsoNetmaskRule3_Type()
)
vapClntIsoNetmaskRule3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoNetmaskRule3.setStatus("current")


class _VapClntIsoProtoRule3_Type(Integer32):
    """Custom type vapClntIsoProtoRule3 based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_VapClntIsoProtoRule3_Type.__name__ = "Integer32"
_VapClntIsoProtoRule3_Object = MibTableColumn
vapClntIsoProtoRule3 = _VapClntIsoProtoRule3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 234),
    _VapClntIsoProtoRule3_Type()
)
vapClntIsoProtoRule3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoProtoRule3.setStatus("current")


class _VapClntIsoPortStartRule3_Type(Integer32):
    """Custom type vapClntIsoPortStartRule3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortStartRule3_Type.__name__ = "Integer32"
_VapClntIsoPortStartRule3_Object = MibTableColumn
vapClntIsoPortStartRule3 = _VapClntIsoPortStartRule3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 235),
    _VapClntIsoPortStartRule3_Type()
)
vapClntIsoPortStartRule3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortStartRule3.setStatus("current")


class _VapClntIsoPortEndRule3_Type(Integer32):
    """Custom type vapClntIsoPortEndRule3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortEndRule3_Type.__name__ = "Integer32"
_VapClntIsoPortEndRule3_Object = MibTableColumn
vapClntIsoPortEndRule3 = _VapClntIsoPortEndRule3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 236),
    _VapClntIsoPortEndRule3_Type()
)
vapClntIsoPortEndRule3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortEndRule3.setStatus("current")


class _VapClntIsoEnableRule4_Type(Integer32):
    """Custom type vapClntIsoEnableRule4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapClntIsoEnableRule4_Type.__name__ = "Integer32"
_VapClntIsoEnableRule4_Object = MibTableColumn
vapClntIsoEnableRule4 = _VapClntIsoEnableRule4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 241),
    _VapClntIsoEnableRule4_Type()
)
vapClntIsoEnableRule4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoEnableRule4.setStatus("current")
_VapClntIsoHostRule4_Type = DisplayString
_VapClntIsoHostRule4_Object = MibTableColumn
vapClntIsoHostRule4 = _VapClntIsoHostRule4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 242),
    _VapClntIsoHostRule4_Type()
)
vapClntIsoHostRule4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoHostRule4.setStatus("current")
_VapClntIsoNetmaskRule4_Type = IpAddress
_VapClntIsoNetmaskRule4_Object = MibTableColumn
vapClntIsoNetmaskRule4 = _VapClntIsoNetmaskRule4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 243),
    _VapClntIsoNetmaskRule4_Type()
)
vapClntIsoNetmaskRule4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoNetmaskRule4.setStatus("current")


class _VapClntIsoProtoRule4_Type(Integer32):
    """Custom type vapClntIsoProtoRule4 based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_VapClntIsoProtoRule4_Type.__name__ = "Integer32"
_VapClntIsoProtoRule4_Object = MibTableColumn
vapClntIsoProtoRule4 = _VapClntIsoProtoRule4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 244),
    _VapClntIsoProtoRule4_Type()
)
vapClntIsoProtoRule4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoProtoRule4.setStatus("current")


class _VapClntIsoPortStartRule4_Type(Integer32):
    """Custom type vapClntIsoPortStartRule4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortStartRule4_Type.__name__ = "Integer32"
_VapClntIsoPortStartRule4_Object = MibTableColumn
vapClntIsoPortStartRule4 = _VapClntIsoPortStartRule4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 245),
    _VapClntIsoPortStartRule4_Type()
)
vapClntIsoPortStartRule4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortStartRule4.setStatus("current")


class _VapClntIsoPortEndRule4_Type(Integer32):
    """Custom type vapClntIsoPortEndRule4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortEndRule4_Type.__name__ = "Integer32"
_VapClntIsoPortEndRule4_Object = MibTableColumn
vapClntIsoPortEndRule4 = _VapClntIsoPortEndRule4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 246),
    _VapClntIsoPortEndRule4_Type()
)
vapClntIsoPortEndRule4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortEndRule4.setStatus("current")


class _VapClntIsoEnableRule5_Type(Integer32):
    """Custom type vapClntIsoEnableRule5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapClntIsoEnableRule5_Type.__name__ = "Integer32"
_VapClntIsoEnableRule5_Object = MibTableColumn
vapClntIsoEnableRule5 = _VapClntIsoEnableRule5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 251),
    _VapClntIsoEnableRule5_Type()
)
vapClntIsoEnableRule5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoEnableRule5.setStatus("current")
_VapClntIsoHostRule5_Type = DisplayString
_VapClntIsoHostRule5_Object = MibTableColumn
vapClntIsoHostRule5 = _VapClntIsoHostRule5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 252),
    _VapClntIsoHostRule5_Type()
)
vapClntIsoHostRule5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoHostRule5.setStatus("current")
_VapClntIsoNetmaskRule5_Type = IpAddress
_VapClntIsoNetmaskRule5_Object = MibTableColumn
vapClntIsoNetmaskRule5 = _VapClntIsoNetmaskRule5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 253),
    _VapClntIsoNetmaskRule5_Type()
)
vapClntIsoNetmaskRule5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoNetmaskRule5.setStatus("current")


class _VapClntIsoProtoRule5_Type(Integer32):
    """Custom type vapClntIsoProtoRule5 based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_VapClntIsoProtoRule5_Type.__name__ = "Integer32"
_VapClntIsoProtoRule5_Object = MibTableColumn
vapClntIsoProtoRule5 = _VapClntIsoProtoRule5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 254),
    _VapClntIsoProtoRule5_Type()
)
vapClntIsoProtoRule5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoProtoRule5.setStatus("current")


class _VapClntIsoPortStartRule5_Type(Integer32):
    """Custom type vapClntIsoPortStartRule5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortStartRule5_Type.__name__ = "Integer32"
_VapClntIsoPortStartRule5_Object = MibTableColumn
vapClntIsoPortStartRule5 = _VapClntIsoPortStartRule5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 255),
    _VapClntIsoPortStartRule5_Type()
)
vapClntIsoPortStartRule5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortStartRule5.setStatus("current")


class _VapClntIsoPortEndRule5_Type(Integer32):
    """Custom type vapClntIsoPortEndRule5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortEndRule5_Type.__name__ = "Integer32"
_VapClntIsoPortEndRule5_Object = MibTableColumn
vapClntIsoPortEndRule5 = _VapClntIsoPortEndRule5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 256),
    _VapClntIsoPortEndRule5_Type()
)
vapClntIsoPortEndRule5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortEndRule5.setStatus("current")


class _VapClntIsoEnableRule6_Type(Integer32):
    """Custom type vapClntIsoEnableRule6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapClntIsoEnableRule6_Type.__name__ = "Integer32"
_VapClntIsoEnableRule6_Object = MibTableColumn
vapClntIsoEnableRule6 = _VapClntIsoEnableRule6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 261),
    _VapClntIsoEnableRule6_Type()
)
vapClntIsoEnableRule6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoEnableRule6.setStatus("current")
_VapClntIsoHostRule6_Type = DisplayString
_VapClntIsoHostRule6_Object = MibTableColumn
vapClntIsoHostRule6 = _VapClntIsoHostRule6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 262),
    _VapClntIsoHostRule6_Type()
)
vapClntIsoHostRule6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoHostRule6.setStatus("current")
_VapClntIsoNetmaskRule6_Type = IpAddress
_VapClntIsoNetmaskRule6_Object = MibTableColumn
vapClntIsoNetmaskRule6 = _VapClntIsoNetmaskRule6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 263),
    _VapClntIsoNetmaskRule6_Type()
)
vapClntIsoNetmaskRule6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoNetmaskRule6.setStatus("current")


class _VapClntIsoProtoRule6_Type(Integer32):
    """Custom type vapClntIsoProtoRule6 based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_VapClntIsoProtoRule6_Type.__name__ = "Integer32"
_VapClntIsoProtoRule6_Object = MibTableColumn
vapClntIsoProtoRule6 = _VapClntIsoProtoRule6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 264),
    _VapClntIsoProtoRule6_Type()
)
vapClntIsoProtoRule6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoProtoRule6.setStatus("current")


class _VapClntIsoPortStartRule6_Type(Integer32):
    """Custom type vapClntIsoPortStartRule6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortStartRule6_Type.__name__ = "Integer32"
_VapClntIsoPortStartRule6_Object = MibTableColumn
vapClntIsoPortStartRule6 = _VapClntIsoPortStartRule6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 265),
    _VapClntIsoPortStartRule6_Type()
)
vapClntIsoPortStartRule6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortStartRule6.setStatus("current")


class _VapClntIsoPortEndRule6_Type(Integer32):
    """Custom type vapClntIsoPortEndRule6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortEndRule6_Type.__name__ = "Integer32"
_VapClntIsoPortEndRule6_Object = MibTableColumn
vapClntIsoPortEndRule6 = _VapClntIsoPortEndRule6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 266),
    _VapClntIsoPortEndRule6_Type()
)
vapClntIsoPortEndRule6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortEndRule6.setStatus("current")


class _VapClntIsoEnableRule7_Type(Integer32):
    """Custom type vapClntIsoEnableRule7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapClntIsoEnableRule7_Type.__name__ = "Integer32"
_VapClntIsoEnableRule7_Object = MibTableColumn
vapClntIsoEnableRule7 = _VapClntIsoEnableRule7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 271),
    _VapClntIsoEnableRule7_Type()
)
vapClntIsoEnableRule7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoEnableRule7.setStatus("current")
_VapClntIsoHostRule7_Type = DisplayString
_VapClntIsoHostRule7_Object = MibTableColumn
vapClntIsoHostRule7 = _VapClntIsoHostRule7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 272),
    _VapClntIsoHostRule7_Type()
)
vapClntIsoHostRule7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoHostRule7.setStatus("current")
_VapClntIsoNetmaskRule7_Type = IpAddress
_VapClntIsoNetmaskRule7_Object = MibTableColumn
vapClntIsoNetmaskRule7 = _VapClntIsoNetmaskRule7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 273),
    _VapClntIsoNetmaskRule7_Type()
)
vapClntIsoNetmaskRule7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoNetmaskRule7.setStatus("current")


class _VapClntIsoProtoRule7_Type(Integer32):
    """Custom type vapClntIsoProtoRule7 based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_VapClntIsoProtoRule7_Type.__name__ = "Integer32"
_VapClntIsoProtoRule7_Object = MibTableColumn
vapClntIsoProtoRule7 = _VapClntIsoProtoRule7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 274),
    _VapClntIsoProtoRule7_Type()
)
vapClntIsoProtoRule7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoProtoRule7.setStatus("current")


class _VapClntIsoPortStartRule7_Type(Integer32):
    """Custom type vapClntIsoPortStartRule7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortStartRule7_Type.__name__ = "Integer32"
_VapClntIsoPortStartRule7_Object = MibTableColumn
vapClntIsoPortStartRule7 = _VapClntIsoPortStartRule7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 275),
    _VapClntIsoPortStartRule7_Type()
)
vapClntIsoPortStartRule7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortStartRule7.setStatus("current")


class _VapClntIsoPortEndRule7_Type(Integer32):
    """Custom type vapClntIsoPortEndRule7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortEndRule7_Type.__name__ = "Integer32"
_VapClntIsoPortEndRule7_Object = MibTableColumn
vapClntIsoPortEndRule7 = _VapClntIsoPortEndRule7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 276),
    _VapClntIsoPortEndRule7_Type()
)
vapClntIsoPortEndRule7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortEndRule7.setStatus("current")


class _VapClntIsoEnableRule8_Type(Integer32):
    """Custom type vapClntIsoEnableRule8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_VapClntIsoEnableRule8_Type.__name__ = "Integer32"
_VapClntIsoEnableRule8_Object = MibTableColumn
vapClntIsoEnableRule8 = _VapClntIsoEnableRule8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 281),
    _VapClntIsoEnableRule8_Type()
)
vapClntIsoEnableRule8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoEnableRule8.setStatus("current")
_VapClntIsoHostRule8_Type = DisplayString
_VapClntIsoHostRule8_Object = MibTableColumn
vapClntIsoHostRule8 = _VapClntIsoHostRule8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 282),
    _VapClntIsoHostRule8_Type()
)
vapClntIsoHostRule8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoHostRule8.setStatus("current")
_VapClntIsoNetmaskRule8_Type = IpAddress
_VapClntIsoNetmaskRule8_Object = MibTableColumn
vapClntIsoNetmaskRule8 = _VapClntIsoNetmaskRule8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 283),
    _VapClntIsoNetmaskRule8_Type()
)
vapClntIsoNetmaskRule8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoNetmaskRule8.setStatus("current")


class _VapClntIsoProtoRule8_Type(Integer32):
    """Custom type vapClntIsoProtoRule8 based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_VapClntIsoProtoRule8_Type.__name__ = "Integer32"
_VapClntIsoProtoRule8_Object = MibTableColumn
vapClntIsoProtoRule8 = _VapClntIsoProtoRule8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 284),
    _VapClntIsoProtoRule8_Type()
)
vapClntIsoProtoRule8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoProtoRule8.setStatus("current")


class _VapClntIsoPortStartRule8_Type(Integer32):
    """Custom type vapClntIsoPortStartRule8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortStartRule8_Type.__name__ = "Integer32"
_VapClntIsoPortStartRule8_Object = MibTableColumn
vapClntIsoPortStartRule8 = _VapClntIsoPortStartRule8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 285),
    _VapClntIsoPortStartRule8_Type()
)
vapClntIsoPortStartRule8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortStartRule8.setStatus("current")


class _VapClntIsoPortEndRule8_Type(Integer32):
    """Custom type vapClntIsoPortEndRule8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VapClntIsoPortEndRule8_Type.__name__ = "Integer32"
_VapClntIsoPortEndRule8_Object = MibTableColumn
vapClntIsoPortEndRule8 = _VapClntIsoPortEndRule8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 3, 1, 286),
    _VapClntIsoPortEndRule8_Type()
)
vapClntIsoPortEndRule8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapClntIsoPortEndRule8.setStatus("current")
_WdsTable_Object = MibTable
wdsTable = _WdsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 5)
)
if mibBuilder.loadTexts:
    wdsTable.setStatus("current")
_WdsEntry_Object = MibTableRow
wdsEntry = _WdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 5, 1)
)
wdsEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "wdsIndex"),
)
if mibBuilder.loadTexts:
    wdsEntry.setStatus("current")


class _WdsIndex_Type(Integer32):
    """Custom type wdsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WdsIndex_Type.__name__ = "Integer32"
_WdsIndex_Object = MibTableColumn
wdsIndex = _WdsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 5, 1, 1),
    _WdsIndex_Type()
)
wdsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdsIndex.setStatus("current")


class _WdsWdsEnable_Type(Integer32):
    """Custom type wdsWdsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_WdsWdsEnable_Type.__name__ = "Integer32"
_WdsWdsEnable_Object = MibTableColumn
wdsWdsEnable = _WdsWdsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 5, 1, 2),
    _WdsWdsEnable_Type()
)
wdsWdsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsWdsEnable.setStatus("current")
_WdsWdsPeerMac_Type = DisplayString
_WdsWdsPeerMac_Object = MibTableColumn
wdsWdsPeerMac = _WdsWdsPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 5, 1, 3),
    _WdsWdsPeerMac_Type()
)
wdsWdsPeerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsWdsPeerMac.setStatus("current")
_CertWlanTable_Object = MibTable
certWlanTable = _CertWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 6)
)
if mibBuilder.loadTexts:
    certWlanTable.setStatus("current")
_CertWlanEntry_Object = MibTableRow
certWlanEntry = _CertWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 6, 1)
)
certWlanEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "certWlanIndex"),
)
if mibBuilder.loadTexts:
    certWlanEntry.setStatus("current")


class _CertWlanIndex_Type(Integer32):
    """Custom type certWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CertWlanIndex_Type.__name__ = "Integer32"
_CertWlanIndex_Object = MibTableColumn
certWlanIndex = _CertWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 6, 1, 1),
    _CertWlanIndex_Type()
)
certWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certWlanIndex.setStatus("current")
_CertWlanIssueTo_Type = DisplayString
_CertWlanIssueTo_Object = MibTableColumn
certWlanIssueTo = _CertWlanIssueTo_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 6, 1, 2),
    _CertWlanIssueTo_Type()
)
certWlanIssueTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certWlanIssueTo.setStatus("current")
_CertWlanIssueBy_Type = DisplayString
_CertWlanIssueBy_Object = MibTableColumn
certWlanIssueBy = _CertWlanIssueBy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 6, 1, 3),
    _CertWlanIssueBy_Type()
)
certWlanIssueBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certWlanIssueBy.setStatus("current")
_CertWlanExpireDate_Type = DisplayString
_CertWlanExpireDate_Object = MibTableColumn
certWlanExpireDate = _CertWlanExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 6, 1, 4),
    _CertWlanExpireDate_Type()
)
certWlanExpireDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certWlanExpireDate.setStatus("current")
_TurboRoamingTable_Object = MibTable
turboRoamingTable = _TurboRoamingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7)
)
if mibBuilder.loadTexts:
    turboRoamingTable.setStatus("current")
_TurboRoamingEntry_Object = MibTableRow
turboRoamingEntry = _TurboRoamingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1)
)
turboRoamingEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "turboRoamingIndex"),
)
if mibBuilder.loadTexts:
    turboRoamingEntry.setStatus("current")


class _TurboRoamingIndex_Type(Integer32):
    """Custom type turboRoamingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TurboRoamingIndex_Type.__name__ = "Integer32"
_TurboRoamingIndex_Object = MibTableColumn
turboRoamingIndex = _TurboRoamingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 1),
    _TurboRoamingIndex_Type()
)
turboRoamingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRoamingIndex.setStatus("current")


class _TurboRoamingEnable_Type(Integer32):
    """Custom type turboRoamingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TurboRoamingEnable_Type.__name__ = "Integer32"
_TurboRoamingEnable_Object = MibTableColumn
turboRoamingEnable = _TurboRoamingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 2),
    _TurboRoamingEnable_Type()
)
turboRoamingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingEnable.setStatus("current")
_TurboRoamingChannelA1_Type = Integer32
_TurboRoamingChannelA1_Object = MibTableColumn
turboRoamingChannelA1 = _TurboRoamingChannelA1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 3),
    _TurboRoamingChannelA1_Type()
)
turboRoamingChannelA1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA1.setStatus("current")
_TurboRoamingChannelA2_Type = Integer32
_TurboRoamingChannelA2_Object = MibTableColumn
turboRoamingChannelA2 = _TurboRoamingChannelA2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 4),
    _TurboRoamingChannelA2_Type()
)
turboRoamingChannelA2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA2.setStatus("current")
_TurboRoamingChannelA3_Type = Integer32
_TurboRoamingChannelA3_Object = MibTableColumn
turboRoamingChannelA3 = _TurboRoamingChannelA3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 5),
    _TurboRoamingChannelA3_Type()
)
turboRoamingChannelA3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA3.setStatus("current")
_TurboRoamingChannelB1_Type = Integer32
_TurboRoamingChannelB1_Object = MibTableColumn
turboRoamingChannelB1 = _TurboRoamingChannelB1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 6),
    _TurboRoamingChannelB1_Type()
)
turboRoamingChannelB1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB1.setStatus("current")
_TurboRoamingChannelB2_Type = Integer32
_TurboRoamingChannelB2_Object = MibTableColumn
turboRoamingChannelB2 = _TurboRoamingChannelB2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 7),
    _TurboRoamingChannelB2_Type()
)
turboRoamingChannelB2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB2.setStatus("current")
_TurboRoamingChannelB3_Type = Integer32
_TurboRoamingChannelB3_Object = MibTableColumn
turboRoamingChannelB3 = _TurboRoamingChannelB3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 8),
    _TurboRoamingChannelB3_Type()
)
turboRoamingChannelB3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB3.setStatus("current")
_TurboRoamingChannelG1_Type = Integer32
_TurboRoamingChannelG1_Object = MibTableColumn
turboRoamingChannelG1 = _TurboRoamingChannelG1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 9),
    _TurboRoamingChannelG1_Type()
)
turboRoamingChannelG1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG1.setStatus("current")
_TurboRoamingChannelG2_Type = Integer32
_TurboRoamingChannelG2_Object = MibTableColumn
turboRoamingChannelG2 = _TurboRoamingChannelG2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 10),
    _TurboRoamingChannelG2_Type()
)
turboRoamingChannelG2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG2.setStatus("current")
_TurboRoamingChannelG3_Type = Integer32
_TurboRoamingChannelG3_Object = MibTableColumn
turboRoamingChannelG3 = _TurboRoamingChannelG3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 11),
    _TurboRoamingChannelG3_Type()
)
turboRoamingChannelG3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG3.setStatus("current")
_TurboRoamingChannelBG1_Type = Integer32
_TurboRoamingChannelBG1_Object = MibTableColumn
turboRoamingChannelBG1 = _TurboRoamingChannelBG1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 12),
    _TurboRoamingChannelBG1_Type()
)
turboRoamingChannelBG1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG1.setStatus("current")
_TurboRoamingChannelBG2_Type = Integer32
_TurboRoamingChannelBG2_Object = MibTableColumn
turboRoamingChannelBG2 = _TurboRoamingChannelBG2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 13),
    _TurboRoamingChannelBG2_Type()
)
turboRoamingChannelBG2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG2.setStatus("current")
_TurboRoamingChannelBG3_Type = Integer32
_TurboRoamingChannelBG3_Object = MibTableColumn
turboRoamingChannelBG3 = _TurboRoamingChannelBG3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 14),
    _TurboRoamingChannelBG3_Type()
)
turboRoamingChannelBG3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG3.setStatus("current")


class _TurboRoamingApAliveCheckEnable_Type(Integer32):
    """Custom type turboRoamingApAliveCheckEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TurboRoamingApAliveCheckEnable_Type.__name__ = "Integer32"
_TurboRoamingApAliveCheckEnable_Object = MibTableColumn
turboRoamingApAliveCheckEnable = _TurboRoamingApAliveCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 15),
    _TurboRoamingApAliveCheckEnable_Type()
)
turboRoamingApAliveCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingApAliveCheckEnable.setStatus("current")
_TurboRoamingChannelN24GHz1_Type = Integer32
_TurboRoamingChannelN24GHz1_Object = MibTableColumn
turboRoamingChannelN24GHz1 = _TurboRoamingChannelN24GHz1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 16),
    _TurboRoamingChannelN24GHz1_Type()
)
turboRoamingChannelN24GHz1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz1.setStatus("current")
_TurboRoamingChannelN24GHz2_Type = Integer32
_TurboRoamingChannelN24GHz2_Object = MibTableColumn
turboRoamingChannelN24GHz2 = _TurboRoamingChannelN24GHz2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 17),
    _TurboRoamingChannelN24GHz2_Type()
)
turboRoamingChannelN24GHz2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz2.setStatus("current")
_TurboRoamingChannelN24GHz3_Type = Integer32
_TurboRoamingChannelN24GHz3_Object = MibTableColumn
turboRoamingChannelN24GHz3 = _TurboRoamingChannelN24GHz3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 18),
    _TurboRoamingChannelN24GHz3_Type()
)
turboRoamingChannelN24GHz3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz3.setStatus("current")
_TurboRoamingChannelN5GHz1_Type = Integer32
_TurboRoamingChannelN5GHz1_Object = MibTableColumn
turboRoamingChannelN5GHz1 = _TurboRoamingChannelN5GHz1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 19),
    _TurboRoamingChannelN5GHz1_Type()
)
turboRoamingChannelN5GHz1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz1.setStatus("current")
_TurboRoamingChannelN5GHz2_Type = Integer32
_TurboRoamingChannelN5GHz2_Object = MibTableColumn
turboRoamingChannelN5GHz2 = _TurboRoamingChannelN5GHz2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 20),
    _TurboRoamingChannelN5GHz2_Type()
)
turboRoamingChannelN5GHz2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz2.setStatus("current")
_TurboRoamingChannelN5GHz3_Type = Integer32
_TurboRoamingChannelN5GHz3_Object = MibTableColumn
turboRoamingChannelN5GHz3 = _TurboRoamingChannelN5GHz3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 21),
    _TurboRoamingChannelN5GHz3_Type()
)
turboRoamingChannelN5GHz3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz3.setStatus("current")


class _TurboRoamingSelectTRtypeEnable_Type(Integer32):
    """Custom type turboRoamingSelectTRtypeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("troam100", 1),
          ("troam50", 2))
    )


_TurboRoamingSelectTRtypeEnable_Type.__name__ = "Integer32"
_TurboRoamingSelectTRtypeEnable_Object = MibTableColumn
turboRoamingSelectTRtypeEnable = _TurboRoamingSelectTRtypeEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 22),
    _TurboRoamingSelectTRtypeEnable_Type()
)
turboRoamingSelectTRtypeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingSelectTRtypeEnable.setStatus("current")


class _TurboRoamingRoamingThreshunit_Type(Integer32):
    """Custom type turboRoamingRoamingThreshunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snr", 1),
          ("signal-strength", 2))
    )


_TurboRoamingRoamingThreshunit_Type.__name__ = "Integer32"
_TurboRoamingRoamingThreshunit_Object = MibTableColumn
turboRoamingRoamingThreshunit = _TurboRoamingRoamingThreshunit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 23),
    _TurboRoamingRoamingThreshunit_Type()
)
turboRoamingRoamingThreshunit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThreshunit.setStatus("current")


class _TurboRoamingRoamingAliveunit_Type(Integer32):
    """Custom type turboRoamingRoamingAliveunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snr", 1),
          ("signal-strength", 2))
    )


_TurboRoamingRoamingAliveunit_Type.__name__ = "Integer32"
_TurboRoamingRoamingAliveunit_Object = MibTableColumn
turboRoamingRoamingAliveunit = _TurboRoamingRoamingAliveunit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 24),
    _TurboRoamingRoamingAliveunit_Type()
)
turboRoamingRoamingAliveunit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingAliveunit.setStatus("current")


class _TurboRoamingRoamingThresh2GSNR_Type(Integer32):
    """Custom type turboRoamingRoamingThresh2GSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TurboRoamingRoamingThresh2GSNR_Type.__name__ = "Integer32"
_TurboRoamingRoamingThresh2GSNR_Object = MibTableColumn
turboRoamingRoamingThresh2GSNR = _TurboRoamingRoamingThresh2GSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 25),
    _TurboRoamingRoamingThresh2GSNR_Type()
)
turboRoamingRoamingThresh2GSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThresh2GSNR.setStatus("current")


class _TurboRoamingRoamingThresh2GSignal_Type(Integer32):
    """Custom type turboRoamingRoamingThresh2GSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingRoamingThresh2GSignal_Type.__name__ = "Integer32"
_TurboRoamingRoamingThresh2GSignal_Object = MibTableColumn
turboRoamingRoamingThresh2GSignal = _TurboRoamingRoamingThresh2GSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 26),
    _TurboRoamingRoamingThresh2GSignal_Type()
)
turboRoamingRoamingThresh2GSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThresh2GSignal.setStatus("current")


class _TurboRoamingRoamingDifference2G_Type(Integer32):
    """Custom type turboRoamingRoamingDifference2G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TurboRoamingRoamingDifference2G_Type.__name__ = "Integer32"
_TurboRoamingRoamingDifference2G_Object = MibTableColumn
turboRoamingRoamingDifference2G = _TurboRoamingRoamingDifference2G_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 27),
    _TurboRoamingRoamingDifference2G_Type()
)
turboRoamingRoamingDifference2G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingDifference2G.setStatus("current")


class _TurboRoamingApCandidateThreshold2GSNR_Type(Integer32):
    """Custom type turboRoamingApCandidateThreshold2GSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_TurboRoamingApCandidateThreshold2GSNR_Type.__name__ = "Integer32"
_TurboRoamingApCandidateThreshold2GSNR_Object = MibTableColumn
turboRoamingApCandidateThreshold2GSNR = _TurboRoamingApCandidateThreshold2GSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 28),
    _TurboRoamingApCandidateThreshold2GSNR_Type()
)
turboRoamingApCandidateThreshold2GSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingApCandidateThreshold2GSNR.setStatus("current")


class _TurboRoamingApCandidateThreshold2GSignal_Type(Integer32):
    """Custom type turboRoamingApCandidateThreshold2GSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingApCandidateThreshold2GSignal_Type.__name__ = "Integer32"
_TurboRoamingApCandidateThreshold2GSignal_Object = MibTableColumn
turboRoamingApCandidateThreshold2GSignal = _TurboRoamingApCandidateThreshold2GSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 29),
    _TurboRoamingApCandidateThreshold2GSignal_Type()
)
turboRoamingApCandidateThreshold2GSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingApCandidateThreshold2GSignal.setStatus("current")


class _TurboRoamingRoamingThresh5GSNR_Type(Integer32):
    """Custom type turboRoamingRoamingThresh5GSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TurboRoamingRoamingThresh5GSNR_Type.__name__ = "Integer32"
_TurboRoamingRoamingThresh5GSNR_Object = MibTableColumn
turboRoamingRoamingThresh5GSNR = _TurboRoamingRoamingThresh5GSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 30),
    _TurboRoamingRoamingThresh5GSNR_Type()
)
turboRoamingRoamingThresh5GSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThresh5GSNR.setStatus("current")


class _TurboRoamingRoamingThresh5GSignal_Type(Integer32):
    """Custom type turboRoamingRoamingThresh5GSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingRoamingThresh5GSignal_Type.__name__ = "Integer32"
_TurboRoamingRoamingThresh5GSignal_Object = MibTableColumn
turboRoamingRoamingThresh5GSignal = _TurboRoamingRoamingThresh5GSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 31),
    _TurboRoamingRoamingThresh5GSignal_Type()
)
turboRoamingRoamingThresh5GSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThresh5GSignal.setStatus("current")


class _TurboRoamingRoamingDifference5G_Type(Integer32):
    """Custom type turboRoamingRoamingDifference5G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_TurboRoamingRoamingDifference5G_Type.__name__ = "Integer32"
_TurboRoamingRoamingDifference5G_Object = MibTableColumn
turboRoamingRoamingDifference5G = _TurboRoamingRoamingDifference5G_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 32),
    _TurboRoamingRoamingDifference5G_Type()
)
turboRoamingRoamingDifference5G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingDifference5G.setStatus("current")


class _TurboRoamingApCandidateThreshold5GSNR_Type(Integer32):
    """Custom type turboRoamingApCandidateThreshold5GSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_TurboRoamingApCandidateThreshold5GSNR_Type.__name__ = "Integer32"
_TurboRoamingApCandidateThreshold5GSNR_Object = MibTableColumn
turboRoamingApCandidateThreshold5GSNR = _TurboRoamingApCandidateThreshold5GSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 33),
    _TurboRoamingApCandidateThreshold5GSNR_Type()
)
turboRoamingApCandidateThreshold5GSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingApCandidateThreshold5GSNR.setStatus("current")


class _TurboRoamingApCandidateThreshold5GSignal_Type(Integer32):
    """Custom type turboRoamingApCandidateThreshold5GSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingApCandidateThreshold5GSignal_Type.__name__ = "Integer32"
_TurboRoamingApCandidateThreshold5GSignal_Object = MibTableColumn
turboRoamingApCandidateThreshold5GSignal = _TurboRoamingApCandidateThreshold5GSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 34),
    _TurboRoamingApCandidateThreshold5GSignal_Type()
)
turboRoamingApCandidateThreshold5GSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingApCandidateThreshold5GSignal.setStatus("current")


class _TurboRoamingRoamingThreshLegacySNR_Type(Integer32):
    """Custom type turboRoamingRoamingThreshLegacySNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TurboRoamingRoamingThreshLegacySNR_Type.__name__ = "Integer32"
_TurboRoamingRoamingThreshLegacySNR_Object = MibTableColumn
turboRoamingRoamingThreshLegacySNR = _TurboRoamingRoamingThreshLegacySNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 36),
    _TurboRoamingRoamingThreshLegacySNR_Type()
)
turboRoamingRoamingThreshLegacySNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThreshLegacySNR.setStatus("current")


class _TurboRoamingRoamingThreshLegacySignal_Type(Integer32):
    """Custom type turboRoamingRoamingThreshLegacySignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingRoamingThreshLegacySignal_Type.__name__ = "Integer32"
_TurboRoamingRoamingThreshLegacySignal_Object = MibTableColumn
turboRoamingRoamingThreshLegacySignal = _TurboRoamingRoamingThreshLegacySignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 37),
    _TurboRoamingRoamingThreshLegacySignal_Type()
)
turboRoamingRoamingThreshLegacySignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThreshLegacySignal.setStatus("current")


class _TurboRoamingRoamingThreshNmodeSNR_Type(Integer32):
    """Custom type turboRoamingRoamingThreshNmodeSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TurboRoamingRoamingThreshNmodeSNR_Type.__name__ = "Integer32"
_TurboRoamingRoamingThreshNmodeSNR_Object = MibTableColumn
turboRoamingRoamingThreshNmodeSNR = _TurboRoamingRoamingThreshNmodeSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 38),
    _TurboRoamingRoamingThreshNmodeSNR_Type()
)
turboRoamingRoamingThreshNmodeSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThreshNmodeSNR.setStatus("current")


class _TurboRoamingRoamingThreshNmode24GSignal_Type(Integer32):
    """Custom type turboRoamingRoamingThreshNmode24GSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingRoamingThreshNmode24GSignal_Type.__name__ = "Integer32"
_TurboRoamingRoamingThreshNmode24GSignal_Object = MibTableColumn
turboRoamingRoamingThreshNmode24GSignal = _TurboRoamingRoamingThreshNmode24GSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 39),
    _TurboRoamingRoamingThreshNmode24GSignal_Type()
)
turboRoamingRoamingThreshNmode24GSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThreshNmode24GSignal.setStatus("current")


class _TurboRoamingRoamingThreshNmode5GSignal_Type(Integer32):
    """Custom type turboRoamingRoamingThreshNmode5GSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingRoamingThreshNmode5GSignal_Type.__name__ = "Integer32"
_TurboRoamingRoamingThreshNmode5GSignal_Object = MibTableColumn
turboRoamingRoamingThreshNmode5GSignal = _TurboRoamingRoamingThreshNmode5GSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 40),
    _TurboRoamingRoamingThreshNmode5GSignal_Type()
)
turboRoamingRoamingThreshNmode5GSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingThreshNmode5GSignal.setStatus("current")
_TurboRoamingChannelA4_Type = Integer32
_TurboRoamingChannelA4_Object = MibTableColumn
turboRoamingChannelA4 = _TurboRoamingChannelA4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 54),
    _TurboRoamingChannelA4_Type()
)
turboRoamingChannelA4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA4.setStatus("current")
_TurboRoamingChannelA5_Type = Integer32
_TurboRoamingChannelA5_Object = MibTableColumn
turboRoamingChannelA5 = _TurboRoamingChannelA5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 55),
    _TurboRoamingChannelA5_Type()
)
turboRoamingChannelA5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA5.setStatus("current")
_TurboRoamingChannelB4_Type = Integer32
_TurboRoamingChannelB4_Object = MibTableColumn
turboRoamingChannelB4 = _TurboRoamingChannelB4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 56),
    _TurboRoamingChannelB4_Type()
)
turboRoamingChannelB4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB4.setStatus("current")
_TurboRoamingChannelB5_Type = Integer32
_TurboRoamingChannelB5_Object = MibTableColumn
turboRoamingChannelB5 = _TurboRoamingChannelB5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 57),
    _TurboRoamingChannelB5_Type()
)
turboRoamingChannelB5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB5.setStatus("current")
_TurboRoamingChannelG4_Type = Integer32
_TurboRoamingChannelG4_Object = MibTableColumn
turboRoamingChannelG4 = _TurboRoamingChannelG4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 58),
    _TurboRoamingChannelG4_Type()
)
turboRoamingChannelG4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG4.setStatus("current")
_TurboRoamingChannelG5_Type = Integer32
_TurboRoamingChannelG5_Object = MibTableColumn
turboRoamingChannelG5 = _TurboRoamingChannelG5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 59),
    _TurboRoamingChannelG5_Type()
)
turboRoamingChannelG5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG5.setStatus("current")
_TurboRoamingChannelBG4_Type = Integer32
_TurboRoamingChannelBG4_Object = MibTableColumn
turboRoamingChannelBG4 = _TurboRoamingChannelBG4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 60),
    _TurboRoamingChannelBG4_Type()
)
turboRoamingChannelBG4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG4.setStatus("current")
_TurboRoamingChannelBG5_Type = Integer32
_TurboRoamingChannelBG5_Object = MibTableColumn
turboRoamingChannelBG5 = _TurboRoamingChannelBG5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 61),
    _TurboRoamingChannelBG5_Type()
)
turboRoamingChannelBG5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG5.setStatus("current")
_TurboRoamingChannelN24GHz4_Type = Integer32
_TurboRoamingChannelN24GHz4_Object = MibTableColumn
turboRoamingChannelN24GHz4 = _TurboRoamingChannelN24GHz4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 62),
    _TurboRoamingChannelN24GHz4_Type()
)
turboRoamingChannelN24GHz4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz4.setStatus("current")
_TurboRoamingChannelN24GHz5_Type = Integer32
_TurboRoamingChannelN24GHz5_Object = MibTableColumn
turboRoamingChannelN24GHz5 = _TurboRoamingChannelN24GHz5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 63),
    _TurboRoamingChannelN24GHz5_Type()
)
turboRoamingChannelN24GHz5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz5.setStatus("current")
_TurboRoamingChannelN5GHz4_Type = Integer32
_TurboRoamingChannelN5GHz4_Object = MibTableColumn
turboRoamingChannelN5GHz4 = _TurboRoamingChannelN5GHz4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 64),
    _TurboRoamingChannelN5GHz4_Type()
)
turboRoamingChannelN5GHz4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz4.setStatus("current")
_TurboRoamingChannelN5GHz5_Type = Integer32
_TurboRoamingChannelN5GHz5_Object = MibTableColumn
turboRoamingChannelN5GHz5 = _TurboRoamingChannelN5GHz5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 65),
    _TurboRoamingChannelN5GHz5_Type()
)
turboRoamingChannelN5GHz5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz5.setStatus("current")


class _TurboRoamingRoamingAliveLegacySNR_Type(Integer32):
    """Custom type turboRoamingRoamingAliveLegacySNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TurboRoamingRoamingAliveLegacySNR_Type.__name__ = "Integer32"
_TurboRoamingRoamingAliveLegacySNR_Object = MibTableColumn
turboRoamingRoamingAliveLegacySNR = _TurboRoamingRoamingAliveLegacySNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 68),
    _TurboRoamingRoamingAliveLegacySNR_Type()
)
turboRoamingRoamingAliveLegacySNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingAliveLegacySNR.setStatus("current")


class _TurboRoamingRoamingAliveSignal_Type(Integer32):
    """Custom type turboRoamingRoamingAliveSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingRoamingAliveSignal_Type.__name__ = "Integer32"
_TurboRoamingRoamingAliveSignal_Object = MibTableColumn
turboRoamingRoamingAliveSignal = _TurboRoamingRoamingAliveSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 69),
    _TurboRoamingRoamingAliveSignal_Type()
)
turboRoamingRoamingAliveSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingAliveSignal.setStatus("current")


class _TurboRoamingRoamingAliveNmode24GSNR_Type(Integer32):
    """Custom type turboRoamingRoamingAliveNmode24GSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TurboRoamingRoamingAliveNmode24GSNR_Type.__name__ = "Integer32"
_TurboRoamingRoamingAliveNmode24GSNR_Object = MibTableColumn
turboRoamingRoamingAliveNmode24GSNR = _TurboRoamingRoamingAliveNmode24GSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 70),
    _TurboRoamingRoamingAliveNmode24GSNR_Type()
)
turboRoamingRoamingAliveNmode24GSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingAliveNmode24GSNR.setStatus("current")


class _TurboRoamingRoamingAliveNmode24GSignal_Type(Integer32):
    """Custom type turboRoamingRoamingAliveNmode24GSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingRoamingAliveNmode24GSignal_Type.__name__ = "Integer32"
_TurboRoamingRoamingAliveNmode24GSignal_Object = MibTableColumn
turboRoamingRoamingAliveNmode24GSignal = _TurboRoamingRoamingAliveNmode24GSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 71),
    _TurboRoamingRoamingAliveNmode24GSignal_Type()
)
turboRoamingRoamingAliveNmode24GSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingAliveNmode24GSignal.setStatus("current")


class _TurboRoamingRoamingAliveNmode5GSNR_Type(Integer32):
    """Custom type turboRoamingRoamingAliveNmode5GSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_TurboRoamingRoamingAliveNmode5GSNR_Type.__name__ = "Integer32"
_TurboRoamingRoamingAliveNmode5GSNR_Object = MibTableColumn
turboRoamingRoamingAliveNmode5GSNR = _TurboRoamingRoamingAliveNmode5GSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 72),
    _TurboRoamingRoamingAliveNmode5GSNR_Type()
)
turboRoamingRoamingAliveNmode5GSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingAliveNmode5GSNR.setStatus("current")


class _TurboRoamingRoamingAliveNmode5GSignal_Type(Integer32):
    """Custom type turboRoamingRoamingAliveNmode5GSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -35),
    )


_TurboRoamingRoamingAliveNmode5GSignal_Type.__name__ = "Integer32"
_TurboRoamingRoamingAliveNmode5GSignal_Object = MibTableColumn
turboRoamingRoamingAliveNmode5GSignal = _TurboRoamingRoamingAliveNmode5GSignal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 73),
    _TurboRoamingRoamingAliveNmode5GSignal_Type()
)
turboRoamingRoamingAliveNmode5GSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingRoamingAliveNmode5GSignal.setStatus("current")
_TurboRoamingChannelA6_Type = Integer32
_TurboRoamingChannelA6_Object = MibTableColumn
turboRoamingChannelA6 = _TurboRoamingChannelA6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 203),
    _TurboRoamingChannelA6_Type()
)
turboRoamingChannelA6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA6.setStatus("current")
_TurboRoamingChannelA7_Type = Integer32
_TurboRoamingChannelA7_Object = MibTableColumn
turboRoamingChannelA7 = _TurboRoamingChannelA7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 204),
    _TurboRoamingChannelA7_Type()
)
turboRoamingChannelA7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA7.setStatus("current")
_TurboRoamingChannelA8_Type = Integer32
_TurboRoamingChannelA8_Object = MibTableColumn
turboRoamingChannelA8 = _TurboRoamingChannelA8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 205),
    _TurboRoamingChannelA8_Type()
)
turboRoamingChannelA8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA8.setStatus("current")
_TurboRoamingChannelA9_Type = Integer32
_TurboRoamingChannelA9_Object = MibTableColumn
turboRoamingChannelA9 = _TurboRoamingChannelA9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 206),
    _TurboRoamingChannelA9_Type()
)
turboRoamingChannelA9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA9.setStatus("current")
_TurboRoamingChannelA10_Type = Integer32
_TurboRoamingChannelA10_Object = MibTableColumn
turboRoamingChannelA10 = _TurboRoamingChannelA10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 207),
    _TurboRoamingChannelA10_Type()
)
turboRoamingChannelA10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA10.setStatus("current")
_TurboRoamingChannelA11_Type = Integer32
_TurboRoamingChannelA11_Object = MibTableColumn
turboRoamingChannelA11 = _TurboRoamingChannelA11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 208),
    _TurboRoamingChannelA11_Type()
)
turboRoamingChannelA11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelA11.setStatus("current")
_TurboRoamingChannelB6_Type = Integer32
_TurboRoamingChannelB6_Object = MibTableColumn
turboRoamingChannelB6 = _TurboRoamingChannelB6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 223),
    _TurboRoamingChannelB6_Type()
)
turboRoamingChannelB6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB6.setStatus("current")
_TurboRoamingChannelB7_Type = Integer32
_TurboRoamingChannelB7_Object = MibTableColumn
turboRoamingChannelB7 = _TurboRoamingChannelB7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 224),
    _TurboRoamingChannelB7_Type()
)
turboRoamingChannelB7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB7.setStatus("current")
_TurboRoamingChannelB8_Type = Integer32
_TurboRoamingChannelB8_Object = MibTableColumn
turboRoamingChannelB8 = _TurboRoamingChannelB8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 225),
    _TurboRoamingChannelB8_Type()
)
turboRoamingChannelB8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB8.setStatus("current")
_TurboRoamingChannelB9_Type = Integer32
_TurboRoamingChannelB9_Object = MibTableColumn
turboRoamingChannelB9 = _TurboRoamingChannelB9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 226),
    _TurboRoamingChannelB9_Type()
)
turboRoamingChannelB9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB9.setStatus("current")
_TurboRoamingChannelB10_Type = Integer32
_TurboRoamingChannelB10_Object = MibTableColumn
turboRoamingChannelB10 = _TurboRoamingChannelB10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 227),
    _TurboRoamingChannelB10_Type()
)
turboRoamingChannelB10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB10.setStatus("current")
_TurboRoamingChannelB11_Type = Integer32
_TurboRoamingChannelB11_Object = MibTableColumn
turboRoamingChannelB11 = _TurboRoamingChannelB11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 228),
    _TurboRoamingChannelB11_Type()
)
turboRoamingChannelB11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelB11.setStatus("current")
_TurboRoamingChannelG6_Type = Integer32
_TurboRoamingChannelG6_Object = MibTableColumn
turboRoamingChannelG6 = _TurboRoamingChannelG6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 243),
    _TurboRoamingChannelG6_Type()
)
turboRoamingChannelG6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG6.setStatus("current")
_TurboRoamingChannelG7_Type = Integer32
_TurboRoamingChannelG7_Object = MibTableColumn
turboRoamingChannelG7 = _TurboRoamingChannelG7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 244),
    _TurboRoamingChannelG7_Type()
)
turboRoamingChannelG7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG7.setStatus("current")
_TurboRoamingChannelG8_Type = Integer32
_TurboRoamingChannelG8_Object = MibTableColumn
turboRoamingChannelG8 = _TurboRoamingChannelG8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 245),
    _TurboRoamingChannelG8_Type()
)
turboRoamingChannelG8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG8.setStatus("current")
_TurboRoamingChannelG9_Type = Integer32
_TurboRoamingChannelG9_Object = MibTableColumn
turboRoamingChannelG9 = _TurboRoamingChannelG9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 246),
    _TurboRoamingChannelG9_Type()
)
turboRoamingChannelG9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG9.setStatus("current")
_TurboRoamingChannelG10_Type = Integer32
_TurboRoamingChannelG10_Object = MibTableColumn
turboRoamingChannelG10 = _TurboRoamingChannelG10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 247),
    _TurboRoamingChannelG10_Type()
)
turboRoamingChannelG10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG10.setStatus("current")
_TurboRoamingChannelG11_Type = Integer32
_TurboRoamingChannelG11_Object = MibTableColumn
turboRoamingChannelG11 = _TurboRoamingChannelG11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 248),
    _TurboRoamingChannelG11_Type()
)
turboRoamingChannelG11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelG11.setStatus("current")
_TurboRoamingChannelBG6_Type = Integer32
_TurboRoamingChannelBG6_Object = MibTableColumn
turboRoamingChannelBG6 = _TurboRoamingChannelBG6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 263),
    _TurboRoamingChannelBG6_Type()
)
turboRoamingChannelBG6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG6.setStatus("current")
_TurboRoamingChannelBG7_Type = Integer32
_TurboRoamingChannelBG7_Object = MibTableColumn
turboRoamingChannelBG7 = _TurboRoamingChannelBG7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 264),
    _TurboRoamingChannelBG7_Type()
)
turboRoamingChannelBG7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG7.setStatus("current")
_TurboRoamingChannelBG8_Type = Integer32
_TurboRoamingChannelBG8_Object = MibTableColumn
turboRoamingChannelBG8 = _TurboRoamingChannelBG8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 265),
    _TurboRoamingChannelBG8_Type()
)
turboRoamingChannelBG8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG8.setStatus("current")
_TurboRoamingChannelBG9_Type = Integer32
_TurboRoamingChannelBG9_Object = MibTableColumn
turboRoamingChannelBG9 = _TurboRoamingChannelBG9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 266),
    _TurboRoamingChannelBG9_Type()
)
turboRoamingChannelBG9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG9.setStatus("current")
_TurboRoamingChannelBG10_Type = Integer32
_TurboRoamingChannelBG10_Object = MibTableColumn
turboRoamingChannelBG10 = _TurboRoamingChannelBG10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 267),
    _TurboRoamingChannelBG10_Type()
)
turboRoamingChannelBG10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG10.setStatus("current")
_TurboRoamingChannelBG11_Type = Integer32
_TurboRoamingChannelBG11_Object = MibTableColumn
turboRoamingChannelBG11 = _TurboRoamingChannelBG11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 268),
    _TurboRoamingChannelBG11_Type()
)
turboRoamingChannelBG11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelBG11.setStatus("current")
_TurboRoamingChannelN24GHz6_Type = Integer32
_TurboRoamingChannelN24GHz6_Object = MibTableColumn
turboRoamingChannelN24GHz6 = _TurboRoamingChannelN24GHz6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 283),
    _TurboRoamingChannelN24GHz6_Type()
)
turboRoamingChannelN24GHz6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz6.setStatus("current")
_TurboRoamingChannelN24GHz7_Type = Integer32
_TurboRoamingChannelN24GHz7_Object = MibTableColumn
turboRoamingChannelN24GHz7 = _TurboRoamingChannelN24GHz7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 284),
    _TurboRoamingChannelN24GHz7_Type()
)
turboRoamingChannelN24GHz7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz7.setStatus("current")
_TurboRoamingChannelN24GHz8_Type = Integer32
_TurboRoamingChannelN24GHz8_Object = MibTableColumn
turboRoamingChannelN24GHz8 = _TurboRoamingChannelN24GHz8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 285),
    _TurboRoamingChannelN24GHz8_Type()
)
turboRoamingChannelN24GHz8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz8.setStatus("current")
_TurboRoamingChannelN24GHz9_Type = Integer32
_TurboRoamingChannelN24GHz9_Object = MibTableColumn
turboRoamingChannelN24GHz9 = _TurboRoamingChannelN24GHz9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 286),
    _TurboRoamingChannelN24GHz9_Type()
)
turboRoamingChannelN24GHz9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz9.setStatus("current")
_TurboRoamingChannelN24GHz10_Type = Integer32
_TurboRoamingChannelN24GHz10_Object = MibTableColumn
turboRoamingChannelN24GHz10 = _TurboRoamingChannelN24GHz10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 287),
    _TurboRoamingChannelN24GHz10_Type()
)
turboRoamingChannelN24GHz10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz10.setStatus("current")
_TurboRoamingChannelN24GHz11_Type = Integer32
_TurboRoamingChannelN24GHz11_Object = MibTableColumn
turboRoamingChannelN24GHz11 = _TurboRoamingChannelN24GHz11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 288),
    _TurboRoamingChannelN24GHz11_Type()
)
turboRoamingChannelN24GHz11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN24GHz11.setStatus("current")
_TurboRoamingChannelN5GHz6_Type = Integer32
_TurboRoamingChannelN5GHz6_Object = MibTableColumn
turboRoamingChannelN5GHz6 = _TurboRoamingChannelN5GHz6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 303),
    _TurboRoamingChannelN5GHz6_Type()
)
turboRoamingChannelN5GHz6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz6.setStatus("current")
_TurboRoamingChannelN5GHz7_Type = Integer32
_TurboRoamingChannelN5GHz7_Object = MibTableColumn
turboRoamingChannelN5GHz7 = _TurboRoamingChannelN5GHz7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 304),
    _TurboRoamingChannelN5GHz7_Type()
)
turboRoamingChannelN5GHz7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz7.setStatus("current")
_TurboRoamingChannelN5GHz8_Type = Integer32
_TurboRoamingChannelN5GHz8_Object = MibTableColumn
turboRoamingChannelN5GHz8 = _TurboRoamingChannelN5GHz8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 305),
    _TurboRoamingChannelN5GHz8_Type()
)
turboRoamingChannelN5GHz8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz8.setStatus("current")
_TurboRoamingChannelN5GHz9_Type = Integer32
_TurboRoamingChannelN5GHz9_Object = MibTableColumn
turboRoamingChannelN5GHz9 = _TurboRoamingChannelN5GHz9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 306),
    _TurboRoamingChannelN5GHz9_Type()
)
turboRoamingChannelN5GHz9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz9.setStatus("current")
_TurboRoamingChannelN5GHz10_Type = Integer32
_TurboRoamingChannelN5GHz10_Object = MibTableColumn
turboRoamingChannelN5GHz10 = _TurboRoamingChannelN5GHz10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 307),
    _TurboRoamingChannelN5GHz10_Type()
)
turboRoamingChannelN5GHz10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz10.setStatus("current")
_TurboRoamingChannelN5GHz11_Type = Integer32
_TurboRoamingChannelN5GHz11_Object = MibTableColumn
turboRoamingChannelN5GHz11 = _TurboRoamingChannelN5GHz11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 7, 1, 308),
    _TurboRoamingChannelN5GHz11_Type()
)
turboRoamingChannelN5GHz11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRoamingChannelN5GHz11.setStatus("current")
_AeroLinkProtection_ObjectIdentity = ObjectIdentity
aeroLinkProtection = _AeroLinkProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23)
)


class _AeroLinkProtectionAPAliveCheck_Type(Integer32):
    """Custom type aeroLinkProtectionAPAliveCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AeroLinkProtectionAPAliveCheck_Type.__name__ = "Integer32"
_AeroLinkProtectionAPAliveCheck_Object = MibScalar
aeroLinkProtectionAPAliveCheck = _AeroLinkProtectionAPAliveCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 1),
    _AeroLinkProtectionAPAliveCheck_Type()
)
aeroLinkProtectionAPAliveCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionAPAliveCheck.setStatus("current")


class _AeroLinkProtectionType_Type(Integer32):
    """Custom type aeroLinkProtectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("enable", 4),
          ("disable", 5))
    )


_AeroLinkProtectionType_Type.__name__ = "Integer32"
_AeroLinkProtectionType_Object = MibScalar
aeroLinkProtectionType = _AeroLinkProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 2),
    _AeroLinkProtectionType_Type()
)
aeroLinkProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionType.setStatus("current")


class _AeroLinkProtectionNumPort_Type(Integer32):
    """Custom type aeroLinkProtectionNumPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port1", 1)
    )


_AeroLinkProtectionNumPort_Type.__name__ = "Integer32"
_AeroLinkProtectionNumPort_Object = MibScalar
aeroLinkProtectionNumPort = _AeroLinkProtectionNumPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 3),
    _AeroLinkProtectionNumPort_Type()
)
aeroLinkProtectionNumPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionNumPort.setStatus("current")


class _AeroLinkProtectionRfIndex_Type(Integer32):
    """Custom type aeroLinkProtectionRfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rf1", 1)
    )


_AeroLinkProtectionRfIndex_Type.__name__ = "Integer32"
_AeroLinkProtectionRfIndex_Object = MibScalar
aeroLinkProtectionRfIndex = _AeroLinkProtectionRfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 4),
    _AeroLinkProtectionRfIndex_Type()
)
aeroLinkProtectionRfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionRfIndex.setStatus("current")


class _AeroLinkProtectionRssi_detect_en_Type(Integer32):
    """Custom type aeroLinkProtectionRssi_detect_en based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AeroLinkProtectionRssi_detect_en_Type.__name__ = "Integer32"
_AeroLinkProtectionRssi_detect_en_Object = MibScalar
aeroLinkProtectionRssi_detect_en = _AeroLinkProtectionRssi_detect_en_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 7),
    _AeroLinkProtectionRssi_detect_en_Type()
)
aeroLinkProtectionRssi_detect_en.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionRssi_detect_en.setStatus("current")


class _AeroLinkProtectionRssi_detect_unit_Type(Integer32):
    """Custom type aeroLinkProtectionRssi_detect_unit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snr", 1),
          ("signal-strength", 2))
    )


_AeroLinkProtectionRssi_detect_unit_Type.__name__ = "Integer32"
_AeroLinkProtectionRssi_detect_unit_Object = MibScalar
aeroLinkProtectionRssi_detect_unit = _AeroLinkProtectionRssi_detect_unit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 8),
    _AeroLinkProtectionRssi_detect_unit_Type()
)
aeroLinkProtectionRssi_detect_unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionRssi_detect_unit.setStatus("current")


class _AeroLinkProtectionThreshold2G_SNR_Type(Integer32):
    """Custom type aeroLinkProtectionThreshold2G_SNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_AeroLinkProtectionThreshold2G_SNR_Type.__name__ = "Integer32"
_AeroLinkProtectionThreshold2G_SNR_Object = MibScalar
aeroLinkProtectionThreshold2G_SNR = _AeroLinkProtectionThreshold2G_SNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 9),
    _AeroLinkProtectionThreshold2G_SNR_Type()
)
aeroLinkProtectionThreshold2G_SNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThreshold2G_SNR.setStatus("current")
_AeroLinkProtectionThreshold2G_Signal_Type = Integer32
_AeroLinkProtectionThreshold2G_Signal_Object = MibScalar
aeroLinkProtectionThreshold2G_Signal = _AeroLinkProtectionThreshold2G_Signal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 10),
    _AeroLinkProtectionThreshold2G_Signal_Type()
)
aeroLinkProtectionThreshold2G_Signal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThreshold2G_Signal.setStatus("current")


class _AeroLinkProtectionDifference2G_Type(Integer32):
    """Custom type aeroLinkProtectionDifference2G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_AeroLinkProtectionDifference2G_Type.__name__ = "Integer32"
_AeroLinkProtectionDifference2G_Object = MibScalar
aeroLinkProtectionDifference2G = _AeroLinkProtectionDifference2G_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 11),
    _AeroLinkProtectionDifference2G_Type()
)
aeroLinkProtectionDifference2G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionDifference2G.setStatus("current")


class _AeroLinkProtectionThreshold5G_SNR_Type(Integer32):
    """Custom type aeroLinkProtectionThreshold5G_SNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_AeroLinkProtectionThreshold5G_SNR_Type.__name__ = "Integer32"
_AeroLinkProtectionThreshold5G_SNR_Object = MibScalar
aeroLinkProtectionThreshold5G_SNR = _AeroLinkProtectionThreshold5G_SNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 12),
    _AeroLinkProtectionThreshold5G_SNR_Type()
)
aeroLinkProtectionThreshold5G_SNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThreshold5G_SNR.setStatus("current")
_AeroLinkProtectionThreshold5G_Signal_Type = Integer32
_AeroLinkProtectionThreshold5G_Signal_Object = MibScalar
aeroLinkProtectionThreshold5G_Signal = _AeroLinkProtectionThreshold5G_Signal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 13),
    _AeroLinkProtectionThreshold5G_Signal_Type()
)
aeroLinkProtectionThreshold5G_Signal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThreshold5G_Signal.setStatus("current")


class _AeroLinkProtectionDifference5G_Type(Integer32):
    """Custom type aeroLinkProtectionDifference5G based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_AeroLinkProtectionDifference5G_Type.__name__ = "Integer32"
_AeroLinkProtectionDifference5G_Object = MibScalar
aeroLinkProtectionDifference5G = _AeroLinkProtectionDifference5G_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 14),
    _AeroLinkProtectionDifference5G_Type()
)
aeroLinkProtectionDifference5G.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionDifference5G.setStatus("current")


class _AeroLinkProtectionThresholdLegacy_SNR_Type(Integer32):
    """Custom type aeroLinkProtectionThresholdLegacy_SNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_AeroLinkProtectionThresholdLegacy_SNR_Type.__name__ = "Integer32"
_AeroLinkProtectionThresholdLegacy_SNR_Object = MibScalar
aeroLinkProtectionThresholdLegacy_SNR = _AeroLinkProtectionThresholdLegacy_SNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 15),
    _AeroLinkProtectionThresholdLegacy_SNR_Type()
)
aeroLinkProtectionThresholdLegacy_SNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThresholdLegacy_SNR.setStatus("current")
_AeroLinkProtectionThresholdLegacy_Signal_Type = Integer32
_AeroLinkProtectionThresholdLegacy_Signal_Object = MibScalar
aeroLinkProtectionThresholdLegacy_Signal = _AeroLinkProtectionThresholdLegacy_Signal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 16),
    _AeroLinkProtectionThresholdLegacy_Signal_Type()
)
aeroLinkProtectionThresholdLegacy_Signal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThresholdLegacy_Signal.setStatus("current")


class _AeroLinkProtectionThresholdNmode_SNR_Type(Integer32):
    """Custom type aeroLinkProtectionThresholdNmode_SNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_AeroLinkProtectionThresholdNmode_SNR_Type.__name__ = "Integer32"
_AeroLinkProtectionThresholdNmode_SNR_Object = MibScalar
aeroLinkProtectionThresholdNmode_SNR = _AeroLinkProtectionThresholdNmode_SNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 17),
    _AeroLinkProtectionThresholdNmode_SNR_Type()
)
aeroLinkProtectionThresholdNmode_SNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThresholdNmode_SNR.setStatus("current")
_AeroLinkProtectionThresholdNmode24G_Signal_Type = Integer32
_AeroLinkProtectionThresholdNmode24G_Signal_Object = MibScalar
aeroLinkProtectionThresholdNmode24G_Signal = _AeroLinkProtectionThresholdNmode24G_Signal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 18),
    _AeroLinkProtectionThresholdNmode24G_Signal_Type()
)
aeroLinkProtectionThresholdNmode24G_Signal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThresholdNmode24G_Signal.setStatus("current")
_AeroLinkProtectionThresholdNmode5G_Signal_Type = Integer32
_AeroLinkProtectionThresholdNmode5G_Signal_Object = MibScalar
aeroLinkProtectionThresholdNmode5G_Signal = _AeroLinkProtectionThresholdNmode5G_Signal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 5, 23, 19),
    _AeroLinkProtectionThresholdNmode5G_Signal_Type()
)
aeroLinkProtectionThresholdNmode5G_Signal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroLinkProtectionThresholdNmode5G_Signal.setStatus("current")
_Advanced_ObjectIdentity = ObjectIdentity
advanced = _Advanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7)
)
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1)
)


class _DhcpServerEnable_Type(Integer32):
    """Custom type dhcpServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DhcpServerEnable_Type.__name__ = "Integer32"
_DhcpServerEnable_Object = MibScalar
dhcpServerEnable = _DhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 1),
    _DhcpServerEnable_Type()
)
dhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerEnable.setStatus("current")
_DhcpServerIPv4Gateway_Type = IpAddress
_DhcpServerIPv4Gateway_Object = MibScalar
dhcpServerIPv4Gateway = _DhcpServerIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 2),
    _DhcpServerIPv4Gateway_Type()
)
dhcpServerIPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIPv4Gateway.setStatus("current")
_DhcpServerIPv4Netmask_Type = IpAddress
_DhcpServerIPv4Netmask_Object = MibScalar
dhcpServerIPv4Netmask = _DhcpServerIPv4Netmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 3),
    _DhcpServerIPv4Netmask_Type()
)
dhcpServerIPv4Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIPv4Netmask.setStatus("current")
_DhcpServerDnsTable_Object = MibTable
dhcpServerDnsTable = _DhcpServerDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 4)
)
if mibBuilder.loadTexts:
    dhcpServerDnsTable.setStatus("current")
_DhcpServerDnsEntry_Object = MibTableRow
dhcpServerDnsEntry = _DhcpServerDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 4, 1)
)
dhcpServerDnsEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "dhcpServerDnsIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerDnsEntry.setStatus("current")


class _DhcpServerDnsIndex_Type(Integer32):
    """Custom type dhcpServerDnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DhcpServerDnsIndex_Type.__name__ = "Integer32"
_DhcpServerDnsIndex_Object = MibTableColumn
dhcpServerDnsIndex = _DhcpServerDnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 4, 1, 1),
    _DhcpServerDnsIndex_Type()
)
dhcpServerDnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerDnsIndex.setStatus("current")
_DhcpServerDnsData_Type = IpAddress
_DhcpServerDnsData_Object = MibTableColumn
dhcpServerDnsData = _DhcpServerDnsData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 4, 1, 2),
    _DhcpServerDnsData_Type()
)
dhcpServerDnsData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerDnsData.setStatus("current")
_DhcpServerIPv4StartAddr_Type = IpAddress
_DhcpServerIPv4StartAddr_Object = MibScalar
dhcpServerIPv4StartAddr = _DhcpServerIPv4StartAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 5),
    _DhcpServerIPv4StartAddr_Type()
)
dhcpServerIPv4StartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIPv4StartAddr.setStatus("current")


class _DhcpServerMaxClient_Type(Integer32):
    """Custom type dhcpServerMaxClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DhcpServerMaxClient_Type.__name__ = "Integer32"
_DhcpServerMaxClient_Object = MibScalar
dhcpServerMaxClient = _DhcpServerMaxClient_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 6),
    _DhcpServerMaxClient_Type()
)
dhcpServerMaxClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerMaxClient.setStatus("current")


class _DhcpServerLeaseTimeMinute_Type(Integer32):
    """Custom type dhcpServerLeaseTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 14400),
    )


_DhcpServerLeaseTimeMinute_Type.__name__ = "Integer32"
_DhcpServerLeaseTimeMinute_Object = MibScalar
dhcpServerLeaseTimeMinute = _DhcpServerLeaseTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 1, 8),
    _DhcpServerLeaseTimeMinute_Type()
)
dhcpServerLeaseTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerLeaseTimeMinute.setStatus("current")
_DhcpServerMapTable_Object = MibTable
dhcpServerMapTable = _DhcpServerMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 2)
)
if mibBuilder.loadTexts:
    dhcpServerMapTable.setStatus("current")
_DhcpServerMapEntry_Object = MibTableRow
dhcpServerMapEntry = _DhcpServerMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 2, 1)
)
dhcpServerMapEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "dhcpServerMapIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerMapEntry.setStatus("current")


class _DhcpServerMapIndex_Type(Integer32):
    """Custom type dhcpServerMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DhcpServerMapIndex_Type.__name__ = "Integer32"
_DhcpServerMapIndex_Object = MibTableColumn
dhcpServerMapIndex = _DhcpServerMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 2, 1, 1),
    _DhcpServerMapIndex_Type()
)
dhcpServerMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerMapIndex.setStatus("current")


class _DhcpServerMapEnable_Type(Integer32):
    """Custom type dhcpServerMapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DhcpServerMapEnable_Type.__name__ = "Integer32"
_DhcpServerMapEnable_Object = MibTableColumn
dhcpServerMapEnable = _DhcpServerMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 2, 1, 2),
    _DhcpServerMapEnable_Type()
)
dhcpServerMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerMapEnable.setStatus("current")
_DhcpServerMapMac_Type = DisplayString
_DhcpServerMapMac_Object = MibTableColumn
dhcpServerMapMac = _DhcpServerMapMac_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 2, 1, 3),
    _DhcpServerMapMac_Type()
)
dhcpServerMapMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerMapMac.setStatus("current")
_DhcpServerMapIPv4Addr_Type = IpAddress
_DhcpServerMapIPv4Addr_Object = MibTableColumn
dhcpServerMapIPv4Addr = _DhcpServerMapIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 2, 1, 4),
    _DhcpServerMapIPv4Addr_Type()
)
dhcpServerMapIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerMapIPv4Addr.setStatus("current")
_MacFilter_ObjectIdentity = ObjectIdentity
macFilter = _MacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3)
)


class _MacFilterEnable_Type(Integer32):
    """Custom type macFilterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MacFilterEnable_Type.__name__ = "Integer32"
_MacFilterEnable_Object = MibScalar
macFilterEnable = _MacFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3, 1),
    _MacFilterEnable_Type()
)
macFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterEnable.setStatus("current")


class _MacFilterPolicy_Type(Integer32):
    """Custom type macFilterPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2))
    )


_MacFilterPolicy_Type.__name__ = "Integer32"
_MacFilterPolicy_Object = MibScalar
macFilterPolicy = _MacFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3, 2),
    _MacFilterPolicy_Type()
)
macFilterPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterPolicy.setStatus("current")
_MacFilterRulesTable_Object = MibTable
macFilterRulesTable = _MacFilterRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3, 3)
)
if mibBuilder.loadTexts:
    macFilterRulesTable.setStatus("current")
_MacFilterRulesEntry_Object = MibTableRow
macFilterRulesEntry = _MacFilterRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3, 3, 1)
)
macFilterRulesEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "macFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    macFilterRulesEntry.setStatus("current")
_MacFilterRuleIndex_Type = Integer32
_MacFilterRuleIndex_Object = MibTableColumn
macFilterRuleIndex = _MacFilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3, 3, 1, 1),
    _MacFilterRuleIndex_Type()
)
macFilterRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterRuleIndex.setStatus("current")


class _MacFilterRuleEnable_Type(Integer32):
    """Custom type macFilterRuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MacFilterRuleEnable_Type.__name__ = "Integer32"
_MacFilterRuleEnable_Object = MibTableColumn
macFilterRuleEnable = _MacFilterRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3, 3, 1, 2),
    _MacFilterRuleEnable_Type()
)
macFilterRuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterRuleEnable.setStatus("current")
_MacFilterRuleName_Type = DisplayString
_MacFilterRuleName_Object = MibTableColumn
macFilterRuleName = _MacFilterRuleName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3, 3, 1, 3),
    _MacFilterRuleName_Type()
)
macFilterRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterRuleName.setStatus("current")
_MacFilterRuleAddr_Type = DisplayString
_MacFilterRuleAddr_Object = MibTableColumn
macFilterRuleAddr = _MacFilterRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 3, 3, 1, 4),
    _MacFilterRuleAddr_Type()
)
macFilterRuleAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFilterRuleAddr.setStatus("current")
_ProtocolFilter_ObjectIdentity = ObjectIdentity
protocolFilter = _ProtocolFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4)
)


class _ProtocolFilterEnable_Type(Integer32):
    """Custom type protocolFilterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ProtocolFilterEnable_Type.__name__ = "Integer32"
_ProtocolFilterEnable_Object = MibScalar
protocolFilterEnable = _ProtocolFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 1),
    _ProtocolFilterEnable_Type()
)
protocolFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterEnable.setStatus("current")


class _ProtocolFilterPolicy_Type(Integer32):
    """Custom type protocolFilterPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2))
    )


_ProtocolFilterPolicy_Type.__name__ = "Integer32"
_ProtocolFilterPolicy_Object = MibScalar
protocolFilterPolicy = _ProtocolFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 2),
    _ProtocolFilterPolicy_Type()
)
protocolFilterPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterPolicy.setStatus("current")
_ProtocolFilterRulesTable_Object = MibTable
protocolFilterRulesTable = _ProtocolFilterRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3)
)
if mibBuilder.loadTexts:
    protocolFilterRulesTable.setStatus("current")
_ProtocolFilterRulesEntry_Object = MibTableRow
protocolFilterRulesEntry = _ProtocolFilterRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3, 1)
)
protocolFilterRulesEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "protocolFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    protocolFilterRulesEntry.setStatus("current")
_ProtocolFilterRuleIndex_Type = Integer32
_ProtocolFilterRuleIndex_Object = MibTableColumn
protocolFilterRuleIndex = _ProtocolFilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3, 1, 1),
    _ProtocolFilterRuleIndex_Type()
)
protocolFilterRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolFilterRuleIndex.setStatus("current")


class _ProtocolFilterRuleEnable_Type(Integer32):
    """Custom type protocolFilterRuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ProtocolFilterRuleEnable_Type.__name__ = "Integer32"
_ProtocolFilterRuleEnable_Object = MibTableColumn
protocolFilterRuleEnable = _ProtocolFilterRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3, 1, 2),
    _ProtocolFilterRuleEnable_Type()
)
protocolFilterRuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterRuleEnable.setStatus("current")


class _ProtocolFilterRuleProtocol_Type(Integer32):
    """Custom type protocolFilterRuleProtocol based on Integer32"""
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
        *(("all", 1),
          ("icmp", 2),
          ("tcp", 3),
          ("udp", 4))
    )


_ProtocolFilterRuleProtocol_Type.__name__ = "Integer32"
_ProtocolFilterRuleProtocol_Object = MibTableColumn
protocolFilterRuleProtocol = _ProtocolFilterRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3, 1, 3),
    _ProtocolFilterRuleProtocol_Type()
)
protocolFilterRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterRuleProtocol.setStatus("current")
_ProtocolFilterRuleSrcIp_Type = IpAddress
_ProtocolFilterRuleSrcIp_Object = MibTableColumn
protocolFilterRuleSrcIp = _ProtocolFilterRuleSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3, 1, 4),
    _ProtocolFilterRuleSrcIp_Type()
)
protocolFilterRuleSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterRuleSrcIp.setStatus("current")
_ProtocolFilterRuleSrcMask_Type = IpAddress
_ProtocolFilterRuleSrcMask_Object = MibTableColumn
protocolFilterRuleSrcMask = _ProtocolFilterRuleSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3, 1, 5),
    _ProtocolFilterRuleSrcMask_Type()
)
protocolFilterRuleSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterRuleSrcMask.setStatus("current")
_ProtocolFilterRuleDstIp_Type = IpAddress
_ProtocolFilterRuleDstIp_Object = MibTableColumn
protocolFilterRuleDstIp = _ProtocolFilterRuleDstIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3, 1, 6),
    _ProtocolFilterRuleDstIp_Type()
)
protocolFilterRuleDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterRuleDstIp.setStatus("current")
_ProtocolFilterRuleDstMask_Type = IpAddress
_ProtocolFilterRuleDstMask_Object = MibTableColumn
protocolFilterRuleDstMask = _ProtocolFilterRuleDstMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 4, 3, 1, 7),
    _ProtocolFilterRuleDstMask_Type()
)
protocolFilterRuleDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolFilterRuleDstMask.setStatus("current")
_PortFilter_ObjectIdentity = ObjectIdentity
portFilter = _PortFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5)
)


class _PortFilterEnable_Type(Integer32):
    """Custom type portFilterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PortFilterEnable_Type.__name__ = "Integer32"
_PortFilterEnable_Object = MibScalar
portFilterEnable = _PortFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 1),
    _PortFilterEnable_Type()
)
portFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterEnable.setStatus("current")


class _PortFilterPolicy_Type(Integer32):
    """Custom type portFilterPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2))
    )


_PortFilterPolicy_Type.__name__ = "Integer32"
_PortFilterPolicy_Object = MibScalar
portFilterPolicy = _PortFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 2),
    _PortFilterPolicy_Type()
)
portFilterPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterPolicy.setStatus("current")
_PortFilterRulesTable_Object = MibTable
portFilterRulesTable = _PortFilterRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3)
)
if mibBuilder.loadTexts:
    portFilterRulesTable.setStatus("current")
_PortFilterRulesEntry_Object = MibTableRow
portFilterRulesEntry = _PortFilterRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1)
)
portFilterRulesEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "portFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    portFilterRulesEntry.setStatus("current")
_PortFilterRuleIndex_Type = Integer32
_PortFilterRuleIndex_Object = MibTableColumn
portFilterRuleIndex = _PortFilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1, 1),
    _PortFilterRuleIndex_Type()
)
portFilterRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFilterRuleIndex.setStatus("current")


class _PortFilterRuleEnable_Type(Integer32):
    """Custom type portFilterRuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PortFilterRuleEnable_Type.__name__ = "Integer32"
_PortFilterRuleEnable_Object = MibTableColumn
portFilterRuleEnable = _PortFilterRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1, 2),
    _PortFilterRuleEnable_Type()
)
portFilterRuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterRuleEnable.setStatus("current")
_PortFilterRuleName_Type = DisplayString
_PortFilterRuleName_Object = MibTableColumn
portFilterRuleName = _PortFilterRuleName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1, 3),
    _PortFilterRuleName_Type()
)
portFilterRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterRuleName.setStatus("current")


class _PortFilterRuleProtocol_Type(Integer32):
    """Custom type portFilterRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_PortFilterRuleProtocol_Type.__name__ = "Integer32"
_PortFilterRuleProtocol_Object = MibTableColumn
portFilterRuleProtocol = _PortFilterRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1, 4),
    _PortFilterRuleProtocol_Type()
)
portFilterRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterRuleProtocol.setStatus("current")


class _PortFilterRuleSrcPortStart_Type(Integer32):
    """Custom type portFilterRuleSrcPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortFilterRuleSrcPortStart_Type.__name__ = "Integer32"
_PortFilterRuleSrcPortStart_Object = MibTableColumn
portFilterRuleSrcPortStart = _PortFilterRuleSrcPortStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1, 5),
    _PortFilterRuleSrcPortStart_Type()
)
portFilterRuleSrcPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterRuleSrcPortStart.setStatus("current")


class _PortFilterRuleSrcPortEnd_Type(Integer32):
    """Custom type portFilterRuleSrcPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortFilterRuleSrcPortEnd_Type.__name__ = "Integer32"
_PortFilterRuleSrcPortEnd_Object = MibTableColumn
portFilterRuleSrcPortEnd = _PortFilterRuleSrcPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1, 6),
    _PortFilterRuleSrcPortEnd_Type()
)
portFilterRuleSrcPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterRuleSrcPortEnd.setStatus("current")


class _PortFilterRuleDstPortStart_Type(Integer32):
    """Custom type portFilterRuleDstPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortFilterRuleDstPortStart_Type.__name__ = "Integer32"
_PortFilterRuleDstPortStart_Object = MibTableColumn
portFilterRuleDstPortStart = _PortFilterRuleDstPortStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1, 7),
    _PortFilterRuleDstPortStart_Type()
)
portFilterRuleDstPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterRuleDstPortStart.setStatus("current")


class _PortFilterRuleDstPortEnd_Type(Integer32):
    """Custom type portFilterRuleDstPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortFilterRuleDstPortEnd_Type.__name__ = "Integer32"
_PortFilterRuleDstPortEnd_Object = MibTableColumn
portFilterRuleDstPortEnd = _PortFilterRuleDstPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 5, 3, 1, 8),
    _PortFilterRuleDstPortEnd_Type()
)
portFilterRuleDstPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFilterRuleDstPortEnd.setStatus("current")
_StpBridge_ObjectIdentity = ObjectIdentity
stpBridge = _StpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 6)
)


class _StpBridgeHelloTime_Type(Integer32):
    """Custom type stpBridgeHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpBridgeHelloTime_Type.__name__ = "Integer32"
_StpBridgeHelloTime_Object = MibScalar
stpBridgeHelloTime = _StpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 6, 1),
    _StpBridgeHelloTime_Type()
)
stpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeHelloTime.setStatus("current")


class _StpBridgeMaxAgeTime_Type(Integer32):
    """Custom type stpBridgeMaxAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StpBridgeMaxAgeTime_Type.__name__ = "Integer32"
_StpBridgeMaxAgeTime_Object = MibScalar
stpBridgeMaxAgeTime = _StpBridgeMaxAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 6, 2),
    _StpBridgeMaxAgeTime_Type()
)
stpBridgeMaxAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeMaxAgeTime.setStatus("current")


class _StpBridgeForwardDelay_Type(Integer32):
    """Custom type stpBridgeForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_StpBridgeForwardDelay_Type.__name__ = "Integer32"
_StpBridgeForwardDelay_Object = MibScalar
stpBridgeForwardDelay = _StpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 6, 3),
    _StpBridgeForwardDelay_Type()
)
stpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeForwardDelay.setStatus("current")


class _StpBridgePriority_Type(Integer32):
    """Custom type stpBridgePriority based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 1),
          ("priority4096", 2),
          ("priority8192", 3),
          ("priority12288", 4),
          ("priority16384", 5),
          ("priority20480", 6),
          ("priority24576", 7),
          ("priority28672", 8),
          ("priority32768", 9),
          ("priority36864", 10),
          ("priority40960", 11),
          ("priority45056", 12),
          ("priority49152", 13),
          ("priority53248", 14),
          ("priority57344", 15),
          ("priority61440", 16))
    )


_StpBridgePriority_Type.__name__ = "Integer32"
_StpBridgePriority_Object = MibScalar
stpBridgePriority = _StpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 6, 4),
    _StpBridgePriority_Type()
)
stpBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgePriority.setStatus("current")
_StpPortLanTable_Object = MibTable
stpPortLanTable = _StpPortLanTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 7)
)
if mibBuilder.loadTexts:
    stpPortLanTable.setStatus("current")
_StpPortLanEntry_Object = MibTableRow
stpPortLanEntry = _StpPortLanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 7, 1)
)
stpPortLanEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "stpPortLanIndex"),
)
if mibBuilder.loadTexts:
    stpPortLanEntry.setStatus("current")


class _StpPortLanIndex_Type(Integer32):
    """Custom type stpPortLanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StpPortLanIndex_Type.__name__ = "Integer32"
_StpPortLanIndex_Object = MibTableColumn
stpPortLanIndex = _StpPortLanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 7, 1, 1),
    _StpPortLanIndex_Type()
)
stpPortLanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortLanIndex.setStatus("current")


class _StpPortLanEnable_Type(Integer32):
    """Custom type stpPortLanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_StpPortLanEnable_Type.__name__ = "Integer32"
_StpPortLanEnable_Object = MibTableColumn
stpPortLanEnable = _StpPortLanEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 7, 1, 2),
    _StpPortLanEnable_Type()
)
stpPortLanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortLanEnable.setStatus("current")


class _StpPortLanPriority_Type(Integer32):
    """Custom type stpPortLanPriority based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 1),
          ("priority16", 2),
          ("priority32", 3),
          ("priority48", 4),
          ("priority64", 5),
          ("priority80", 6),
          ("priority96", 7),
          ("priority112", 8),
          ("priority128", 9),
          ("priority144", 10),
          ("priority160", 11),
          ("priority176", 12),
          ("priority192", 13),
          ("priority208", 14),
          ("priority224", 15),
          ("priority240", 16))
    )


_StpPortLanPriority_Type.__name__ = "Integer32"
_StpPortLanPriority_Object = MibTableColumn
stpPortLanPriority = _StpPortLanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 7, 1, 3),
    _StpPortLanPriority_Type()
)
stpPortLanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortLanPriority.setStatus("current")


class _StpPortLanPathCost_Type(Integer32):
    """Custom type stpPortLanPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StpPortLanPathCost_Type.__name__ = "Integer32"
_StpPortLanPathCost_Object = MibTableColumn
stpPortLanPathCost = _StpPortLanPathCost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 7, 1, 4),
    _StpPortLanPathCost_Type()
)
stpPortLanPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortLanPathCost.setStatus("current")


class _StpPortLanEdgePort_Type(Integer32):
    """Custom type stpPortLanEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_StpPortLanEdgePort_Type.__name__ = "Integer32"
_StpPortLanEdgePort_Object = MibTableColumn
stpPortLanEdgePort = _StpPortLanEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 7, 1, 5),
    _StpPortLanEdgePort_Type()
)
stpPortLanEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortLanEdgePort.setStatus("current")
_StpPortWlanTable_Object = MibTable
stpPortWlanTable = _StpPortWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 8)
)
if mibBuilder.loadTexts:
    stpPortWlanTable.setStatus("current")
_StpPortWlanEntry_Object = MibTableRow
stpPortWlanEntry = _StpPortWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 8, 1)
)
stpPortWlanEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "stpPortWlanIndex"),
)
if mibBuilder.loadTexts:
    stpPortWlanEntry.setStatus("current")


class _StpPortWlanIndex_Type(Integer32):
    """Custom type stpPortWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StpPortWlanIndex_Type.__name__ = "Integer32"
_StpPortWlanIndex_Object = MibTableColumn
stpPortWlanIndex = _StpPortWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 8, 1, 1),
    _StpPortWlanIndex_Type()
)
stpPortWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortWlanIndex.setStatus("current")


class _StpPortWlanEnable_Type(Integer32):
    """Custom type stpPortWlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_StpPortWlanEnable_Type.__name__ = "Integer32"
_StpPortWlanEnable_Object = MibTableColumn
stpPortWlanEnable = _StpPortWlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 8, 1, 2),
    _StpPortWlanEnable_Type()
)
stpPortWlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortWlanEnable.setStatus("current")


class _StpPortWlanPriority_Type(Integer32):
    """Custom type stpPortWlanPriority based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 1),
          ("priority16", 2),
          ("priority32", 3),
          ("priority48", 4),
          ("priority64", 5),
          ("priority80", 6),
          ("priority96", 7),
          ("priority112", 8),
          ("priority128", 9),
          ("priority144", 10),
          ("priority160", 11),
          ("priority176", 12),
          ("priority192", 13),
          ("priority208", 14),
          ("priority224", 15),
          ("priority240", 16))
    )


_StpPortWlanPriority_Type.__name__ = "Integer32"
_StpPortWlanPriority_Object = MibTableColumn
stpPortWlanPriority = _StpPortWlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 8, 1, 3),
    _StpPortWlanPriority_Type()
)
stpPortWlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortWlanPriority.setStatus("current")


class _StpPortWlanPathCost_Type(Integer32):
    """Custom type stpPortWlanPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StpPortWlanPathCost_Type.__name__ = "Integer32"
_StpPortWlanPathCost_Object = MibTableColumn
stpPortWlanPathCost = _StpPortWlanPathCost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 8, 1, 4),
    _StpPortWlanPathCost_Type()
)
stpPortWlanPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortWlanPathCost.setStatus("current")


class _StpPortWlanEdgePort_Type(Integer32):
    """Custom type stpPortWlanEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_StpPortWlanEdgePort_Type.__name__ = "Integer32"
_StpPortWlanEdgePort_Object = MibTableColumn
stpPortWlanEdgePort = _StpPortWlanEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 8, 1, 5),
    _StpPortWlanEdgePort_Type()
)
stpPortWlanEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortWlanEdgePort.setStatus("current")
_ManagementVID_ObjectIdentity = ObjectIdentity
managementVID = _ManagementVID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 11)
)


class _ManagementVIDVid_Type(Integer32):
    """Custom type managementVIDVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ManagementVIDVid_Type.__name__ = "Integer32"
_ManagementVIDVid_Object = MibScalar
managementVIDVid = _ManagementVIDVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 11, 1),
    _ManagementVIDVid_Type()
)
managementVIDVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVIDVid.setStatus("current")
_LanVLANTable_Object = MibTable
lanVLANTable = _LanVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12)
)
if mibBuilder.loadTexts:
    lanVLANTable.setStatus("current")
_LanVLANEntry_Object = MibTableRow
lanVLANEntry = _LanVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1)
)
lanVLANEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "lanVLANIndex"),
)
if mibBuilder.loadTexts:
    lanVLANEntry.setStatus("current")


class _LanVLANIndex_Type(Integer32):
    """Custom type lanVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_LanVLANIndex_Type.__name__ = "Integer32"
_LanVLANIndex_Object = MibTableColumn
lanVLANIndex = _LanVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 1),
    _LanVLANIndex_Type()
)
lanVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanVLANIndex.setStatus("current")


class _LanVLANPvid_Type(Integer32):
    """Custom type lanVLANPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_LanVLANPvid_Type.__name__ = "Integer32"
_LanVLANPvid_Object = MibTableColumn
lanVLANPvid = _LanVLANPvid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 2),
    _LanVLANPvid_Type()
)
lanVLANPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANPvid.setStatus("current")


class _LanVLANVlanTag0_Type(Integer32):
    """Custom type lanVLANVlanTag0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag0_Type.__name__ = "Integer32"
_LanVLANVlanTag0_Object = MibTableColumn
lanVLANVlanTag0 = _LanVLANVlanTag0_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 3),
    _LanVLANVlanTag0_Type()
)
lanVLANVlanTag0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag0.setStatus("current")


class _LanVLANVlanTag1_Type(Integer32):
    """Custom type lanVLANVlanTag1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag1_Type.__name__ = "Integer32"
_LanVLANVlanTag1_Object = MibTableColumn
lanVLANVlanTag1 = _LanVLANVlanTag1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 4),
    _LanVLANVlanTag1_Type()
)
lanVLANVlanTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag1.setStatus("current")


class _LanVLANVlanTag2_Type(Integer32):
    """Custom type lanVLANVlanTag2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag2_Type.__name__ = "Integer32"
_LanVLANVlanTag2_Object = MibTableColumn
lanVLANVlanTag2 = _LanVLANVlanTag2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 5),
    _LanVLANVlanTag2_Type()
)
lanVLANVlanTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag2.setStatus("current")


class _LanVLANVlanTag3_Type(Integer32):
    """Custom type lanVLANVlanTag3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag3_Type.__name__ = "Integer32"
_LanVLANVlanTag3_Object = MibTableColumn
lanVLANVlanTag3 = _LanVLANVlanTag3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 6),
    _LanVLANVlanTag3_Type()
)
lanVLANVlanTag3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag3.setStatus("current")


class _LanVLANVlanTag4_Type(Integer32):
    """Custom type lanVLANVlanTag4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag4_Type.__name__ = "Integer32"
_LanVLANVlanTag4_Object = MibTableColumn
lanVLANVlanTag4 = _LanVLANVlanTag4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 7),
    _LanVLANVlanTag4_Type()
)
lanVLANVlanTag4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag4.setStatus("current")


class _LanVLANVlanTag5_Type(Integer32):
    """Custom type lanVLANVlanTag5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag5_Type.__name__ = "Integer32"
_LanVLANVlanTag5_Object = MibTableColumn
lanVLANVlanTag5 = _LanVLANVlanTag5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 8),
    _LanVLANVlanTag5_Type()
)
lanVLANVlanTag5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag5.setStatus("current")


class _LanVLANVlanTag6_Type(Integer32):
    """Custom type lanVLANVlanTag6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag6_Type.__name__ = "Integer32"
_LanVLANVlanTag6_Object = MibTableColumn
lanVLANVlanTag6 = _LanVLANVlanTag6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 9),
    _LanVLANVlanTag6_Type()
)
lanVLANVlanTag6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag6.setStatus("current")


class _LanVLANVlanTag7_Type(Integer32):
    """Custom type lanVLANVlanTag7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag7_Type.__name__ = "Integer32"
_LanVLANVlanTag7_Object = MibTableColumn
lanVLANVlanTag7 = _LanVLANVlanTag7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 10),
    _LanVLANVlanTag7_Type()
)
lanVLANVlanTag7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag7.setStatus("current")


class _LanVLANVlanTag8_Type(Integer32):
    """Custom type lanVLANVlanTag8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag8_Type.__name__ = "Integer32"
_LanVLANVlanTag8_Object = MibTableColumn
lanVLANVlanTag8 = _LanVLANVlanTag8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 11),
    _LanVLANVlanTag8_Type()
)
lanVLANVlanTag8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag8.setStatus("current")


class _LanVLANVlanTag9_Type(Integer32):
    """Custom type lanVLANVlanTag9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag9_Type.__name__ = "Integer32"
_LanVLANVlanTag9_Object = MibTableColumn
lanVLANVlanTag9 = _LanVLANVlanTag9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 12),
    _LanVLANVlanTag9_Type()
)
lanVLANVlanTag9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag9.setStatus("current")


class _LanVLANVlanTag10_Type(Integer32):
    """Custom type lanVLANVlanTag10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag10_Type.__name__ = "Integer32"
_LanVLANVlanTag10_Object = MibTableColumn
lanVLANVlanTag10 = _LanVLANVlanTag10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 13),
    _LanVLANVlanTag10_Type()
)
lanVLANVlanTag10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag10.setStatus("current")


class _LanVLANVlanTag11_Type(Integer32):
    """Custom type lanVLANVlanTag11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag11_Type.__name__ = "Integer32"
_LanVLANVlanTag11_Object = MibTableColumn
lanVLANVlanTag11 = _LanVLANVlanTag11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 14),
    _LanVLANVlanTag11_Type()
)
lanVLANVlanTag11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag11.setStatus("current")


class _LanVLANVlanTag12_Type(Integer32):
    """Custom type lanVLANVlanTag12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag12_Type.__name__ = "Integer32"
_LanVLANVlanTag12_Object = MibTableColumn
lanVLANVlanTag12 = _LanVLANVlanTag12_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 15),
    _LanVLANVlanTag12_Type()
)
lanVLANVlanTag12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag12.setStatus("current")


class _LanVLANVlanTag13_Type(Integer32):
    """Custom type lanVLANVlanTag13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag13_Type.__name__ = "Integer32"
_LanVLANVlanTag13_Object = MibTableColumn
lanVLANVlanTag13 = _LanVLANVlanTag13_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 16),
    _LanVLANVlanTag13_Type()
)
lanVLANVlanTag13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag13.setStatus("current")


class _LanVLANVlanTag14_Type(Integer32):
    """Custom type lanVLANVlanTag14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag14_Type.__name__ = "Integer32"
_LanVLANVlanTag14_Object = MibTableColumn
lanVLANVlanTag14 = _LanVLANVlanTag14_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 17),
    _LanVLANVlanTag14_Type()
)
lanVLANVlanTag14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag14.setStatus("current")


class _LanVLANVlanTag15_Type(Integer32):
    """Custom type lanVLANVlanTag15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag15_Type.__name__ = "Integer32"
_LanVLANVlanTag15_Object = MibTableColumn
lanVLANVlanTag15 = _LanVLANVlanTag15_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 18),
    _LanVLANVlanTag15_Type()
)
lanVLANVlanTag15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag15.setStatus("current")


class _LanVLANVlanTag16_Type(Integer32):
    """Custom type lanVLANVlanTag16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag16_Type.__name__ = "Integer32"
_LanVLANVlanTag16_Object = MibTableColumn
lanVLANVlanTag16 = _LanVLANVlanTag16_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 19),
    _LanVLANVlanTag16_Type()
)
lanVLANVlanTag16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag16.setStatus("current")


class _LanVLANVlanTag17_Type(Integer32):
    """Custom type lanVLANVlanTag17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag17_Type.__name__ = "Integer32"
_LanVLANVlanTag17_Object = MibTableColumn
lanVLANVlanTag17 = _LanVLANVlanTag17_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 20),
    _LanVLANVlanTag17_Type()
)
lanVLANVlanTag17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag17.setStatus("current")


class _LanVLANVlanTag18_Type(Integer32):
    """Custom type lanVLANVlanTag18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag18_Type.__name__ = "Integer32"
_LanVLANVlanTag18_Object = MibTableColumn
lanVLANVlanTag18 = _LanVLANVlanTag18_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 21),
    _LanVLANVlanTag18_Type()
)
lanVLANVlanTag18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag18.setStatus("current")


class _LanVLANVlanTag19_Type(Integer32):
    """Custom type lanVLANVlanTag19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag19_Type.__name__ = "Integer32"
_LanVLANVlanTag19_Object = MibTableColumn
lanVLANVlanTag19 = _LanVLANVlanTag19_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 22),
    _LanVLANVlanTag19_Type()
)
lanVLANVlanTag19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag19.setStatus("current")


class _LanVLANVlanTag20_Type(Integer32):
    """Custom type lanVLANVlanTag20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag20_Type.__name__ = "Integer32"
_LanVLANVlanTag20_Object = MibTableColumn
lanVLANVlanTag20 = _LanVLANVlanTag20_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 23),
    _LanVLANVlanTag20_Type()
)
lanVLANVlanTag20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag20.setStatus("current")


class _LanVLANVlanTag21_Type(Integer32):
    """Custom type lanVLANVlanTag21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag21_Type.__name__ = "Integer32"
_LanVLANVlanTag21_Object = MibTableColumn
lanVLANVlanTag21 = _LanVLANVlanTag21_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 24),
    _LanVLANVlanTag21_Type()
)
lanVLANVlanTag21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag21.setStatus("current")


class _LanVLANVlanTag22_Type(Integer32):
    """Custom type lanVLANVlanTag22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag22_Type.__name__ = "Integer32"
_LanVLANVlanTag22_Object = MibTableColumn
lanVLANVlanTag22 = _LanVLANVlanTag22_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 25),
    _LanVLANVlanTag22_Type()
)
lanVLANVlanTag22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag22.setStatus("current")


class _LanVLANVlanTag23_Type(Integer32):
    """Custom type lanVLANVlanTag23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag23_Type.__name__ = "Integer32"
_LanVLANVlanTag23_Object = MibTableColumn
lanVLANVlanTag23 = _LanVLANVlanTag23_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 26),
    _LanVLANVlanTag23_Type()
)
lanVLANVlanTag23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag23.setStatus("current")


class _LanVLANVlanTag24_Type(Integer32):
    """Custom type lanVLANVlanTag24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag24_Type.__name__ = "Integer32"
_LanVLANVlanTag24_Object = MibTableColumn
lanVLANVlanTag24 = _LanVLANVlanTag24_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 27),
    _LanVLANVlanTag24_Type()
)
lanVLANVlanTag24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag24.setStatus("current")


class _LanVLANVlanTag25_Type(Integer32):
    """Custom type lanVLANVlanTag25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag25_Type.__name__ = "Integer32"
_LanVLANVlanTag25_Object = MibTableColumn
lanVLANVlanTag25 = _LanVLANVlanTag25_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 28),
    _LanVLANVlanTag25_Type()
)
lanVLANVlanTag25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag25.setStatus("current")


class _LanVLANVlanTag26_Type(Integer32):
    """Custom type lanVLANVlanTag26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag26_Type.__name__ = "Integer32"
_LanVLANVlanTag26_Object = MibTableColumn
lanVLANVlanTag26 = _LanVLANVlanTag26_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 29),
    _LanVLANVlanTag26_Type()
)
lanVLANVlanTag26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag26.setStatus("current")


class _LanVLANVlanTag27_Type(Integer32):
    """Custom type lanVLANVlanTag27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag27_Type.__name__ = "Integer32"
_LanVLANVlanTag27_Object = MibTableColumn
lanVLANVlanTag27 = _LanVLANVlanTag27_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 30),
    _LanVLANVlanTag27_Type()
)
lanVLANVlanTag27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag27.setStatus("current")


class _LanVLANVlanTag28_Type(Integer32):
    """Custom type lanVLANVlanTag28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag28_Type.__name__ = "Integer32"
_LanVLANVlanTag28_Object = MibTableColumn
lanVLANVlanTag28 = _LanVLANVlanTag28_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 31),
    _LanVLANVlanTag28_Type()
)
lanVLANVlanTag28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag28.setStatus("current")


class _LanVLANVlanTag29_Type(Integer32):
    """Custom type lanVLANVlanTag29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag29_Type.__name__ = "Integer32"
_LanVLANVlanTag29_Object = MibTableColumn
lanVLANVlanTag29 = _LanVLANVlanTag29_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 32),
    _LanVLANVlanTag29_Type()
)
lanVLANVlanTag29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag29.setStatus("current")


class _LanVLANVlanTag30_Type(Integer32):
    """Custom type lanVLANVlanTag30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag30_Type.__name__ = "Integer32"
_LanVLANVlanTag30_Object = MibTableColumn
lanVLANVlanTag30 = _LanVLANVlanTag30_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 33),
    _LanVLANVlanTag30_Type()
)
lanVLANVlanTag30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag30.setStatus("current")


class _LanVLANVlanTag31_Type(Integer32):
    """Custom type lanVLANVlanTag31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_LanVLANVlanTag31_Type.__name__ = "Integer32"
_LanVLANVlanTag31_Object = MibTableColumn
lanVLANVlanTag31 = _LanVLANVlanTag31_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 12, 1, 34),
    _LanVLANVlanTag31_Type()
)
lanVLANVlanTag31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanVLANVlanTag31.setStatus("current")
_WlanVLANTable_Object = MibTable
wlanVLANTable = _WlanVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13)
)
if mibBuilder.loadTexts:
    wlanVLANTable.setStatus("current")
_WlanVLANEntry_Object = MibTableRow
wlanVLANEntry = _WlanVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1)
)
wlanVLANEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "wlanVLANIndex"),
)
if mibBuilder.loadTexts:
    wlanVLANEntry.setStatus("current")


class _WlanVLANIndex_Type(Integer32):
    """Custom type wlanVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_WlanVLANIndex_Type.__name__ = "Integer32"
_WlanVLANIndex_Object = MibTableColumn
wlanVLANIndex = _WlanVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 1),
    _WlanVLANIndex_Type()
)
wlanVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanVLANIndex.setStatus("current")


class _WlanVLANPvid_Type(Integer32):
    """Custom type wlanVLANPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WlanVLANPvid_Type.__name__ = "Integer32"
_WlanVLANPvid_Object = MibTableColumn
wlanVLANPvid = _WlanVLANPvid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 2),
    _WlanVLANPvid_Type()
)
wlanVLANPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANPvid.setStatus("current")


class _WlanVLANVlanTag0_Type(Integer32):
    """Custom type wlanVLANVlanTag0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag0_Type.__name__ = "Integer32"
_WlanVLANVlanTag0_Object = MibTableColumn
wlanVLANVlanTag0 = _WlanVLANVlanTag0_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 3),
    _WlanVLANVlanTag0_Type()
)
wlanVLANVlanTag0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag0.setStatus("current")


class _WlanVLANVlanTag1_Type(Integer32):
    """Custom type wlanVLANVlanTag1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag1_Type.__name__ = "Integer32"
_WlanVLANVlanTag1_Object = MibTableColumn
wlanVLANVlanTag1 = _WlanVLANVlanTag1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 4),
    _WlanVLANVlanTag1_Type()
)
wlanVLANVlanTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag1.setStatus("current")


class _WlanVLANVlanTag2_Type(Integer32):
    """Custom type wlanVLANVlanTag2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag2_Type.__name__ = "Integer32"
_WlanVLANVlanTag2_Object = MibTableColumn
wlanVLANVlanTag2 = _WlanVLANVlanTag2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 5),
    _WlanVLANVlanTag2_Type()
)
wlanVLANVlanTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag2.setStatus("current")


class _WlanVLANVlanTag3_Type(Integer32):
    """Custom type wlanVLANVlanTag3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag3_Type.__name__ = "Integer32"
_WlanVLANVlanTag3_Object = MibTableColumn
wlanVLANVlanTag3 = _WlanVLANVlanTag3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 6),
    _WlanVLANVlanTag3_Type()
)
wlanVLANVlanTag3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag3.setStatus("current")


class _WlanVLANVlanTag4_Type(Integer32):
    """Custom type wlanVLANVlanTag4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag4_Type.__name__ = "Integer32"
_WlanVLANVlanTag4_Object = MibTableColumn
wlanVLANVlanTag4 = _WlanVLANVlanTag4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 7),
    _WlanVLANVlanTag4_Type()
)
wlanVLANVlanTag4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag4.setStatus("current")


class _WlanVLANVlanTag5_Type(Integer32):
    """Custom type wlanVLANVlanTag5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag5_Type.__name__ = "Integer32"
_WlanVLANVlanTag5_Object = MibTableColumn
wlanVLANVlanTag5 = _WlanVLANVlanTag5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 8),
    _WlanVLANVlanTag5_Type()
)
wlanVLANVlanTag5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag5.setStatus("current")


class _WlanVLANVlanTag6_Type(Integer32):
    """Custom type wlanVLANVlanTag6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag6_Type.__name__ = "Integer32"
_WlanVLANVlanTag6_Object = MibTableColumn
wlanVLANVlanTag6 = _WlanVLANVlanTag6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 9),
    _WlanVLANVlanTag6_Type()
)
wlanVLANVlanTag6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag6.setStatus("current")


class _WlanVLANVlanTag7_Type(Integer32):
    """Custom type wlanVLANVlanTag7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag7_Type.__name__ = "Integer32"
_WlanVLANVlanTag7_Object = MibTableColumn
wlanVLANVlanTag7 = _WlanVLANVlanTag7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 10),
    _WlanVLANVlanTag7_Type()
)
wlanVLANVlanTag7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag7.setStatus("current")


class _WlanVLANVlanTag8_Type(Integer32):
    """Custom type wlanVLANVlanTag8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag8_Type.__name__ = "Integer32"
_WlanVLANVlanTag8_Object = MibTableColumn
wlanVLANVlanTag8 = _WlanVLANVlanTag8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 11),
    _WlanVLANVlanTag8_Type()
)
wlanVLANVlanTag8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag8.setStatus("current")


class _WlanVLANVlanTag9_Type(Integer32):
    """Custom type wlanVLANVlanTag9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag9_Type.__name__ = "Integer32"
_WlanVLANVlanTag9_Object = MibTableColumn
wlanVLANVlanTag9 = _WlanVLANVlanTag9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 12),
    _WlanVLANVlanTag9_Type()
)
wlanVLANVlanTag9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag9.setStatus("current")


class _WlanVLANVlanTag10_Type(Integer32):
    """Custom type wlanVLANVlanTag10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag10_Type.__name__ = "Integer32"
_WlanVLANVlanTag10_Object = MibTableColumn
wlanVLANVlanTag10 = _WlanVLANVlanTag10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 13),
    _WlanVLANVlanTag10_Type()
)
wlanVLANVlanTag10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag10.setStatus("current")


class _WlanVLANVlanTag11_Type(Integer32):
    """Custom type wlanVLANVlanTag11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag11_Type.__name__ = "Integer32"
_WlanVLANVlanTag11_Object = MibTableColumn
wlanVLANVlanTag11 = _WlanVLANVlanTag11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 14),
    _WlanVLANVlanTag11_Type()
)
wlanVLANVlanTag11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag11.setStatus("current")


class _WlanVLANVlanTag12_Type(Integer32):
    """Custom type wlanVLANVlanTag12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag12_Type.__name__ = "Integer32"
_WlanVLANVlanTag12_Object = MibTableColumn
wlanVLANVlanTag12 = _WlanVLANVlanTag12_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 15),
    _WlanVLANVlanTag12_Type()
)
wlanVLANVlanTag12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag12.setStatus("current")


class _WlanVLANVlanTag13_Type(Integer32):
    """Custom type wlanVLANVlanTag13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag13_Type.__name__ = "Integer32"
_WlanVLANVlanTag13_Object = MibTableColumn
wlanVLANVlanTag13 = _WlanVLANVlanTag13_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 16),
    _WlanVLANVlanTag13_Type()
)
wlanVLANVlanTag13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag13.setStatus("current")


class _WlanVLANVlanTag14_Type(Integer32):
    """Custom type wlanVLANVlanTag14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag14_Type.__name__ = "Integer32"
_WlanVLANVlanTag14_Object = MibTableColumn
wlanVLANVlanTag14 = _WlanVLANVlanTag14_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 17),
    _WlanVLANVlanTag14_Type()
)
wlanVLANVlanTag14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag14.setStatus("current")


class _WlanVLANVlanTag15_Type(Integer32):
    """Custom type wlanVLANVlanTag15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag15_Type.__name__ = "Integer32"
_WlanVLANVlanTag15_Object = MibTableColumn
wlanVLANVlanTag15 = _WlanVLANVlanTag15_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 18),
    _WlanVLANVlanTag15_Type()
)
wlanVLANVlanTag15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag15.setStatus("current")


class _WlanVLANVlanTag16_Type(Integer32):
    """Custom type wlanVLANVlanTag16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag16_Type.__name__ = "Integer32"
_WlanVLANVlanTag16_Object = MibTableColumn
wlanVLANVlanTag16 = _WlanVLANVlanTag16_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 19),
    _WlanVLANVlanTag16_Type()
)
wlanVLANVlanTag16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag16.setStatus("current")


class _WlanVLANVlanTag17_Type(Integer32):
    """Custom type wlanVLANVlanTag17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag17_Type.__name__ = "Integer32"
_WlanVLANVlanTag17_Object = MibTableColumn
wlanVLANVlanTag17 = _WlanVLANVlanTag17_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 20),
    _WlanVLANVlanTag17_Type()
)
wlanVLANVlanTag17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag17.setStatus("current")


class _WlanVLANVlanTag18_Type(Integer32):
    """Custom type wlanVLANVlanTag18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag18_Type.__name__ = "Integer32"
_WlanVLANVlanTag18_Object = MibTableColumn
wlanVLANVlanTag18 = _WlanVLANVlanTag18_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 21),
    _WlanVLANVlanTag18_Type()
)
wlanVLANVlanTag18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag18.setStatus("current")


class _WlanVLANVlanTag19_Type(Integer32):
    """Custom type wlanVLANVlanTag19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag19_Type.__name__ = "Integer32"
_WlanVLANVlanTag19_Object = MibTableColumn
wlanVLANVlanTag19 = _WlanVLANVlanTag19_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 22),
    _WlanVLANVlanTag19_Type()
)
wlanVLANVlanTag19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag19.setStatus("current")


class _WlanVLANVlanTag20_Type(Integer32):
    """Custom type wlanVLANVlanTag20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag20_Type.__name__ = "Integer32"
_WlanVLANVlanTag20_Object = MibTableColumn
wlanVLANVlanTag20 = _WlanVLANVlanTag20_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 23),
    _WlanVLANVlanTag20_Type()
)
wlanVLANVlanTag20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag20.setStatus("current")


class _WlanVLANVlanTag21_Type(Integer32):
    """Custom type wlanVLANVlanTag21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag21_Type.__name__ = "Integer32"
_WlanVLANVlanTag21_Object = MibTableColumn
wlanVLANVlanTag21 = _WlanVLANVlanTag21_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 24),
    _WlanVLANVlanTag21_Type()
)
wlanVLANVlanTag21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag21.setStatus("current")


class _WlanVLANVlanTag22_Type(Integer32):
    """Custom type wlanVLANVlanTag22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag22_Type.__name__ = "Integer32"
_WlanVLANVlanTag22_Object = MibTableColumn
wlanVLANVlanTag22 = _WlanVLANVlanTag22_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 25),
    _WlanVLANVlanTag22_Type()
)
wlanVLANVlanTag22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag22.setStatus("current")


class _WlanVLANVlanTag23_Type(Integer32):
    """Custom type wlanVLANVlanTag23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag23_Type.__name__ = "Integer32"
_WlanVLANVlanTag23_Object = MibTableColumn
wlanVLANVlanTag23 = _WlanVLANVlanTag23_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 26),
    _WlanVLANVlanTag23_Type()
)
wlanVLANVlanTag23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag23.setStatus("current")


class _WlanVLANVlanTag24_Type(Integer32):
    """Custom type wlanVLANVlanTag24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag24_Type.__name__ = "Integer32"
_WlanVLANVlanTag24_Object = MibTableColumn
wlanVLANVlanTag24 = _WlanVLANVlanTag24_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 27),
    _WlanVLANVlanTag24_Type()
)
wlanVLANVlanTag24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag24.setStatus("current")


class _WlanVLANVlanTag25_Type(Integer32):
    """Custom type wlanVLANVlanTag25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag25_Type.__name__ = "Integer32"
_WlanVLANVlanTag25_Object = MibTableColumn
wlanVLANVlanTag25 = _WlanVLANVlanTag25_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 28),
    _WlanVLANVlanTag25_Type()
)
wlanVLANVlanTag25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag25.setStatus("current")


class _WlanVLANVlanTag26_Type(Integer32):
    """Custom type wlanVLANVlanTag26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag26_Type.__name__ = "Integer32"
_WlanVLANVlanTag26_Object = MibTableColumn
wlanVLANVlanTag26 = _WlanVLANVlanTag26_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 29),
    _WlanVLANVlanTag26_Type()
)
wlanVLANVlanTag26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag26.setStatus("current")


class _WlanVLANVlanTag27_Type(Integer32):
    """Custom type wlanVLANVlanTag27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag27_Type.__name__ = "Integer32"
_WlanVLANVlanTag27_Object = MibTableColumn
wlanVLANVlanTag27 = _WlanVLANVlanTag27_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 30),
    _WlanVLANVlanTag27_Type()
)
wlanVLANVlanTag27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag27.setStatus("current")


class _WlanVLANVlanTag28_Type(Integer32):
    """Custom type wlanVLANVlanTag28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag28_Type.__name__ = "Integer32"
_WlanVLANVlanTag28_Object = MibTableColumn
wlanVLANVlanTag28 = _WlanVLANVlanTag28_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 31),
    _WlanVLANVlanTag28_Type()
)
wlanVLANVlanTag28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag28.setStatus("current")


class _WlanVLANVlanTag29_Type(Integer32):
    """Custom type wlanVLANVlanTag29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag29_Type.__name__ = "Integer32"
_WlanVLANVlanTag29_Object = MibTableColumn
wlanVLANVlanTag29 = _WlanVLANVlanTag29_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 32),
    _WlanVLANVlanTag29_Type()
)
wlanVLANVlanTag29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag29.setStatus("current")


class _WlanVLANVlanTag30_Type(Integer32):
    """Custom type wlanVLANVlanTag30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag30_Type.__name__ = "Integer32"
_WlanVLANVlanTag30_Object = MibTableColumn
wlanVLANVlanTag30 = _WlanVLANVlanTag30_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 33),
    _WlanVLANVlanTag30_Type()
)
wlanVLANVlanTag30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag30.setStatus("current")


class _WlanVLANVlanTag31_Type(Integer32):
    """Custom type wlanVLANVlanTag31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WlanVLANVlanTag31_Type.__name__ = "Integer32"
_WlanVLANVlanTag31_Object = MibTableColumn
wlanVLANVlanTag31 = _WlanVLANVlanTag31_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 13, 1, 34),
    _WlanVLANVlanTag31_Type()
)
wlanVLANVlanTag31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanVLANVlanTag31.setStatus("current")
_WdsVLANTable_Object = MibTable
wdsVLANTable = _WdsVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14)
)
if mibBuilder.loadTexts:
    wdsVLANTable.setStatus("current")
_WdsVLANEntry_Object = MibTableRow
wdsVLANEntry = _WdsVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1)
)
wdsVLANEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "wdsVLANIndex"),
)
if mibBuilder.loadTexts:
    wdsVLANEntry.setStatus("current")


class _WdsVLANIndex_Type(Integer32):
    """Custom type wdsVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WdsVLANIndex_Type.__name__ = "Integer32"
_WdsVLANIndex_Object = MibTableColumn
wdsVLANIndex = _WdsVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 1),
    _WdsVLANIndex_Type()
)
wdsVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdsVLANIndex.setStatus("current")


class _WdsVLANPvid_Type(Integer32):
    """Custom type wdsVLANPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WdsVLANPvid_Type.__name__ = "Integer32"
_WdsVLANPvid_Object = MibTableColumn
wdsVLANPvid = _WdsVLANPvid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 2),
    _WdsVLANPvid_Type()
)
wdsVLANPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANPvid.setStatus("current")


class _WdsVLANVlanTag0_Type(Integer32):
    """Custom type wdsVLANVlanTag0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag0_Type.__name__ = "Integer32"
_WdsVLANVlanTag0_Object = MibTableColumn
wdsVLANVlanTag0 = _WdsVLANVlanTag0_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 3),
    _WdsVLANVlanTag0_Type()
)
wdsVLANVlanTag0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag0.setStatus("current")


class _WdsVLANVlanTag1_Type(Integer32):
    """Custom type wdsVLANVlanTag1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag1_Type.__name__ = "Integer32"
_WdsVLANVlanTag1_Object = MibTableColumn
wdsVLANVlanTag1 = _WdsVLANVlanTag1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 4),
    _WdsVLANVlanTag1_Type()
)
wdsVLANVlanTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag1.setStatus("current")


class _WdsVLANVlanTag2_Type(Integer32):
    """Custom type wdsVLANVlanTag2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag2_Type.__name__ = "Integer32"
_WdsVLANVlanTag2_Object = MibTableColumn
wdsVLANVlanTag2 = _WdsVLANVlanTag2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 5),
    _WdsVLANVlanTag2_Type()
)
wdsVLANVlanTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag2.setStatus("current")


class _WdsVLANVlanTag3_Type(Integer32):
    """Custom type wdsVLANVlanTag3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag3_Type.__name__ = "Integer32"
_WdsVLANVlanTag3_Object = MibTableColumn
wdsVLANVlanTag3 = _WdsVLANVlanTag3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 6),
    _WdsVLANVlanTag3_Type()
)
wdsVLANVlanTag3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag3.setStatus("current")


class _WdsVLANVlanTag4_Type(Integer32):
    """Custom type wdsVLANVlanTag4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag4_Type.__name__ = "Integer32"
_WdsVLANVlanTag4_Object = MibTableColumn
wdsVLANVlanTag4 = _WdsVLANVlanTag4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 7),
    _WdsVLANVlanTag4_Type()
)
wdsVLANVlanTag4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag4.setStatus("current")


class _WdsVLANVlanTag5_Type(Integer32):
    """Custom type wdsVLANVlanTag5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag5_Type.__name__ = "Integer32"
_WdsVLANVlanTag5_Object = MibTableColumn
wdsVLANVlanTag5 = _WdsVLANVlanTag5_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 8),
    _WdsVLANVlanTag5_Type()
)
wdsVLANVlanTag5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag5.setStatus("current")


class _WdsVLANVlanTag6_Type(Integer32):
    """Custom type wdsVLANVlanTag6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag6_Type.__name__ = "Integer32"
_WdsVLANVlanTag6_Object = MibTableColumn
wdsVLANVlanTag6 = _WdsVLANVlanTag6_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 9),
    _WdsVLANVlanTag6_Type()
)
wdsVLANVlanTag6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag6.setStatus("current")


class _WdsVLANVlanTag7_Type(Integer32):
    """Custom type wdsVLANVlanTag7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag7_Type.__name__ = "Integer32"
_WdsVLANVlanTag7_Object = MibTableColumn
wdsVLANVlanTag7 = _WdsVLANVlanTag7_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 10),
    _WdsVLANVlanTag7_Type()
)
wdsVLANVlanTag7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag7.setStatus("current")


class _WdsVLANVlanTag8_Type(Integer32):
    """Custom type wdsVLANVlanTag8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag8_Type.__name__ = "Integer32"
_WdsVLANVlanTag8_Object = MibTableColumn
wdsVLANVlanTag8 = _WdsVLANVlanTag8_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 11),
    _WdsVLANVlanTag8_Type()
)
wdsVLANVlanTag8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag8.setStatus("current")


class _WdsVLANVlanTag9_Type(Integer32):
    """Custom type wdsVLANVlanTag9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag9_Type.__name__ = "Integer32"
_WdsVLANVlanTag9_Object = MibTableColumn
wdsVLANVlanTag9 = _WdsVLANVlanTag9_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 12),
    _WdsVLANVlanTag9_Type()
)
wdsVLANVlanTag9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag9.setStatus("current")


class _WdsVLANVlanTag10_Type(Integer32):
    """Custom type wdsVLANVlanTag10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag10_Type.__name__ = "Integer32"
_WdsVLANVlanTag10_Object = MibTableColumn
wdsVLANVlanTag10 = _WdsVLANVlanTag10_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 13),
    _WdsVLANVlanTag10_Type()
)
wdsVLANVlanTag10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag10.setStatus("current")


class _WdsVLANVlanTag11_Type(Integer32):
    """Custom type wdsVLANVlanTag11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag11_Type.__name__ = "Integer32"
_WdsVLANVlanTag11_Object = MibTableColumn
wdsVLANVlanTag11 = _WdsVLANVlanTag11_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 14),
    _WdsVLANVlanTag11_Type()
)
wdsVLANVlanTag11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag11.setStatus("current")


class _WdsVLANVlanTag12_Type(Integer32):
    """Custom type wdsVLANVlanTag12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag12_Type.__name__ = "Integer32"
_WdsVLANVlanTag12_Object = MibTableColumn
wdsVLANVlanTag12 = _WdsVLANVlanTag12_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 15),
    _WdsVLANVlanTag12_Type()
)
wdsVLANVlanTag12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag12.setStatus("current")


class _WdsVLANVlanTag13_Type(Integer32):
    """Custom type wdsVLANVlanTag13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag13_Type.__name__ = "Integer32"
_WdsVLANVlanTag13_Object = MibTableColumn
wdsVLANVlanTag13 = _WdsVLANVlanTag13_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 16),
    _WdsVLANVlanTag13_Type()
)
wdsVLANVlanTag13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag13.setStatus("current")


class _WdsVLANVlanTag14_Type(Integer32):
    """Custom type wdsVLANVlanTag14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag14_Type.__name__ = "Integer32"
_WdsVLANVlanTag14_Object = MibTableColumn
wdsVLANVlanTag14 = _WdsVLANVlanTag14_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 17),
    _WdsVLANVlanTag14_Type()
)
wdsVLANVlanTag14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag14.setStatus("current")


class _WdsVLANVlanTag15_Type(Integer32):
    """Custom type wdsVLANVlanTag15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag15_Type.__name__ = "Integer32"
_WdsVLANVlanTag15_Object = MibTableColumn
wdsVLANVlanTag15 = _WdsVLANVlanTag15_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 18),
    _WdsVLANVlanTag15_Type()
)
wdsVLANVlanTag15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag15.setStatus("current")


class _WdsVLANVlanTag16_Type(Integer32):
    """Custom type wdsVLANVlanTag16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag16_Type.__name__ = "Integer32"
_WdsVLANVlanTag16_Object = MibTableColumn
wdsVLANVlanTag16 = _WdsVLANVlanTag16_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 19),
    _WdsVLANVlanTag16_Type()
)
wdsVLANVlanTag16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag16.setStatus("current")


class _WdsVLANVlanTag17_Type(Integer32):
    """Custom type wdsVLANVlanTag17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag17_Type.__name__ = "Integer32"
_WdsVLANVlanTag17_Object = MibTableColumn
wdsVLANVlanTag17 = _WdsVLANVlanTag17_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 20),
    _WdsVLANVlanTag17_Type()
)
wdsVLANVlanTag17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag17.setStatus("current")


class _WdsVLANVlanTag18_Type(Integer32):
    """Custom type wdsVLANVlanTag18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag18_Type.__name__ = "Integer32"
_WdsVLANVlanTag18_Object = MibTableColumn
wdsVLANVlanTag18 = _WdsVLANVlanTag18_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 21),
    _WdsVLANVlanTag18_Type()
)
wdsVLANVlanTag18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag18.setStatus("current")


class _WdsVLANVlanTag19_Type(Integer32):
    """Custom type wdsVLANVlanTag19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag19_Type.__name__ = "Integer32"
_WdsVLANVlanTag19_Object = MibTableColumn
wdsVLANVlanTag19 = _WdsVLANVlanTag19_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 22),
    _WdsVLANVlanTag19_Type()
)
wdsVLANVlanTag19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag19.setStatus("current")


class _WdsVLANVlanTag20_Type(Integer32):
    """Custom type wdsVLANVlanTag20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag20_Type.__name__ = "Integer32"
_WdsVLANVlanTag20_Object = MibTableColumn
wdsVLANVlanTag20 = _WdsVLANVlanTag20_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 23),
    _WdsVLANVlanTag20_Type()
)
wdsVLANVlanTag20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag20.setStatus("current")


class _WdsVLANVlanTag21_Type(Integer32):
    """Custom type wdsVLANVlanTag21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag21_Type.__name__ = "Integer32"
_WdsVLANVlanTag21_Object = MibTableColumn
wdsVLANVlanTag21 = _WdsVLANVlanTag21_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 24),
    _WdsVLANVlanTag21_Type()
)
wdsVLANVlanTag21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag21.setStatus("current")


class _WdsVLANVlanTag22_Type(Integer32):
    """Custom type wdsVLANVlanTag22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag22_Type.__name__ = "Integer32"
_WdsVLANVlanTag22_Object = MibTableColumn
wdsVLANVlanTag22 = _WdsVLANVlanTag22_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 25),
    _WdsVLANVlanTag22_Type()
)
wdsVLANVlanTag22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag22.setStatus("current")


class _WdsVLANVlanTag23_Type(Integer32):
    """Custom type wdsVLANVlanTag23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag23_Type.__name__ = "Integer32"
_WdsVLANVlanTag23_Object = MibTableColumn
wdsVLANVlanTag23 = _WdsVLANVlanTag23_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 26),
    _WdsVLANVlanTag23_Type()
)
wdsVLANVlanTag23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag23.setStatus("current")


class _WdsVLANVlanTag24_Type(Integer32):
    """Custom type wdsVLANVlanTag24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag24_Type.__name__ = "Integer32"
_WdsVLANVlanTag24_Object = MibTableColumn
wdsVLANVlanTag24 = _WdsVLANVlanTag24_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 27),
    _WdsVLANVlanTag24_Type()
)
wdsVLANVlanTag24.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag24.setStatus("current")


class _WdsVLANVlanTag25_Type(Integer32):
    """Custom type wdsVLANVlanTag25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag25_Type.__name__ = "Integer32"
_WdsVLANVlanTag25_Object = MibTableColumn
wdsVLANVlanTag25 = _WdsVLANVlanTag25_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 28),
    _WdsVLANVlanTag25_Type()
)
wdsVLANVlanTag25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag25.setStatus("current")


class _WdsVLANVlanTag26_Type(Integer32):
    """Custom type wdsVLANVlanTag26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag26_Type.__name__ = "Integer32"
_WdsVLANVlanTag26_Object = MibTableColumn
wdsVLANVlanTag26 = _WdsVLANVlanTag26_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 29),
    _WdsVLANVlanTag26_Type()
)
wdsVLANVlanTag26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag26.setStatus("current")


class _WdsVLANVlanTag27_Type(Integer32):
    """Custom type wdsVLANVlanTag27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag27_Type.__name__ = "Integer32"
_WdsVLANVlanTag27_Object = MibTableColumn
wdsVLANVlanTag27 = _WdsVLANVlanTag27_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 30),
    _WdsVLANVlanTag27_Type()
)
wdsVLANVlanTag27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag27.setStatus("current")


class _WdsVLANVlanTag28_Type(Integer32):
    """Custom type wdsVLANVlanTag28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag28_Type.__name__ = "Integer32"
_WdsVLANVlanTag28_Object = MibTableColumn
wdsVLANVlanTag28 = _WdsVLANVlanTag28_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 31),
    _WdsVLANVlanTag28_Type()
)
wdsVLANVlanTag28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag28.setStatus("current")


class _WdsVLANVlanTag29_Type(Integer32):
    """Custom type wdsVLANVlanTag29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag29_Type.__name__ = "Integer32"
_WdsVLANVlanTag29_Object = MibTableColumn
wdsVLANVlanTag29 = _WdsVLANVlanTag29_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 32),
    _WdsVLANVlanTag29_Type()
)
wdsVLANVlanTag29.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag29.setStatus("current")


class _WdsVLANVlanTag30_Type(Integer32):
    """Custom type wdsVLANVlanTag30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag30_Type.__name__ = "Integer32"
_WdsVLANVlanTag30_Object = MibTableColumn
wdsVLANVlanTag30 = _WdsVLANVlanTag30_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 33),
    _WdsVLANVlanTag30_Type()
)
wdsVLANVlanTag30.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag30.setStatus("current")


class _WdsVLANVlanTag31_Type(Integer32):
    """Custom type wdsVLANVlanTag31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WdsVLANVlanTag31_Type.__name__ = "Integer32"
_WdsVLANVlanTag31_Object = MibTableColumn
wdsVLANVlanTag31 = _WdsVLANVlanTag31_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 14, 1, 34),
    _WdsVLANVlanTag31_Type()
)
wdsVLANVlanTag31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdsVLANVlanTag31.setStatus("current")
_LinkFaultPassThrough_ObjectIdentity = ObjectIdentity
linkFaultPassThrough = _LinkFaultPassThrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 15)
)


class _LinkFaultPassThroughEnable_Type(Integer32):
    """Custom type linkFaultPassThroughEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LinkFaultPassThroughEnable_Type.__name__ = "Integer32"
_LinkFaultPassThroughEnable_Object = MibScalar
linkFaultPassThroughEnable = _LinkFaultPassThroughEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 15, 1),
    _LinkFaultPassThroughEnable_Type()
)
linkFaultPassThroughEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkFaultPassThroughEnable.setStatus("current")
_AeroMag_ObjectIdentity = ObjectIdentity
aeroMag = _AeroMag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 16)
)


class _AeroMagEnable_Type(Integer32):
    """Custom type aeroMagEnable based on Integer32"""
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
        *(("disable", 1),
          ("ap", 2),
          ("client", 3),
          ("clientRouter", 4))
    )


_AeroMagEnable_Type.__name__ = "Integer32"
_AeroMagEnable_Object = MibScalar
aeroMagEnable = _AeroMagEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 16, 2),
    _AeroMagEnable_Type()
)
aeroMagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroMagEnable.setStatus("current")


class _AeroMagReset_Type(Integer32):
    """Custom type aeroMagReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AeroMagReset_Type.__name__ = "Integer32"
_AeroMagReset_Object = MibScalar
aeroMagReset = _AeroMagReset_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 16, 3),
    _AeroMagReset_Type()
)
aeroMagReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeroMagReset.setStatus("current")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("current")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17, 1)
)
staticRouteEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "staticRouteIndex"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("current")


class _StaticRouteIndex_Type(Integer32):
    """Custom type staticRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_StaticRouteIndex_Type.__name__ = "Integer32"
_StaticRouteIndex_Object = MibTableColumn
staticRouteIndex = _StaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17, 1, 1),
    _StaticRouteIndex_Type()
)
staticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRouteIndex.setStatus("current")


class _StaticRouteStaticRouteEnable_Type(Integer32):
    """Custom type staticRouteStaticRouteEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_StaticRouteStaticRouteEnable_Type.__name__ = "Integer32"
_StaticRouteStaticRouteEnable_Object = MibTableColumn
staticRouteStaticRouteEnable = _StaticRouteStaticRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17, 1, 2),
    _StaticRouteStaticRouteEnable_Type()
)
staticRouteStaticRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteStaticRouteEnable.setStatus("current")


class _StaticRouteStaticRouteInterface_Type(Integer32):
    """Custom type staticRouteStaticRouteInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wlan", 1),
          ("lan", 2))
    )


_StaticRouteStaticRouteInterface_Type.__name__ = "Integer32"
_StaticRouteStaticRouteInterface_Object = MibTableColumn
staticRouteStaticRouteInterface = _StaticRouteStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17, 1, 3),
    _StaticRouteStaticRouteInterface_Type()
)
staticRouteStaticRouteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteStaticRouteInterface.setStatus("current")
_StaticRouteStaticRouteDst_Type = IpAddress
_StaticRouteStaticRouteDst_Object = MibTableColumn
staticRouteStaticRouteDst = _StaticRouteStaticRouteDst_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17, 1, 4),
    _StaticRouteStaticRouteDst_Type()
)
staticRouteStaticRouteDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteStaticRouteDst.setStatus("current")
_StaticRouteStaticRouteNetmask_Type = IpAddress
_StaticRouteStaticRouteNetmask_Object = MibTableColumn
staticRouteStaticRouteNetmask = _StaticRouteStaticRouteNetmask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17, 1, 5),
    _StaticRouteStaticRouteNetmask_Type()
)
staticRouteStaticRouteNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteStaticRouteNetmask.setStatus("current")
_StaticRouteStaticRouteGateway_Type = IpAddress
_StaticRouteStaticRouteGateway_Object = MibTableColumn
staticRouteStaticRouteGateway = _StaticRouteStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17, 1, 6),
    _StaticRouteStaticRouteGateway_Type()
)
staticRouteStaticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteStaticRouteGateway.setStatus("current")


class _StaticRouteStaticRouteMetric_Type(Integer32):
    """Custom type staticRouteStaticRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_StaticRouteStaticRouteMetric_Type.__name__ = "Integer32"
_StaticRouteStaticRouteMetric_Object = MibTableColumn
staticRouteStaticRouteMetric = _StaticRouteStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 17, 1, 7),
    _StaticRouteStaticRouteMetric_Type()
)
staticRouteStaticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteStaticRouteMetric.setStatus("current")
_Nat_ObjectIdentity = ObjectIdentity
nat = _Nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 18)
)


class _NatNatMode_Type(Integer32):
    """Custom type natNatMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nto1", 1),
          ("disable", 2),
          ("oneToOne", 3))
    )


_NatNatMode_Type.__name__ = "Integer32"
_NatNatMode_Object = MibScalar
natNatMode = _NatNatMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 18, 1),
    _NatNatMode_Type()
)
natNatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natNatMode.setStatus("current")
_PortForwardingTable_Object = MibTable
portForwardingTable = _PortForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 19)
)
if mibBuilder.loadTexts:
    portForwardingTable.setStatus("current")
_PortForwardingEntry_Object = MibTableRow
portForwardingEntry = _PortForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 19, 1)
)
portForwardingEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "portForwardingIndex"),
)
if mibBuilder.loadTexts:
    portForwardingEntry.setStatus("current")


class _PortForwardingIndex_Type(Integer32):
    """Custom type portForwardingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PortForwardingIndex_Type.__name__ = "Integer32"
_PortForwardingIndex_Object = MibTableColumn
portForwardingIndex = _PortForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 19, 1, 1),
    _PortForwardingIndex_Type()
)
portForwardingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portForwardingIndex.setStatus("current")


class _PortForwardingPortForwardingEnable_Type(Integer32):
    """Custom type portForwardingPortForwardingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PortForwardingPortForwardingEnable_Type.__name__ = "Integer32"
_PortForwardingPortForwardingEnable_Object = MibTableColumn
portForwardingPortForwardingEnable = _PortForwardingPortForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 19, 1, 2),
    _PortForwardingPortForwardingEnable_Type()
)
portForwardingPortForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingPortForwardingEnable.setStatus("current")


class _PortForwardingPortForwardingProtocol_Type(Integer32):
    """Custom type portForwardingPortForwardingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_PortForwardingPortForwardingProtocol_Type.__name__ = "Integer32"
_PortForwardingPortForwardingProtocol_Object = MibTableColumn
portForwardingPortForwardingProtocol = _PortForwardingPortForwardingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 19, 1, 3),
    _PortForwardingPortForwardingProtocol_Type()
)
portForwardingPortForwardingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingPortForwardingProtocol.setStatus("current")


class _PortForwardingPortForwardingWANPort_Type(Integer32):
    """Custom type portForwardingPortForwardingWANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortForwardingPortForwardingWANPort_Type.__name__ = "Integer32"
_PortForwardingPortForwardingWANPort_Object = MibTableColumn
portForwardingPortForwardingWANPort = _PortForwardingPortForwardingWANPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 19, 1, 4),
    _PortForwardingPortForwardingWANPort_Type()
)
portForwardingPortForwardingWANPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingPortForwardingWANPort.setStatus("current")
_PortForwardingPortForwardingLANIP_Type = IpAddress
_PortForwardingPortForwardingLANIP_Object = MibTableColumn
portForwardingPortForwardingLANIP = _PortForwardingPortForwardingLANIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 19, 1, 5),
    _PortForwardingPortForwardingLANIP_Type()
)
portForwardingPortForwardingLANIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingPortForwardingLANIP.setStatus("current")


class _PortForwardingPortForwardingLANPort_Type(Integer32):
    """Custom type portForwardingPortForwardingLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortForwardingPortForwardingLANPort_Type.__name__ = "Integer32"
_PortForwardingPortForwardingLANPort_Object = MibTableColumn
portForwardingPortForwardingLANPort = _PortForwardingPortForwardingLANPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 19, 1, 6),
    _PortForwardingPortForwardingLANPort_Type()
)
portForwardingPortForwardingLANPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingPortForwardingLANPort.setStatus("current")
_PortForwardingservice_ObjectIdentity = ObjectIdentity
portForwardingservice = _PortForwardingservice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 20)
)


class _PortForwardingservicePortForwardingserviceEnable_Type(Integer32):
    """Custom type portForwardingservicePortForwardingserviceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PortForwardingservicePortForwardingserviceEnable_Type.__name__ = "Integer32"
_PortForwardingservicePortForwardingserviceEnable_Object = MibScalar
portForwardingservicePortForwardingserviceEnable = _PortForwardingservicePortForwardingserviceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 20, 2),
    _PortForwardingservicePortForwardingserviceEnable_Type()
)
portForwardingservicePortForwardingserviceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForwardingservicePortForwardingserviceEnable.setStatus("current")
_AeroMagAction_ObjectIdentity = ObjectIdentity
aeroMagAction = _AeroMagAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 23)
)
_RefreshChannel_Type = Integer32
_RefreshChannel_Object = MibScalar
refreshChannel = _RefreshChannel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 23, 1),
    _RefreshChannel_Type()
)
refreshChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refreshChannel.setStatus("current")
_OneToOneNatEntryTable_Object = MibTable
oneToOneNatEntryTable = _OneToOneNatEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 61)
)
if mibBuilder.loadTexts:
    oneToOneNatEntryTable.setStatus("current")
_OneToOneNatEntryEntry_Object = MibTableRow
oneToOneNatEntryEntry = _OneToOneNatEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 61, 1)
)
oneToOneNatEntryEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "oneToOneNatEntryIndex"),
)
if mibBuilder.loadTexts:
    oneToOneNatEntryEntry.setStatus("current")


class _OneToOneNatEntryIndex_Type(Integer32):
    """Custom type oneToOneNatEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OneToOneNatEntryIndex_Type.__name__ = "Integer32"
_OneToOneNatEntryIndex_Object = MibTableColumn
oneToOneNatEntryIndex = _OneToOneNatEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 61, 1, 1),
    _OneToOneNatEntryIndex_Type()
)
oneToOneNatEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oneToOneNatEntryIndex.setStatus("current")


class _OneToOneNatEntryEnable_Type(Integer32):
    """Custom type oneToOneNatEntryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_OneToOneNatEntryEnable_Type.__name__ = "Integer32"
_OneToOneNatEntryEnable_Object = MibTableColumn
oneToOneNatEntryEnable = _OneToOneNatEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 61, 1, 2),
    _OneToOneNatEntryEnable_Type()
)
oneToOneNatEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oneToOneNatEntryEnable.setStatus("current")
_OneToOneNatEntryLanIP_Type = IpAddress
_OneToOneNatEntryLanIP_Object = MibTableColumn
oneToOneNatEntryLanIP = _OneToOneNatEntryLanIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 61, 1, 3),
    _OneToOneNatEntryLanIP_Type()
)
oneToOneNatEntryLanIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oneToOneNatEntryLanIP.setStatus("current")
_OneToOneNatEntryWanIP_Type = IpAddress
_OneToOneNatEntryWanIP_Object = MibTableColumn
oneToOneNatEntryWanIP = _OneToOneNatEntryWanIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 61, 1, 4),
    _OneToOneNatEntryWanIP_Type()
)
oneToOneNatEntryWanIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oneToOneNatEntryWanIP.setStatus("current")
_HTTPSetting_ObjectIdentity = ObjectIdentity
hTTPSetting = _HTTPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 62)
)


class _HTTPSettingHTTPPort_Type(Integer32):
    """Custom type hTTPSettingHTTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HTTPSettingHTTPPort_Type.__name__ = "Integer32"
_HTTPSettingHTTPPort_Object = MibScalar
hTTPSettingHTTPPort = _HTTPSettingHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 62, 1),
    _HTTPSettingHTTPPort_Type()
)
hTTPSettingHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPSettingHTTPPort.setStatus("current")


class _HTTPSettingHTTPSPort_Type(Integer32):
    """Custom type hTTPSettingHTTPSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HTTPSettingHTTPSPort_Type.__name__ = "Integer32"
_HTTPSettingHTTPSPort_Object = MibScalar
hTTPSettingHTTPSPort = _HTTPSettingHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 7, 62, 2),
    _HTTPSettingHTTPSPort_Type()
)
hTTPSettingHTTPSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hTTPSettingHTTPSPort.setStatus("current")
_AutoWarning_ObjectIdentity = ObjectIdentity
autoWarning = _AutoWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9)
)
_EmailAction_ObjectIdentity = ObjectIdentity
emailAction = _EmailAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1)
)


class _EmailActionColdStart_Type(Integer32):
    """Custom type emailActionColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionColdStart_Type.__name__ = "Integer32"
_EmailActionColdStart_Object = MibScalar
emailActionColdStart = _EmailActionColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 1),
    _EmailActionColdStart_Type()
)
emailActionColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionColdStart.setStatus("current")


class _EmailActionWarmStart_Type(Integer32):
    """Custom type emailActionWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWarmStart_Type.__name__ = "Integer32"
_EmailActionWarmStart_Object = MibScalar
emailActionWarmStart = _EmailActionWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 2),
    _EmailActionWarmStart_Type()
)
emailActionWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWarmStart.setStatus("current")


class _EmailActionPower1Off_Type(Integer32):
    """Custom type emailActionPower1Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionPower1Off_Type.__name__ = "Integer32"
_EmailActionPower1Off_Object = MibScalar
emailActionPower1Off = _EmailActionPower1Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 3),
    _EmailActionPower1Off_Type()
)
emailActionPower1Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionPower1Off.setStatus("current")


class _EmailActionPower1On_Type(Integer32):
    """Custom type emailActionPower1On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionPower1On_Type.__name__ = "Integer32"
_EmailActionPower1On_Object = MibScalar
emailActionPower1On = _EmailActionPower1On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 4),
    _EmailActionPower1On_Type()
)
emailActionPower1On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionPower1On.setStatus("current")


class _EmailActionPower2Off_Type(Integer32):
    """Custom type emailActionPower2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionPower2Off_Type.__name__ = "Integer32"
_EmailActionPower2Off_Object = MibScalar
emailActionPower2Off = _EmailActionPower2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 5),
    _EmailActionPower2Off_Type()
)
emailActionPower2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionPower2Off.setStatus("current")


class _EmailActionPower2On_Type(Integer32):
    """Custom type emailActionPower2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionPower2On_Type.__name__ = "Integer32"
_EmailActionPower2On_Object = MibScalar
emailActionPower2On = _EmailActionPower2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 6),
    _EmailActionPower2On_Type()
)
emailActionPower2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionPower2On.setStatus("current")


class _EmailActionPoeOff_Type(Integer32):
    """Custom type emailActionPoeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionPoeOff_Type.__name__ = "Integer32"
_EmailActionPoeOff_Object = MibScalar
emailActionPoeOff = _EmailActionPoeOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 7),
    _EmailActionPoeOff_Type()
)
emailActionPoeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionPoeOff.setStatus("current")


class _EmailActionPoeOn_Type(Integer32):
    """Custom type emailActionPoeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionPoeOn_Type.__name__ = "Integer32"
_EmailActionPoeOn_Object = MibScalar
emailActionPoeOn = _EmailActionPoeOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 8),
    _EmailActionPoeOn_Type()
)
emailActionPoeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionPoeOn.setStatus("current")


class _EmailActionDi1On2Off_Type(Integer32):
    """Custom type emailActionDi1On2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionDi1On2Off_Type.__name__ = "Integer32"
_EmailActionDi1On2Off_Object = MibScalar
emailActionDi1On2Off = _EmailActionDi1On2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 9),
    _EmailActionDi1On2Off_Type()
)
emailActionDi1On2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionDi1On2Off.setStatus("current")


class _EmailActionDi1Off2On_Type(Integer32):
    """Custom type emailActionDi1Off2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionDi1Off2On_Type.__name__ = "Integer32"
_EmailActionDi1Off2On_Object = MibScalar
emailActionDi1Off2On = _EmailActionDi1Off2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 10),
    _EmailActionDi1Off2On_Type()
)
emailActionDi1Off2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionDi1Off2On.setStatus("current")


class _EmailActionDi2On2Off_Type(Integer32):
    """Custom type emailActionDi2On2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionDi2On2Off_Type.__name__ = "Integer32"
_EmailActionDi2On2Off_Object = MibScalar
emailActionDi2On2Off = _EmailActionDi2On2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 11),
    _EmailActionDi2On2Off_Type()
)
emailActionDi2On2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionDi2On2Off.setStatus("current")


class _EmailActionDi2Off2On_Type(Integer32):
    """Custom type emailActionDi2Off2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionDi2Off2On_Type.__name__ = "Integer32"
_EmailActionDi2Off2On_Object = MibScalar
emailActionDi2Off2On = _EmailActionDi2Off2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 12),
    _EmailActionDi2Off2On_Type()
)
emailActionDi2Off2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionDi2Off2On.setStatus("current")


class _EmailActionConfigChange_Type(Integer32):
    """Custom type emailActionConfigChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionConfigChange_Type.__name__ = "Integer32"
_EmailActionConfigChange_Object = MibScalar
emailActionConfigChange = _EmailActionConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 13),
    _EmailActionConfigChange_Type()
)
emailActionConfigChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionConfigChange.setStatus("current")


class _EmailActionConsoleAuthFail_Type(Integer32):
    """Custom type emailActionConsoleAuthFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionConsoleAuthFail_Type.__name__ = "Integer32"
_EmailActionConsoleAuthFail_Object = MibScalar
emailActionConsoleAuthFail = _EmailActionConsoleAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 14),
    _EmailActionConsoleAuthFail_Type()
)
emailActionConsoleAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionConsoleAuthFail.setStatus("current")


class _EmailActionLanLinkOn_Type(Integer32):
    """Custom type emailActionLanLinkOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionLanLinkOn_Type.__name__ = "Integer32"
_EmailActionLanLinkOn_Object = MibScalar
emailActionLanLinkOn = _EmailActionLanLinkOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 18),
    _EmailActionLanLinkOn_Type()
)
emailActionLanLinkOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionLanLinkOn.setStatus("current")


class _EmailActionLanLinkOff_Type(Integer32):
    """Custom type emailActionLanLinkOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionLanLinkOff_Type.__name__ = "Integer32"
_EmailActionLanLinkOff_Object = MibScalar
emailActionLanLinkOff = _EmailActionLanLinkOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 19),
    _EmailActionLanLinkOff_Type()
)
emailActionLanLinkOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionLanLinkOff.setStatus("current")


class _EmailActionWlan1Connect_Type(Integer32):
    """Custom type emailActionWlan1Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1Connect_Type.__name__ = "Integer32"
_EmailActionWlan1Connect_Object = MibScalar
emailActionWlan1Connect = _EmailActionWlan1Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 40),
    _EmailActionWlan1Connect_Type()
)
emailActionWlan1Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1Connect.setStatus("current")


class _EmailActionWlan1Disconnect_Type(Integer32):
    """Custom type emailActionWlan1Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1Disconnect_Object = MibScalar
emailActionWlan1Disconnect = _EmailActionWlan1Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 41),
    _EmailActionWlan1Disconnect_Type()
)
emailActionWlan1Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1Disconnect.setStatus("current")


class _EmailActionWlan1_1Connect_Type(Integer32):
    """Custom type emailActionWlan1_1Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_1Connect_Type.__name__ = "Integer32"
_EmailActionWlan1_1Connect_Object = MibScalar
emailActionWlan1_1Connect = _EmailActionWlan1_1Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 46),
    _EmailActionWlan1_1Connect_Type()
)
emailActionWlan1_1Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_1Connect.setStatus("current")


class _EmailActionWlan1_1Disconnect_Type(Integer32):
    """Custom type emailActionWlan1_1Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_1Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1_1Disconnect_Object = MibScalar
emailActionWlan1_1Disconnect = _EmailActionWlan1_1Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 47),
    _EmailActionWlan1_1Disconnect_Type()
)
emailActionWlan1_1Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_1Disconnect.setStatus("current")


class _EmailActionWlan1_2Connect_Type(Integer32):
    """Custom type emailActionWlan1_2Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_2Connect_Type.__name__ = "Integer32"
_EmailActionWlan1_2Connect_Object = MibScalar
emailActionWlan1_2Connect = _EmailActionWlan1_2Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 49),
    _EmailActionWlan1_2Connect_Type()
)
emailActionWlan1_2Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_2Connect.setStatus("current")


class _EmailActionWlan1_2Disconnect_Type(Integer32):
    """Custom type emailActionWlan1_2Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_2Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1_2Disconnect_Object = MibScalar
emailActionWlan1_2Disconnect = _EmailActionWlan1_2Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 50),
    _EmailActionWlan1_2Disconnect_Type()
)
emailActionWlan1_2Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_2Disconnect.setStatus("current")


class _EmailActionWlan1_3Connect_Type(Integer32):
    """Custom type emailActionWlan1_3Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_3Connect_Type.__name__ = "Integer32"
_EmailActionWlan1_3Connect_Object = MibScalar
emailActionWlan1_3Connect = _EmailActionWlan1_3Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 52),
    _EmailActionWlan1_3Connect_Type()
)
emailActionWlan1_3Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_3Connect.setStatus("current")


class _EmailActionWlan1_3Disconnect_Type(Integer32):
    """Custom type emailActionWlan1_3Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_3Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1_3Disconnect_Object = MibScalar
emailActionWlan1_3Disconnect = _EmailActionWlan1_3Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 53),
    _EmailActionWlan1_3Disconnect_Type()
)
emailActionWlan1_3Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_3Disconnect.setStatus("current")


class _EmailActionWlan1_4Connect_Type(Integer32):
    """Custom type emailActionWlan1_4Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_4Connect_Type.__name__ = "Integer32"
_EmailActionWlan1_4Connect_Object = MibScalar
emailActionWlan1_4Connect = _EmailActionWlan1_4Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 55),
    _EmailActionWlan1_4Connect_Type()
)
emailActionWlan1_4Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_4Connect.setStatus("current")


class _EmailActionWlan1_4Disconnect_Type(Integer32):
    """Custom type emailActionWlan1_4Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_4Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1_4Disconnect_Object = MibScalar
emailActionWlan1_4Disconnect = _EmailActionWlan1_4Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 56),
    _EmailActionWlan1_4Disconnect_Type()
)
emailActionWlan1_4Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_4Disconnect.setStatus("current")


class _EmailActionWlan1_5Connect_Type(Integer32):
    """Custom type emailActionWlan1_5Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_5Connect_Type.__name__ = "Integer32"
_EmailActionWlan1_5Connect_Object = MibScalar
emailActionWlan1_5Connect = _EmailActionWlan1_5Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 58),
    _EmailActionWlan1_5Connect_Type()
)
emailActionWlan1_5Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_5Connect.setStatus("current")


class _EmailActionWlan1_5Disconnect_Type(Integer32):
    """Custom type emailActionWlan1_5Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_5Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1_5Disconnect_Object = MibScalar
emailActionWlan1_5Disconnect = _EmailActionWlan1_5Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 59),
    _EmailActionWlan1_5Disconnect_Type()
)
emailActionWlan1_5Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_5Disconnect.setStatus("current")


class _EmailActionWlan1_6Connect_Type(Integer32):
    """Custom type emailActionWlan1_6Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_6Connect_Type.__name__ = "Integer32"
_EmailActionWlan1_6Connect_Object = MibScalar
emailActionWlan1_6Connect = _EmailActionWlan1_6Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 61),
    _EmailActionWlan1_6Connect_Type()
)
emailActionWlan1_6Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_6Connect.setStatus("current")


class _EmailActionWlan1_6Disconnect_Type(Integer32):
    """Custom type emailActionWlan1_6Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_6Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1_6Disconnect_Object = MibScalar
emailActionWlan1_6Disconnect = _EmailActionWlan1_6Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 62),
    _EmailActionWlan1_6Disconnect_Type()
)
emailActionWlan1_6Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_6Disconnect.setStatus("current")


class _EmailActionWlan1_7Connect_Type(Integer32):
    """Custom type emailActionWlan1_7Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_7Connect_Type.__name__ = "Integer32"
_EmailActionWlan1_7Connect_Object = MibScalar
emailActionWlan1_7Connect = _EmailActionWlan1_7Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 64),
    _EmailActionWlan1_7Connect_Type()
)
emailActionWlan1_7Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_7Connect.setStatus("current")


class _EmailActionWlan1_7Disconnect_Type(Integer32):
    """Custom type emailActionWlan1_7Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_7Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1_7Disconnect_Object = MibScalar
emailActionWlan1_7Disconnect = _EmailActionWlan1_7Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 65),
    _EmailActionWlan1_7Disconnect_Type()
)
emailActionWlan1_7Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_7Disconnect.setStatus("current")


class _EmailActionWlan1_8Connect_Type(Integer32):
    """Custom type emailActionWlan1_8Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_8Connect_Type.__name__ = "Integer32"
_EmailActionWlan1_8Connect_Object = MibScalar
emailActionWlan1_8Connect = _EmailActionWlan1_8Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 67),
    _EmailActionWlan1_8Connect_Type()
)
emailActionWlan1_8Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_8Connect.setStatus("current")


class _EmailActionWlan1_8Disconnect_Type(Integer32):
    """Custom type emailActionWlan1_8Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EmailActionWlan1_8Disconnect_Type.__name__ = "Integer32"
_EmailActionWlan1_8Disconnect_Object = MibScalar
emailActionWlan1_8Disconnect = _EmailActionWlan1_8Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 1, 68),
    _EmailActionWlan1_8Disconnect_Type()
)
emailActionWlan1_8Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailActionWlan1_8Disconnect.setStatus("current")
_RelayAction_ObjectIdentity = ObjectIdentity
relayAction = _RelayAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2)
)


class _RelayActionColdStart_Type(Integer32):
    """Custom type relayActionColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionColdStart_Type.__name__ = "Integer32"
_RelayActionColdStart_Object = MibScalar
relayActionColdStart = _RelayActionColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 1),
    _RelayActionColdStart_Type()
)
relayActionColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionColdStart.setStatus("current")


class _RelayActionWarmStart_Type(Integer32):
    """Custom type relayActionWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWarmStart_Type.__name__ = "Integer32"
_RelayActionWarmStart_Object = MibScalar
relayActionWarmStart = _RelayActionWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 2),
    _RelayActionWarmStart_Type()
)
relayActionWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWarmStart.setStatus("current")


class _RelayActionPower1Off_Type(Integer32):
    """Custom type relayActionPower1Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionPower1Off_Type.__name__ = "Integer32"
_RelayActionPower1Off_Object = MibScalar
relayActionPower1Off = _RelayActionPower1Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 3),
    _RelayActionPower1Off_Type()
)
relayActionPower1Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionPower1Off.setStatus("current")


class _RelayActionPower1On_Type(Integer32):
    """Custom type relayActionPower1On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionPower1On_Type.__name__ = "Integer32"
_RelayActionPower1On_Object = MibScalar
relayActionPower1On = _RelayActionPower1On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 4),
    _RelayActionPower1On_Type()
)
relayActionPower1On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionPower1On.setStatus("current")


class _RelayActionPower2Off_Type(Integer32):
    """Custom type relayActionPower2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionPower2Off_Type.__name__ = "Integer32"
_RelayActionPower2Off_Object = MibScalar
relayActionPower2Off = _RelayActionPower2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 5),
    _RelayActionPower2Off_Type()
)
relayActionPower2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionPower2Off.setStatus("current")


class _RelayActionPower2On_Type(Integer32):
    """Custom type relayActionPower2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionPower2On_Type.__name__ = "Integer32"
_RelayActionPower2On_Object = MibScalar
relayActionPower2On = _RelayActionPower2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 6),
    _RelayActionPower2On_Type()
)
relayActionPower2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionPower2On.setStatus("current")


class _RelayActionPoeOff_Type(Integer32):
    """Custom type relayActionPoeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionPoeOff_Type.__name__ = "Integer32"
_RelayActionPoeOff_Object = MibScalar
relayActionPoeOff = _RelayActionPoeOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 7),
    _RelayActionPoeOff_Type()
)
relayActionPoeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionPoeOff.setStatus("current")


class _RelayActionPoeOn_Type(Integer32):
    """Custom type relayActionPoeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionPoeOn_Type.__name__ = "Integer32"
_RelayActionPoeOn_Object = MibScalar
relayActionPoeOn = _RelayActionPoeOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 8),
    _RelayActionPoeOn_Type()
)
relayActionPoeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionPoeOn.setStatus("current")


class _RelayActionDi1On2Off_Type(Integer32):
    """Custom type relayActionDi1On2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionDi1On2Off_Type.__name__ = "Integer32"
_RelayActionDi1On2Off_Object = MibScalar
relayActionDi1On2Off = _RelayActionDi1On2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 9),
    _RelayActionDi1On2Off_Type()
)
relayActionDi1On2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionDi1On2Off.setStatus("current")


class _RelayActionDi1Off2On_Type(Integer32):
    """Custom type relayActionDi1Off2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionDi1Off2On_Type.__name__ = "Integer32"
_RelayActionDi1Off2On_Object = MibScalar
relayActionDi1Off2On = _RelayActionDi1Off2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 10),
    _RelayActionDi1Off2On_Type()
)
relayActionDi1Off2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionDi1Off2On.setStatus("current")


class _RelayActionDi2On2Off_Type(Integer32):
    """Custom type relayActionDi2On2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionDi2On2Off_Type.__name__ = "Integer32"
_RelayActionDi2On2Off_Object = MibScalar
relayActionDi2On2Off = _RelayActionDi2On2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 11),
    _RelayActionDi2On2Off_Type()
)
relayActionDi2On2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionDi2On2Off.setStatus("current")


class _RelayActionDi2Off2On_Type(Integer32):
    """Custom type relayActionDi2Off2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionDi2Off2On_Type.__name__ = "Integer32"
_RelayActionDi2Off2On_Object = MibScalar
relayActionDi2Off2On = _RelayActionDi2Off2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 12),
    _RelayActionDi2Off2On_Type()
)
relayActionDi2Off2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionDi2Off2On.setStatus("current")


class _RelayActionConfigChange_Type(Integer32):
    """Custom type relayActionConfigChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionConfigChange_Type.__name__ = "Integer32"
_RelayActionConfigChange_Object = MibScalar
relayActionConfigChange = _RelayActionConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 13),
    _RelayActionConfigChange_Type()
)
relayActionConfigChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionConfigChange.setStatus("current")


class _RelayActionConsoleAuthFail_Type(Integer32):
    """Custom type relayActionConsoleAuthFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionConsoleAuthFail_Type.__name__ = "Integer32"
_RelayActionConsoleAuthFail_Object = MibScalar
relayActionConsoleAuthFail = _RelayActionConsoleAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 14),
    _RelayActionConsoleAuthFail_Type()
)
relayActionConsoleAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionConsoleAuthFail.setStatus("current")


class _RelayActionLanLinkOn_Type(Integer32):
    """Custom type relayActionLanLinkOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionLanLinkOn_Type.__name__ = "Integer32"
_RelayActionLanLinkOn_Object = MibScalar
relayActionLanLinkOn = _RelayActionLanLinkOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 18),
    _RelayActionLanLinkOn_Type()
)
relayActionLanLinkOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionLanLinkOn.setStatus("current")


class _RelayActionLanLinkOff_Type(Integer32):
    """Custom type relayActionLanLinkOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionLanLinkOff_Type.__name__ = "Integer32"
_RelayActionLanLinkOff_Object = MibScalar
relayActionLanLinkOff = _RelayActionLanLinkOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 19),
    _RelayActionLanLinkOff_Type()
)
relayActionLanLinkOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionLanLinkOff.setStatus("current")


class _RelayActionWlan1Connect_Type(Integer32):
    """Custom type relayActionWlan1Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1Connect_Type.__name__ = "Integer32"
_RelayActionWlan1Connect_Object = MibScalar
relayActionWlan1Connect = _RelayActionWlan1Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 40),
    _RelayActionWlan1Connect_Type()
)
relayActionWlan1Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1Connect.setStatus("current")


class _RelayActionWlan1Disconnect_Type(Integer32):
    """Custom type relayActionWlan1Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1Disconnect_Object = MibScalar
relayActionWlan1Disconnect = _RelayActionWlan1Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 41),
    _RelayActionWlan1Disconnect_Type()
)
relayActionWlan1Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1Disconnect.setStatus("current")


class _RelayActionWlan1_1Connect_Type(Integer32):
    """Custom type relayActionWlan1_1Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_1Connect_Type.__name__ = "Integer32"
_RelayActionWlan1_1Connect_Object = MibScalar
relayActionWlan1_1Connect = _RelayActionWlan1_1Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 46),
    _RelayActionWlan1_1Connect_Type()
)
relayActionWlan1_1Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_1Connect.setStatus("current")


class _RelayActionWlan1_1Disconnect_Type(Integer32):
    """Custom type relayActionWlan1_1Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_1Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1_1Disconnect_Object = MibScalar
relayActionWlan1_1Disconnect = _RelayActionWlan1_1Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 47),
    _RelayActionWlan1_1Disconnect_Type()
)
relayActionWlan1_1Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_1Disconnect.setStatus("current")


class _RelayActionWlan1_2Connect_Type(Integer32):
    """Custom type relayActionWlan1_2Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_2Connect_Type.__name__ = "Integer32"
_RelayActionWlan1_2Connect_Object = MibScalar
relayActionWlan1_2Connect = _RelayActionWlan1_2Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 49),
    _RelayActionWlan1_2Connect_Type()
)
relayActionWlan1_2Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_2Connect.setStatus("current")


class _RelayActionWlan1_2Disconnect_Type(Integer32):
    """Custom type relayActionWlan1_2Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_2Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1_2Disconnect_Object = MibScalar
relayActionWlan1_2Disconnect = _RelayActionWlan1_2Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 50),
    _RelayActionWlan1_2Disconnect_Type()
)
relayActionWlan1_2Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_2Disconnect.setStatus("current")


class _RelayActionWlan1_3Connect_Type(Integer32):
    """Custom type relayActionWlan1_3Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_3Connect_Type.__name__ = "Integer32"
_RelayActionWlan1_3Connect_Object = MibScalar
relayActionWlan1_3Connect = _RelayActionWlan1_3Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 52),
    _RelayActionWlan1_3Connect_Type()
)
relayActionWlan1_3Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_3Connect.setStatus("current")


class _RelayActionWlan1_3Disconnect_Type(Integer32):
    """Custom type relayActionWlan1_3Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_3Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1_3Disconnect_Object = MibScalar
relayActionWlan1_3Disconnect = _RelayActionWlan1_3Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 53),
    _RelayActionWlan1_3Disconnect_Type()
)
relayActionWlan1_3Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_3Disconnect.setStatus("current")


class _RelayActionWlan1_4Connect_Type(Integer32):
    """Custom type relayActionWlan1_4Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_4Connect_Type.__name__ = "Integer32"
_RelayActionWlan1_4Connect_Object = MibScalar
relayActionWlan1_4Connect = _RelayActionWlan1_4Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 55),
    _RelayActionWlan1_4Connect_Type()
)
relayActionWlan1_4Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_4Connect.setStatus("current")


class _RelayActionWlan1_4Disconnect_Type(Integer32):
    """Custom type relayActionWlan1_4Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_4Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1_4Disconnect_Object = MibScalar
relayActionWlan1_4Disconnect = _RelayActionWlan1_4Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 56),
    _RelayActionWlan1_4Disconnect_Type()
)
relayActionWlan1_4Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_4Disconnect.setStatus("current")


class _RelayActionWlan1_5Connect_Type(Integer32):
    """Custom type relayActionWlan1_5Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_5Connect_Type.__name__ = "Integer32"
_RelayActionWlan1_5Connect_Object = MibScalar
relayActionWlan1_5Connect = _RelayActionWlan1_5Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 58),
    _RelayActionWlan1_5Connect_Type()
)
relayActionWlan1_5Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_5Connect.setStatus("current")


class _RelayActionWlan1_5Disconnect_Type(Integer32):
    """Custom type relayActionWlan1_5Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_5Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1_5Disconnect_Object = MibScalar
relayActionWlan1_5Disconnect = _RelayActionWlan1_5Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 59),
    _RelayActionWlan1_5Disconnect_Type()
)
relayActionWlan1_5Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_5Disconnect.setStatus("current")


class _RelayActionWlan1_6Connect_Type(Integer32):
    """Custom type relayActionWlan1_6Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_6Connect_Type.__name__ = "Integer32"
_RelayActionWlan1_6Connect_Object = MibScalar
relayActionWlan1_6Connect = _RelayActionWlan1_6Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 61),
    _RelayActionWlan1_6Connect_Type()
)
relayActionWlan1_6Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_6Connect.setStatus("current")


class _RelayActionWlan1_6Disconnect_Type(Integer32):
    """Custom type relayActionWlan1_6Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_6Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1_6Disconnect_Object = MibScalar
relayActionWlan1_6Disconnect = _RelayActionWlan1_6Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 62),
    _RelayActionWlan1_6Disconnect_Type()
)
relayActionWlan1_6Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_6Disconnect.setStatus("current")


class _RelayActionWlan1_7Connect_Type(Integer32):
    """Custom type relayActionWlan1_7Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_7Connect_Type.__name__ = "Integer32"
_RelayActionWlan1_7Connect_Object = MibScalar
relayActionWlan1_7Connect = _RelayActionWlan1_7Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 64),
    _RelayActionWlan1_7Connect_Type()
)
relayActionWlan1_7Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_7Connect.setStatus("current")


class _RelayActionWlan1_7Disconnect_Type(Integer32):
    """Custom type relayActionWlan1_7Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_7Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1_7Disconnect_Object = MibScalar
relayActionWlan1_7Disconnect = _RelayActionWlan1_7Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 65),
    _RelayActionWlan1_7Disconnect_Type()
)
relayActionWlan1_7Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_7Disconnect.setStatus("current")


class _RelayActionWlan1_8Connect_Type(Integer32):
    """Custom type relayActionWlan1_8Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_8Connect_Type.__name__ = "Integer32"
_RelayActionWlan1_8Connect_Object = MibScalar
relayActionWlan1_8Connect = _RelayActionWlan1_8Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 67),
    _RelayActionWlan1_8Connect_Type()
)
relayActionWlan1_8Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_8Connect.setStatus("current")


class _RelayActionWlan1_8Disconnect_Type(Integer32):
    """Custom type relayActionWlan1_8Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RelayActionWlan1_8Disconnect_Type.__name__ = "Integer32"
_RelayActionWlan1_8Disconnect_Object = MibScalar
relayActionWlan1_8Disconnect = _RelayActionWlan1_8Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 2, 68),
    _RelayActionWlan1_8Disconnect_Type()
)
relayActionWlan1_8Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActionWlan1_8Disconnect.setStatus("current")
_TrapAction_ObjectIdentity = ObjectIdentity
trapAction = _TrapAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3)
)


class _TrapActionColdStart_Type(Integer32):
    """Custom type trapActionColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionColdStart_Type.__name__ = "Integer32"
_TrapActionColdStart_Object = MibScalar
trapActionColdStart = _TrapActionColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 1),
    _TrapActionColdStart_Type()
)
trapActionColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionColdStart.setStatus("current")


class _TrapActionWarmStart_Type(Integer32):
    """Custom type trapActionWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWarmStart_Type.__name__ = "Integer32"
_TrapActionWarmStart_Object = MibScalar
trapActionWarmStart = _TrapActionWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 2),
    _TrapActionWarmStart_Type()
)
trapActionWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWarmStart.setStatus("current")


class _TrapActionPower1Off_Type(Integer32):
    """Custom type trapActionPower1Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionPower1Off_Type.__name__ = "Integer32"
_TrapActionPower1Off_Object = MibScalar
trapActionPower1Off = _TrapActionPower1Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 3),
    _TrapActionPower1Off_Type()
)
trapActionPower1Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionPower1Off.setStatus("current")


class _TrapActionPower1On_Type(Integer32):
    """Custom type trapActionPower1On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionPower1On_Type.__name__ = "Integer32"
_TrapActionPower1On_Object = MibScalar
trapActionPower1On = _TrapActionPower1On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 4),
    _TrapActionPower1On_Type()
)
trapActionPower1On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionPower1On.setStatus("current")


class _TrapActionPower2Off_Type(Integer32):
    """Custom type trapActionPower2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionPower2Off_Type.__name__ = "Integer32"
_TrapActionPower2Off_Object = MibScalar
trapActionPower2Off = _TrapActionPower2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 5),
    _TrapActionPower2Off_Type()
)
trapActionPower2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionPower2Off.setStatus("current")


class _TrapActionPower2On_Type(Integer32):
    """Custom type trapActionPower2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionPower2On_Type.__name__ = "Integer32"
_TrapActionPower2On_Object = MibScalar
trapActionPower2On = _TrapActionPower2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 6),
    _TrapActionPower2On_Type()
)
trapActionPower2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionPower2On.setStatus("current")


class _TrapActionPoeOff_Type(Integer32):
    """Custom type trapActionPoeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionPoeOff_Type.__name__ = "Integer32"
_TrapActionPoeOff_Object = MibScalar
trapActionPoeOff = _TrapActionPoeOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 7),
    _TrapActionPoeOff_Type()
)
trapActionPoeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionPoeOff.setStatus("current")


class _TrapActionPoeOn_Type(Integer32):
    """Custom type trapActionPoeOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionPoeOn_Type.__name__ = "Integer32"
_TrapActionPoeOn_Object = MibScalar
trapActionPoeOn = _TrapActionPoeOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 8),
    _TrapActionPoeOn_Type()
)
trapActionPoeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionPoeOn.setStatus("current")


class _TrapActionDi1On2Off_Type(Integer32):
    """Custom type trapActionDi1On2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionDi1On2Off_Type.__name__ = "Integer32"
_TrapActionDi1On2Off_Object = MibScalar
trapActionDi1On2Off = _TrapActionDi1On2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 9),
    _TrapActionDi1On2Off_Type()
)
trapActionDi1On2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionDi1On2Off.setStatus("current")


class _TrapActionDi1Off2On_Type(Integer32):
    """Custom type trapActionDi1Off2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionDi1Off2On_Type.__name__ = "Integer32"
_TrapActionDi1Off2On_Object = MibScalar
trapActionDi1Off2On = _TrapActionDi1Off2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 10),
    _TrapActionDi1Off2On_Type()
)
trapActionDi1Off2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionDi1Off2On.setStatus("current")


class _TrapActionDi2On2Off_Type(Integer32):
    """Custom type trapActionDi2On2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionDi2On2Off_Type.__name__ = "Integer32"
_TrapActionDi2On2Off_Object = MibScalar
trapActionDi2On2Off = _TrapActionDi2On2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 11),
    _TrapActionDi2On2Off_Type()
)
trapActionDi2On2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionDi2On2Off.setStatus("current")


class _TrapActionDi2Off2On_Type(Integer32):
    """Custom type trapActionDi2Off2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionDi2Off2On_Type.__name__ = "Integer32"
_TrapActionDi2Off2On_Object = MibScalar
trapActionDi2Off2On = _TrapActionDi2Off2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 12),
    _TrapActionDi2Off2On_Type()
)
trapActionDi2Off2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionDi2Off2On.setStatus("current")


class _TrapActionConfigChange_Type(Integer32):
    """Custom type trapActionConfigChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionConfigChange_Type.__name__ = "Integer32"
_TrapActionConfigChange_Object = MibScalar
trapActionConfigChange = _TrapActionConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 13),
    _TrapActionConfigChange_Type()
)
trapActionConfigChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionConfigChange.setStatus("current")


class _TrapActionConsoleAuthFail_Type(Integer32):
    """Custom type trapActionConsoleAuthFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionConsoleAuthFail_Type.__name__ = "Integer32"
_TrapActionConsoleAuthFail_Object = MibScalar
trapActionConsoleAuthFail = _TrapActionConsoleAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 14),
    _TrapActionConsoleAuthFail_Type()
)
trapActionConsoleAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionConsoleAuthFail.setStatus("current")


class _TrapActionLanLinkOn_Type(Integer32):
    """Custom type trapActionLanLinkOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionLanLinkOn_Type.__name__ = "Integer32"
_TrapActionLanLinkOn_Object = MibScalar
trapActionLanLinkOn = _TrapActionLanLinkOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 18),
    _TrapActionLanLinkOn_Type()
)
trapActionLanLinkOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionLanLinkOn.setStatus("current")


class _TrapActionLanLinkOff_Type(Integer32):
    """Custom type trapActionLanLinkOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionLanLinkOff_Type.__name__ = "Integer32"
_TrapActionLanLinkOff_Object = MibScalar
trapActionLanLinkOff = _TrapActionLanLinkOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 19),
    _TrapActionLanLinkOff_Type()
)
trapActionLanLinkOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionLanLinkOff.setStatus("current")


class _TrapActionWlan1Connect_Type(Integer32):
    """Custom type trapActionWlan1Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1Connect_Type.__name__ = "Integer32"
_TrapActionWlan1Connect_Object = MibScalar
trapActionWlan1Connect = _TrapActionWlan1Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 40),
    _TrapActionWlan1Connect_Type()
)
trapActionWlan1Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1Connect.setStatus("current")


class _TrapActionWlan1Disconnect_Type(Integer32):
    """Custom type trapActionWlan1Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1Disconnect_Object = MibScalar
trapActionWlan1Disconnect = _TrapActionWlan1Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 41),
    _TrapActionWlan1Disconnect_Type()
)
trapActionWlan1Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1Disconnect.setStatus("current")


class _TrapActionWlan1_1Connect_Type(Integer32):
    """Custom type trapActionWlan1_1Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_1Connect_Type.__name__ = "Integer32"
_TrapActionWlan1_1Connect_Object = MibScalar
trapActionWlan1_1Connect = _TrapActionWlan1_1Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 46),
    _TrapActionWlan1_1Connect_Type()
)
trapActionWlan1_1Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_1Connect.setStatus("current")


class _TrapActionWlan1_1Disconnect_Type(Integer32):
    """Custom type trapActionWlan1_1Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_1Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1_1Disconnect_Object = MibScalar
trapActionWlan1_1Disconnect = _TrapActionWlan1_1Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 47),
    _TrapActionWlan1_1Disconnect_Type()
)
trapActionWlan1_1Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_1Disconnect.setStatus("current")


class _TrapActionWlan1_2Connect_Type(Integer32):
    """Custom type trapActionWlan1_2Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_2Connect_Type.__name__ = "Integer32"
_TrapActionWlan1_2Connect_Object = MibScalar
trapActionWlan1_2Connect = _TrapActionWlan1_2Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 49),
    _TrapActionWlan1_2Connect_Type()
)
trapActionWlan1_2Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_2Connect.setStatus("current")


class _TrapActionWlan1_2Disconnect_Type(Integer32):
    """Custom type trapActionWlan1_2Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_2Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1_2Disconnect_Object = MibScalar
trapActionWlan1_2Disconnect = _TrapActionWlan1_2Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 50),
    _TrapActionWlan1_2Disconnect_Type()
)
trapActionWlan1_2Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_2Disconnect.setStatus("current")


class _TrapActionWlan1_3Connect_Type(Integer32):
    """Custom type trapActionWlan1_3Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_3Connect_Type.__name__ = "Integer32"
_TrapActionWlan1_3Connect_Object = MibScalar
trapActionWlan1_3Connect = _TrapActionWlan1_3Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 52),
    _TrapActionWlan1_3Connect_Type()
)
trapActionWlan1_3Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_3Connect.setStatus("current")


class _TrapActionWlan1_3Disconnect_Type(Integer32):
    """Custom type trapActionWlan1_3Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_3Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1_3Disconnect_Object = MibScalar
trapActionWlan1_3Disconnect = _TrapActionWlan1_3Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 53),
    _TrapActionWlan1_3Disconnect_Type()
)
trapActionWlan1_3Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_3Disconnect.setStatus("current")


class _TrapActionWlan1_4Connect_Type(Integer32):
    """Custom type trapActionWlan1_4Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_4Connect_Type.__name__ = "Integer32"
_TrapActionWlan1_4Connect_Object = MibScalar
trapActionWlan1_4Connect = _TrapActionWlan1_4Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 55),
    _TrapActionWlan1_4Connect_Type()
)
trapActionWlan1_4Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_4Connect.setStatus("current")


class _TrapActionWlan1_4Disconnect_Type(Integer32):
    """Custom type trapActionWlan1_4Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_4Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1_4Disconnect_Object = MibScalar
trapActionWlan1_4Disconnect = _TrapActionWlan1_4Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 56),
    _TrapActionWlan1_4Disconnect_Type()
)
trapActionWlan1_4Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_4Disconnect.setStatus("current")


class _TrapActionWlan1_5Connect_Type(Integer32):
    """Custom type trapActionWlan1_5Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_5Connect_Type.__name__ = "Integer32"
_TrapActionWlan1_5Connect_Object = MibScalar
trapActionWlan1_5Connect = _TrapActionWlan1_5Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 58),
    _TrapActionWlan1_5Connect_Type()
)
trapActionWlan1_5Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_5Connect.setStatus("current")


class _TrapActionWlan1_5Disconnect_Type(Integer32):
    """Custom type trapActionWlan1_5Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_5Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1_5Disconnect_Object = MibScalar
trapActionWlan1_5Disconnect = _TrapActionWlan1_5Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 59),
    _TrapActionWlan1_5Disconnect_Type()
)
trapActionWlan1_5Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_5Disconnect.setStatus("current")


class _TrapActionWlan1_6Connect_Type(Integer32):
    """Custom type trapActionWlan1_6Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_6Connect_Type.__name__ = "Integer32"
_TrapActionWlan1_6Connect_Object = MibScalar
trapActionWlan1_6Connect = _TrapActionWlan1_6Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 61),
    _TrapActionWlan1_6Connect_Type()
)
trapActionWlan1_6Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_6Connect.setStatus("current")


class _TrapActionWlan1_6Disconnect_Type(Integer32):
    """Custom type trapActionWlan1_6Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_6Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1_6Disconnect_Object = MibScalar
trapActionWlan1_6Disconnect = _TrapActionWlan1_6Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 62),
    _TrapActionWlan1_6Disconnect_Type()
)
trapActionWlan1_6Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_6Disconnect.setStatus("current")


class _TrapActionWlan1_7Connect_Type(Integer32):
    """Custom type trapActionWlan1_7Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_7Connect_Type.__name__ = "Integer32"
_TrapActionWlan1_7Connect_Object = MibScalar
trapActionWlan1_7Connect = _TrapActionWlan1_7Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 64),
    _TrapActionWlan1_7Connect_Type()
)
trapActionWlan1_7Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_7Connect.setStatus("current")


class _TrapActionWlan1_7Disconnect_Type(Integer32):
    """Custom type trapActionWlan1_7Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_7Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1_7Disconnect_Object = MibScalar
trapActionWlan1_7Disconnect = _TrapActionWlan1_7Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 65),
    _TrapActionWlan1_7Disconnect_Type()
)
trapActionWlan1_7Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_7Disconnect.setStatus("current")


class _TrapActionWlan1_8Connect_Type(Integer32):
    """Custom type trapActionWlan1_8Connect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_8Connect_Type.__name__ = "Integer32"
_TrapActionWlan1_8Connect_Object = MibScalar
trapActionWlan1_8Connect = _TrapActionWlan1_8Connect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 67),
    _TrapActionWlan1_8Connect_Type()
)
trapActionWlan1_8Connect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_8Connect.setStatus("current")


class _TrapActionWlan1_8Disconnect_Type(Integer32):
    """Custom type trapActionWlan1_8Disconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TrapActionWlan1_8Disconnect_Type.__name__ = "Integer32"
_TrapActionWlan1_8Disconnect_Object = MibScalar
trapActionWlan1_8Disconnect = _TrapActionWlan1_8Disconnect_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 3, 68),
    _TrapActionWlan1_8Disconnect_Type()
)
trapActionWlan1_8Disconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapActionWlan1_8Disconnect.setStatus("current")
_SystemLog_ObjectIdentity = ObjectIdentity
systemLog = _SystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 4)
)


class _SystemLogSystemEnable_Type(Integer32):
    """Custom type systemLogSystemEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SystemLogSystemEnable_Type.__name__ = "Integer32"
_SystemLogSystemEnable_Object = MibScalar
systemLogSystemEnable = _SystemLogSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 4, 1),
    _SystemLogSystemEnable_Type()
)
systemLogSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogSystemEnable.setStatus("current")


class _SystemLogNetworkEnable_Type(Integer32):
    """Custom type systemLogNetworkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SystemLogNetworkEnable_Type.__name__ = "Integer32"
_SystemLogNetworkEnable_Object = MibScalar
systemLogNetworkEnable = _SystemLogNetworkEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 4, 2),
    _SystemLogNetworkEnable_Type()
)
systemLogNetworkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogNetworkEnable.setStatus("current")


class _SystemLogConfigEnable_Type(Integer32):
    """Custom type systemLogConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SystemLogConfigEnable_Type.__name__ = "Integer32"
_SystemLogConfigEnable_Object = MibScalar
systemLogConfigEnable = _SystemLogConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 4, 3),
    _SystemLogConfigEnable_Type()
)
systemLogConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogConfigEnable.setStatus("current")


class _SystemLogPowerEnable_Type(Integer32):
    """Custom type systemLogPowerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SystemLogPowerEnable_Type.__name__ = "Integer32"
_SystemLogPowerEnable_Object = MibScalar
systemLogPowerEnable = _SystemLogPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 4, 4),
    _SystemLogPowerEnable_Type()
)
systemLogPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogPowerEnable.setStatus("current")


class _SystemLogDinEnable_Type(Integer32):
    """Custom type systemLogDinEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SystemLogDinEnable_Type.__name__ = "Integer32"
_SystemLogDinEnable_Object = MibScalar
systemLogDinEnable = _SystemLogDinEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 4, 5),
    _SystemLogDinEnable_Type()
)
systemLogDinEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogDinEnable.setStatus("current")


class _SystemLogRssiReport_Type(Integer32):
    """Custom type systemLogRssiReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SystemLogRssiReport_Type.__name__ = "Integer32"
_SystemLogRssiReport_Object = MibScalar
systemLogRssiReport = _SystemLogRssiReport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 4, 7),
    _SystemLogRssiReport_Type()
)
systemLogRssiReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogRssiReport.setStatus("current")
_SysLog_ObjectIdentity = ObjectIdentity
sysLog = _SysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 5)
)


class _SysLogSystemEnable_Type(Integer32):
    """Custom type sysLogSystemEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysLogSystemEnable_Type.__name__ = "Integer32"
_SysLogSystemEnable_Object = MibScalar
sysLogSystemEnable = _SysLogSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 5, 1),
    _SysLogSystemEnable_Type()
)
sysLogSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogSystemEnable.setStatus("current")


class _SysLogNetworkEnable_Type(Integer32):
    """Custom type sysLogNetworkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysLogNetworkEnable_Type.__name__ = "Integer32"
_SysLogNetworkEnable_Object = MibScalar
sysLogNetworkEnable = _SysLogNetworkEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 5, 2),
    _SysLogNetworkEnable_Type()
)
sysLogNetworkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogNetworkEnable.setStatus("current")


class _SysLogConfigEnable_Type(Integer32):
    """Custom type sysLogConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysLogConfigEnable_Type.__name__ = "Integer32"
_SysLogConfigEnable_Object = MibScalar
sysLogConfigEnable = _SysLogConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 5, 3),
    _SysLogConfigEnable_Type()
)
sysLogConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogConfigEnable.setStatus("current")


class _SysLogPowerEnable_Type(Integer32):
    """Custom type sysLogPowerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysLogPowerEnable_Type.__name__ = "Integer32"
_SysLogPowerEnable_Object = MibScalar
sysLogPowerEnable = _SysLogPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 5, 4),
    _SysLogPowerEnable_Type()
)
sysLogPowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogPowerEnable.setStatus("current")


class _SysLogDinEnable_Type(Integer32):
    """Custom type sysLogDinEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysLogDinEnable_Type.__name__ = "Integer32"
_SysLogDinEnable_Object = MibScalar
sysLogDinEnable = _SysLogDinEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 5, 5),
    _SysLogDinEnable_Type()
)
sysLogDinEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogDinEnable.setStatus("current")


class _SysLogRssiReport_Type(Integer32):
    """Custom type sysLogRssiReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysLogRssiReport_Type.__name__ = "Integer32"
_SysLogRssiReport_Object = MibScalar
sysLogRssiReport = _SysLogRssiReport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 5, 7),
    _SysLogRssiReport_Type()
)
sysLogRssiReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogRssiReport.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6)
)


class _SnmpEnable_Type(Integer32):
    """Custom type snmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SnmpEnable_Type.__name__ = "Integer32"
_SnmpEnable_Object = MibScalar
snmpEnable = _SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 1),
    _SnmpEnable_Type()
)
snmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnable.setStatus("current")


class _SnmpVersion_Type(Integer32):
    """Custom type snmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1-v2c-v3", 1),
          ("v1-v2c", 2),
          ("v3", 3))
    )


_SnmpVersion_Type.__name__ = "Integer32"
_SnmpVersion_Object = MibScalar
snmpVersion = _SnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 2),
    _SnmpVersion_Type()
)
snmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpVersion.setStatus("current")
_SnmpRoCommunity_Type = DisplayString
_SnmpRoCommunity_Object = MibScalar
snmpRoCommunity = _SnmpRoCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 3),
    _SnmpRoCommunity_Type()
)
snmpRoCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRoCommunity.setStatus("current")
_SnmpRwCommunity_Type = DisplayString
_SnmpRwCommunity_Object = MibScalar
snmpRwCommunity = _SnmpRwCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 4),
    _SnmpRwCommunity_Type()
)
snmpRwCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRwCommunity.setStatus("current")
_SnmpFirstTrapServer_Type = DisplayString
_SnmpFirstTrapServer_Object = MibScalar
snmpFirstTrapServer = _SnmpFirstTrapServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 5),
    _SnmpFirstTrapServer_Type()
)
snmpFirstTrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFirstTrapServer.setStatus("current")


class _SnmpFirstTrapVersion_Type(Integer32):
    """Custom type snmpFirstTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_SnmpFirstTrapVersion_Type.__name__ = "Integer32"
_SnmpFirstTrapVersion_Object = MibScalar
snmpFirstTrapVersion = _SnmpFirstTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 6),
    _SnmpFirstTrapVersion_Type()
)
snmpFirstTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFirstTrapVersion.setStatus("current")
_SnmpFirstTrapCommunity_Type = DisplayString
_SnmpFirstTrapCommunity_Object = MibScalar
snmpFirstTrapCommunity = _SnmpFirstTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 7),
    _SnmpFirstTrapCommunity_Type()
)
snmpFirstTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFirstTrapCommunity.setStatus("current")
_SnmpSecondTrapServer_Type = DisplayString
_SnmpSecondTrapServer_Object = MibScalar
snmpSecondTrapServer = _SnmpSecondTrapServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 8),
    _SnmpSecondTrapServer_Type()
)
snmpSecondTrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSecondTrapServer.setStatus("current")


class _SnmpSecondTrapVersion_Type(Integer32):
    """Custom type snmpSecondTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_SnmpSecondTrapVersion_Type.__name__ = "Integer32"
_SnmpSecondTrapVersion_Object = MibScalar
snmpSecondTrapVersion = _SnmpSecondTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 9),
    _SnmpSecondTrapVersion_Type()
)
snmpSecondTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSecondTrapVersion.setStatus("current")
_SnmpSecondTrapCommunity_Type = DisplayString
_SnmpSecondTrapCommunity_Object = MibScalar
snmpSecondTrapCommunity = _SnmpSecondTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 10),
    _SnmpSecondTrapCommunity_Type()
)
snmpSecondTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSecondTrapCommunity.setStatus("current")


class _SnmpAdminAuthType_Type(Integer32):
    """Custom type snmpAdminAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_SnmpAdminAuthType_Type.__name__ = "Integer32"
_SnmpAdminAuthType_Object = MibScalar
snmpAdminAuthType = _SnmpAdminAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 11),
    _SnmpAdminAuthType_Type()
)
snmpAdminAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAdminAuthType.setStatus("current")


class _SnmpAdminAuthKey_Type(Integer32):
    """Custom type snmpAdminAuthKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("des", 2),
          ("aes", 3))
    )


_SnmpAdminAuthKey_Type.__name__ = "Integer32"
_SnmpAdminAuthKey_Object = MibScalar
snmpAdminAuthKey = _SnmpAdminAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 12),
    _SnmpAdminAuthKey_Type()
)
snmpAdminAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAdminAuthKey.setStatus("current")
_SnmpPrivMib_Type = DisplayString
_SnmpPrivMib_Object = MibScalar
snmpPrivMib = _SnmpPrivMib_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 17),
    _SnmpPrivMib_Type()
)
snmpPrivMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPrivMib.setStatus("current")


class _SnmpRmtMngtEnable_Type(Integer32):
    """Custom type snmpRmtMngtEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SnmpRmtMngtEnable_Type.__name__ = "Integer32"
_SnmpRmtMngtEnable_Object = MibScalar
snmpRmtMngtEnable = _SnmpRmtMngtEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 18),
    _SnmpRmtMngtEnable_Type()
)
snmpRmtMngtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpRmtMngtEnable.setStatus("current")


class _SnmpUserAuthAccount_Type(Integer32):
    """Custom type snmpUserAuthAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnmpUserAuthAccount_Type.__name__ = "Integer32"
_SnmpUserAuthAccount_Object = MibScalar
snmpUserAuthAccount = _SnmpUserAuthAccount_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 19),
    _SnmpUserAuthAccount_Type()
)
snmpUserAuthAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthAccount.setStatus("current")
_SnmpThirdTrapServer_Type = DisplayString
_SnmpThirdTrapServer_Object = MibScalar
snmpThirdTrapServer = _SnmpThirdTrapServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 20),
    _SnmpThirdTrapServer_Type()
)
snmpThirdTrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpThirdTrapServer.setStatus("current")


class _SnmpThirdTrapVersion_Type(Integer32):
    """Custom type snmpThirdTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_SnmpThirdTrapVersion_Type.__name__ = "Integer32"
_SnmpThirdTrapVersion_Object = MibScalar
snmpThirdTrapVersion = _SnmpThirdTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 21),
    _SnmpThirdTrapVersion_Type()
)
snmpThirdTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpThirdTrapVersion.setStatus("current")
_SnmpThirdTrapCommunity_Type = DisplayString
_SnmpThirdTrapCommunity_Object = MibScalar
snmpThirdTrapCommunity = _SnmpThirdTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 6, 22),
    _SnmpThirdTrapCommunity_Type()
)
snmpThirdTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpThirdTrapCommunity.setStatus("current")
_EmailSmtp_ObjectIdentity = ObjectIdentity
emailSmtp = _EmailSmtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7)
)
_EmailSmtpServerTable_Object = MibTable
emailSmtpServerTable = _EmailSmtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 1)
)
if mibBuilder.loadTexts:
    emailSmtpServerTable.setStatus("current")
_EmailSmtpServerEntry_Object = MibTableRow
emailSmtpServerEntry = _EmailSmtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 1, 1)
)
emailSmtpServerEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "emailSmtpServerIndex"),
)
if mibBuilder.loadTexts:
    emailSmtpServerEntry.setStatus("current")


class _EmailSmtpServerIndex_Type(Integer32):
    """Custom type emailSmtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EmailSmtpServerIndex_Type.__name__ = "Integer32"
_EmailSmtpServerIndex_Object = MibTableColumn
emailSmtpServerIndex = _EmailSmtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 1, 1, 1),
    _EmailSmtpServerIndex_Type()
)
emailSmtpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emailSmtpServerIndex.setStatus("current")
_EmailSmtpServerData_Type = DisplayString
_EmailSmtpServerData_Object = MibTableColumn
emailSmtpServerData = _EmailSmtpServerData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 1, 1, 2),
    _EmailSmtpServerData_Type()
)
emailSmtpServerData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpServerData.setStatus("current")
_EmailSmtpMailAddressTable_Object = MibTable
emailSmtpMailAddressTable = _EmailSmtpMailAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 2)
)
if mibBuilder.loadTexts:
    emailSmtpMailAddressTable.setStatus("current")
_EmailSmtpMailAddressEntry_Object = MibTableRow
emailSmtpMailAddressEntry = _EmailSmtpMailAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 2, 1)
)
emailSmtpMailAddressEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "emailSmtpMailAddressIndex"),
)
if mibBuilder.loadTexts:
    emailSmtpMailAddressEntry.setStatus("current")


class _EmailSmtpMailAddressIndex_Type(Integer32):
    """Custom type emailSmtpMailAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EmailSmtpMailAddressIndex_Type.__name__ = "Integer32"
_EmailSmtpMailAddressIndex_Object = MibTableColumn
emailSmtpMailAddressIndex = _EmailSmtpMailAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 2, 1, 1),
    _EmailSmtpMailAddressIndex_Type()
)
emailSmtpMailAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emailSmtpMailAddressIndex.setStatus("current")
_EmailSmtpMailAddressData_Type = DisplayString
_EmailSmtpMailAddressData_Object = MibTableColumn
emailSmtpMailAddressData = _EmailSmtpMailAddressData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 2, 1, 2),
    _EmailSmtpMailAddressData_Type()
)
emailSmtpMailAddressData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpMailAddressData.setStatus("current")
_EmailSmtpUserName_Type = DisplayString
_EmailSmtpUserName_Object = MibScalar
emailSmtpUserName = _EmailSmtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 3),
    _EmailSmtpUserName_Type()
)
emailSmtpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpUserName.setStatus("current")
_EmailSmtpFrom_Type = DisplayString
_EmailSmtpFrom_Object = MibScalar
emailSmtpFrom = _EmailSmtpFrom_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 7, 5),
    _EmailSmtpFrom_Type()
)
emailSmtpFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailSmtpFrom.setStatus("current")
_SysLogServerTable_Object = MibTable
sysLogServerTable = _SysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 8)
)
if mibBuilder.loadTexts:
    sysLogServerTable.setStatus("current")
_SysLogServerEntry_Object = MibTableRow
sysLogServerEntry = _SysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 8, 1)
)
sysLogServerEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "sysLogServerIndex"),
)
if mibBuilder.loadTexts:
    sysLogServerEntry.setStatus("current")


class _SysLogServerIndex_Type(Integer32):
    """Custom type sysLogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SysLogServerIndex_Type.__name__ = "Integer32"
_SysLogServerIndex_Object = MibTableColumn
sysLogServerIndex = _SysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 8, 1, 1),
    _SysLogServerIndex_Type()
)
sysLogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogServerIndex.setStatus("current")
_SysLogServerServer_Type = DisplayString
_SysLogServerServer_Object = MibTableColumn
sysLogServerServer = _SysLogServerServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 8, 1, 2),
    _SysLogServerServer_Type()
)
sysLogServerServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerServer.setStatus("current")


class _SysLogServerPort_Type(Integer32):
    """Custom type sysLogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysLogServerPort_Type.__name__ = "Integer32"
_SysLogServerPort_Object = MibTableColumn
sysLogServerPort = _SysLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 9, 8, 1, 3),
    _SysLogServerPort_Type()
)
sysLogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerPort.setStatus("current")
_SysStatus_ObjectIdentity = ObjectIdentity
sysStatus = _SysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11)
)
_PowerInputTable_Object = MibTable
powerInputTable = _PowerInputTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 9)
)
if mibBuilder.loadTexts:
    powerInputTable.setStatus("current")
_PowerInputEntry_Object = MibTableRow
powerInputEntry = _PowerInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 9, 1)
)
powerInputEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "powerInputIndex"),
)
if mibBuilder.loadTexts:
    powerInputEntry.setStatus("current")
_PowerInputIndex_Type = Integer32
_PowerInputIndex_Object = MibTableColumn
powerInputIndex = _PowerInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 9, 1, 1),
    _PowerInputIndex_Type()
)
powerInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerInputIndex.setStatus("current")


class _PowerInputStatus_Type(Integer32):
    """Custom type powerInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PowerInputStatus_Type.__name__ = "Integer32"
_PowerInputStatus_Object = MibTableColumn
powerInputStatus = _PowerInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 9, 1, 2),
    _PowerInputStatus_Type()
)
powerInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerInputStatus.setStatus("current")
_DiTable_Object = MibTable
diTable = _DiTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 11)
)
if mibBuilder.loadTexts:
    diTable.setStatus("current")
_DiEntry_Object = MibTableRow
diEntry = _DiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 11, 1)
)
diEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "diIndex"),
)
if mibBuilder.loadTexts:
    diEntry.setStatus("current")
_DiIndex_Type = Integer32
_DiIndex_Object = MibTableColumn
diIndex = _DiIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 11, 1, 1),
    _DiIndex_Type()
)
diIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diIndex.setStatus("current")


class _DiInputStatus_Type(Integer32):
    """Custom type diInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DiInputStatus_Type.__name__ = "Integer32"
_DiInputStatus_Object = MibTableColumn
diInputStatus = _DiInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 11, 1, 2),
    _DiInputStatus_Type()
)
diInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diInputStatus.setStatus("current")
_WlanClientListTable_Object = MibTable
wlanClientListTable = _WlanClientListTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13)
)
if mibBuilder.loadTexts:
    wlanClientListTable.setStatus("current")
_WlanClientListEntry_Object = MibTableRow
wlanClientListEntry = _WlanClientListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1)
)
wlanClientListEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "wlanDevIndex"),
    (0, "MOXA-AWK4131A-MIB", "wlanSsidIndex"),
    (0, "MOXA-AWK4131A-MIB", "wlanClientIndex"),
)
if mibBuilder.loadTexts:
    wlanClientListEntry.setStatus("current")
_WlanDevIndex_Type = Integer32
_WlanDevIndex_Object = MibTableColumn
wlanDevIndex = _WlanDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1, 1),
    _WlanDevIndex_Type()
)
wlanDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanDevIndex.setStatus("current")
_WlanSsidIndex_Type = Integer32
_WlanSsidIndex_Object = MibTableColumn
wlanSsidIndex = _WlanSsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1, 2),
    _WlanSsidIndex_Type()
)
wlanSsidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSsidIndex.setStatus("current")
_WlanClientIndex_Type = Integer32
_WlanClientIndex_Object = MibTableColumn
wlanClientIndex = _WlanClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1, 3),
    _WlanClientIndex_Type()
)
wlanClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientIndex.setStatus("current")
_WlanClientMAC_Type = DisplayString
_WlanClientMAC_Object = MibTableColumn
wlanClientMAC = _WlanClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1, 4),
    _WlanClientMAC_Type()
)
wlanClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientMAC.setStatus("current")
_WlanClientIP_Type = DisplayString
_WlanClientIP_Object = MibTableColumn
wlanClientIP = _WlanClientIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1, 5),
    _WlanClientIP_Type()
)
wlanClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientIP.setStatus("current")
_WlanClientSignalStrength_Type = Integer32
_WlanClientSignalStrength_Object = MibTableColumn
wlanClientSignalStrength = _WlanClientSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1, 6),
    _WlanClientSignalStrength_Type()
)
wlanClientSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientSignalStrength.setStatus("current")
_WlanClientSNR_Type = Integer32
_WlanClientSNR_Object = MibTableColumn
wlanClientSNR = _WlanClientSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1, 7),
    _WlanClientSNR_Type()
)
wlanClientSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientSNR.setStatus("current")
_WlanClientConnectionTime_Type = Integer32
_WlanClientConnectionTime_Object = MibTableColumn
wlanClientConnectionTime = _WlanClientConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 13, 1, 8),
    _WlanClientConnectionTime_Type()
)
wlanClientConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanClientConnectionTime.setStatus("current")
_DhcpClientListTable_Object = MibTable
dhcpClientListTable = _DhcpClientListTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 15)
)
if mibBuilder.loadTexts:
    dhcpClientListTable.setStatus("current")
_DhcpClientListEntry_Object = MibTableRow
dhcpClientListEntry = _DhcpClientListEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 15, 1)
)
dhcpClientListEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "dhcpClientIndex"),
)
if mibBuilder.loadTexts:
    dhcpClientListEntry.setStatus("current")
_DhcpClientIndex_Type = Integer32
_DhcpClientIndex_Object = MibTableColumn
dhcpClientIndex = _DhcpClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 15, 1, 1),
    _DhcpClientIndex_Type()
)
dhcpClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientIndex.setStatus("current")
_DhcpClientIP_Type = DisplayString
_DhcpClientIP_Object = MibTableColumn
dhcpClientIP = _DhcpClientIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 15, 1, 2),
    _DhcpClientIP_Type()
)
dhcpClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientIP.setStatus("current")
_DhcpClientMAC_Type = DisplayString
_DhcpClientMAC_Object = MibTableColumn
dhcpClientMAC = _DhcpClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 15, 1, 3),
    _DhcpClientMAC_Type()
)
dhcpClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientMAC.setStatus("current")
_WirelessStatusTable_Object = MibTable
wirelessStatusTable = _WirelessStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17)
)
if mibBuilder.loadTexts:
    wirelessStatusTable.setStatus("current")
_WirelessStatusEntry_Object = MibTableRow
wirelessStatusEntry = _WirelessStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1)
)
wirelessStatusEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "wlanIndex"),
    (0, "MOXA-AWK4131A-MIB", "wlanVapIndex"),
)
if mibBuilder.loadTexts:
    wirelessStatusEntry.setStatus("current")
_WlanIndex_Type = Integer32
_WlanIndex_Object = MibTableColumn
wlanIndex = _WlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 1),
    _WlanIndex_Type()
)
wlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanIndex.setStatus("current")
_WlanChannel_Type = Integer32
_WlanChannel_Object = MibTableColumn
wlanChannel = _WlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 2),
    _WlanChannel_Type()
)
wlanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanChannel.setStatus("current")
_WlanBSSID_Type = DisplayString
_WlanBSSID_Object = MibTableColumn
wlanBSSID = _WlanBSSID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 3),
    _WlanBSSID_Type()
)
wlanBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanBSSID.setStatus("current")
_WlanSingal_Type = DisplayString
_WlanSingal_Object = MibTableColumn
wlanSingal = _WlanSingal_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 4),
    _WlanSingal_Type()
)
wlanSingal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSingal.setStatus("current")
_WlanTxRate_Type = Integer32
_WlanTxRate_Object = MibTableColumn
wlanTxRate = _WlanTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 5),
    _WlanTxRate_Type()
)
wlanTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanTxRate.setStatus("current")
_WlanSSID_Type = DisplayString
_WlanSSID_Object = MibTableColumn
wlanSSID = _WlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 6),
    _WlanSSID_Type()
)
wlanSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSSID.setStatus("current")
_WlanVapIndex_Type = Integer32
_WlanVapIndex_Object = MibTableColumn
wlanVapIndex = _WlanVapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 7),
    _WlanVapIndex_Type()
)
wlanVapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanVapIndex.setStatus("current")
_WlanAPip_Type = DisplayString
_WlanAPip_Object = MibTableColumn
wlanAPip = _WlanAPip_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 10),
    _WlanAPip_Type()
)
wlanAPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanAPip.setStatus("current")
_WlanSNR_Type = DisplayString
_WlanSNR_Object = MibTableColumn
wlanSNR = _WlanSNR_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 11),
    _WlanSNR_Type()
)
wlanSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSNR.setStatus("current")
_WlanNoiseLevel_Type = DisplayString
_WlanNoiseLevel_Object = MibTableColumn
wlanNoiseLevel = _WlanNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 12),
    _WlanNoiseLevel_Type()
)
wlanNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanNoiseLevel.setStatus("current")
_WlanSNR_A_Type = DisplayString
_WlanSNR_A_Object = MibTableColumn
wlanSNR_A = _WlanSNR_A_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 13),
    _WlanSNR_A_Type()
)
wlanSNR_A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSNR_A.setStatus("current")
_WlanSNR_B_Type = DisplayString
_WlanSNR_B_Object = MibTableColumn
wlanSNR_B = _WlanSNR_B_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 14),
    _WlanSNR_B_Type()
)
wlanSNR_B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSNR_B.setStatus("current")
_WlanChannelWidth_Type = DisplayString
_WlanChannelWidth_Object = MibTableColumn
wlanChannelWidth = _WlanChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 15),
    _WlanChannelWidth_Type()
)
wlanChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanChannelWidth.setStatus("current")
_WlanConnectionTime_Type = Integer32
_WlanConnectionTime_Object = MibTableColumn
wlanConnectionTime = _WlanConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 16),
    _WlanConnectionTime_Type()
)
wlanConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanConnectionTime.setStatus("current")


class _WlanOperationMode_Type(Integer32):
    """Custom type wlanOperationMode based on Integer32"""
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
        *(("client", 1),
          ("ap", 2),
          ("sniffer", 3),
          ("master", 4),
          ("slave", 5),
          ("clientRouter", 6))
    )


_WlanOperationMode_Type.__name__ = "Integer32"
_WlanOperationMode_Object = MibTableColumn
wlanOperationMode = _WlanOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 17, 1, 17),
    _WlanOperationMode_Type()
)
wlanOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanOperationMode.setStatus("current")
_RelayStatusAckTable_Object = MibTable
relayStatusAckTable = _RelayStatusAckTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 19)
)
if mibBuilder.loadTexts:
    relayStatusAckTable.setStatus("current")
_RelayStatusAckEntry_Object = MibTableRow
relayStatusAckEntry = _RelayStatusAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 19, 1)
)
relayStatusAckEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "relayIndex"),
)
if mibBuilder.loadTexts:
    relayStatusAckEntry.setStatus("current")
_RelayIndex_Type = Integer32
_RelayIndex_Object = MibTableColumn
relayIndex = _RelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 19, 1, 1),
    _RelayIndex_Type()
)
relayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayIndex.setStatus("current")
_RelayType_Type = DisplayString
_RelayType_Object = MibTableColumn
relayType = _RelayType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 19, 1, 2),
    _RelayType_Type()
)
relayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayType.setStatus("current")


class _RelayStatus_Type(Integer32):
    """Custom type relayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("alarm", 2),
          ("alarmAck", 3))
    )


_RelayStatus_Type.__name__ = "Integer32"
_RelayStatus_Object = MibTableColumn
relayStatus = _RelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 19, 1, 3),
    _RelayStatus_Type()
)
relayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayStatus.setStatus("current")


class _RelayAck_Type(Integer32):
    """Custom type relayAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("none", 2))
    )


_RelayAck_Type.__name__ = "Integer32"
_RelayAck_Object = MibTableColumn
relayAck = _RelayAck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 19, 1, 4),
    _RelayAck_Type()
)
relayAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayAck.setStatus("current")
_BridgeStatusTable_Object = MibTable
bridgeStatusTable = _BridgeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 20)
)
if mibBuilder.loadTexts:
    bridgeStatusTable.setStatus("current")
_BridgeStatusEntry_Object = MibTableRow
bridgeStatusEntry = _BridgeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 20, 1)
)
bridgeStatusEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "entryIndex"),
)
if mibBuilder.loadTexts:
    bridgeStatusEntry.setStatus("current")
_EntryIndex_Type = Integer32
_EntryIndex_Object = MibTableColumn
entryIndex = _EntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 20, 1, 1),
    _EntryIndex_Type()
)
entryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entryIndex.setStatus("current")
_Interface_Type = DisplayString
_Interface_Object = MibTableColumn
interface = _Interface_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 20, 1, 2),
    _Interface_Type()
)
interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interface.setStatus("current")
_MacAddr_Type = DisplayString
_MacAddr_Object = MibTableColumn
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 20, 1, 3),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddr.setStatus("current")
_SystemStatus_ObjectIdentity = ObjectIdentity
systemStatus = _SystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 25)
)
_CpuUsage_Type = Integer32
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 25, 1),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_MemTotalKB_Type = Integer32
_MemTotalKB_Object = MibScalar
memTotalKB = _MemTotalKB_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 25, 2),
    _MemTotalKB_Type()
)
memTotalKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalKB.setStatus("current")
_MemUsedKB_Type = Integer32
_MemUsedKB_Object = MibScalar
memUsedKB = _MemUsedKB_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 25, 3),
    _MemUsedKB_Type()
)
memUsedKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsedKB.setStatus("current")
_MemFreeKB_Type = Integer32
_MemFreeKB_Object = MibScalar
memFreeKB = _MemFreeKB_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 11, 25, 4),
    _MemFreeKB_Type()
)
memFreeKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFreeKB.setStatus("current")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13)
)
_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1)
)


class _MiscTelnetEnable_Type(Integer32):
    """Custom type miscTelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscTelnetEnable_Type.__name__ = "Integer32"
_MiscTelnetEnable_Object = MibScalar
miscTelnetEnable = _MiscTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 1),
    _MiscTelnetEnable_Type()
)
miscTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscTelnetEnable.setStatus("current")


class _MiscWebEnable_Type(Integer32):
    """Custom type miscWebEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscWebEnable_Type.__name__ = "Integer32"
_MiscWebEnable_Object = MibScalar
miscWebEnable = _MiscWebEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 2),
    _MiscWebEnable_Type()
)
miscWebEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscWebEnable.setStatus("current")


class _MiscSshEnable_Type(Integer32):
    """Custom type miscSshEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscSshEnable_Type.__name__ = "Integer32"
_MiscSshEnable_Object = MibScalar
miscSshEnable = _MiscSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 3),
    _MiscSshEnable_Type()
)
miscSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscSshEnable.setStatus("current")


class _MiscHttpsEnable_Type(Integer32):
    """Custom type miscHttpsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscHttpsEnable_Type.__name__ = "Integer32"
_MiscHttpsEnable_Object = MibScalar
miscHttpsEnable = _MiscHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 4),
    _MiscHttpsEnable_Type()
)
miscHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscHttpsEnable.setStatus("current")


class _MiscWlanEnable_Type(Integer32):
    """Custom type miscWlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscWlanEnable_Type.__name__ = "Integer32"
_MiscWlanEnable_Object = MibScalar
miscWlanEnable = _MiscWlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 7),
    _MiscWlanEnable_Type()
)
miscWlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscWlanEnable.setStatus("current")


class _MiscResetButtonEnable_Type(Integer32):
    """Custom type miscResetButtonEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscResetButtonEnable_Type.__name__ = "Integer32"
_MiscResetButtonEnable_Object = MibScalar
miscResetButtonEnable = _MiscResetButtonEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 8),
    _MiscResetButtonEnable_Type()
)
miscResetButtonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscResetButtonEnable.setStatus("current")


class _MiscAutoLogoutTimeout_Type(Integer32):
    """Custom type miscAutoLogoutTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MiscAutoLogoutTimeout_Type.__name__ = "Integer32"
_MiscAutoLogoutTimeout_Object = MibScalar
miscAutoLogoutTimeout = _MiscAutoLogoutTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 11),
    _MiscAutoLogoutTimeout_Type()
)
miscAutoLogoutTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscAutoLogoutTimeout.setStatus("current")


class _MiscMoxaServiceEnable_Type(Integer32):
    """Custom type miscMoxaServiceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscMoxaServiceEnable_Type.__name__ = "Integer32"
_MiscMoxaServiceEnable_Object = MibScalar
miscMoxaServiceEnable = _MiscMoxaServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 12),
    _MiscMoxaServiceEnable_Type()
)
miscMoxaServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscMoxaServiceEnable.setStatus("current")


class _MiscLanEnable_Type(Integer32):
    """Custom type miscLanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscLanEnable_Type.__name__ = "Integer32"
_MiscLanEnable_Object = MibScalar
miscLanEnable = _MiscLanEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 15),
    _MiscLanEnable_Type()
)
miscLanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscLanEnable.setStatus("current")


class _MiscAllowSpecialCharacters_Type(Integer32):
    """Custom type miscAllowSpecialCharacters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_MiscAllowSpecialCharacters_Type.__name__ = "Integer32"
_MiscAllowSpecialCharacters_Object = MibScalar
miscAllowSpecialCharacters = _MiscAllowSpecialCharacters_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 1, 22),
    _MiscAllowSpecialCharacters_Type()
)
miscAllowSpecialCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscAllowSpecialCharacters.setStatus("current")
_SaveAndReboot_ObjectIdentity = ObjectIdentity
saveAndReboot = _SaveAndReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 3)
)


class _ConfigChangeStatus_Type(Integer32):
    """Custom type configChangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unchanged", 0),
          ("changeSavedRequireReboot", 1),
          ("changedNotSaved", 2))
    )


_ConfigChangeStatus_Type.__name__ = "Integer32"
_ConfigChangeStatus_Object = MibScalar
configChangeStatus = _ConfigChangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 3, 1),
    _ConfigChangeStatus_Type()
)
configChangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configChangeStatus.setStatus("current")


class _SaveConfig_Type(Integer32):
    """Custom type saveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("savedConfig", 1)
    )


_SaveConfig_Type.__name__ = "Integer32"
_SaveConfig_Object = MibScalar
saveConfig = _SaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 3, 2),
    _SaveConfig_Type()
)
saveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveConfig.setStatus("current")


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 3, 3),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")
_AccountMgmt_ObjectIdentity = ObjectIdentity
accountMgmt = _AccountMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 6)
)


class _AccountMgmtPasswdStrengthCheck_Type(Integer32):
    """Custom type accountMgmtPasswdStrengthCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AccountMgmtPasswdStrengthCheck_Type.__name__ = "Integer32"
_AccountMgmtPasswdStrengthCheck_Object = MibScalar
accountMgmtPasswdStrengthCheck = _AccountMgmtPasswdStrengthCheck_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 6, 1),
    _AccountMgmtPasswdStrengthCheck_Type()
)
accountMgmtPasswdStrengthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountMgmtPasswdStrengthCheck.setStatus("current")


class _AccountMgmtPasswdLength_Type(Integer32):
    """Custom type accountMgmtPasswdLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 16),
    )


_AccountMgmtPasswdLength_Type.__name__ = "Integer32"
_AccountMgmtPasswdLength_Object = MibScalar
accountMgmtPasswdLength = _AccountMgmtPasswdLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 6, 2),
    _AccountMgmtPasswdLength_Type()
)
accountMgmtPasswdLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountMgmtPasswdLength.setStatus("current")


class _AccountMgmtPasswdExpiredTime_Type(Integer32):
    """Custom type accountMgmtPasswdExpiredTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_AccountMgmtPasswdExpiredTime_Type.__name__ = "Integer32"
_AccountMgmtPasswdExpiredTime_Object = MibScalar
accountMgmtPasswdExpiredTime = _AccountMgmtPasswdExpiredTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 6, 3),
    _AccountMgmtPasswdExpiredTime_Type()
)
accountMgmtPasswdExpiredTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountMgmtPasswdExpiredTime.setStatus("current")


class _AccountMgmtRetry_Type(Integer32):
    """Custom type accountMgmtRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AccountMgmtRetry_Type.__name__ = "Integer32"
_AccountMgmtRetry_Object = MibScalar
accountMgmtRetry = _AccountMgmtRetry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 6, 4),
    _AccountMgmtRetry_Type()
)
accountMgmtRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountMgmtRetry.setStatus("current")


class _AccountMgmtLockTime_Type(Integer32):
    """Custom type accountMgmtLockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AccountMgmtLockTime_Type.__name__ = "Integer32"
_AccountMgmtLockTime_Object = MibScalar
accountMgmtLockTime = _AccountMgmtLockTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 6, 5),
    _AccountMgmtLockTime_Type()
)
accountMgmtLockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountMgmtLockTime.setStatus("current")
_AccountTable_Object = MibTable
accountTable = _AccountTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7)
)
if mibBuilder.loadTexts:
    accountTable.setStatus("current")
_AccountEntry_Object = MibTableRow
accountEntry = _AccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1)
)
accountEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "accountIndex"),
)
if mibBuilder.loadTexts:
    accountEntry.setStatus("current")


class _AccountIndex_Type(Integer32):
    """Custom type accountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AccountIndex_Type.__name__ = "Integer32"
_AccountIndex_Object = MibTableColumn
accountIndex = _AccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1, 1),
    _AccountIndex_Type()
)
accountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountIndex.setStatus("current")


class _AccountActive_Type(Integer32):
    """Custom type accountActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AccountActive_Type.__name__ = "Integer32"
_AccountActive_Object = MibTableColumn
accountActive = _AccountActive_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1, 2),
    _AccountActive_Type()
)
accountActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountActive.setStatus("current")
_AccountUsername_Type = DisplayString
_AccountUsername_Object = MibTableColumn
accountUsername = _AccountUsername_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1, 3),
    _AccountUsername_Type()
)
accountUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountUsername.setStatus("current")


class _AccountGroup_Type(Integer32):
    """Custom type accountGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("user", 2))
    )


_AccountGroup_Type.__name__ = "Integer32"
_AccountGroup_Object = MibTableColumn
accountGroup = _AccountGroup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1, 5),
    _AccountGroup_Type()
)
accountGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountGroup.setStatus("current")


class _AccountAccessHttp_Type(Integer32):
    """Custom type accountAccessHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AccountAccessHttp_Type.__name__ = "Integer32"
_AccountAccessHttp_Object = MibTableColumn
accountAccessHttp = _AccountAccessHttp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1, 7),
    _AccountAccessHttp_Type()
)
accountAccessHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountAccessHttp.setStatus("current")


class _AccountAccessConsole_Type(Integer32):
    """Custom type accountAccessConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AccountAccessConsole_Type.__name__ = "Integer32"
_AccountAccessConsole_Object = MibTableColumn
accountAccessConsole = _AccountAccessConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1, 8),
    _AccountAccessConsole_Type()
)
accountAccessConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountAccessConsole.setStatus("current")


class _AccountAccessMoxaService_Type(Integer32):
    """Custom type accountAccessMoxaService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AccountAccessMoxaService_Type.__name__ = "Integer32"
_AccountAccessMoxaService_Object = MibTableColumn
accountAccessMoxaService = _AccountAccessMoxaService_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1, 9),
    _AccountAccessMoxaService_Type()
)
accountAccessMoxaService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountAccessMoxaService.setStatus("current")


class _AccountAccessDiag_Type(Integer32):
    """Custom type accountAccessDiag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AccountAccessDiag_Type.__name__ = "Integer32"
_AccountAccessDiag_Object = MibTableColumn
accountAccessDiag = _AccountAccessDiag_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 7, 1, 10),
    _AccountAccessDiag_Type()
)
accountAccessDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountAccessDiag.setStatus("current")
_ConfigEncrypt_ObjectIdentity = ObjectIdentity
configEncrypt = _ConfigEncrypt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 8)
)


class _ConfigEncryptEnable_Type(Integer32):
    """Custom type configEncryptEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConfigEncryptEnable_Type.__name__ = "Integer32"
_ConfigEncryptEnable_Object = MibScalar
configEncryptEnable = _ConfigEncryptEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 8, 1),
    _ConfigEncryptEnable_Type()
)
configEncryptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEncryptEnable.setStatus("current")
_ConfigEncryptPassword_Type = DisplayString
_ConfigEncryptPassword_Object = MibScalar
configEncryptPassword = _ConfigEncryptPassword_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 8, 2),
    _ConfigEncryptPassword_Type()
)
configEncryptPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEncryptPassword.setStatus("current")
_Consoles_ObjectIdentity = ObjectIdentity
consoles = _Consoles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9)
)


class _ConsolesEthTelnetEnable_Type(Integer32):
    """Custom type consolesEthTelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesEthTelnetEnable_Type.__name__ = "Integer32"
_ConsolesEthTelnetEnable_Object = MibScalar
consolesEthTelnetEnable = _ConsolesEthTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 11),
    _ConsolesEthTelnetEnable_Type()
)
consolesEthTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesEthTelnetEnable.setStatus("current")


class _ConsolesEthWebEnable_Type(Integer32):
    """Custom type consolesEthWebEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesEthWebEnable_Type.__name__ = "Integer32"
_ConsolesEthWebEnable_Object = MibScalar
consolesEthWebEnable = _ConsolesEthWebEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 12),
    _ConsolesEthWebEnable_Type()
)
consolesEthWebEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesEthWebEnable.setStatus("current")


class _ConsolesEthSshEnable_Type(Integer32):
    """Custom type consolesEthSshEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesEthSshEnable_Type.__name__ = "Integer32"
_ConsolesEthSshEnable_Object = MibScalar
consolesEthSshEnable = _ConsolesEthSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 13),
    _ConsolesEthSshEnable_Type()
)
consolesEthSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesEthSshEnable.setStatus("current")


class _ConsolesEthHttpsEnable_Type(Integer32):
    """Custom type consolesEthHttpsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesEthHttpsEnable_Type.__name__ = "Integer32"
_ConsolesEthHttpsEnable_Object = MibScalar
consolesEthHttpsEnable = _ConsolesEthHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 14),
    _ConsolesEthHttpsEnable_Type()
)
consolesEthHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesEthHttpsEnable.setStatus("current")


class _ConsolesEthSnmpEnable_Type(Integer32):
    """Custom type consolesEthSnmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesEthSnmpEnable_Type.__name__ = "Integer32"
_ConsolesEthSnmpEnable_Object = MibScalar
consolesEthSnmpEnable = _ConsolesEthSnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 15),
    _ConsolesEthSnmpEnable_Type()
)
consolesEthSnmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesEthSnmpEnable.setStatus("current")


class _ConsolesEthMoxaServiceEnable_Type(Integer32):
    """Custom type consolesEthMoxaServiceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesEthMoxaServiceEnable_Type.__name__ = "Integer32"
_ConsolesEthMoxaServiceEnable_Object = MibScalar
consolesEthMoxaServiceEnable = _ConsolesEthMoxaServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 16),
    _ConsolesEthMoxaServiceEnable_Type()
)
consolesEthMoxaServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesEthMoxaServiceEnable.setStatus("current")
_ConsolesWlanTelnetEnableTable_Object = MibTable
consolesWlanTelnetEnableTable = _ConsolesWlanTelnetEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 31)
)
if mibBuilder.loadTexts:
    consolesWlanTelnetEnableTable.setStatus("current")
_ConsolesWlanTelnetEnableEntry_Object = MibTableRow
consolesWlanTelnetEnableEntry = _ConsolesWlanTelnetEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 31, 1)
)
consolesWlanTelnetEnableEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "consolesWlanTelnetEnableIndex"),
)
if mibBuilder.loadTexts:
    consolesWlanTelnetEnableEntry.setStatus("current")


class _ConsolesWlanTelnetEnableIndex_Type(Integer32):
    """Custom type consolesWlanTelnetEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_ConsolesWlanTelnetEnableIndex_Type.__name__ = "Integer32"
_ConsolesWlanTelnetEnableIndex_Object = MibTableColumn
consolesWlanTelnetEnableIndex = _ConsolesWlanTelnetEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 31, 1, 1),
    _ConsolesWlanTelnetEnableIndex_Type()
)
consolesWlanTelnetEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolesWlanTelnetEnableIndex.setStatus("current")


class _ConsolesWlanTelnetEnableData_Type(Integer32):
    """Custom type consolesWlanTelnetEnableData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesWlanTelnetEnableData_Type.__name__ = "Integer32"
_ConsolesWlanTelnetEnableData_Object = MibTableColumn
consolesWlanTelnetEnableData = _ConsolesWlanTelnetEnableData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 31, 1, 2),
    _ConsolesWlanTelnetEnableData_Type()
)
consolesWlanTelnetEnableData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesWlanTelnetEnableData.setStatus("current")
_ConsolesWlanWebEnableTable_Object = MibTable
consolesWlanWebEnableTable = _ConsolesWlanWebEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 32)
)
if mibBuilder.loadTexts:
    consolesWlanWebEnableTable.setStatus("current")
_ConsolesWlanWebEnableEntry_Object = MibTableRow
consolesWlanWebEnableEntry = _ConsolesWlanWebEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 32, 1)
)
consolesWlanWebEnableEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "consolesWlanWebEnableIndex"),
)
if mibBuilder.loadTexts:
    consolesWlanWebEnableEntry.setStatus("current")


class _ConsolesWlanWebEnableIndex_Type(Integer32):
    """Custom type consolesWlanWebEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_ConsolesWlanWebEnableIndex_Type.__name__ = "Integer32"
_ConsolesWlanWebEnableIndex_Object = MibTableColumn
consolesWlanWebEnableIndex = _ConsolesWlanWebEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 32, 1, 1),
    _ConsolesWlanWebEnableIndex_Type()
)
consolesWlanWebEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolesWlanWebEnableIndex.setStatus("current")


class _ConsolesWlanWebEnableData_Type(Integer32):
    """Custom type consolesWlanWebEnableData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesWlanWebEnableData_Type.__name__ = "Integer32"
_ConsolesWlanWebEnableData_Object = MibTableColumn
consolesWlanWebEnableData = _ConsolesWlanWebEnableData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 32, 1, 2),
    _ConsolesWlanWebEnableData_Type()
)
consolesWlanWebEnableData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesWlanWebEnableData.setStatus("current")
_ConsolesWlanSshEnableTable_Object = MibTable
consolesWlanSshEnableTable = _ConsolesWlanSshEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 33)
)
if mibBuilder.loadTexts:
    consolesWlanSshEnableTable.setStatus("current")
_ConsolesWlanSshEnableEntry_Object = MibTableRow
consolesWlanSshEnableEntry = _ConsolesWlanSshEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 33, 1)
)
consolesWlanSshEnableEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "consolesWlanSshEnableIndex"),
)
if mibBuilder.loadTexts:
    consolesWlanSshEnableEntry.setStatus("current")


class _ConsolesWlanSshEnableIndex_Type(Integer32):
    """Custom type consolesWlanSshEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_ConsolesWlanSshEnableIndex_Type.__name__ = "Integer32"
_ConsolesWlanSshEnableIndex_Object = MibTableColumn
consolesWlanSshEnableIndex = _ConsolesWlanSshEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 33, 1, 1),
    _ConsolesWlanSshEnableIndex_Type()
)
consolesWlanSshEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolesWlanSshEnableIndex.setStatus("current")


class _ConsolesWlanSshEnableData_Type(Integer32):
    """Custom type consolesWlanSshEnableData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesWlanSshEnableData_Type.__name__ = "Integer32"
_ConsolesWlanSshEnableData_Object = MibTableColumn
consolesWlanSshEnableData = _ConsolesWlanSshEnableData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 33, 1, 2),
    _ConsolesWlanSshEnableData_Type()
)
consolesWlanSshEnableData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesWlanSshEnableData.setStatus("current")
_ConsolesWlanHttpsEnableTable_Object = MibTable
consolesWlanHttpsEnableTable = _ConsolesWlanHttpsEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 34)
)
if mibBuilder.loadTexts:
    consolesWlanHttpsEnableTable.setStatus("current")
_ConsolesWlanHttpsEnableEntry_Object = MibTableRow
consolesWlanHttpsEnableEntry = _ConsolesWlanHttpsEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 34, 1)
)
consolesWlanHttpsEnableEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "consolesWlanHttpsEnableIndex"),
)
if mibBuilder.loadTexts:
    consolesWlanHttpsEnableEntry.setStatus("current")


class _ConsolesWlanHttpsEnableIndex_Type(Integer32):
    """Custom type consolesWlanHttpsEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_ConsolesWlanHttpsEnableIndex_Type.__name__ = "Integer32"
_ConsolesWlanHttpsEnableIndex_Object = MibTableColumn
consolesWlanHttpsEnableIndex = _ConsolesWlanHttpsEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 34, 1, 1),
    _ConsolesWlanHttpsEnableIndex_Type()
)
consolesWlanHttpsEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolesWlanHttpsEnableIndex.setStatus("current")


class _ConsolesWlanHttpsEnableData_Type(Integer32):
    """Custom type consolesWlanHttpsEnableData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesWlanHttpsEnableData_Type.__name__ = "Integer32"
_ConsolesWlanHttpsEnableData_Object = MibTableColumn
consolesWlanHttpsEnableData = _ConsolesWlanHttpsEnableData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 34, 1, 2),
    _ConsolesWlanHttpsEnableData_Type()
)
consolesWlanHttpsEnableData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesWlanHttpsEnableData.setStatus("current")
_ConsolesWlanSnmpEnableTable_Object = MibTable
consolesWlanSnmpEnableTable = _ConsolesWlanSnmpEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 35)
)
if mibBuilder.loadTexts:
    consolesWlanSnmpEnableTable.setStatus("current")
_ConsolesWlanSnmpEnableEntry_Object = MibTableRow
consolesWlanSnmpEnableEntry = _ConsolesWlanSnmpEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 35, 1)
)
consolesWlanSnmpEnableEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "consolesWlanSnmpEnableIndex"),
)
if mibBuilder.loadTexts:
    consolesWlanSnmpEnableEntry.setStatus("current")


class _ConsolesWlanSnmpEnableIndex_Type(Integer32):
    """Custom type consolesWlanSnmpEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_ConsolesWlanSnmpEnableIndex_Type.__name__ = "Integer32"
_ConsolesWlanSnmpEnableIndex_Object = MibTableColumn
consolesWlanSnmpEnableIndex = _ConsolesWlanSnmpEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 35, 1, 1),
    _ConsolesWlanSnmpEnableIndex_Type()
)
consolesWlanSnmpEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolesWlanSnmpEnableIndex.setStatus("current")


class _ConsolesWlanSnmpEnableData_Type(Integer32):
    """Custom type consolesWlanSnmpEnableData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesWlanSnmpEnableData_Type.__name__ = "Integer32"
_ConsolesWlanSnmpEnableData_Object = MibTableColumn
consolesWlanSnmpEnableData = _ConsolesWlanSnmpEnableData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 35, 1, 2),
    _ConsolesWlanSnmpEnableData_Type()
)
consolesWlanSnmpEnableData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesWlanSnmpEnableData.setStatus("current")
_ConsolesWlanMoxaServiceEnableTable_Object = MibTable
consolesWlanMoxaServiceEnableTable = _ConsolesWlanMoxaServiceEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 36)
)
if mibBuilder.loadTexts:
    consolesWlanMoxaServiceEnableTable.setStatus("current")
_ConsolesWlanMoxaServiceEnableEntry_Object = MibTableRow
consolesWlanMoxaServiceEnableEntry = _ConsolesWlanMoxaServiceEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 36, 1)
)
consolesWlanMoxaServiceEnableEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "consolesWlanMoxaServiceEnableIndex"),
)
if mibBuilder.loadTexts:
    consolesWlanMoxaServiceEnableEntry.setStatus("current")


class _ConsolesWlanMoxaServiceEnableIndex_Type(Integer32):
    """Custom type consolesWlanMoxaServiceEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_ConsolesWlanMoxaServiceEnableIndex_Type.__name__ = "Integer32"
_ConsolesWlanMoxaServiceEnableIndex_Object = MibTableColumn
consolesWlanMoxaServiceEnableIndex = _ConsolesWlanMoxaServiceEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 36, 1, 1),
    _ConsolesWlanMoxaServiceEnableIndex_Type()
)
consolesWlanMoxaServiceEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolesWlanMoxaServiceEnableIndex.setStatus("current")


class _ConsolesWlanMoxaServiceEnableData_Type(Integer32):
    """Custom type consolesWlanMoxaServiceEnableData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesWlanMoxaServiceEnableData_Type.__name__ = "Integer32"
_ConsolesWlanMoxaServiceEnableData_Object = MibTableColumn
consolesWlanMoxaServiceEnableData = _ConsolesWlanMoxaServiceEnableData_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 9, 36, 1, 2),
    _ConsolesWlanMoxaServiceEnableData_Type()
)
consolesWlanMoxaServiceEnableData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesWlanMoxaServiceEnableData.setStatus("current")
_ConsolesAccessibleNet_ObjectIdentity = ObjectIdentity
consolesAccessibleNet = _ConsolesAccessibleNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 10)
)


class _ConsolesAccessibleNetAccessibleNet_Type(Integer32):
    """Custom type consolesAccessibleNetAccessibleNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesAccessibleNetAccessibleNet_Type.__name__ = "Integer32"
_ConsolesAccessibleNetAccessibleNet_Object = MibScalar
consolesAccessibleNetAccessibleNet = _ConsolesAccessibleNetAccessibleNet_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 10, 1),
    _ConsolesAccessibleNetAccessibleNet_Type()
)
consolesAccessibleNetAccessibleNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesAccessibleNetAccessibleNet.setStatus("current")


class _ConsolesAccessibleNetAccessibleNetPolicy_Type(Integer32):
    """Custom type consolesAccessibleNetAccessibleNetPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2))
    )


_ConsolesAccessibleNetAccessibleNetPolicy_Type.__name__ = "Integer32"
_ConsolesAccessibleNetAccessibleNetPolicy_Object = MibScalar
consolesAccessibleNetAccessibleNetPolicy = _ConsolesAccessibleNetAccessibleNetPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 10, 2),
    _ConsolesAccessibleNetAccessibleNetPolicy_Type()
)
consolesAccessibleNetAccessibleNetPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesAccessibleNetAccessibleNetPolicy.setStatus("current")
_ConsolesAccessibleNetTable_Object = MibTable
consolesAccessibleNetTable = _ConsolesAccessibleNetTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 11)
)
if mibBuilder.loadTexts:
    consolesAccessibleNetTable.setStatus("current")
_ConsolesAccessibleNetEntry_Object = MibTableRow
consolesAccessibleNetEntry = _ConsolesAccessibleNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 11, 1)
)
consolesAccessibleNetEntry.setIndexNames(
    (0, "MOXA-AWK4131A-MIB", "consolesAccessibleNetIndex"),
)
if mibBuilder.loadTexts:
    consolesAccessibleNetEntry.setStatus("current")


class _ConsolesAccessibleNetIndex_Type(Integer32):
    """Custom type consolesAccessibleNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ConsolesAccessibleNetIndex_Type.__name__ = "Integer32"
_ConsolesAccessibleNetIndex_Object = MibTableColumn
consolesAccessibleNetIndex = _ConsolesAccessibleNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 11, 1, 1),
    _ConsolesAccessibleNetIndex_Type()
)
consolesAccessibleNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consolesAccessibleNetIndex.setStatus("current")


class _ConsolesAccessibleNetActive_Type(Integer32):
    """Custom type consolesAccessibleNetActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ConsolesAccessibleNetActive_Type.__name__ = "Integer32"
_ConsolesAccessibleNetActive_Object = MibTableColumn
consolesAccessibleNetActive = _ConsolesAccessibleNetActive_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 11, 1, 2),
    _ConsolesAccessibleNetActive_Type()
)
consolesAccessibleNetActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesAccessibleNetActive.setStatus("current")
_ConsolesAccessibleNetSrcIP_Type = IpAddress
_ConsolesAccessibleNetSrcIP_Object = MibTableColumn
consolesAccessibleNetSrcIP = _ConsolesAccessibleNetSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 11, 1, 3),
    _ConsolesAccessibleNetSrcIP_Type()
)
consolesAccessibleNetSrcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesAccessibleNetSrcIP.setStatus("current")
_ConsolesAccessibleNetSrcMask_Type = IpAddress
_ConsolesAccessibleNetSrcMask_Object = MibTableColumn
consolesAccessibleNetSrcMask = _ConsolesAccessibleNetSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 11, 1, 4),
    _ConsolesAccessibleNetSrcMask_Type()
)
consolesAccessibleNetSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolesAccessibleNetSrcMask.setStatus("current")
_UserWebCertificate_ObjectIdentity = ObjectIdentity
userWebCertificate = _UserWebCertificate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 13)
)


class _UserWebCertificateEnable_Type(Integer32):
    """Custom type userWebCertificateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_UserWebCertificateEnable_Type.__name__ = "Integer32"
_UserWebCertificateEnable_Object = MibScalar
userWebCertificateEnable = _UserWebCertificateEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 1, 13, 13, 1),
    _UserWebCertificateEnable_Type()
)
userWebCertificateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userWebCertificateEnable.setStatus("current")

# Managed Objects groups


# Notification objects

configChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 0, 1)
)
if mibBuilder.loadTexts:
    configChange.setStatus(
        "current"
    )

powerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 0, 2)
)
powerOn.setObjects(
    ("MOXA-AWK4131A-MIB", "powerInputIndex")
)
if mibBuilder.loadTexts:
    powerOn.setStatus(
        "current"
    )

powerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 0, 3)
)
powerOff.setObjects(
    ("MOXA-AWK4131A-MIB", "powerInputIndex")
)
if mibBuilder.loadTexts:
    powerOff.setStatus(
        "current"
    )

diOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 0, 4)
)
diOn.setObjects(
    ("MOXA-AWK4131A-MIB", "diIndex")
)
if mibBuilder.loadTexts:
    diOn.setStatus(
        "current"
    )

diOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 0, 5)
)
diOff.setObjects(
    ("MOXA-AWK4131A-MIB", "diIndex")
)
if mibBuilder.loadTexts:
    diOff.setStatus(
        "current"
    )

clientJoined = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 0, 6)
)
clientJoined.setObjects(
    ("MOXA-AWK4131A-MIB", "wlanClientMAC")
)
if mibBuilder.loadTexts:
    clientJoined.setStatus(
        "current"
    )

clientLeft = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 15, 34, 0, 7)
)
clientLeft.setObjects(
    ("MOXA-AWK4131A-MIB", "wlanClientMAC")
)
if mibBuilder.loadTexts:
    clientLeft.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-AWK4131A-MIB",
    **{"PortList": PortList,
       "moxa": moxa,
       "industrialWirelessLan": industrialWirelessLan,
       "awk4131A": awk4131A,
       "awkTraps": awkTraps,
       "configChange": configChange,
       "powerOn": powerOn,
       "powerOff": powerOff,
       "diOn": diOn,
       "diOff": diOff,
       "clientJoined": clientJoined,
       "clientLeft": clientLeft,
       "swMgmt": swMgmt,
       "overview": overview,
       "overviewModelName": overviewModelName,
       "overviewDeviceName": overviewDeviceName,
       "overviewSerialNumber": overviewSerialNumber,
       "overviewUpTime": overviewUpTime,
       "overviewFirmwareVersion": overviewFirmwareVersion,
       "overviewMacAddress": overviewMacAddress,
       "overviewDeviceLocation": overviewDeviceLocation,
       "overviewDeviceDescription": overviewDeviceDescription,
       "overviewDeviceContactInfo": overviewDeviceContactInfo,
       "overviewWebLoginMessage": overviewWebLoginMessage,
       "overviewWebLoginFailMessage": overviewWebLoginFailMessage,
       "basic": basic,
       "netDev": netDev,
       "netDevDhcpEnable": netDevDhcpEnable,
       "netDevIpV4Addr": netDevIpV4Addr,
       "netDevIpV4Mask": netDevIpV4Mask,
       "netDevIpV4Gateway": netDevIpV4Gateway,
       "netDevIpV4DnsTable": netDevIpV4DnsTable,
       "netDevIpV4DnsEntry": netDevIpV4DnsEntry,
       "netDevIpV4DnsIndex": netDevIpV4DnsIndex,
       "netDevIpV4DnsData": netDevIpV4DnsData,
       "time": time,
       "timeNow": timeNow,
       "timeTimeZone": timeTimeZone,
       "timeTimeServerTable": timeTimeServerTable,
       "timeTimeServerEntry": timeTimeServerEntry,
       "timeTimeServerIndex": timeTimeServerIndex,
       "timeTimeServerData": timeTimeServerData,
       "timeQueryPeriod": timeQueryPeriod,
       "timeDaylightSavingEnable": timeDaylightSavingEnable,
       "timeDaylightSavingStartMonth": timeDaylightSavingStartMonth,
       "timeDaylightSavingStartWeekIndex": timeDaylightSavingStartWeekIndex,
       "timeDaylightSavingStartWeekday": timeDaylightSavingStartWeekday,
       "timeDaylightSavingStartHour": timeDaylightSavingStartHour,
       "timeDaylightSavingStartMin": timeDaylightSavingStartMin,
       "timeDaylightSavingStopMonth": timeDaylightSavingStopMonth,
       "timeDaylightSavingStopWeekIndex": timeDaylightSavingStopWeekIndex,
       "timeDaylightSavingStopWeekday": timeDaylightSavingStopWeekday,
       "timeDaylightSavingStophour": timeDaylightSavingStophour,
       "timeDaylightSavingStopMin": timeDaylightSavingStopMin,
       "timeDaylightSavingTimeOffset": timeDaylightSavingTimeOffset,
       "timeNtpOption": timeNtpOption,
       "netDevWlan": netDevWlan,
       "netDevWlanDhcpEnable": netDevWlanDhcpEnable,
       "netDevWlanIpV4Addr": netDevWlanIpV4Addr,
       "netDevWlanIpV4Mask": netDevWlanIpV4Mask,
       "netDevWlanIpV4Gateway": netDevWlanIpV4Gateway,
       "netDevWlanIpV4DnsTable": netDevWlanIpV4DnsTable,
       "netDevWlanIpV4DnsEntry": netDevWlanIpV4DnsEntry,
       "netDevWlanIpV4DnsIndex": netDevWlanIpV4DnsIndex,
       "netDevWlanIpV4DnsData": netDevWlanIpV4DnsData,
       "netDevLan": netDevLan,
       "netDevLanDhcpEnable": netDevLanDhcpEnable,
       "netDevLanIpV4Addr": netDevLanIpV4Addr,
       "netDevLanIpV4Mask": netDevLanIpV4Mask,
       "wireless": wireless,
       "devTable": devTable,
       "devEntry": devEntry,
       "devIndex": devIndex,
       "devChannelA": devChannelA,
       "devChannelB": devChannelB,
       "devChannelG": devChannelG,
       "devChannelListA": devChannelListA,
       "devChannelListB": devChannelListB,
       "devChannelListG": devChannelListG,
       "devRfType": devRfType,
       "devCountryCode": devCountryCode,
       "devTXrateA": devTXrateA,
       "devTXrateB": devTXrateB,
       "devTXrateG": devTXrateG,
       "devTXrateBG": devTXrateBG,
       "devBeaconInterval": devBeaconInterval,
       "devDTIMinterval": devDTIMinterval,
       "devFragThresh": devFragThresh,
       "devRtsthreshold": devRtsthreshold,
       "devTxRange": devTxRange,
       "devTxAntenna": devTxAntenna,
       "devWMMenable": devWMMenable,
       "devOperationmode": devOperationmode,
       "devChannelWidth": devChannelWidth,
       "devChannelN24GHz": devChannelN24GHz,
       "devChannelN5GHz": devChannelN5GHz,
       "devTxRateN": devTxRateN,
       "devMulticastRateA": devMulticastRateA,
       "devMulticastRateB": devMulticastRateB,
       "devMulticastRateG": devMulticastRateG,
       "devMulticastRateBG": devMulticastRateBG,
       "devMulticastRateBGN": devMulticastRateBGN,
       "devMulticastRateAN": devMulticastRateAN,
       "devMulticastRateN": devMulticastRateN,
       "devTxPowerdBm": devTxPowerdBm,
       "devMacClone": devMacClone,
       "devTXrateMin": devTXrateMin,
       "devInactiveTimeout": devInactiveTimeout,
       "devProxyArp": devProxyArp,
       "devMacCloneMethod": devMacCloneMethod,
       "devMacCloneStaticMac": devMacCloneStaticMac,
       "devRemoteConnCheckEnable": devRemoteConnCheckEnable,
       "devRemoteConnCheckReconnWLAN": devRemoteConnCheckReconnWLAN,
       "devRemoteConnCheckRebootDevice": devRemoteConnCheckRebootDevice,
       "devRemoteConnCheckRemoteHost": devRemoteConnCheckRemoteHost,
       "devRemoteConnCheckCheckInterval": devRemoteConnCheckCheckInterval,
       "devRemoteConnCheckCheckTimeout": devRemoteConnCheckCheckTimeout,
       "devRemoteConnCheckRetryCount": devRemoteConnCheckRetryCount,
       "devRemoteConnCheckRetryInterval": devRemoteConnCheckRetryInterval,
       "devRemoteConnCheckRebootCount": devRemoteConnCheckRebootCount,
       "vapTable": vapTable,
       "vapEntry": vapEntry,
       "vapIndex": vapIndex,
       "vapSSID": vapSSID,
       "vapSignalLV": vapSignalLV,
       "vapSsidBroadcast": vapSsidBroadcast,
       "vapWdsEnable": vapWdsEnable,
       "vapAPfunctionality": vapAPfunctionality,
       "vapAuthType": vapAuthType,
       "vapWEPauth": vapWEPauth,
       "vapWEPtype": vapWEPtype,
       "vapWEPlen": vapWEPlen,
       "vapWEPkeyIndex": vapWEPkeyIndex,
       "vapWPAtype": vapWPAtype,
       "vapEapolVer": vapEapolVer,
       "vapWpaEncrypt": vapWpaEncrypt,
       "vap1stAuthServerIPv4Addr": vap1stAuthServerIPv4Addr,
       "vap1stAuthServerPort": vap1stAuthServerPort,
       "vap2ndAuthServerIPv4Addr": vap2ndAuthServerIPv4Addr,
       "vap2ndAuthServerPort": vap2ndAuthServerPort,
       "vapCertInfo": vapCertInfo,
       "vapEapProto": vapEapProto,
       "vapEAPanonymous": vapEAPanonymous,
       "vapTtlsInner": vapTtlsInner,
       "vapPeapInner": vapPeapInner,
       "vapEapUser": vapEapUser,
       "vapRekey": vapRekey,
       "vapBssidClient": vapBssidClient,
       "vapClientIsolation": vapClientIsolation,
       "vapClientIsolationGateway": vapClientIsolationGateway,
       "vapClientIsolationNetMask": vapClientIsolationNetMask,
       "vapMgmtEncryption": vapMgmtEncryption,
       "vapAerolink-ap": vapAerolink_ap,
       "vapClientIsolationSubnetType": vapClientIsolationSubnetType,
       "vapClntIsoEnableRule1": vapClntIsoEnableRule1,
       "vapClntIsoHostRule1": vapClntIsoHostRule1,
       "vapClntIsoNetmaskRule1": vapClntIsoNetmaskRule1,
       "vapClntIsoProtoRule1": vapClntIsoProtoRule1,
       "vapClntIsoPortStartRule1": vapClntIsoPortStartRule1,
       "vapClntIsoPortEndRule1": vapClntIsoPortEndRule1,
       "vapClntIsoEnableRule2": vapClntIsoEnableRule2,
       "vapClntIsoHostRule2": vapClntIsoHostRule2,
       "vapClntIsoNetmaskRule2": vapClntIsoNetmaskRule2,
       "vapClntIsoProtoRule2": vapClntIsoProtoRule2,
       "vapClntIsoPortStartRule2": vapClntIsoPortStartRule2,
       "vapClntIsoPortEndRule2": vapClntIsoPortEndRule2,
       "vapClntIsoEnableRule3": vapClntIsoEnableRule3,
       "vapClntIsoHostRule3": vapClntIsoHostRule3,
       "vapClntIsoNetmaskRule3": vapClntIsoNetmaskRule3,
       "vapClntIsoProtoRule3": vapClntIsoProtoRule3,
       "vapClntIsoPortStartRule3": vapClntIsoPortStartRule3,
       "vapClntIsoPortEndRule3": vapClntIsoPortEndRule3,
       "vapClntIsoEnableRule4": vapClntIsoEnableRule4,
       "vapClntIsoHostRule4": vapClntIsoHostRule4,
       "vapClntIsoNetmaskRule4": vapClntIsoNetmaskRule4,
       "vapClntIsoProtoRule4": vapClntIsoProtoRule4,
       "vapClntIsoPortStartRule4": vapClntIsoPortStartRule4,
       "vapClntIsoPortEndRule4": vapClntIsoPortEndRule4,
       "vapClntIsoEnableRule5": vapClntIsoEnableRule5,
       "vapClntIsoHostRule5": vapClntIsoHostRule5,
       "vapClntIsoNetmaskRule5": vapClntIsoNetmaskRule5,
       "vapClntIsoProtoRule5": vapClntIsoProtoRule5,
       "vapClntIsoPortStartRule5": vapClntIsoPortStartRule5,
       "vapClntIsoPortEndRule5": vapClntIsoPortEndRule5,
       "vapClntIsoEnableRule6": vapClntIsoEnableRule6,
       "vapClntIsoHostRule6": vapClntIsoHostRule6,
       "vapClntIsoNetmaskRule6": vapClntIsoNetmaskRule6,
       "vapClntIsoProtoRule6": vapClntIsoProtoRule6,
       "vapClntIsoPortStartRule6": vapClntIsoPortStartRule6,
       "vapClntIsoPortEndRule6": vapClntIsoPortEndRule6,
       "vapClntIsoEnableRule7": vapClntIsoEnableRule7,
       "vapClntIsoHostRule7": vapClntIsoHostRule7,
       "vapClntIsoNetmaskRule7": vapClntIsoNetmaskRule7,
       "vapClntIsoProtoRule7": vapClntIsoProtoRule7,
       "vapClntIsoPortStartRule7": vapClntIsoPortStartRule7,
       "vapClntIsoPortEndRule7": vapClntIsoPortEndRule7,
       "vapClntIsoEnableRule8": vapClntIsoEnableRule8,
       "vapClntIsoHostRule8": vapClntIsoHostRule8,
       "vapClntIsoNetmaskRule8": vapClntIsoNetmaskRule8,
       "vapClntIsoProtoRule8": vapClntIsoProtoRule8,
       "vapClntIsoPortStartRule8": vapClntIsoPortStartRule8,
       "vapClntIsoPortEndRule8": vapClntIsoPortEndRule8,
       "wdsTable": wdsTable,
       "wdsEntry": wdsEntry,
       "wdsIndex": wdsIndex,
       "wdsWdsEnable": wdsWdsEnable,
       "wdsWdsPeerMac": wdsWdsPeerMac,
       "certWlanTable": certWlanTable,
       "certWlanEntry": certWlanEntry,
       "certWlanIndex": certWlanIndex,
       "certWlanIssueTo": certWlanIssueTo,
       "certWlanIssueBy": certWlanIssueBy,
       "certWlanExpireDate": certWlanExpireDate,
       "turboRoamingTable": turboRoamingTable,
       "turboRoamingEntry": turboRoamingEntry,
       "turboRoamingIndex": turboRoamingIndex,
       "turboRoamingEnable": turboRoamingEnable,
       "turboRoamingChannelA1": turboRoamingChannelA1,
       "turboRoamingChannelA2": turboRoamingChannelA2,
       "turboRoamingChannelA3": turboRoamingChannelA3,
       "turboRoamingChannelB1": turboRoamingChannelB1,
       "turboRoamingChannelB2": turboRoamingChannelB2,
       "turboRoamingChannelB3": turboRoamingChannelB3,
       "turboRoamingChannelG1": turboRoamingChannelG1,
       "turboRoamingChannelG2": turboRoamingChannelG2,
       "turboRoamingChannelG3": turboRoamingChannelG3,
       "turboRoamingChannelBG1": turboRoamingChannelBG1,
       "turboRoamingChannelBG2": turboRoamingChannelBG2,
       "turboRoamingChannelBG3": turboRoamingChannelBG3,
       "turboRoamingApAliveCheckEnable": turboRoamingApAliveCheckEnable,
       "turboRoamingChannelN24GHz1": turboRoamingChannelN24GHz1,
       "turboRoamingChannelN24GHz2": turboRoamingChannelN24GHz2,
       "turboRoamingChannelN24GHz3": turboRoamingChannelN24GHz3,
       "turboRoamingChannelN5GHz1": turboRoamingChannelN5GHz1,
       "turboRoamingChannelN5GHz2": turboRoamingChannelN5GHz2,
       "turboRoamingChannelN5GHz3": turboRoamingChannelN5GHz3,
       "turboRoamingSelectTRtypeEnable": turboRoamingSelectTRtypeEnable,
       "turboRoamingRoamingThreshunit": turboRoamingRoamingThreshunit,
       "turboRoamingRoamingAliveunit": turboRoamingRoamingAliveunit,
       "turboRoamingRoamingThresh2GSNR": turboRoamingRoamingThresh2GSNR,
       "turboRoamingRoamingThresh2GSignal": turboRoamingRoamingThresh2GSignal,
       "turboRoamingRoamingDifference2G": turboRoamingRoamingDifference2G,
       "turboRoamingApCandidateThreshold2GSNR": turboRoamingApCandidateThreshold2GSNR,
       "turboRoamingApCandidateThreshold2GSignal": turboRoamingApCandidateThreshold2GSignal,
       "turboRoamingRoamingThresh5GSNR": turboRoamingRoamingThresh5GSNR,
       "turboRoamingRoamingThresh5GSignal": turboRoamingRoamingThresh5GSignal,
       "turboRoamingRoamingDifference5G": turboRoamingRoamingDifference5G,
       "turboRoamingApCandidateThreshold5GSNR": turboRoamingApCandidateThreshold5GSNR,
       "turboRoamingApCandidateThreshold5GSignal": turboRoamingApCandidateThreshold5GSignal,
       "turboRoamingRoamingThreshLegacySNR": turboRoamingRoamingThreshLegacySNR,
       "turboRoamingRoamingThreshLegacySignal": turboRoamingRoamingThreshLegacySignal,
       "turboRoamingRoamingThreshNmodeSNR": turboRoamingRoamingThreshNmodeSNR,
       "turboRoamingRoamingThreshNmode24GSignal": turboRoamingRoamingThreshNmode24GSignal,
       "turboRoamingRoamingThreshNmode5GSignal": turboRoamingRoamingThreshNmode5GSignal,
       "turboRoamingChannelA4": turboRoamingChannelA4,
       "turboRoamingChannelA5": turboRoamingChannelA5,
       "turboRoamingChannelB4": turboRoamingChannelB4,
       "turboRoamingChannelB5": turboRoamingChannelB5,
       "turboRoamingChannelG4": turboRoamingChannelG4,
       "turboRoamingChannelG5": turboRoamingChannelG5,
       "turboRoamingChannelBG4": turboRoamingChannelBG4,
       "turboRoamingChannelBG5": turboRoamingChannelBG5,
       "turboRoamingChannelN24GHz4": turboRoamingChannelN24GHz4,
       "turboRoamingChannelN24GHz5": turboRoamingChannelN24GHz5,
       "turboRoamingChannelN5GHz4": turboRoamingChannelN5GHz4,
       "turboRoamingChannelN5GHz5": turboRoamingChannelN5GHz5,
       "turboRoamingRoamingAliveLegacySNR": turboRoamingRoamingAliveLegacySNR,
       "turboRoamingRoamingAliveSignal": turboRoamingRoamingAliveSignal,
       "turboRoamingRoamingAliveNmode24GSNR": turboRoamingRoamingAliveNmode24GSNR,
       "turboRoamingRoamingAliveNmode24GSignal": turboRoamingRoamingAliveNmode24GSignal,
       "turboRoamingRoamingAliveNmode5GSNR": turboRoamingRoamingAliveNmode5GSNR,
       "turboRoamingRoamingAliveNmode5GSignal": turboRoamingRoamingAliveNmode5GSignal,
       "turboRoamingChannelA6": turboRoamingChannelA6,
       "turboRoamingChannelA7": turboRoamingChannelA7,
       "turboRoamingChannelA8": turboRoamingChannelA8,
       "turboRoamingChannelA9": turboRoamingChannelA9,
       "turboRoamingChannelA10": turboRoamingChannelA10,
       "turboRoamingChannelA11": turboRoamingChannelA11,
       "turboRoamingChannelB6": turboRoamingChannelB6,
       "turboRoamingChannelB7": turboRoamingChannelB7,
       "turboRoamingChannelB8": turboRoamingChannelB8,
       "turboRoamingChannelB9": turboRoamingChannelB9,
       "turboRoamingChannelB10": turboRoamingChannelB10,
       "turboRoamingChannelB11": turboRoamingChannelB11,
       "turboRoamingChannelG6": turboRoamingChannelG6,
       "turboRoamingChannelG7": turboRoamingChannelG7,
       "turboRoamingChannelG8": turboRoamingChannelG8,
       "turboRoamingChannelG9": turboRoamingChannelG9,
       "turboRoamingChannelG10": turboRoamingChannelG10,
       "turboRoamingChannelG11": turboRoamingChannelG11,
       "turboRoamingChannelBG6": turboRoamingChannelBG6,
       "turboRoamingChannelBG7": turboRoamingChannelBG7,
       "turboRoamingChannelBG8": turboRoamingChannelBG8,
       "turboRoamingChannelBG9": turboRoamingChannelBG9,
       "turboRoamingChannelBG10": turboRoamingChannelBG10,
       "turboRoamingChannelBG11": turboRoamingChannelBG11,
       "turboRoamingChannelN24GHz6": turboRoamingChannelN24GHz6,
       "turboRoamingChannelN24GHz7": turboRoamingChannelN24GHz7,
       "turboRoamingChannelN24GHz8": turboRoamingChannelN24GHz8,
       "turboRoamingChannelN24GHz9": turboRoamingChannelN24GHz9,
       "turboRoamingChannelN24GHz10": turboRoamingChannelN24GHz10,
       "turboRoamingChannelN24GHz11": turboRoamingChannelN24GHz11,
       "turboRoamingChannelN5GHz6": turboRoamingChannelN5GHz6,
       "turboRoamingChannelN5GHz7": turboRoamingChannelN5GHz7,
       "turboRoamingChannelN5GHz8": turboRoamingChannelN5GHz8,
       "turboRoamingChannelN5GHz9": turboRoamingChannelN5GHz9,
       "turboRoamingChannelN5GHz10": turboRoamingChannelN5GHz10,
       "turboRoamingChannelN5GHz11": turboRoamingChannelN5GHz11,
       "aeroLinkProtection": aeroLinkProtection,
       "aeroLinkProtectionAPAliveCheck": aeroLinkProtectionAPAliveCheck,
       "aeroLinkProtectionType": aeroLinkProtectionType,
       "aeroLinkProtectionNumPort": aeroLinkProtectionNumPort,
       "aeroLinkProtectionRfIndex": aeroLinkProtectionRfIndex,
       "aeroLinkProtectionRssi-detect-en": aeroLinkProtectionRssi_detect_en,
       "aeroLinkProtectionRssi-detect-unit": aeroLinkProtectionRssi_detect_unit,
       "aeroLinkProtectionThreshold2G-SNR": aeroLinkProtectionThreshold2G_SNR,
       "aeroLinkProtectionThreshold2G-Signal": aeroLinkProtectionThreshold2G_Signal,
       "aeroLinkProtectionDifference2G": aeroLinkProtectionDifference2G,
       "aeroLinkProtectionThreshold5G-SNR": aeroLinkProtectionThreshold5G_SNR,
       "aeroLinkProtectionThreshold5G-Signal": aeroLinkProtectionThreshold5G_Signal,
       "aeroLinkProtectionDifference5G": aeroLinkProtectionDifference5G,
       "aeroLinkProtectionThresholdLegacy-SNR": aeroLinkProtectionThresholdLegacy_SNR,
       "aeroLinkProtectionThresholdLegacy-Signal": aeroLinkProtectionThresholdLegacy_Signal,
       "aeroLinkProtectionThresholdNmode-SNR": aeroLinkProtectionThresholdNmode_SNR,
       "aeroLinkProtectionThresholdNmode24G-Signal": aeroLinkProtectionThresholdNmode24G_Signal,
       "aeroLinkProtectionThresholdNmode5G-Signal": aeroLinkProtectionThresholdNmode5G_Signal,
       "advanced": advanced,
       "dhcpServer": dhcpServer,
       "dhcpServerEnable": dhcpServerEnable,
       "dhcpServerIPv4Gateway": dhcpServerIPv4Gateway,
       "dhcpServerIPv4Netmask": dhcpServerIPv4Netmask,
       "dhcpServerDnsTable": dhcpServerDnsTable,
       "dhcpServerDnsEntry": dhcpServerDnsEntry,
       "dhcpServerDnsIndex": dhcpServerDnsIndex,
       "dhcpServerDnsData": dhcpServerDnsData,
       "dhcpServerIPv4StartAddr": dhcpServerIPv4StartAddr,
       "dhcpServerMaxClient": dhcpServerMaxClient,
       "dhcpServerLeaseTimeMinute": dhcpServerLeaseTimeMinute,
       "dhcpServerMapTable": dhcpServerMapTable,
       "dhcpServerMapEntry": dhcpServerMapEntry,
       "dhcpServerMapIndex": dhcpServerMapIndex,
       "dhcpServerMapEnable": dhcpServerMapEnable,
       "dhcpServerMapMac": dhcpServerMapMac,
       "dhcpServerMapIPv4Addr": dhcpServerMapIPv4Addr,
       "macFilter": macFilter,
       "macFilterEnable": macFilterEnable,
       "macFilterPolicy": macFilterPolicy,
       "macFilterRulesTable": macFilterRulesTable,
       "macFilterRulesEntry": macFilterRulesEntry,
       "macFilterRuleIndex": macFilterRuleIndex,
       "macFilterRuleEnable": macFilterRuleEnable,
       "macFilterRuleName": macFilterRuleName,
       "macFilterRuleAddr": macFilterRuleAddr,
       "protocolFilter": protocolFilter,
       "protocolFilterEnable": protocolFilterEnable,
       "protocolFilterPolicy": protocolFilterPolicy,
       "protocolFilterRulesTable": protocolFilterRulesTable,
       "protocolFilterRulesEntry": protocolFilterRulesEntry,
       "protocolFilterRuleIndex": protocolFilterRuleIndex,
       "protocolFilterRuleEnable": protocolFilterRuleEnable,
       "protocolFilterRuleProtocol": protocolFilterRuleProtocol,
       "protocolFilterRuleSrcIp": protocolFilterRuleSrcIp,
       "protocolFilterRuleSrcMask": protocolFilterRuleSrcMask,
       "protocolFilterRuleDstIp": protocolFilterRuleDstIp,
       "protocolFilterRuleDstMask": protocolFilterRuleDstMask,
       "portFilter": portFilter,
       "portFilterEnable": portFilterEnable,
       "portFilterPolicy": portFilterPolicy,
       "portFilterRulesTable": portFilterRulesTable,
       "portFilterRulesEntry": portFilterRulesEntry,
       "portFilterRuleIndex": portFilterRuleIndex,
       "portFilterRuleEnable": portFilterRuleEnable,
       "portFilterRuleName": portFilterRuleName,
       "portFilterRuleProtocol": portFilterRuleProtocol,
       "portFilterRuleSrcPortStart": portFilterRuleSrcPortStart,
       "portFilterRuleSrcPortEnd": portFilterRuleSrcPortEnd,
       "portFilterRuleDstPortStart": portFilterRuleDstPortStart,
       "portFilterRuleDstPortEnd": portFilterRuleDstPortEnd,
       "stpBridge": stpBridge,
       "stpBridgeHelloTime": stpBridgeHelloTime,
       "stpBridgeMaxAgeTime": stpBridgeMaxAgeTime,
       "stpBridgeForwardDelay": stpBridgeForwardDelay,
       "stpBridgePriority": stpBridgePriority,
       "stpPortLanTable": stpPortLanTable,
       "stpPortLanEntry": stpPortLanEntry,
       "stpPortLanIndex": stpPortLanIndex,
       "stpPortLanEnable": stpPortLanEnable,
       "stpPortLanPriority": stpPortLanPriority,
       "stpPortLanPathCost": stpPortLanPathCost,
       "stpPortLanEdgePort": stpPortLanEdgePort,
       "stpPortWlanTable": stpPortWlanTable,
       "stpPortWlanEntry": stpPortWlanEntry,
       "stpPortWlanIndex": stpPortWlanIndex,
       "stpPortWlanEnable": stpPortWlanEnable,
       "stpPortWlanPriority": stpPortWlanPriority,
       "stpPortWlanPathCost": stpPortWlanPathCost,
       "stpPortWlanEdgePort": stpPortWlanEdgePort,
       "managementVID": managementVID,
       "managementVIDVid": managementVIDVid,
       "lanVLANTable": lanVLANTable,
       "lanVLANEntry": lanVLANEntry,
       "lanVLANIndex": lanVLANIndex,
       "lanVLANPvid": lanVLANPvid,
       "lanVLANVlanTag0": lanVLANVlanTag0,
       "lanVLANVlanTag1": lanVLANVlanTag1,
       "lanVLANVlanTag2": lanVLANVlanTag2,
       "lanVLANVlanTag3": lanVLANVlanTag3,
       "lanVLANVlanTag4": lanVLANVlanTag4,
       "lanVLANVlanTag5": lanVLANVlanTag5,
       "lanVLANVlanTag6": lanVLANVlanTag6,
       "lanVLANVlanTag7": lanVLANVlanTag7,
       "lanVLANVlanTag8": lanVLANVlanTag8,
       "lanVLANVlanTag9": lanVLANVlanTag9,
       "lanVLANVlanTag10": lanVLANVlanTag10,
       "lanVLANVlanTag11": lanVLANVlanTag11,
       "lanVLANVlanTag12": lanVLANVlanTag12,
       "lanVLANVlanTag13": lanVLANVlanTag13,
       "lanVLANVlanTag14": lanVLANVlanTag14,
       "lanVLANVlanTag15": lanVLANVlanTag15,
       "lanVLANVlanTag16": lanVLANVlanTag16,
       "lanVLANVlanTag17": lanVLANVlanTag17,
       "lanVLANVlanTag18": lanVLANVlanTag18,
       "lanVLANVlanTag19": lanVLANVlanTag19,
       "lanVLANVlanTag20": lanVLANVlanTag20,
       "lanVLANVlanTag21": lanVLANVlanTag21,
       "lanVLANVlanTag22": lanVLANVlanTag22,
       "lanVLANVlanTag23": lanVLANVlanTag23,
       "lanVLANVlanTag24": lanVLANVlanTag24,
       "lanVLANVlanTag25": lanVLANVlanTag25,
       "lanVLANVlanTag26": lanVLANVlanTag26,
       "lanVLANVlanTag27": lanVLANVlanTag27,
       "lanVLANVlanTag28": lanVLANVlanTag28,
       "lanVLANVlanTag29": lanVLANVlanTag29,
       "lanVLANVlanTag30": lanVLANVlanTag30,
       "lanVLANVlanTag31": lanVLANVlanTag31,
       "wlanVLANTable": wlanVLANTable,
       "wlanVLANEntry": wlanVLANEntry,
       "wlanVLANIndex": wlanVLANIndex,
       "wlanVLANPvid": wlanVLANPvid,
       "wlanVLANVlanTag0": wlanVLANVlanTag0,
       "wlanVLANVlanTag1": wlanVLANVlanTag1,
       "wlanVLANVlanTag2": wlanVLANVlanTag2,
       "wlanVLANVlanTag3": wlanVLANVlanTag3,
       "wlanVLANVlanTag4": wlanVLANVlanTag4,
       "wlanVLANVlanTag5": wlanVLANVlanTag5,
       "wlanVLANVlanTag6": wlanVLANVlanTag6,
       "wlanVLANVlanTag7": wlanVLANVlanTag7,
       "wlanVLANVlanTag8": wlanVLANVlanTag8,
       "wlanVLANVlanTag9": wlanVLANVlanTag9,
       "wlanVLANVlanTag10": wlanVLANVlanTag10,
       "wlanVLANVlanTag11": wlanVLANVlanTag11,
       "wlanVLANVlanTag12": wlanVLANVlanTag12,
       "wlanVLANVlanTag13": wlanVLANVlanTag13,
       "wlanVLANVlanTag14": wlanVLANVlanTag14,
       "wlanVLANVlanTag15": wlanVLANVlanTag15,
       "wlanVLANVlanTag16": wlanVLANVlanTag16,
       "wlanVLANVlanTag17": wlanVLANVlanTag17,
       "wlanVLANVlanTag18": wlanVLANVlanTag18,
       "wlanVLANVlanTag19": wlanVLANVlanTag19,
       "wlanVLANVlanTag20": wlanVLANVlanTag20,
       "wlanVLANVlanTag21": wlanVLANVlanTag21,
       "wlanVLANVlanTag22": wlanVLANVlanTag22,
       "wlanVLANVlanTag23": wlanVLANVlanTag23,
       "wlanVLANVlanTag24": wlanVLANVlanTag24,
       "wlanVLANVlanTag25": wlanVLANVlanTag25,
       "wlanVLANVlanTag26": wlanVLANVlanTag26,
       "wlanVLANVlanTag27": wlanVLANVlanTag27,
       "wlanVLANVlanTag28": wlanVLANVlanTag28,
       "wlanVLANVlanTag29": wlanVLANVlanTag29,
       "wlanVLANVlanTag30": wlanVLANVlanTag30,
       "wlanVLANVlanTag31": wlanVLANVlanTag31,
       "wdsVLANTable": wdsVLANTable,
       "wdsVLANEntry": wdsVLANEntry,
       "wdsVLANIndex": wdsVLANIndex,
       "wdsVLANPvid": wdsVLANPvid,
       "wdsVLANVlanTag0": wdsVLANVlanTag0,
       "wdsVLANVlanTag1": wdsVLANVlanTag1,
       "wdsVLANVlanTag2": wdsVLANVlanTag2,
       "wdsVLANVlanTag3": wdsVLANVlanTag3,
       "wdsVLANVlanTag4": wdsVLANVlanTag4,
       "wdsVLANVlanTag5": wdsVLANVlanTag5,
       "wdsVLANVlanTag6": wdsVLANVlanTag6,
       "wdsVLANVlanTag7": wdsVLANVlanTag7,
       "wdsVLANVlanTag8": wdsVLANVlanTag8,
       "wdsVLANVlanTag9": wdsVLANVlanTag9,
       "wdsVLANVlanTag10": wdsVLANVlanTag10,
       "wdsVLANVlanTag11": wdsVLANVlanTag11,
       "wdsVLANVlanTag12": wdsVLANVlanTag12,
       "wdsVLANVlanTag13": wdsVLANVlanTag13,
       "wdsVLANVlanTag14": wdsVLANVlanTag14,
       "wdsVLANVlanTag15": wdsVLANVlanTag15,
       "wdsVLANVlanTag16": wdsVLANVlanTag16,
       "wdsVLANVlanTag17": wdsVLANVlanTag17,
       "wdsVLANVlanTag18": wdsVLANVlanTag18,
       "wdsVLANVlanTag19": wdsVLANVlanTag19,
       "wdsVLANVlanTag20": wdsVLANVlanTag20,
       "wdsVLANVlanTag21": wdsVLANVlanTag21,
       "wdsVLANVlanTag22": wdsVLANVlanTag22,
       "wdsVLANVlanTag23": wdsVLANVlanTag23,
       "wdsVLANVlanTag24": wdsVLANVlanTag24,
       "wdsVLANVlanTag25": wdsVLANVlanTag25,
       "wdsVLANVlanTag26": wdsVLANVlanTag26,
       "wdsVLANVlanTag27": wdsVLANVlanTag27,
       "wdsVLANVlanTag28": wdsVLANVlanTag28,
       "wdsVLANVlanTag29": wdsVLANVlanTag29,
       "wdsVLANVlanTag30": wdsVLANVlanTag30,
       "wdsVLANVlanTag31": wdsVLANVlanTag31,
       "linkFaultPassThrough": linkFaultPassThrough,
       "linkFaultPassThroughEnable": linkFaultPassThroughEnable,
       "aeroMag": aeroMag,
       "aeroMagEnable": aeroMagEnable,
       "aeroMagReset": aeroMagReset,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteIndex": staticRouteIndex,
       "staticRouteStaticRouteEnable": staticRouteStaticRouteEnable,
       "staticRouteStaticRouteInterface": staticRouteStaticRouteInterface,
       "staticRouteStaticRouteDst": staticRouteStaticRouteDst,
       "staticRouteStaticRouteNetmask": staticRouteStaticRouteNetmask,
       "staticRouteStaticRouteGateway": staticRouteStaticRouteGateway,
       "staticRouteStaticRouteMetric": staticRouteStaticRouteMetric,
       "nat": nat,
       "natNatMode": natNatMode,
       "portForwardingTable": portForwardingTable,
       "portForwardingEntry": portForwardingEntry,
       "portForwardingIndex": portForwardingIndex,
       "portForwardingPortForwardingEnable": portForwardingPortForwardingEnable,
       "portForwardingPortForwardingProtocol": portForwardingPortForwardingProtocol,
       "portForwardingPortForwardingWANPort": portForwardingPortForwardingWANPort,
       "portForwardingPortForwardingLANIP": portForwardingPortForwardingLANIP,
       "portForwardingPortForwardingLANPort": portForwardingPortForwardingLANPort,
       "portForwardingservice": portForwardingservice,
       "portForwardingservicePortForwardingserviceEnable": portForwardingservicePortForwardingserviceEnable,
       "aeroMagAction": aeroMagAction,
       "refreshChannel": refreshChannel,
       "oneToOneNatEntryTable": oneToOneNatEntryTable,
       "oneToOneNatEntryEntry": oneToOneNatEntryEntry,
       "oneToOneNatEntryIndex": oneToOneNatEntryIndex,
       "oneToOneNatEntryEnable": oneToOneNatEntryEnable,
       "oneToOneNatEntryLanIP": oneToOneNatEntryLanIP,
       "oneToOneNatEntryWanIP": oneToOneNatEntryWanIP,
       "hTTPSetting": hTTPSetting,
       "hTTPSettingHTTPPort": hTTPSettingHTTPPort,
       "hTTPSettingHTTPSPort": hTTPSettingHTTPSPort,
       "autoWarning": autoWarning,
       "emailAction": emailAction,
       "emailActionColdStart": emailActionColdStart,
       "emailActionWarmStart": emailActionWarmStart,
       "emailActionPower1Off": emailActionPower1Off,
       "emailActionPower1On": emailActionPower1On,
       "emailActionPower2Off": emailActionPower2Off,
       "emailActionPower2On": emailActionPower2On,
       "emailActionPoeOff": emailActionPoeOff,
       "emailActionPoeOn": emailActionPoeOn,
       "emailActionDi1On2Off": emailActionDi1On2Off,
       "emailActionDi1Off2On": emailActionDi1Off2On,
       "emailActionDi2On2Off": emailActionDi2On2Off,
       "emailActionDi2Off2On": emailActionDi2Off2On,
       "emailActionConfigChange": emailActionConfigChange,
       "emailActionConsoleAuthFail": emailActionConsoleAuthFail,
       "emailActionLanLinkOn": emailActionLanLinkOn,
       "emailActionLanLinkOff": emailActionLanLinkOff,
       "emailActionWlan1Connect": emailActionWlan1Connect,
       "emailActionWlan1Disconnect": emailActionWlan1Disconnect,
       "emailActionWlan1-1Connect": emailActionWlan1_1Connect,
       "emailActionWlan1-1Disconnect": emailActionWlan1_1Disconnect,
       "emailActionWlan1-2Connect": emailActionWlan1_2Connect,
       "emailActionWlan1-2Disconnect": emailActionWlan1_2Disconnect,
       "emailActionWlan1-3Connect": emailActionWlan1_3Connect,
       "emailActionWlan1-3Disconnect": emailActionWlan1_3Disconnect,
       "emailActionWlan1-4Connect": emailActionWlan1_4Connect,
       "emailActionWlan1-4Disconnect": emailActionWlan1_4Disconnect,
       "emailActionWlan1-5Connect": emailActionWlan1_5Connect,
       "emailActionWlan1-5Disconnect": emailActionWlan1_5Disconnect,
       "emailActionWlan1-6Connect": emailActionWlan1_6Connect,
       "emailActionWlan1-6Disconnect": emailActionWlan1_6Disconnect,
       "emailActionWlan1-7Connect": emailActionWlan1_7Connect,
       "emailActionWlan1-7Disconnect": emailActionWlan1_7Disconnect,
       "emailActionWlan1-8Connect": emailActionWlan1_8Connect,
       "emailActionWlan1-8Disconnect": emailActionWlan1_8Disconnect,
       "relayAction": relayAction,
       "relayActionColdStart": relayActionColdStart,
       "relayActionWarmStart": relayActionWarmStart,
       "relayActionPower1Off": relayActionPower1Off,
       "relayActionPower1On": relayActionPower1On,
       "relayActionPower2Off": relayActionPower2Off,
       "relayActionPower2On": relayActionPower2On,
       "relayActionPoeOff": relayActionPoeOff,
       "relayActionPoeOn": relayActionPoeOn,
       "relayActionDi1On2Off": relayActionDi1On2Off,
       "relayActionDi1Off2On": relayActionDi1Off2On,
       "relayActionDi2On2Off": relayActionDi2On2Off,
       "relayActionDi2Off2On": relayActionDi2Off2On,
       "relayActionConfigChange": relayActionConfigChange,
       "relayActionConsoleAuthFail": relayActionConsoleAuthFail,
       "relayActionLanLinkOn": relayActionLanLinkOn,
       "relayActionLanLinkOff": relayActionLanLinkOff,
       "relayActionWlan1Connect": relayActionWlan1Connect,
       "relayActionWlan1Disconnect": relayActionWlan1Disconnect,
       "relayActionWlan1-1Connect": relayActionWlan1_1Connect,
       "relayActionWlan1-1Disconnect": relayActionWlan1_1Disconnect,
       "relayActionWlan1-2Connect": relayActionWlan1_2Connect,
       "relayActionWlan1-2Disconnect": relayActionWlan1_2Disconnect,
       "relayActionWlan1-3Connect": relayActionWlan1_3Connect,
       "relayActionWlan1-3Disconnect": relayActionWlan1_3Disconnect,
       "relayActionWlan1-4Connect": relayActionWlan1_4Connect,
       "relayActionWlan1-4Disconnect": relayActionWlan1_4Disconnect,
       "relayActionWlan1-5Connect": relayActionWlan1_5Connect,
       "relayActionWlan1-5Disconnect": relayActionWlan1_5Disconnect,
       "relayActionWlan1-6Connect": relayActionWlan1_6Connect,
       "relayActionWlan1-6Disconnect": relayActionWlan1_6Disconnect,
       "relayActionWlan1-7Connect": relayActionWlan1_7Connect,
       "relayActionWlan1-7Disconnect": relayActionWlan1_7Disconnect,
       "relayActionWlan1-8Connect": relayActionWlan1_8Connect,
       "relayActionWlan1-8Disconnect": relayActionWlan1_8Disconnect,
       "trapAction": trapAction,
       "trapActionColdStart": trapActionColdStart,
       "trapActionWarmStart": trapActionWarmStart,
       "trapActionPower1Off": trapActionPower1Off,
       "trapActionPower1On": trapActionPower1On,
       "trapActionPower2Off": trapActionPower2Off,
       "trapActionPower2On": trapActionPower2On,
       "trapActionPoeOff": trapActionPoeOff,
       "trapActionPoeOn": trapActionPoeOn,
       "trapActionDi1On2Off": trapActionDi1On2Off,
       "trapActionDi1Off2On": trapActionDi1Off2On,
       "trapActionDi2On2Off": trapActionDi2On2Off,
       "trapActionDi2Off2On": trapActionDi2Off2On,
       "trapActionConfigChange": trapActionConfigChange,
       "trapActionConsoleAuthFail": trapActionConsoleAuthFail,
       "trapActionLanLinkOn": trapActionLanLinkOn,
       "trapActionLanLinkOff": trapActionLanLinkOff,
       "trapActionWlan1Connect": trapActionWlan1Connect,
       "trapActionWlan1Disconnect": trapActionWlan1Disconnect,
       "trapActionWlan1-1Connect": trapActionWlan1_1Connect,
       "trapActionWlan1-1Disconnect": trapActionWlan1_1Disconnect,
       "trapActionWlan1-2Connect": trapActionWlan1_2Connect,
       "trapActionWlan1-2Disconnect": trapActionWlan1_2Disconnect,
       "trapActionWlan1-3Connect": trapActionWlan1_3Connect,
       "trapActionWlan1-3Disconnect": trapActionWlan1_3Disconnect,
       "trapActionWlan1-4Connect": trapActionWlan1_4Connect,
       "trapActionWlan1-4Disconnect": trapActionWlan1_4Disconnect,
       "trapActionWlan1-5Connect": trapActionWlan1_5Connect,
       "trapActionWlan1-5Disconnect": trapActionWlan1_5Disconnect,
       "trapActionWlan1-6Connect": trapActionWlan1_6Connect,
       "trapActionWlan1-6Disconnect": trapActionWlan1_6Disconnect,
       "trapActionWlan1-7Connect": trapActionWlan1_7Connect,
       "trapActionWlan1-7Disconnect": trapActionWlan1_7Disconnect,
       "trapActionWlan1-8Connect": trapActionWlan1_8Connect,
       "trapActionWlan1-8Disconnect": trapActionWlan1_8Disconnect,
       "systemLog": systemLog,
       "systemLogSystemEnable": systemLogSystemEnable,
       "systemLogNetworkEnable": systemLogNetworkEnable,
       "systemLogConfigEnable": systemLogConfigEnable,
       "systemLogPowerEnable": systemLogPowerEnable,
       "systemLogDinEnable": systemLogDinEnable,
       "systemLogRssiReport": systemLogRssiReport,
       "sysLog": sysLog,
       "sysLogSystemEnable": sysLogSystemEnable,
       "sysLogNetworkEnable": sysLogNetworkEnable,
       "sysLogConfigEnable": sysLogConfigEnable,
       "sysLogPowerEnable": sysLogPowerEnable,
       "sysLogDinEnable": sysLogDinEnable,
       "sysLogRssiReport": sysLogRssiReport,
       "snmp": snmp,
       "snmpEnable": snmpEnable,
       "snmpVersion": snmpVersion,
       "snmpRoCommunity": snmpRoCommunity,
       "snmpRwCommunity": snmpRwCommunity,
       "snmpFirstTrapServer": snmpFirstTrapServer,
       "snmpFirstTrapVersion": snmpFirstTrapVersion,
       "snmpFirstTrapCommunity": snmpFirstTrapCommunity,
       "snmpSecondTrapServer": snmpSecondTrapServer,
       "snmpSecondTrapVersion": snmpSecondTrapVersion,
       "snmpSecondTrapCommunity": snmpSecondTrapCommunity,
       "snmpAdminAuthType": snmpAdminAuthType,
       "snmpAdminAuthKey": snmpAdminAuthKey,
       "snmpPrivMib": snmpPrivMib,
       "snmpRmtMngtEnable": snmpRmtMngtEnable,
       "snmpUserAuthAccount": snmpUserAuthAccount,
       "snmpThirdTrapServer": snmpThirdTrapServer,
       "snmpThirdTrapVersion": snmpThirdTrapVersion,
       "snmpThirdTrapCommunity": snmpThirdTrapCommunity,
       "emailSmtp": emailSmtp,
       "emailSmtpServerTable": emailSmtpServerTable,
       "emailSmtpServerEntry": emailSmtpServerEntry,
       "emailSmtpServerIndex": emailSmtpServerIndex,
       "emailSmtpServerData": emailSmtpServerData,
       "emailSmtpMailAddressTable": emailSmtpMailAddressTable,
       "emailSmtpMailAddressEntry": emailSmtpMailAddressEntry,
       "emailSmtpMailAddressIndex": emailSmtpMailAddressIndex,
       "emailSmtpMailAddressData": emailSmtpMailAddressData,
       "emailSmtpUserName": emailSmtpUserName,
       "emailSmtpFrom": emailSmtpFrom,
       "sysLogServerTable": sysLogServerTable,
       "sysLogServerEntry": sysLogServerEntry,
       "sysLogServerIndex": sysLogServerIndex,
       "sysLogServerServer": sysLogServerServer,
       "sysLogServerPort": sysLogServerPort,
       "sysStatus": sysStatus,
       "powerInputTable": powerInputTable,
       "powerInputEntry": powerInputEntry,
       "powerInputIndex": powerInputIndex,
       "powerInputStatus": powerInputStatus,
       "diTable": diTable,
       "diEntry": diEntry,
       "diIndex": diIndex,
       "diInputStatus": diInputStatus,
       "wlanClientListTable": wlanClientListTable,
       "wlanClientListEntry": wlanClientListEntry,
       "wlanDevIndex": wlanDevIndex,
       "wlanSsidIndex": wlanSsidIndex,
       "wlanClientIndex": wlanClientIndex,
       "wlanClientMAC": wlanClientMAC,
       "wlanClientIP": wlanClientIP,
       "wlanClientSignalStrength": wlanClientSignalStrength,
       "wlanClientSNR": wlanClientSNR,
       "wlanClientConnectionTime": wlanClientConnectionTime,
       "dhcpClientListTable": dhcpClientListTable,
       "dhcpClientListEntry": dhcpClientListEntry,
       "dhcpClientIndex": dhcpClientIndex,
       "dhcpClientIP": dhcpClientIP,
       "dhcpClientMAC": dhcpClientMAC,
       "wirelessStatusTable": wirelessStatusTable,
       "wirelessStatusEntry": wirelessStatusEntry,
       "wlanIndex": wlanIndex,
       "wlanChannel": wlanChannel,
       "wlanBSSID": wlanBSSID,
       "wlanSingal": wlanSingal,
       "wlanTxRate": wlanTxRate,
       "wlanSSID": wlanSSID,
       "wlanVapIndex": wlanVapIndex,
       "wlanAPip": wlanAPip,
       "wlanSNR": wlanSNR,
       "wlanNoiseLevel": wlanNoiseLevel,
       "wlanSNR-A": wlanSNR_A,
       "wlanSNR-B": wlanSNR_B,
       "wlanChannelWidth": wlanChannelWidth,
       "wlanConnectionTime": wlanConnectionTime,
       "wlanOperationMode": wlanOperationMode,
       "relayStatusAckTable": relayStatusAckTable,
       "relayStatusAckEntry": relayStatusAckEntry,
       "relayIndex": relayIndex,
       "relayType": relayType,
       "relayStatus": relayStatus,
       "relayAck": relayAck,
       "bridgeStatusTable": bridgeStatusTable,
       "bridgeStatusEntry": bridgeStatusEntry,
       "entryIndex": entryIndex,
       "interface": interface,
       "macAddr": macAddr,
       "systemStatus": systemStatus,
       "cpuUsage": cpuUsage,
       "memTotalKB": memTotalKB,
       "memUsedKB": memUsedKB,
       "memFreeKB": memFreeKB,
       "maintenance": maintenance,
       "misc": misc,
       "miscTelnetEnable": miscTelnetEnable,
       "miscWebEnable": miscWebEnable,
       "miscSshEnable": miscSshEnable,
       "miscHttpsEnable": miscHttpsEnable,
       "miscWlanEnable": miscWlanEnable,
       "miscResetButtonEnable": miscResetButtonEnable,
       "miscAutoLogoutTimeout": miscAutoLogoutTimeout,
       "miscMoxaServiceEnable": miscMoxaServiceEnable,
       "miscLanEnable": miscLanEnable,
       "miscAllowSpecialCharacters": miscAllowSpecialCharacters,
       "saveAndReboot": saveAndReboot,
       "configChangeStatus": configChangeStatus,
       "saveConfig": saveConfig,
       "reboot": reboot,
       "accountMgmt": accountMgmt,
       "accountMgmtPasswdStrengthCheck": accountMgmtPasswdStrengthCheck,
       "accountMgmtPasswdLength": accountMgmtPasswdLength,
       "accountMgmtPasswdExpiredTime": accountMgmtPasswdExpiredTime,
       "accountMgmtRetry": accountMgmtRetry,
       "accountMgmtLockTime": accountMgmtLockTime,
       "accountTable": accountTable,
       "accountEntry": accountEntry,
       "accountIndex": accountIndex,
       "accountActive": accountActive,
       "accountUsername": accountUsername,
       "accountGroup": accountGroup,
       "accountAccessHttp": accountAccessHttp,
       "accountAccessConsole": accountAccessConsole,
       "accountAccessMoxaService": accountAccessMoxaService,
       "accountAccessDiag": accountAccessDiag,
       "configEncrypt": configEncrypt,
       "configEncryptEnable": configEncryptEnable,
       "configEncryptPassword": configEncryptPassword,
       "consoles": consoles,
       "consolesEthTelnetEnable": consolesEthTelnetEnable,
       "consolesEthWebEnable": consolesEthWebEnable,
       "consolesEthSshEnable": consolesEthSshEnable,
       "consolesEthHttpsEnable": consolesEthHttpsEnable,
       "consolesEthSnmpEnable": consolesEthSnmpEnable,
       "consolesEthMoxaServiceEnable": consolesEthMoxaServiceEnable,
       "consolesWlanTelnetEnableTable": consolesWlanTelnetEnableTable,
       "consolesWlanTelnetEnableEntry": consolesWlanTelnetEnableEntry,
       "consolesWlanTelnetEnableIndex": consolesWlanTelnetEnableIndex,
       "consolesWlanTelnetEnableData": consolesWlanTelnetEnableData,
       "consolesWlanWebEnableTable": consolesWlanWebEnableTable,
       "consolesWlanWebEnableEntry": consolesWlanWebEnableEntry,
       "consolesWlanWebEnableIndex": consolesWlanWebEnableIndex,
       "consolesWlanWebEnableData": consolesWlanWebEnableData,
       "consolesWlanSshEnableTable": consolesWlanSshEnableTable,
       "consolesWlanSshEnableEntry": consolesWlanSshEnableEntry,
       "consolesWlanSshEnableIndex": consolesWlanSshEnableIndex,
       "consolesWlanSshEnableData": consolesWlanSshEnableData,
       "consolesWlanHttpsEnableTable": consolesWlanHttpsEnableTable,
       "consolesWlanHttpsEnableEntry": consolesWlanHttpsEnableEntry,
       "consolesWlanHttpsEnableIndex": consolesWlanHttpsEnableIndex,
       "consolesWlanHttpsEnableData": consolesWlanHttpsEnableData,
       "consolesWlanSnmpEnableTable": consolesWlanSnmpEnableTable,
       "consolesWlanSnmpEnableEntry": consolesWlanSnmpEnableEntry,
       "consolesWlanSnmpEnableIndex": consolesWlanSnmpEnableIndex,
       "consolesWlanSnmpEnableData": consolesWlanSnmpEnableData,
       "consolesWlanMoxaServiceEnableTable": consolesWlanMoxaServiceEnableTable,
       "consolesWlanMoxaServiceEnableEntry": consolesWlanMoxaServiceEnableEntry,
       "consolesWlanMoxaServiceEnableIndex": consolesWlanMoxaServiceEnableIndex,
       "consolesWlanMoxaServiceEnableData": consolesWlanMoxaServiceEnableData,
       "consolesAccessibleNet": consolesAccessibleNet,
       "consolesAccessibleNetAccessibleNet": consolesAccessibleNetAccessibleNet,
       "consolesAccessibleNetAccessibleNetPolicy": consolesAccessibleNetAccessibleNetPolicy,
       "consolesAccessibleNetTable": consolesAccessibleNetTable,
       "consolesAccessibleNetEntry": consolesAccessibleNetEntry,
       "consolesAccessibleNetIndex": consolesAccessibleNetIndex,
       "consolesAccessibleNetActive": consolesAccessibleNetActive,
       "consolesAccessibleNetSrcIP": consolesAccessibleNetSrcIP,
       "consolesAccessibleNetSrcMask": consolesAccessibleNetSrcMask,
       "userWebCertificate": userWebCertificate,
       "userWebCertificateEnable": userWebCertificateEnable}
)
