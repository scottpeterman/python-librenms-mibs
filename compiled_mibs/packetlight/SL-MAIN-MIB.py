# SNMP MIB module (SL-MAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-MAIN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:42 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slMain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UserLogin(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class UserPassword(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class UserCommunity(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class SoftwareRevision(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class AdminAccess(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("readwrite", 2),
          ("provisioning", 3),
          ("admin", 4),
          ("trap", 5))
    )



# MIB Managed Objects in the order of their OIDs

_SlmSys_ObjectIdentity = ObjectIdentity
slmSys = _SlmSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1)
)
_SlmSysGatewayAddr_Type = IpAddress
_SlmSysGatewayAddr_Object = MibScalar
slmSysGatewayAddr = _SlmSysGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 1),
    _SlmSysGatewayAddr_Type()
)
slmSysGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysGatewayAddr.setStatus("current")
_SlmSysSubnetMask_Type = IpAddress
_SlmSysSubnetMask_Object = MibScalar
slmSysSubnetMask = _SlmSysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 2),
    _SlmSysSubnetMask_Type()
)
slmSysSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysSubnetMask.setStatus("current")
_SlmSysIpAddr_Type = IpAddress
_SlmSysIpAddr_Object = MibScalar
slmSysIpAddr = _SlmSysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 3),
    _SlmSysIpAddr_Type()
)
slmSysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysIpAddr.setStatus("current")


class _SlmSysAlmAct_Type(Integer32):
    """Custom type slmSysAlmAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlmSysAlmAct_Type.__name__ = "Integer32"
_SlmSysAlmAct_Object = MibScalar
slmSysAlmAct = _SlmSysAlmAct_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 4),
    _SlmSysAlmAct_Type()
)
slmSysAlmAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysAlmAct.setStatus("current")


class _SlmSysAlmDeact_Type(Integer32):
    """Custom type slmSysAlmDeact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlmSysAlmDeact_Type.__name__ = "Integer32"
_SlmSysAlmDeact_Object = MibScalar
slmSysAlmDeact = _SlmSysAlmDeact_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 5),
    _SlmSysAlmDeact_Type()
)
slmSysAlmDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysAlmDeact.setStatus("current")


class _SlmSysAdminStatus_Type(Integer32):
    """Custom type slmSysAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("warmBoot", 3),
          ("coldBoot", 4),
          ("factoryBoot", 5),
          ("testing", 6),
          ("hotBoot", 7))
    )


_SlmSysAdminStatus_Type.__name__ = "Integer32"
_SlmSysAdminStatus_Object = MibScalar
slmSysAdminStatus = _SlmSysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 6),
    _SlmSysAdminStatus_Type()
)
slmSysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysAdminStatus.setStatus("current")


class _SlmSysOperStatus_Type(Integer32):
    """Custom type slmSysOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SlmSysOperStatus_Type.__name__ = "Integer32"
_SlmSysOperStatus_Object = MibScalar
slmSysOperStatus = _SlmSysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 7),
    _SlmSysOperStatus_Type()
)
slmSysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysOperStatus.setStatus("current")


class _SlmBoxSize_Type(Integer32):
    """Custom type slmBoxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )


_SlmBoxSize_Type.__name__ = "Integer32"
_SlmBoxSize_Object = MibScalar
slmBoxSize = _SlmBoxSize_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 8),
    _SlmBoxSize_Type()
)
slmBoxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmBoxSize.setStatus("current")
_SlmSysCalendarTime_Type = DateAndTime
_SlmSysCalendarTime_Object = MibScalar
slmSysCalendarTime = _SlmSysCalendarTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 9),
    _SlmSysCalendarTime_Type()
)
slmSysCalendarTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysCalendarTime.setStatus("current")


class _SlmSysPmStartOfDay_Type(Integer32):
    """Custom type slmSysPmStartOfDay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SlmSysPmStartOfDay_Type.__name__ = "Integer32"
_SlmSysPmStartOfDay_Object = MibScalar
slmSysPmStartOfDay = _SlmSysPmStartOfDay_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 10),
    _SlmSysPmStartOfDay_Type()
)
slmSysPmStartOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysPmStartOfDay.setStatus("current")


class _SlmSysActiveSwVersion_Type(Integer32):
    """Custom type slmSysActiveSwVersion based on Integer32"""
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
        *(("swRevA", 1),
          ("swRevB", 2),
          ("swRevFtpStart", 3),
          ("swRevFtpEnd", 4),
          ("swRevAHot", 5),
          ("swRevBHot", 6))
    )


_SlmSysActiveSwVersion_Type.__name__ = "Integer32"
_SlmSysActiveSwVersion_Object = MibScalar
slmSysActiveSwVersion = _SlmSysActiveSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 11),
    _SlmSysActiveSwVersion_Type()
)
slmSysActiveSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysActiveSwVersion.setStatus("current")
_SlmSwRevTable_Object = MibTable
slmSwRevTable = _SlmSwRevTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12)
)
if mibBuilder.loadTexts:
    slmSwRevTable.setStatus("current")
_SlmSwRevEntry_Object = MibTableRow
slmSwRevEntry = _SlmSwRevEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1)
)
slmSwRevEntry.setIndexNames(
    (0, "SL-MAIN-MIB", "slmSwRevDirectory"),
)
if mibBuilder.loadTexts:
    slmSwRevEntry.setStatus("current")


class _SlmSwRevDirectory_Type(Integer32):
    """Custom type slmSwRevDirectory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swRevDirA", 1),
          ("swRevDirB", 2))
    )


_SlmSwRevDirectory_Type.__name__ = "Integer32"
_SlmSwRevDirectory_Object = MibTableColumn
slmSwRevDirectory = _SlmSwRevDirectory_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1, 1),
    _SlmSwRevDirectory_Type()
)
slmSwRevDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSwRevDirectory.setStatus("current")


class _SlmSwRevStatus_Type(Integer32):
    """Custom type slmSwRevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("copyingToStandby", 3))
    )


_SlmSwRevStatus_Type.__name__ = "Integer32"
_SlmSwRevStatus_Object = MibTableColumn
slmSwRevStatus = _SlmSwRevStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1, 2),
    _SlmSwRevStatus_Type()
)
slmSwRevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSwRevStatus.setStatus("current")
_SlmSwRevName_Type = SoftwareRevision
_SlmSwRevName_Object = MibTableColumn
slmSwRevName = _SlmSwRevName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1, 3),
    _SlmSwRevName_Type()
)
slmSwRevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSwRevName.setStatus("current")
_SlmSwRevDate_Type = DateAndTime
_SlmSwRevDate_Object = MibTableColumn
slmSwRevDate = _SlmSwRevDate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 12, 1, 4),
    _SlmSwRevDate_Type()
)
slmSwRevDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSwRevDate.setStatus("current")
_SlmConfigSysUptime_Type = TimeTicks
_SlmConfigSysUptime_Object = MibScalar
slmConfigSysUptime = _SlmConfigSysUptime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 13),
    _SlmConfigSysUptime_Type()
)
slmConfigSysUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmConfigSysUptime.setStatus("current")


class _SlmConfigSysSignalType_Type(Integer32):
    """Custom type slmConfigSysSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonet", 1),
          ("sdh", 2))
    )


_SlmConfigSysSignalType_Type.__name__ = "Integer32"
_SlmConfigSysSignalType_Object = MibScalar
slmConfigSysSignalType = _SlmConfigSysSignalType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 14),
    _SlmConfigSysSignalType_Type()
)
slmConfigSysSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmConfigSysSignalType.setStatus("current")


class _SlmRebootDelay_Type(Integer32):
    """Custom type slmRebootDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SlmRebootDelay_Type.__name__ = "Integer32"
_SlmRebootDelay_Object = MibScalar
slmRebootDelay = _SlmRebootDelay_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 16),
    _SlmRebootDelay_Type()
)
slmRebootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmRebootDelay.setStatus("current")
_SlmVcatDelay_Type = Integer32
_SlmVcatDelay_Object = MibScalar
slmVcatDelay = _SlmVcatDelay_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 17),
    _SlmVcatDelay_Type()
)
slmVcatDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmVcatDelay.setStatus("current")


class _SlmTid_Type(DisplayString):
    """Custom type slmTid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlmTid_Type.__name__ = "DisplayString"
_SlmTid_Object = MibScalar
slmTid = _SlmTid_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 18),
    _SlmTid_Type()
)
slmTid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmTid.setStatus("current")
_SlmPsuNumber_Type = Integer32
_SlmPsuNumber_Object = MibScalar
slmPsuNumber = _SlmPsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 19),
    _SlmPsuNumber_Type()
)
slmPsuNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmPsuNumber.setStatus("current")
_SlmOemType_Type = Integer32
_SlmOemType_Object = MibScalar
slmOemType = _SlmOemType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 20),
    _SlmOemType_Type()
)
slmOemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmOemType.setStatus("current")
_SlmSysName_Type = DisplayString
_SlmSysName_Object = MibScalar
slmSysName = _SlmSysName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 21),
    _SlmSysName_Type()
)
slmSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysName.setStatus("current")
_SlmSysLocation_Type = DisplayString
_SlmSysLocation_Object = MibScalar
slmSysLocation = _SlmSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 22),
    _SlmSysLocation_Type()
)
slmSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysLocation.setStatus("current")
_SlmSysResetPm_Type = Integer32
_SlmSysResetPm_Object = MibScalar
slmSysResetPm = _SlmSysResetPm_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 23),
    _SlmSysResetPm_Type()
)
slmSysResetPm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysResetPm.setStatus("current")


class _SlmSysUplinkRate_Type(Integer32):
    """Custom type slmSysUplinkRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up100", 1),
          ("up1000", 2))
    )


_SlmSysUplinkRate_Type.__name__ = "Integer32"
_SlmSysUplinkRate_Object = MibScalar
slmSysUplinkRate = _SlmSysUplinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 24),
    _SlmSysUplinkRate_Type()
)
slmSysUplinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysUplinkRate.setStatus("current")
_SlmSysChassisId_Type = Integer32
_SlmSysChassisId_Object = MibScalar
slmSysChassisId = _SlmSysChassisId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 25),
    _SlmSysChassisId_Type()
)
slmSysChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysChassisId.setStatus("current")
_SlmSysNetworkPrefix_Type = Integer32
_SlmSysNetworkPrefix_Object = MibScalar
slmSysNetworkPrefix = _SlmSysNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 26),
    _SlmSysNetworkPrefix_Type()
)
slmSysNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysNetworkPrefix.setStatus("current")
_SlmSysLanIpAddr_Type = IpAddress
_SlmSysLanIpAddr_Object = MibScalar
slmSysLanIpAddr = _SlmSysLanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 27),
    _SlmSysLanIpAddr_Type()
)
slmSysLanIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysLanIpAddr.setStatus("current")
_SlmSysLanSubnetAddr_Type = IpAddress
_SlmSysLanSubnetAddr_Object = MibScalar
slmSysLanSubnetAddr = _SlmSysLanSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 28),
    _SlmSysLanSubnetAddr_Type()
)
slmSysLanSubnetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysLanSubnetAddr.setStatus("current")
_SlmPmAvailable_Type = TruthValue
_SlmPmAvailable_Object = MibScalar
slmPmAvailable = _SlmPmAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 29),
    _SlmPmAvailable_Type()
)
slmPmAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmPmAvailable.setStatus("current")
_SlmPortsNumber_Type = Integer32
_SlmPortsNumber_Object = MibScalar
slmPortsNumber = _SlmPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 30),
    _SlmPortsNumber_Type()
)
slmPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmPortsNumber.setStatus("current")
_SlmEdfaNumber_Type = Integer32
_SlmEdfaNumber_Object = MibScalar
slmEdfaNumber = _SlmEdfaNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 31),
    _SlmEdfaNumber_Type()
)
slmEdfaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmEdfaNumber.setStatus("current")
_SlmMuxNumber_Type = Integer32
_SlmMuxNumber_Object = MibScalar
slmMuxNumber = _SlmMuxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 32),
    _SlmMuxNumber_Type()
)
slmMuxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmMuxNumber.setStatus("current")
_SlmOpticalSwitchExist_Type = TruthValue
_SlmOpticalSwitchExist_Object = MibScalar
slmOpticalSwitchExist = _SlmOpticalSwitchExist_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 33),
    _SlmOpticalSwitchExist_Type()
)
slmOpticalSwitchExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmOpticalSwitchExist.setStatus("current")
_SlmReadCommunity_Type = DisplayString
_SlmReadCommunity_Object = MibScalar
slmReadCommunity = _SlmReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 34),
    _SlmReadCommunity_Type()
)
slmReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmReadCommunity.setStatus("current")
_SlmWriteCommunity_Type = DisplayString
_SlmWriteCommunity_Object = MibScalar
slmWriteCommunity = _SlmWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 35),
    _SlmWriteCommunity_Type()
)
slmWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmWriteCommunity.setStatus("current")
_SlmSysEffectiveSubnetMask_Type = IpAddress
_SlmSysEffectiveSubnetMask_Object = MibScalar
slmSysEffectiveSubnetMask = _SlmSysEffectiveSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 36),
    _SlmSysEffectiveSubnetMask_Type()
)
slmSysEffectiveSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysEffectiveSubnetMask.setStatus("current")
_SlmSysEffectiveIpAddr_Type = IpAddress
_SlmSysEffectiveIpAddr_Object = MibScalar
slmSysEffectiveIpAddr = _SlmSysEffectiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 37),
    _SlmSysEffectiveIpAddr_Type()
)
slmSysEffectiveIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysEffectiveIpAddr.setStatus("current")
_SlmSysLanEffectiveIpAddr_Type = IpAddress
_SlmSysLanEffectiveIpAddr_Object = MibScalar
slmSysLanEffectiveIpAddr = _SlmSysLanEffectiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 38),
    _SlmSysLanEffectiveIpAddr_Type()
)
slmSysLanEffectiveIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysLanEffectiveIpAddr.setStatus("current")
_SlmSysLanEffectiveSubnetAddr_Type = IpAddress
_SlmSysLanEffectiveSubnetAddr_Object = MibScalar
slmSysLanEffectiveSubnetAddr = _SlmSysLanEffectiveSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 39),
    _SlmSysLanEffectiveSubnetAddr_Type()
)
slmSysLanEffectiveSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysLanEffectiveSubnetAddr.setStatus("current")
_SlmSysGatewayEffectiveIpAddr_Type = IpAddress
_SlmSysGatewayEffectiveIpAddr_Object = MibScalar
slmSysGatewayEffectiveIpAddr = _SlmSysGatewayEffectiveIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 40),
    _SlmSysGatewayEffectiveIpAddr_Type()
)
slmSysGatewayEffectiveIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysGatewayEffectiveIpAddr.setStatus("current")
_SlmSysMode_Type = Integer32
_SlmSysMode_Object = MibScalar
slmSysMode = _SlmSysMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 41),
    _SlmSysMode_Type()
)
slmSysMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysMode.setStatus("current")


class _SlmSysTrapFormat_Type(Integer32):
    """Custom type slmSysTrapFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullIfIndex", 1),
          ("portIfIndex", 2))
    )


_SlmSysTrapFormat_Type.__name__ = "Integer32"
_SlmSysTrapFormat_Object = MibScalar
slmSysTrapFormat = _SlmSysTrapFormat_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 42),
    _SlmSysTrapFormat_Type()
)
slmSysTrapFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysTrapFormat.setStatus("current")
_SlmSysTemperature_Type = Integer32
_SlmSysTemperature_Object = MibScalar
slmSysTemperature = _SlmSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 43),
    _SlmSysTemperature_Type()
)
slmSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysTemperature.setStatus("current")


class _SlmNetworkMode_Type(Integer32):
    """Custom type slmNetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routing", 1),
          ("switching", 2))
    )


_SlmNetworkMode_Type.__name__ = "Integer32"
_SlmNetworkMode_Object = MibScalar
slmNetworkMode = _SlmNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 44),
    _SlmNetworkMode_Type()
)
slmNetworkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmNetworkMode.setStatus("current")


class _Slm40GConf_Type(Integer32):
    """Custom type slm40GConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("g40", 0),
          ("g41", 1),
          ("g42", 2),
          ("g43", 3),
          ("g100", 100))
    )


_Slm40GConf_Type.__name__ = "Integer32"
_Slm40GConf_Object = MibScalar
slm40GConf = _Slm40GConf_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 45),
    _Slm40GConf_Type()
)
slm40GConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slm40GConf.setStatus("current")
_SlmRstpEnabled_Type = TruthValue
_SlmRstpEnabled_Object = MibScalar
slmRstpEnabled = _SlmRstpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 46),
    _SlmRstpEnabled_Type()
)
slmRstpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmRstpEnabled.setStatus("current")
_SlmTopologyEnabled_Type = TruthValue
_SlmTopologyEnabled_Object = MibScalar
slmTopologyEnabled = _SlmTopologyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 47),
    _SlmTopologyEnabled_Type()
)
slmTopologyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmTopologyEnabled.setStatus("current")
_SlmAdminCommunity_Type = DisplayString
_SlmAdminCommunity_Object = MibScalar
slmAdminCommunity = _SlmAdminCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 48),
    _SlmAdminCommunity_Type()
)
slmAdminCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmAdminCommunity.setStatus("current")
_SlmTrapCommunity_Type = DisplayString
_SlmTrapCommunity_Object = MibScalar
slmTrapCommunity = _SlmTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 49),
    _SlmTrapCommunity_Type()
)
slmTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmTrapCommunity.setStatus("current")


class _SlmSysSnmpVersion_Type(Integer32):
    """Custom type slmSysSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("v3Only", 3),
          ("v1v2v3", 4))
    )


_SlmSysSnmpVersion_Type.__name__ = "Integer32"
_SlmSysSnmpVersion_Object = MibScalar
slmSysSnmpVersion = _SlmSysSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 50),
    _SlmSysSnmpVersion_Type()
)
slmSysSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmSysSnmpVersion.setStatus("current")


class _SlmSysEncryptionCapability_Type(Integer32):
    """Custom type slmSysEncryptionCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SlmSysEncryptionCapability_Type.__name__ = "Integer32"
_SlmSysEncryptionCapability_Object = MibScalar
slmSysEncryptionCapability = _SlmSysEncryptionCapability_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 1, 51),
    _SlmSysEncryptionCapability_Type()
)
slmSysEncryptionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmSysEncryptionCapability.setStatus("current")
_SlmAdmin_ObjectIdentity = ObjectIdentity
slmAdmin = _SlmAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2)
)
_SlmAdminTable_Object = MibTable
slmAdminTable = _SlmAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    slmAdminTable.setStatus("current")
_SlmAdminEntry_Object = MibTableRow
slmAdminEntry = _SlmAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1)
)
slmAdminEntry.setIndexNames(
    (0, "SL-MAIN-MIB", "slmAdminLogin"),
)
if mibBuilder.loadTexts:
    slmAdminEntry.setStatus("current")
_SlmAdminLogin_Type = UserLogin
_SlmAdminLogin_Object = MibTableColumn
slmAdminLogin = _SlmAdminLogin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 3),
    _SlmAdminLogin_Type()
)
slmAdminLogin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmAdminLogin.setStatus("current")
_SlmAdminPassword_Type = UserPassword
_SlmAdminPassword_Object = MibTableColumn
slmAdminPassword = _SlmAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 4),
    _SlmAdminPassword_Type()
)
slmAdminPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmAdminPassword.setStatus("current")
_SlmAdminRowStatus_Type = RowStatus
_SlmAdminRowStatus_Object = MibTableColumn
slmAdminRowStatus = _SlmAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 5),
    _SlmAdminRowStatus_Type()
)
slmAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmAdminRowStatus.setStatus("current")
_SlmAdminAccess_Type = AdminAccess
_SlmAdminAccess_Object = MibTableColumn
slmAdminAccess = _SlmAdminAccess_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 6),
    _SlmAdminAccess_Type()
)
slmAdminAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmAdminAccess.setStatus("current")


class _SlmSnmpv3Auth_Type(Integer32):
    """Custom type slmSnmpv3Auth based on Integer32"""
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
        *(("noaccess", 1),
          ("noauth", 2),
          ("md5", 3),
          ("sha", 4),
          ("sha224", 5),
          ("sha256", 6),
          ("sha384", 7),
          ("sha512", 8))
    )


_SlmSnmpv3Auth_Type.__name__ = "Integer32"
_SlmSnmpv3Auth_Object = MibTableColumn
slmSnmpv3Auth = _SlmSnmpv3Auth_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 7),
    _SlmSnmpv3Auth_Type()
)
slmSnmpv3Auth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmSnmpv3Auth.setStatus("current")


class _SlmSnmpv3Priv_Type(Integer32):
    """Custom type slmSnmpv3Priv based on Integer32"""
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
        *(("noaccess", 1),
          ("nopriv", 2),
          ("des", 3),
          ("aes", 4),
          ("des3", 5),
          ("aes192", 6),
          ("aes256", 7))
    )


_SlmSnmpv3Priv_Type.__name__ = "Integer32"
_SlmSnmpv3Priv_Object = MibTableColumn
slmSnmpv3Priv = _SlmSnmpv3Priv_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 8),
    _SlmSnmpv3Priv_Type()
)
slmSnmpv3Priv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmSnmpv3Priv.setStatus("current")
_SlmSnmpv3Password_Type = UserPassword
_SlmSnmpv3Password_Object = MibTableColumn
slmSnmpv3Password = _SlmSnmpv3Password_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 2, 1, 1, 9),
    _SlmSnmpv3Password_Type()
)
slmSnmpv3Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmSnmpv3Password.setStatus("current")
_SlmAuth_ObjectIdentity = ObjectIdentity
slmAuth = _SlmAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 3)
)
_SlmAuthTable_Object = MibTable
slmAuthTable = _SlmAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    slmAuthTable.setStatus("current")
_SlmAuthEntry_Object = MibTableRow
slmAuthEntry = _SlmAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1, 1)
)
slmAuthEntry.setIndexNames(
    (0, "SL-MAIN-MIB", "slmAuthLogin"),
    (0, "SL-MAIN-MIB", "slmAuthPassword"),
)
if mibBuilder.loadTexts:
    slmAuthEntry.setStatus("current")
_SlmAuthLogin_Type = UserLogin
_SlmAuthLogin_Object = MibTableColumn
slmAuthLogin = _SlmAuthLogin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1, 1, 1),
    _SlmAuthLogin_Type()
)
slmAuthLogin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slmAuthLogin.setStatus("current")
_SlmAuthPassword_Type = UserPassword
_SlmAuthPassword_Object = MibTableColumn
slmAuthPassword = _SlmAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1, 1, 2),
    _SlmAuthPassword_Type()
)
slmAuthPassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slmAuthPassword.setStatus("current")
_SlmAuthCommunity_Type = UserCommunity
_SlmAuthCommunity_Object = MibTableColumn
slmAuthCommunity = _SlmAuthCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 3, 1, 1, 3),
    _SlmAuthCommunity_Type()
)
slmAuthCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmAuthCommunity.setStatus("current")
_SlmLogin_ObjectIdentity = ObjectIdentity
slmLogin = _SlmLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 4)
)
_SlmTrap_ObjectIdentity = ObjectIdentity
slmTrap = _SlmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5)
)
_SlmTrapDestTable_Object = MibTable
slmTrapDestTable = _SlmTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    slmTrapDestTable.setStatus("current")
_SlmTrapDestEntry_Object = MibTableRow
slmTrapDestEntry = _SlmTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1)
)
slmTrapDestEntry.setIndexNames(
    (0, "SL-MAIN-MIB", "slmTrapDestAddress"),
)
if mibBuilder.loadTexts:
    slmTrapDestEntry.setStatus("current")
_SlmTrapDestAddress_Type = Integer32
_SlmTrapDestAddress_Object = MibTableColumn
slmTrapDestAddress = _SlmTrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 1),
    _SlmTrapDestAddress_Type()
)
slmTrapDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapDestAddress.setStatus("current")
_SlmTrapDestRowStatus_Type = RowStatus
_SlmTrapDestRowStatus_Object = MibTableColumn
slmTrapDestRowStatus = _SlmTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 2),
    _SlmTrapDestRowStatus_Type()
)
slmTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapDestRowStatus.setStatus("current")
_SlmTrapDestCommunity_Type = UserCommunity
_SlmTrapDestCommunity_Object = MibTableColumn
slmTrapDestCommunity = _SlmTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 3),
    _SlmTrapDestCommunity_Type()
)
slmTrapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapDestCommunity.setStatus("current")


class _SlmTrapDestProtVersion_Type(Integer32):
    """Custom type slmTrapDestProtVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpVer1", 1),
          ("snmpVer2", 2),
          ("snmpVer3", 3))
    )


_SlmTrapDestProtVersion_Type.__name__ = "Integer32"
_SlmTrapDestProtVersion_Object = MibTableColumn
slmTrapDestProtVersion = _SlmTrapDestProtVersion_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 4),
    _SlmTrapDestProtVersion_Type()
)
slmTrapDestProtVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapDestProtVersion.setStatus("current")
_SlmTrapUserLogin_Type = UserLogin
_SlmTrapUserLogin_Object = MibTableColumn
slmTrapUserLogin = _SlmTrapUserLogin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 5),
    _SlmTrapUserLogin_Type()
)
slmTrapUserLogin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapUserLogin.setStatus("current")
_SlmTrapUserAccess_Type = AdminAccess
_SlmTrapUserAccess_Object = MibTableColumn
slmTrapUserAccess = _SlmTrapUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 6),
    _SlmTrapUserAccess_Type()
)
slmTrapUserAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapUserAccess.setStatus("current")
_SlmTrapEnable_Type = TruthValue
_SlmTrapEnable_Object = MibTableColumn
slmTrapEnable = _SlmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 7),
    _SlmTrapEnable_Type()
)
slmTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapEnable.setStatus("current")
_SlmTrapPort_Type = Integer32
_SlmTrapPort_Object = MibTableColumn
slmTrapPort = _SlmTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 8),
    _SlmTrapPort_Type()
)
slmTrapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapPort.setStatus("current")
_SlmTrapDestIpAddress_Type = IpAddress
_SlmTrapDestIpAddress_Object = MibTableColumn
slmTrapDestIpAddress = _SlmTrapDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 1, 1, 9),
    _SlmTrapDestIpAddress_Type()
)
slmTrapDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmTrapDestIpAddress.setStatus("current")
_SlmTrapLogTable_Object = MibTable
slmTrapLogTable = _SlmTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    slmTrapLogTable.setStatus("current")
_SlmTrapLogEntry_Object = MibTableRow
slmTrapLogEntry = _SlmTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1)
)
slmTrapLogEntry.setIndexNames(
    (0, "SL-MAIN-MIB", "slmTrapLogId"),
)
if mibBuilder.loadTexts:
    slmTrapLogEntry.setStatus("current")
_SlmTrapLogId_Type = Gauge32
_SlmTrapLogId_Object = MibTableColumn
slmTrapLogId = _SlmTrapLogId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 1),
    _SlmTrapLogId_Type()
)
slmTrapLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogId.setStatus("current")


class _SlmTrapLogName_Type(OctetString):
    """Custom type slmTrapLogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlmTrapLogName_Type.__name__ = "OctetString"
_SlmTrapLogName_Object = MibTableColumn
slmTrapLogName = _SlmTrapLogName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 2),
    _SlmTrapLogName_Type()
)
slmTrapLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogName.setStatus("current")
_SlmTrapLogTimeStamp_Type = TimeTicks
_SlmTrapLogTimeStamp_Object = MibTableColumn
slmTrapLogTimeStamp = _SlmTrapLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 3),
    _SlmTrapLogTimeStamp_Type()
)
slmTrapLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogTimeStamp.setStatus("current")


class _SlmTrapLogParam1_Type(OctetString):
    """Custom type slmTrapLogParam1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlmTrapLogParam1_Type.__name__ = "OctetString"
_SlmTrapLogParam1_Object = MibTableColumn
slmTrapLogParam1 = _SlmTrapLogParam1_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 4),
    _SlmTrapLogParam1_Type()
)
slmTrapLogParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogParam1.setStatus("current")


class _SlmTrapLogParam2_Type(OctetString):
    """Custom type slmTrapLogParam2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlmTrapLogParam2_Type.__name__ = "OctetString"
_SlmTrapLogParam2_Object = MibTableColumn
slmTrapLogParam2 = _SlmTrapLogParam2_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 5),
    _SlmTrapLogParam2_Type()
)
slmTrapLogParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogParam2.setStatus("current")


class _SlmTrapLogParam3_Type(OctetString):
    """Custom type slmTrapLogParam3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlmTrapLogParam3_Type.__name__ = "OctetString"
_SlmTrapLogParam3_Object = MibTableColumn
slmTrapLogParam3 = _SlmTrapLogParam3_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 6),
    _SlmTrapLogParam3_Type()
)
slmTrapLogParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogParam3.setStatus("current")


class _SlmTrapLogParam4_Type(OctetString):
    """Custom type slmTrapLogParam4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlmTrapLogParam4_Type.__name__ = "OctetString"
_SlmTrapLogParam4_Object = MibTableColumn
slmTrapLogParam4 = _SlmTrapLogParam4_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 7),
    _SlmTrapLogParam4_Type()
)
slmTrapLogParam4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogParam4.setStatus("current")


class _SlmTrapLogParam5_Type(OctetString):
    """Custom type slmTrapLogParam5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlmTrapLogParam5_Type.__name__ = "OctetString"
_SlmTrapLogParam5_Object = MibTableColumn
slmTrapLogParam5 = _SlmTrapLogParam5_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 8),
    _SlmTrapLogParam5_Type()
)
slmTrapLogParam5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogParam5.setStatus("current")


class _SlmTrapLogParam6_Type(OctetString):
    """Custom type slmTrapLogParam6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlmTrapLogParam6_Type.__name__ = "OctetString"
_SlmTrapLogParam6_Object = MibTableColumn
slmTrapLogParam6 = _SlmTrapLogParam6_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 2, 1, 9),
    _SlmTrapLogParam6_Type()
)
slmTrapLogParam6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmTrapLogParam6.setStatus("current")
_SlmSyslogDestTable_Object = MibTable
slmSyslogDestTable = _SlmSyslogDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7)
)
if mibBuilder.loadTexts:
    slmSyslogDestTable.setStatus("current")
_SlmSyslogDestEntry_Object = MibTableRow
slmSyslogDestEntry = _SlmSyslogDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1)
)
slmSyslogDestEntry.setIndexNames(
    (0, "SL-MAIN-MIB", "slmSyslogDestAddress"),
)
if mibBuilder.loadTexts:
    slmSyslogDestEntry.setStatus("current")
_SlmSyslogDestAddress_Type = Integer32
_SlmSyslogDestAddress_Object = MibTableColumn
slmSyslogDestAddress = _SlmSyslogDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 1),
    _SlmSyslogDestAddress_Type()
)
slmSyslogDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmSyslogDestAddress.setStatus("current")
_SlmSyslogDestRowStatus_Type = RowStatus
_SlmSyslogDestRowStatus_Object = MibTableColumn
slmSyslogDestRowStatus = _SlmSyslogDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 2),
    _SlmSyslogDestRowStatus_Type()
)
slmSyslogDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmSyslogDestRowStatus.setStatus("current")


class _SlmSyslogLevel_Type(Integer32):
    """Custom type slmSyslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("traps", 1),
          ("log", 2),
          ("debug", 3))
    )


_SlmSyslogLevel_Type.__name__ = "Integer32"
_SlmSyslogLevel_Object = MibTableColumn
slmSyslogLevel = _SlmSyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 3),
    _SlmSyslogLevel_Type()
)
slmSyslogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmSyslogLevel.setStatus("current")
_SlmSyslogPort_Type = Integer32
_SlmSyslogPort_Object = MibTableColumn
slmSyslogPort = _SlmSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 4),
    _SlmSyslogPort_Type()
)
slmSyslogPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmSyslogPort.setStatus("current")
_SlmSyslogDestIpAddress_Type = IpAddress
_SlmSyslogDestIpAddress_Object = MibTableColumn
slmSyslogDestIpAddress = _SlmSyslogDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 7, 1, 5),
    _SlmSyslogDestIpAddress_Type()
)
slmSyslogDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slmSyslogDestIpAddress.setStatus("current")
_SlmLogFile_ObjectIdentity = ObjectIdentity
slmLogFile = _SlmLogFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 8)
)
_SlmConfigFile_ObjectIdentity = ObjectIdentity
slmConfigFile = _SlmConfigFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 9)
)
_SlmChPass_ObjectIdentity = ObjectIdentity
slmChPass = _SlmChPass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 12)
)
_SlmChPassTable_Object = MibTable
slmChPassTable = _SlmChPassTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1)
)
if mibBuilder.loadTexts:
    slmChPassTable.setStatus("current")
_SlmChPassEntry_Object = MibTableRow
slmChPassEntry = _SlmChPassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1, 1)
)
slmChPassEntry.setIndexNames(
    (0, "SL-MAIN-MIB", "slmChPassLogin"),
    (0, "SL-MAIN-MIB", "slmChPassOldPass"),
)
if mibBuilder.loadTexts:
    slmChPassEntry.setStatus("current")
_SlmChPassLogin_Type = UserLogin
_SlmChPassLogin_Object = MibTableColumn
slmChPassLogin = _SlmChPassLogin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1, 1, 1),
    _SlmChPassLogin_Type()
)
slmChPassLogin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slmChPassLogin.setStatus("current")
_SlmChPassOldPass_Type = UserPassword
_SlmChPassOldPass_Object = MibTableColumn
slmChPassOldPass = _SlmChPassOldPass_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1, 1, 2),
    _SlmChPassOldPass_Type()
)
slmChPassOldPass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slmChPassOldPass.setStatus("current")
_SlmChPassNewPass_Type = UserPassword
_SlmChPassNewPass_Object = MibTableColumn
slmChPassNewPass = _SlmChPassNewPass_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 12, 1, 1, 3),
    _SlmChPassNewPass_Type()
)
slmChPassNewPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmChPassNewPass.setStatus("current")
_SlmLicense_ObjectIdentity = ObjectIdentity
slmLicense = _SlmLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 17)
)
_SlmLicenseTable_Object = MibTable
slmLicenseTable = _SlmLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1)
)
if mibBuilder.loadTexts:
    slmLicenseTable.setStatus("current")
_SlmLicenseEntry_Object = MibTableRow
slmLicenseEntry = _SlmLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1, 1)
)
slmLicenseEntry.setIndexNames(
    (0, "SL-MAIN-MIB", "slmLicenseIndex"),
)
if mibBuilder.loadTexts:
    slmLicenseEntry.setStatus("current")
_SlmLicenseIndex_Type = Integer32
_SlmLicenseIndex_Object = MibTableColumn
slmLicenseIndex = _SlmLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1, 1, 1),
    _SlmLicenseIndex_Type()
)
slmLicenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmLicenseIndex.setStatus("current")
_SlmLicenseExpiration_Type = Integer32
_SlmLicenseExpiration_Object = MibTableColumn
slmLicenseExpiration = _SlmLicenseExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1, 1, 2),
    _SlmLicenseExpiration_Type()
)
slmLicenseExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmLicenseExpiration.setStatus("current")


class _SlmLicenseId_Type(DisplayString):
    """Custom type slmLicenseId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlmLicenseId_Type.__name__ = "DisplayString"
_SlmLicenseId_Object = MibTableColumn
slmLicenseId = _SlmLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 17, 1, 1, 3),
    _SlmLicenseId_Type()
)
slmLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slmLicenseId.setStatus("current")

# Managed Objects groups


# Notification objects

slmTrapSoftwareStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 4)
)
slmTrapSoftwareStatusChange.setObjects(
      *(("SL-MAIN-MIB", "slmSwRevDirectory"),
        ("SL-MAIN-MIB", "slmSwRevStatus"))
)
if mibBuilder.loadTexts:
    slmTrapSoftwareStatusChange.setStatus(
        "current"
    )

slmTrapSysNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 5)
)
slmTrapSysNameChange.setObjects(
    ("SL-MAIN-MIB", "slmSysName")
)
if mibBuilder.loadTexts:
    slmTrapSysNameChange.setStatus(
        "current"
    )

slmTrapSysLocationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 5, 6)
)
slmTrapSysLocationChange.setObjects(
    ("SL-MAIN-MIB", "slmSysLocation")
)
if mibBuilder.loadTexts:
    slmTrapSysLocationChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-MAIN-MIB",
    **{"UserLogin": UserLogin,
       "UserPassword": UserPassword,
       "UserCommunity": UserCommunity,
       "SoftwareRevision": SoftwareRevision,
       "AdminAccess": AdminAccess,
       "slMain": slMain,
       "slmSys": slmSys,
       "slmSysGatewayAddr": slmSysGatewayAddr,
       "slmSysSubnetMask": slmSysSubnetMask,
       "slmSysIpAddr": slmSysIpAddr,
       "slmSysAlmAct": slmSysAlmAct,
       "slmSysAlmDeact": slmSysAlmDeact,
       "slmSysAdminStatus": slmSysAdminStatus,
       "slmSysOperStatus": slmSysOperStatus,
       "slmBoxSize": slmBoxSize,
       "slmSysCalendarTime": slmSysCalendarTime,
       "slmSysPmStartOfDay": slmSysPmStartOfDay,
       "slmSysActiveSwVersion": slmSysActiveSwVersion,
       "slmSwRevTable": slmSwRevTable,
       "slmSwRevEntry": slmSwRevEntry,
       "slmSwRevDirectory": slmSwRevDirectory,
       "slmSwRevStatus": slmSwRevStatus,
       "slmSwRevName": slmSwRevName,
       "slmSwRevDate": slmSwRevDate,
       "slmConfigSysUptime": slmConfigSysUptime,
       "slmConfigSysSignalType": slmConfigSysSignalType,
       "slmRebootDelay": slmRebootDelay,
       "slmVcatDelay": slmVcatDelay,
       "slmTid": slmTid,
       "slmPsuNumber": slmPsuNumber,
       "slmOemType": slmOemType,
       "slmSysName": slmSysName,
       "slmSysLocation": slmSysLocation,
       "slmSysResetPm": slmSysResetPm,
       "slmSysUplinkRate": slmSysUplinkRate,
       "slmSysChassisId": slmSysChassisId,
       "slmSysNetworkPrefix": slmSysNetworkPrefix,
       "slmSysLanIpAddr": slmSysLanIpAddr,
       "slmSysLanSubnetAddr": slmSysLanSubnetAddr,
       "slmPmAvailable": slmPmAvailable,
       "slmPortsNumber": slmPortsNumber,
       "slmEdfaNumber": slmEdfaNumber,
       "slmMuxNumber": slmMuxNumber,
       "slmOpticalSwitchExist": slmOpticalSwitchExist,
       "slmReadCommunity": slmReadCommunity,
       "slmWriteCommunity": slmWriteCommunity,
       "slmSysEffectiveSubnetMask": slmSysEffectiveSubnetMask,
       "slmSysEffectiveIpAddr": slmSysEffectiveIpAddr,
       "slmSysLanEffectiveIpAddr": slmSysLanEffectiveIpAddr,
       "slmSysLanEffectiveSubnetAddr": slmSysLanEffectiveSubnetAddr,
       "slmSysGatewayEffectiveIpAddr": slmSysGatewayEffectiveIpAddr,
       "slmSysMode": slmSysMode,
       "slmSysTrapFormat": slmSysTrapFormat,
       "slmSysTemperature": slmSysTemperature,
       "slmNetworkMode": slmNetworkMode,
       "slm40GConf": slm40GConf,
       "slmRstpEnabled": slmRstpEnabled,
       "slmTopologyEnabled": slmTopologyEnabled,
       "slmAdminCommunity": slmAdminCommunity,
       "slmTrapCommunity": slmTrapCommunity,
       "slmSysSnmpVersion": slmSysSnmpVersion,
       "slmSysEncryptionCapability": slmSysEncryptionCapability,
       "slmAdmin": slmAdmin,
       "slmAdminTable": slmAdminTable,
       "slmAdminEntry": slmAdminEntry,
       "slmAdminLogin": slmAdminLogin,
       "slmAdminPassword": slmAdminPassword,
       "slmAdminRowStatus": slmAdminRowStatus,
       "slmAdminAccess": slmAdminAccess,
       "slmSnmpv3Auth": slmSnmpv3Auth,
       "slmSnmpv3Priv": slmSnmpv3Priv,
       "slmSnmpv3Password": slmSnmpv3Password,
       "slmAuth": slmAuth,
       "slmAuthTable": slmAuthTable,
       "slmAuthEntry": slmAuthEntry,
       "slmAuthLogin": slmAuthLogin,
       "slmAuthPassword": slmAuthPassword,
       "slmAuthCommunity": slmAuthCommunity,
       "slmLogin": slmLogin,
       "slmTrap": slmTrap,
       "slmTrapDestTable": slmTrapDestTable,
       "slmTrapDestEntry": slmTrapDestEntry,
       "slmTrapDestAddress": slmTrapDestAddress,
       "slmTrapDestRowStatus": slmTrapDestRowStatus,
       "slmTrapDestCommunity": slmTrapDestCommunity,
       "slmTrapDestProtVersion": slmTrapDestProtVersion,
       "slmTrapUserLogin": slmTrapUserLogin,
       "slmTrapUserAccess": slmTrapUserAccess,
       "slmTrapEnable": slmTrapEnable,
       "slmTrapPort": slmTrapPort,
       "slmTrapDestIpAddress": slmTrapDestIpAddress,
       "slmTrapLogTable": slmTrapLogTable,
       "slmTrapLogEntry": slmTrapLogEntry,
       "slmTrapLogId": slmTrapLogId,
       "slmTrapLogName": slmTrapLogName,
       "slmTrapLogTimeStamp": slmTrapLogTimeStamp,
       "slmTrapLogParam1": slmTrapLogParam1,
       "slmTrapLogParam2": slmTrapLogParam2,
       "slmTrapLogParam3": slmTrapLogParam3,
       "slmTrapLogParam4": slmTrapLogParam4,
       "slmTrapLogParam5": slmTrapLogParam5,
       "slmTrapLogParam6": slmTrapLogParam6,
       "slmTrapSoftwareStatusChange": slmTrapSoftwareStatusChange,
       "slmTrapSysNameChange": slmTrapSysNameChange,
       "slmTrapSysLocationChange": slmTrapSysLocationChange,
       "slmSyslogDestTable": slmSyslogDestTable,
       "slmSyslogDestEntry": slmSyslogDestEntry,
       "slmSyslogDestAddress": slmSyslogDestAddress,
       "slmSyslogDestRowStatus": slmSyslogDestRowStatus,
       "slmSyslogLevel": slmSyslogLevel,
       "slmSyslogPort": slmSyslogPort,
       "slmSyslogDestIpAddress": slmSyslogDestIpAddress,
       "slmLogFile": slmLogFile,
       "slmConfigFile": slmConfigFile,
       "slmChPass": slmChPass,
       "slmChPassTable": slmChPassTable,
       "slmChPassEntry": slmChPassEntry,
       "slmChPassLogin": slmChPassLogin,
       "slmChPassOldPass": slmChPassOldPass,
       "slmChPassNewPass": slmChPassNewPass,
       "slmLicense": slmLicense,
       "slmLicenseTable": slmLicenseTable,
       "slmLicenseEntry": slmLicenseEntry,
       "slmLicenseIndex": slmLicenseIndex,
       "slmLicenseExpiration": slmLicenseExpiration,
       "slmLicenseId": slmLicenseId}
)
