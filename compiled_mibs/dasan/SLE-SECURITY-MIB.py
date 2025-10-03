# SNMP MIB module (SLE-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-SECURITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:02 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(SleControlRequestResultType,
 SleControlStatusType,
 SlePermissionType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType",
    "SlePermissionType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

sleSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleSecurityBase_ObjectIdentity = ObjectIdentity
sleSecurityBase = _SleSecurityBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1)
)
_SleSecurityBaseInfo_ObjectIdentity = ObjectIdentity
sleSecurityBaseInfo = _SleSecurityBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1)
)
_SleSecurityRadiusRetransmissions_Type = Integer32
_SleSecurityRadiusRetransmissions_Object = MibScalar
sleSecurityRadiusRetransmissions = _SleSecurityRadiusRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 1),
    _SleSecurityRadiusRetransmissions_Type()
)
sleSecurityRadiusRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityRadiusRetransmissions.setStatus("current")
_SleSecurityRadiusTimeouts_Type = Integer32
_SleSecurityRadiusTimeouts_Object = MibScalar
sleSecurityRadiusTimeouts = _SleSecurityRadiusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 2),
    _SleSecurityRadiusTimeouts_Type()
)
sleSecurityRadiusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityRadiusTimeouts.setStatus("current")


class _SleSecurityRadiusInterfaceName_Type(OctetString):
    """Custom type sleSecurityRadiusInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleSecurityRadiusInterfaceName_Type.__name__ = "OctetString"
_SleSecurityRadiusInterfaceName_Object = MibScalar
sleSecurityRadiusInterfaceName = _SleSecurityRadiusInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 3),
    _SleSecurityRadiusInterfaceName_Type()
)
sleSecurityRadiusInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityRadiusInterfaceName.setStatus("current")
_SleSecurityRadiusInterfaceAddress_Type = IpAddress
_SleSecurityRadiusInterfaceAddress_Object = MibScalar
sleSecurityRadiusInterfaceAddress = _SleSecurityRadiusInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 4),
    _SleSecurityRadiusInterfaceAddress_Type()
)
sleSecurityRadiusInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityRadiusInterfaceAddress.setStatus("current")


class _SleSecurityTacacsInterfaceName_Type(OctetString):
    """Custom type sleSecurityTacacsInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleSecurityTacacsInterfaceName_Type.__name__ = "OctetString"
_SleSecurityTacacsInterfaceName_Object = MibScalar
sleSecurityTacacsInterfaceName = _SleSecurityTacacsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 5),
    _SleSecurityTacacsInterfaceName_Type()
)
sleSecurityTacacsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityTacacsInterfaceName.setStatus("current")
_SleSecurityTacacsInterfaceAddress_Type = IpAddress
_SleSecurityTacacsInterfaceAddress_Object = MibScalar
sleSecurityTacacsInterfaceAddress = _SleSecurityTacacsInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 6),
    _SleSecurityTacacsInterfaceAddress_Type()
)
sleSecurityTacacsInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityTacacsInterfaceAddress.setStatus("current")


class _SleSecurityTacacsPort_Type(Integer32):
    """Custom type sleSecurityTacacsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSecurityTacacsPort_Type.__name__ = "Integer32"
_SleSecurityTacacsPort_Object = MibScalar
sleSecurityTacacsPort = _SleSecurityTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 7),
    _SleSecurityTacacsPort_Type()
)
sleSecurityTacacsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityTacacsPort.setStatus("current")


class _SleSecurityTacacsAuthType_Type(Integer32):
    """Custom type sleSecurityTacacsAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("pap", 1),
          ("chap", 2))
    )


_SleSecurityTacacsAuthType_Type.__name__ = "Integer32"
_SleSecurityTacacsAuthType_Object = MibScalar
sleSecurityTacacsAuthType = _SleSecurityTacacsAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 8),
    _SleSecurityTacacsAuthType_Type()
)
sleSecurityTacacsAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityTacacsAuthType.setStatus("current")
_SleSecurityTacacsTimeouts_Type = Integer32
_SleSecurityTacacsTimeouts_Object = MibScalar
sleSecurityTacacsTimeouts = _SleSecurityTacacsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 9),
    _SleSecurityTacacsTimeouts_Type()
)
sleSecurityTacacsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityTacacsTimeouts.setStatus("current")


class _SleSecurityTacacsPriorityLevel_Type(Integer32):
    """Custom type sleSecurityTacacsPriorityLevel based on Integer32"""
    defaultValue = 1

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
        *(("max", 0),
          ("min", 1),
          ("root", 2),
          ("user", 3))
    )


_SleSecurityTacacsPriorityLevel_Type.__name__ = "Integer32"
_SleSecurityTacacsPriorityLevel_Object = MibScalar
sleSecurityTacacsPriorityLevel = _SleSecurityTacacsPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 10),
    _SleSecurityTacacsPriorityLevel_Type()
)
sleSecurityTacacsPriorityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityTacacsPriorityLevel.setStatus("current")


class _SleSecurityDot1xActivity_Type(Integer32):
    """Custom type sleSecurityDot1xActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityDot1xActivity_Type.__name__ = "Integer32"
_SleSecurityDot1xActivity_Object = MibScalar
sleSecurityDot1xActivity = _SleSecurityDot1xActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 11),
    _SleSecurityDot1xActivity_Type()
)
sleSecurityDot1xActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityDot1xActivity.setStatus("current")
_SleSecurityLoginLimits_Type = Integer32
_SleSecurityLoginLimits_Object = MibScalar
sleSecurityLoginLimits = _SleSecurityLoginLimits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 12),
    _SleSecurityLoginLimits_Type()
)
sleSecurityLoginLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityLoginLimits.setStatus("current")


class _SleSecurityLoginLockAttemptsCount_Type(Integer32):
    """Custom type sleSecurityLoginLockAttemptsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_SleSecurityLoginLockAttemptsCount_Type.__name__ = "Integer32"
_SleSecurityLoginLockAttemptsCount_Object = MibScalar
sleSecurityLoginLockAttemptsCount = _SleSecurityLoginLockAttemptsCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 13),
    _SleSecurityLoginLockAttemptsCount_Type()
)
sleSecurityLoginLockAttemptsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityLoginLockAttemptsCount.setStatus("current")


class _SleSecurityLoginLockDelayTime_Type(Integer32):
    """Custom type sleSecurityLoginLockDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SleSecurityLoginLockDelayTime_Type.__name__ = "Integer32"
_SleSecurityLoginLockDelayTime_Object = MibScalar
sleSecurityLoginLockDelayTime = _SleSecurityLoginLockDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 14),
    _SleSecurityLoginLockDelayTime_Type()
)
sleSecurityLoginLockDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityLoginLockDelayTime.setStatus("current")


class _SleSecurityLoginAccountingMode_Type(Integer32):
    """Custom type sleSecurityLoginAccountingMode based on Integer32"""
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
        *(("none", 0),
          ("start", 1),
          ("stop", 2),
          ("both", 3))
    )


_SleSecurityLoginAccountingMode_Type.__name__ = "Integer32"
_SleSecurityLoginAccountingMode_Object = MibScalar
sleSecurityLoginAccountingMode = _SleSecurityLoginAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 1, 15),
    _SleSecurityLoginAccountingMode_Type()
)
sleSecurityLoginAccountingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityLoginAccountingMode.setStatus("current")
_SleSecurityBaseControl_ObjectIdentity = ObjectIdentity
sleSecurityBaseControl = _SleSecurityBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2)
)


class _SleSecurityControlRequest_Type(Integer32):
    """Custom type sleSecurityControlRequest based on Integer32"""
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
        *(("setSecurityBaseRadiusProfile", 1),
          ("setSecurityBaseTacacsProfile", 2),
          ("setSecurityBaseDot1xActivity", 3),
          ("setSecurityBaseLoginLimits", 4),
          ("setSecurityBaseLoginLockConf", 5),
          ("destroySecurityBaseLoginLockConf", 6),
          ("setLoginAccountingMode", 7))
    )


_SleSecurityControlRequest_Type.__name__ = "Integer32"
_SleSecurityControlRequest_Object = MibScalar
sleSecurityControlRequest = _SleSecurityControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 1),
    _SleSecurityControlRequest_Type()
)
sleSecurityControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlRequest.setStatus("current")
_SleSecurityControlStatus_Type = SleControlStatusType
_SleSecurityControlStatus_Object = MibScalar
sleSecurityControlStatus = _SleSecurityControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 2),
    _SleSecurityControlStatus_Type()
)
sleSecurityControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityControlStatus.setStatus("current")
_SleSecurityControlTimer_Type = Gauge32
_SleSecurityControlTimer_Object = MibScalar
sleSecurityControlTimer = _SleSecurityControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 3),
    _SleSecurityControlTimer_Type()
)
sleSecurityControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlTimer.setStatus("current")
_SleSecurityControlTimeStamp_Type = TimeStamp
_SleSecurityControlTimeStamp_Object = MibScalar
sleSecurityControlTimeStamp = _SleSecurityControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 4),
    _SleSecurityControlTimeStamp_Type()
)
sleSecurityControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityControlTimeStamp.setStatus("current")
_SleSecurityControlReqResult_Type = SleControlRequestResultType
_SleSecurityControlReqResult_Object = MibScalar
sleSecurityControlReqResult = _SleSecurityControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 5),
    _SleSecurityControlReqResult_Type()
)
sleSecurityControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityControlReqResult.setStatus("current")
_SleSecurityControlRadiusRetransmissions_Type = Integer32
_SleSecurityControlRadiusRetransmissions_Object = MibScalar
sleSecurityControlRadiusRetransmissions = _SleSecurityControlRadiusRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 6),
    _SleSecurityControlRadiusRetransmissions_Type()
)
sleSecurityControlRadiusRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlRadiusRetransmissions.setStatus("current")
_SleSecurityControlRadiusTimeouts_Type = Integer32
_SleSecurityControlRadiusTimeouts_Object = MibScalar
sleSecurityControlRadiusTimeouts = _SleSecurityControlRadiusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 7),
    _SleSecurityControlRadiusTimeouts_Type()
)
sleSecurityControlRadiusTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlRadiusTimeouts.setStatus("current")


class _SleSecurityControlRadiusInterfaceName_Type(OctetString):
    """Custom type sleSecurityControlRadiusInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleSecurityControlRadiusInterfaceName_Type.__name__ = "OctetString"
_SleSecurityControlRadiusInterfaceName_Object = MibScalar
sleSecurityControlRadiusInterfaceName = _SleSecurityControlRadiusInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 8),
    _SleSecurityControlRadiusInterfaceName_Type()
)
sleSecurityControlRadiusInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlRadiusInterfaceName.setStatus("current")
_SleSecurityControlRadiusInterfaceAddress_Type = IpAddress
_SleSecurityControlRadiusInterfaceAddress_Object = MibScalar
sleSecurityControlRadiusInterfaceAddress = _SleSecurityControlRadiusInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 9),
    _SleSecurityControlRadiusInterfaceAddress_Type()
)
sleSecurityControlRadiusInterfaceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlRadiusInterfaceAddress.setStatus("current")


class _SleSecurityControlTacacsInterfaceName_Type(OctetString):
    """Custom type sleSecurityControlTacacsInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleSecurityControlTacacsInterfaceName_Type.__name__ = "OctetString"
_SleSecurityControlTacacsInterfaceName_Object = MibScalar
sleSecurityControlTacacsInterfaceName = _SleSecurityControlTacacsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 10),
    _SleSecurityControlTacacsInterfaceName_Type()
)
sleSecurityControlTacacsInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlTacacsInterfaceName.setStatus("current")
_SleSecurityControlTacacsInterfaceAddress_Type = IpAddress
_SleSecurityControlTacacsInterfaceAddress_Object = MibScalar
sleSecurityControlTacacsInterfaceAddress = _SleSecurityControlTacacsInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 11),
    _SleSecurityControlTacacsInterfaceAddress_Type()
)
sleSecurityControlTacacsInterfaceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlTacacsInterfaceAddress.setStatus("current")


class _SleSecurityControlTacacsPort_Type(Integer32):
    """Custom type sleSecurityControlTacacsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSecurityControlTacacsPort_Type.__name__ = "Integer32"
_SleSecurityControlTacacsPort_Object = MibScalar
sleSecurityControlTacacsPort = _SleSecurityControlTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 12),
    _SleSecurityControlTacacsPort_Type()
)
sleSecurityControlTacacsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlTacacsPort.setStatus("current")


class _SleSecurityControlTacacsAuthType_Type(Integer32):
    """Custom type sleSecurityControlTacacsAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("pap", 1),
          ("chap", 2))
    )


_SleSecurityControlTacacsAuthType_Type.__name__ = "Integer32"
_SleSecurityControlTacacsAuthType_Object = MibScalar
sleSecurityControlTacacsAuthType = _SleSecurityControlTacacsAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 13),
    _SleSecurityControlTacacsAuthType_Type()
)
sleSecurityControlTacacsAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlTacacsAuthType.setStatus("current")
_SleSecurityControlTacacsTimeouts_Type = Integer32
_SleSecurityControlTacacsTimeouts_Object = MibScalar
sleSecurityControlTacacsTimeouts = _SleSecurityControlTacacsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 14),
    _SleSecurityControlTacacsTimeouts_Type()
)
sleSecurityControlTacacsTimeouts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlTacacsTimeouts.setStatus("current")


class _SleSecurityControlTacacsPriorityLevel_Type(Integer32):
    """Custom type sleSecurityControlTacacsPriorityLevel based on Integer32"""
    defaultValue = 1

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
        *(("max", 0),
          ("min", 1),
          ("root", 2),
          ("user", 3))
    )


_SleSecurityControlTacacsPriorityLevel_Type.__name__ = "Integer32"
_SleSecurityControlTacacsPriorityLevel_Object = MibScalar
sleSecurityControlTacacsPriorityLevel = _SleSecurityControlTacacsPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 15),
    _SleSecurityControlTacacsPriorityLevel_Type()
)
sleSecurityControlTacacsPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlTacacsPriorityLevel.setStatus("current")


class _SleSecurityControlDot1xActivity_Type(Integer32):
    """Custom type sleSecurityControlDot1xActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityControlDot1xActivity_Type.__name__ = "Integer32"
_SleSecurityControlDot1xActivity_Object = MibScalar
sleSecurityControlDot1xActivity = _SleSecurityControlDot1xActivity_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 16),
    _SleSecurityControlDot1xActivity_Type()
)
sleSecurityControlDot1xActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlDot1xActivity.setStatus("current")
_SleSecurityControlLoginLimits_Type = Integer32
_SleSecurityControlLoginLimits_Object = MibScalar
sleSecurityControlLoginLimits = _SleSecurityControlLoginLimits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 17),
    _SleSecurityControlLoginLimits_Type()
)
sleSecurityControlLoginLimits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlLoginLimits.setStatus("current")


class _SleSecurityControlLoginLockAttemptsCount_Type(Integer32):
    """Custom type sleSecurityControlLoginLockAttemptsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_SleSecurityControlLoginLockAttemptsCount_Type.__name__ = "Integer32"
_SleSecurityControlLoginLockAttemptsCount_Object = MibScalar
sleSecurityControlLoginLockAttemptsCount = _SleSecurityControlLoginLockAttemptsCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 18),
    _SleSecurityControlLoginLockAttemptsCount_Type()
)
sleSecurityControlLoginLockAttemptsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlLoginLockAttemptsCount.setStatus("current")


class _SleSecurityControlLoginLockDelayTime_Type(Integer32):
    """Custom type sleSecurityControlLoginLockDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SleSecurityControlLoginLockDelayTime_Type.__name__ = "Integer32"
_SleSecurityControlLoginLockDelayTime_Object = MibScalar
sleSecurityControlLoginLockDelayTime = _SleSecurityControlLoginLockDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 19),
    _SleSecurityControlLoginLockDelayTime_Type()
)
sleSecurityControlLoginLockDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityControlLoginLockDelayTime.setStatus("current")


class _SleSecurityControlLoginAccountingMode_Type(Integer32):
    """Custom type sleSecurityControlLoginAccountingMode based on Integer32"""
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
        *(("none", 0),
          ("start", 1),
          ("stop", 2),
          ("both", 3))
    )


_SleSecurityControlLoginAccountingMode_Type.__name__ = "Integer32"
_SleSecurityControlLoginAccountingMode_Object = MibScalar
sleSecurityControlLoginAccountingMode = _SleSecurityControlLoginAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 2, 20),
    _SleSecurityControlLoginAccountingMode_Type()
)
sleSecurityControlLoginAccountingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityControlLoginAccountingMode.setStatus("current")
_SleSecurityBaseNotification_ObjectIdentity = ObjectIdentity
sleSecurityBaseNotification = _SleSecurityBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 3)
)
_SleAAA_ObjectIdentity = ObjectIdentity
sleAAA = _SleAAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2)
)
_SleAaaTable_Object = MibTable
sleAaaTable = _SleAaaTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 1)
)
if mibBuilder.loadTexts:
    sleAaaTable.setStatus("current")
_SleAaaEntry_Object = MibTableRow
sleAaaEntry = _SleAaaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 1, 1)
)
sleAaaEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleAaaSession"),
    (0, "SLE-SECURITY-MIB", "sleAaaAuthen"),
)
if mibBuilder.loadTexts:
    sleAaaEntry.setStatus("current")


class _SleAaaSession_Type(Integer32):
    """Custom type sleAaaSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("remote", 2))
    )


_SleAaaSession_Type.__name__ = "Integer32"
_SleAaaSession_Object = MibTableColumn
sleAaaSession = _SleAaaSession_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 1, 1, 1),
    _SleAaaSession_Type()
)
sleAaaSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAaaSession.setStatus("current")


class _SleAaaAuthen_Type(Integer32):
    """Custom type sleAaaAuthen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("radius", 2),
          ("tacacs", 3))
    )


_SleAaaAuthen_Type.__name__ = "Integer32"
_SleAaaAuthen_Object = MibTableColumn
sleAaaAuthen = _SleAaaAuthen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 1, 1, 2),
    _SleAaaAuthen_Type()
)
sleAaaAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAaaAuthen.setStatus("current")


class _SleAaaEnable_Type(Integer32):
    """Custom type sleAaaEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleAaaEnable_Type.__name__ = "Integer32"
_SleAaaEnable_Object = MibTableColumn
sleAaaEnable = _SleAaaEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 1, 1, 3),
    _SleAaaEnable_Type()
)
sleAaaEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAaaEnable.setStatus("current")


class _SleAaaPrimarySequence_Type(Integer32):
    """Custom type sleAaaPrimarySequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SleAaaPrimarySequence_Type.__name__ = "Integer32"
_SleAaaPrimarySequence_Object = MibTableColumn
sleAaaPrimarySequence = _SleAaaPrimarySequence_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 1, 1, 4),
    _SleAaaPrimarySequence_Type()
)
sleAaaPrimarySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAaaPrimarySequence.setStatus("current")
_SleAaaControl_ObjectIdentity = ObjectIdentity
sleAaaControl = _SleAaaControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2)
)


class _SleAaaControlRequest_Type(Integer32):
    """Custom type sleAaaControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setAaaProfile", 1)
    )


_SleAaaControlRequest_Type.__name__ = "Integer32"
_SleAaaControlRequest_Object = MibScalar
sleAaaControlRequest = _SleAaaControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 1),
    _SleAaaControlRequest_Type()
)
sleAaaControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAaaControlRequest.setStatus("current")
_SleAaaControlStatus_Type = SleControlStatusType
_SleAaaControlStatus_Object = MibScalar
sleAaaControlStatus = _SleAaaControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 2),
    _SleAaaControlStatus_Type()
)
sleAaaControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAaaControlStatus.setStatus("current")
_SleAaaControlTimer_Type = Gauge32
_SleAaaControlTimer_Object = MibScalar
sleAaaControlTimer = _SleAaaControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 3),
    _SleAaaControlTimer_Type()
)
sleAaaControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAaaControlTimer.setStatus("current")
_SleAaaControlTimeStamp_Type = TimeStamp
_SleAaaControlTimeStamp_Object = MibScalar
sleAaaControlTimeStamp = _SleAaaControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 4),
    _SleAaaControlTimeStamp_Type()
)
sleAaaControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAaaControlTimeStamp.setStatus("current")
_SleAaaControlReqResult_Type = SleControlRequestResultType
_SleAaaControlReqResult_Object = MibScalar
sleAaaControlReqResult = _SleAaaControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 5),
    _SleAaaControlReqResult_Type()
)
sleAaaControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAaaControlReqResult.setStatus("current")


class _SleAaaControlSession_Type(Integer32):
    """Custom type sleAaaControlSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("remote", 2))
    )


_SleAaaControlSession_Type.__name__ = "Integer32"
_SleAaaControlSession_Object = MibScalar
sleAaaControlSession = _SleAaaControlSession_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 6),
    _SleAaaControlSession_Type()
)
sleAaaControlSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAaaControlSession.setStatus("current")


class _SleAaaControlAuthen_Type(Integer32):
    """Custom type sleAaaControlAuthen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("radius", 2),
          ("tacacs", 3))
    )


_SleAaaControlAuthen_Type.__name__ = "Integer32"
_SleAaaControlAuthen_Object = MibScalar
sleAaaControlAuthen = _SleAaaControlAuthen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 7),
    _SleAaaControlAuthen_Type()
)
sleAaaControlAuthen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAaaControlAuthen.setStatus("current")


class _SleAaaControlEnable_Type(Integer32):
    """Custom type sleAaaControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleAaaControlEnable_Type.__name__ = "Integer32"
_SleAaaControlEnable_Object = MibScalar
sleAaaControlEnable = _SleAaaControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 8),
    _SleAaaControlEnable_Type()
)
sleAaaControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAaaControlEnable.setStatus("current")


class _SleAaaControlPrimaryFlag_Type(Integer32):
    """Custom type sleAaaControlPrimaryFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleAaaControlPrimaryFlag_Type.__name__ = "Integer32"
_SleAaaControlPrimaryFlag_Object = MibScalar
sleAaaControlPrimaryFlag = _SleAaaControlPrimaryFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 2, 9),
    _SleAaaControlPrimaryFlag_Type()
)
sleAaaControlPrimaryFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAaaControlPrimaryFlag.setStatus("current")
_SleAaaNotification_ObjectIdentity = ObjectIdentity
sleAaaNotification = _SleAaaNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 3)
)
_SleRadiusServer_ObjectIdentity = ObjectIdentity
sleRadiusServer = _SleRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3)
)
_SleRadiusServerTable_Object = MibTable
sleRadiusServerTable = _SleRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 1)
)
if mibBuilder.loadTexts:
    sleRadiusServerTable.setStatus("current")
_SleRadiusServerEntry_Object = MibTableRow
sleRadiusServerEntry = _SleRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 1, 1)
)
sleRadiusServerEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleRadiusServerAddress"),
)
if mibBuilder.loadTexts:
    sleRadiusServerEntry.setStatus("current")
_SleRadiusServerAddress_Type = IpAddress
_SleRadiusServerAddress_Object = MibTableColumn
sleRadiusServerAddress = _SleRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 1, 1, 1),
    _SleRadiusServerAddress_Type()
)
sleRadiusServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerAddress.setStatus("current")


class _SleRadiusServerClientKey_Type(OctetString):
    """Custom type sleRadiusServerClientKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleRadiusServerClientKey_Type.__name__ = "OctetString"
_SleRadiusServerClientKey_Object = MibTableColumn
sleRadiusServerClientKey = _SleRadiusServerClientKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 1, 1, 2),
    _SleRadiusServerClientKey_Type()
)
sleRadiusServerClientKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerClientKey.setStatus("current")


class _SleRadiusServerAuthPort_Type(Integer32):
    """Custom type sleRadiusServerAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRadiusServerAuthPort_Type.__name__ = "Integer32"
_SleRadiusServerAuthPort_Object = MibTableColumn
sleRadiusServerAuthPort = _SleRadiusServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 1, 1, 3),
    _SleRadiusServerAuthPort_Type()
)
sleRadiusServerAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerAuthPort.setStatus("current")


class _SleRadiusServerAccPort_Type(Integer32):
    """Custom type sleRadiusServerAccPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRadiusServerAccPort_Type.__name__ = "Integer32"
_SleRadiusServerAccPort_Object = MibTableColumn
sleRadiusServerAccPort = _SleRadiusServerAccPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 1, 1, 4),
    _SleRadiusServerAccPort_Type()
)
sleRadiusServerAccPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerAccPort.setStatus("current")


class _SleRadiusServerMode_Type(Bits):
    """Custom type sleRadiusServerMode based on Bits"""
    namedValues = NamedValues(
        *(("aaa", 0),
          ("dot1x", 1))
    )

_SleRadiusServerMode_Type.__name__ = "Bits"
_SleRadiusServerMode_Object = MibTableColumn
sleRadiusServerMode = _SleRadiusServerMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 1, 1, 5),
    _SleRadiusServerMode_Type()
)
sleRadiusServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerMode.setStatus("current")
_SleRadiusServerControl_ObjectIdentity = ObjectIdentity
sleRadiusServerControl = _SleRadiusServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2)
)


class _SleRadiusServerControlRequest_Type(Integer32):
    """Custom type sleRadiusServerControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createRadiusServer", 1),
          ("destroyRadiusServer", 2),
          ("setRadiusServerProfile", 3))
    )


_SleRadiusServerControlRequest_Type.__name__ = "Integer32"
_SleRadiusServerControlRequest_Object = MibScalar
sleRadiusServerControlRequest = _SleRadiusServerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 1),
    _SleRadiusServerControlRequest_Type()
)
sleRadiusServerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerControlRequest.setStatus("current")
_SleRadiusServerControlStatus_Type = SleControlStatusType
_SleRadiusServerControlStatus_Object = MibScalar
sleRadiusServerControlStatus = _SleRadiusServerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 2),
    _SleRadiusServerControlStatus_Type()
)
sleRadiusServerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerControlStatus.setStatus("current")
_SleRadiusServerControlTimer_Type = Gauge32
_SleRadiusServerControlTimer_Object = MibScalar
sleRadiusServerControlTimer = _SleRadiusServerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 3),
    _SleRadiusServerControlTimer_Type()
)
sleRadiusServerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerControlTimer.setStatus("current")
_SleRadiusServerControlTimeStamp_Type = TimeStamp
_SleRadiusServerControlTimeStamp_Object = MibScalar
sleRadiusServerControlTimeStamp = _SleRadiusServerControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 4),
    _SleRadiusServerControlTimeStamp_Type()
)
sleRadiusServerControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerControlTimeStamp.setStatus("current")
_SleRadiusServerControlReqResult_Type = SleControlRequestResultType
_SleRadiusServerControlReqResult_Object = MibScalar
sleRadiusServerControlReqResult = _SleRadiusServerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 5),
    _SleRadiusServerControlReqResult_Type()
)
sleRadiusServerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerControlReqResult.setStatus("current")
_SleRadiusServerControlAddress_Type = IpAddress
_SleRadiusServerControlAddress_Object = MibScalar
sleRadiusServerControlAddress = _SleRadiusServerControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 6),
    _SleRadiusServerControlAddress_Type()
)
sleRadiusServerControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerControlAddress.setStatus("current")


class _SleRadiusServerControlClientKey_Type(OctetString):
    """Custom type sleRadiusServerControlClientKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleRadiusServerControlClientKey_Type.__name__ = "OctetString"
_SleRadiusServerControlClientKey_Object = MibScalar
sleRadiusServerControlClientKey = _SleRadiusServerControlClientKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 7),
    _SleRadiusServerControlClientKey_Type()
)
sleRadiusServerControlClientKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerControlClientKey.setStatus("current")


class _SleRadiusServerControlAuthPort_Type(Integer32):
    """Custom type sleRadiusServerControlAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRadiusServerControlAuthPort_Type.__name__ = "Integer32"
_SleRadiusServerControlAuthPort_Object = MibScalar
sleRadiusServerControlAuthPort = _SleRadiusServerControlAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 8),
    _SleRadiusServerControlAuthPort_Type()
)
sleRadiusServerControlAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerControlAuthPort.setStatus("current")


class _SleRadiusServerControlAccPort_Type(Integer32):
    """Custom type sleRadiusServerControlAccPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRadiusServerControlAccPort_Type.__name__ = "Integer32"
_SleRadiusServerControlAccPort_Object = MibScalar
sleRadiusServerControlAccPort = _SleRadiusServerControlAccPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 9),
    _SleRadiusServerControlAccPort_Type()
)
sleRadiusServerControlAccPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerControlAccPort.setStatus("current")


class _SleRadiusServerControlMode_Type(Bits):
    """Custom type sleRadiusServerControlMode based on Bits"""
    namedValues = NamedValues(
        *(("aaa", 0),
          ("dot1x", 1))
    )

_SleRadiusServerControlMode_Type.__name__ = "Bits"
_SleRadiusServerControlMode_Object = MibScalar
sleRadiusServerControlMode = _SleRadiusServerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 2, 10),
    _SleRadiusServerControlMode_Type()
)
sleRadiusServerControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerControlMode.setStatus("current")
_SleRadiusServerNotification_ObjectIdentity = ObjectIdentity
sleRadiusServerNotification = _SleRadiusServerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 3)
)
_SleTacacsServer_ObjectIdentity = ObjectIdentity
sleTacacsServer = _SleTacacsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4)
)
_SleTacacsServerTable_Object = MibTable
sleTacacsServerTable = _SleTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 1)
)
if mibBuilder.loadTexts:
    sleTacacsServerTable.setStatus("current")
_SleTacacsServerEntry_Object = MibTableRow
sleTacacsServerEntry = _SleTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 1, 1)
)
sleTacacsServerEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleTacacsServerAddress"),
)
if mibBuilder.loadTexts:
    sleTacacsServerEntry.setStatus("current")
_SleTacacsServerAddress_Type = IpAddress
_SleTacacsServerAddress_Object = MibTableColumn
sleTacacsServerAddress = _SleTacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 1, 1, 1),
    _SleTacacsServerAddress_Type()
)
sleTacacsServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTacacsServerAddress.setStatus("current")


class _SleTacacsServerClientKey_Type(OctetString):
    """Custom type sleTacacsServerClientKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleTacacsServerClientKey_Type.__name__ = "OctetString"
_SleTacacsServerClientKey_Object = MibTableColumn
sleTacacsServerClientKey = _SleTacacsServerClientKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 1, 1, 2),
    _SleTacacsServerClientKey_Type()
)
sleTacacsServerClientKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTacacsServerClientKey.setStatus("current")
_SleTacacsServerControl_ObjectIdentity = ObjectIdentity
sleTacacsServerControl = _SleTacacsServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 2)
)


class _SleTacacsServerControlRequest_Type(Integer32):
    """Custom type sleTacacsServerControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createTacacsServer", 1),
          ("destroyTacacsServer", 2),
          ("setTacacsServerClientKey", 3))
    )


_SleTacacsServerControlRequest_Type.__name__ = "Integer32"
_SleTacacsServerControlRequest_Object = MibScalar
sleTacacsServerControlRequest = _SleTacacsServerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 2, 1),
    _SleTacacsServerControlRequest_Type()
)
sleTacacsServerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTacacsServerControlRequest.setStatus("current")
_SleTacacsServerControlStatus_Type = SleControlStatusType
_SleTacacsServerControlStatus_Object = MibScalar
sleTacacsServerControlStatus = _SleTacacsServerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 2, 2),
    _SleTacacsServerControlStatus_Type()
)
sleTacacsServerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTacacsServerControlStatus.setStatus("current")
_SleTacacsServerControlTimer_Type = Gauge32
_SleTacacsServerControlTimer_Object = MibScalar
sleTacacsServerControlTimer = _SleTacacsServerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 2, 3),
    _SleTacacsServerControlTimer_Type()
)
sleTacacsServerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTacacsServerControlTimer.setStatus("current")
_SleTacacsServerControlTimeStamp_Type = TimeStamp
_SleTacacsServerControlTimeStamp_Object = MibScalar
sleTacacsServerControlTimeStamp = _SleTacacsServerControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 2, 4),
    _SleTacacsServerControlTimeStamp_Type()
)
sleTacacsServerControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTacacsServerControlTimeStamp.setStatus("current")
_SleTacacsServerControlReqResult_Type = SleControlRequestResultType
_SleTacacsServerControlReqResult_Object = MibScalar
sleTacacsServerControlReqResult = _SleTacacsServerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 2, 5),
    _SleTacacsServerControlReqResult_Type()
)
sleTacacsServerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleTacacsServerControlReqResult.setStatus("current")
_SleTacacsServerControlAddress_Type = IpAddress
_SleTacacsServerControlAddress_Object = MibScalar
sleTacacsServerControlAddress = _SleTacacsServerControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 2, 6),
    _SleTacacsServerControlAddress_Type()
)
sleTacacsServerControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTacacsServerControlAddress.setStatus("current")


class _SleTacacsServerControlClientKey_Type(OctetString):
    """Custom type sleTacacsServerControlClientKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleTacacsServerControlClientKey_Type.__name__ = "OctetString"
_SleTacacsServerControlClientKey_Object = MibScalar
sleTacacsServerControlClientKey = _SleTacacsServerControlClientKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 2, 7),
    _SleTacacsServerControlClientKey_Type()
)
sleTacacsServerControlClientKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleTacacsServerControlClientKey.setStatus("current")
_SleTacacsServerNotification_ObjectIdentity = ObjectIdentity
sleTacacsServerNotification = _SleTacacsServerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 3)
)
_SleAcl_ObjectIdentity = ObjectIdentity
sleAcl = _SleAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5)
)
_SleAclTable_Object = MibTable
sleAclTable = _SleAclTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1)
)
if mibBuilder.loadTexts:
    sleAclTable.setStatus("current")
_SleAclEntry_Object = MibTableRow
sleAclEntry = _SleAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1)
)
sleAclEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleAclName"),
)
if mibBuilder.loadTexts:
    sleAclEntry.setStatus("current")


class _SleAclName_Type(OctetString):
    """Custom type sleAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleAclName_Type.__name__ = "OctetString"
_SleAclName_Object = MibTableColumn
sleAclName = _SleAclName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 1),
    _SleAclName_Type()
)
sleAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclName.setStatus("current")
_SleAclSrcIpAddr_Type = IpAddress
_SleAclSrcIpAddr_Object = MibTableColumn
sleAclSrcIpAddr = _SleAclSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 2),
    _SleAclSrcIpAddr_Type()
)
sleAclSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclSrcIpAddr.setStatus("current")


class _SleAclSrcPrefixLength_Type(Integer32):
    """Custom type sleAclSrcPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SleAclSrcPrefixLength_Type.__name__ = "Integer32"
_SleAclSrcPrefixLength_Object = MibTableColumn
sleAclSrcPrefixLength = _SleAclSrcPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 3),
    _SleAclSrcPrefixLength_Type()
)
sleAclSrcPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclSrcPrefixLength.setStatus("current")
_SleAclDstIpAddr_Type = IpAddress
_SleAclDstIpAddr_Object = MibTableColumn
sleAclDstIpAddr = _SleAclDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 4),
    _SleAclDstIpAddr_Type()
)
sleAclDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclDstIpAddr.setStatus("current")


class _SleAclDstPrefixLength_Type(Integer32):
    """Custom type sleAclDstPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SleAclDstPrefixLength_Type.__name__ = "Integer32"
_SleAclDstPrefixLength_Object = MibTableColumn
sleAclDstPrefixLength = _SleAclDstPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 5),
    _SleAclDstPrefixLength_Type()
)
sleAclDstPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclDstPrefixLength.setStatus("current")


class _SleAclDscp_Type(Integer32):
    """Custom type sleAclDscp based on Integer32"""
    defaultValue = -1


_SleAclDscp_Type.__name__ = "Integer32"
_SleAclDscp_Object = MibTableColumn
sleAclDscp = _SleAclDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 6),
    _SleAclDscp_Type()
)
sleAclDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclDscp.setStatus("current")


class _SleAclProtocolType_Type(Integer32):
    """Custom type sleAclProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleAclProtocolType_Type.__name__ = "Integer32"
_SleAclProtocolType_Object = MibTableColumn
sleAclProtocolType = _SleAclProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 7),
    _SleAclProtocolType_Type()
)
sleAclProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclProtocolType.setStatus("current")


class _SleAclTcpFlag_Type(Bits):
    """Custom type sleAclTcpFlag based on Bits"""
    namedValues = NamedValues(
        *(("reserv", 0),
          ("reserv1", 1),
          ("urg", 2),
          ("ack", 3),
          ("psh", 4),
          ("rst", 5),
          ("syn", 6),
          ("fin", 7))
    )

_SleAclTcpFlag_Type.__name__ = "Bits"
_SleAclTcpFlag_Object = MibTableColumn
sleAclTcpFlag = _SleAclTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 8),
    _SleAclTcpFlag_Type()
)
sleAclTcpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclTcpFlag.setStatus("current")


class _SleAclSrcL4Port_Type(Integer32):
    """Custom type sleAclSrcL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleAclSrcL4Port_Type.__name__ = "Integer32"
_SleAclSrcL4Port_Object = MibTableColumn
sleAclSrcL4Port = _SleAclSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 9),
    _SleAclSrcL4Port_Type()
)
sleAclSrcL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclSrcL4Port.setStatus("current")


class _SleAclDstL4Port_Type(Integer32):
    """Custom type sleAclDstL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleAclDstL4Port_Type.__name__ = "Integer32"
_SleAclDstL4Port_Object = MibTableColumn
sleAclDstL4Port = _SleAclDstL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 10),
    _SleAclDstL4Port_Type()
)
sleAclDstL4Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclDstL4Port.setStatus("current")


class _SleAclPktLen_Type(Integer32):
    """Custom type sleAclPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 65535),
    )


_SleAclPktLen_Type.__name__ = "Integer32"
_SleAclPktLen_Object = MibTableColumn
sleAclPktLen = _SleAclPktLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 11),
    _SleAclPktLen_Type()
)
sleAclPktLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclPktLen.setStatus("current")


class _SleAclValidFlags_Type(Bits):
    """Custom type sleAclValidFlags based on Bits"""
    namedValues = NamedValues(
        *(("aclSrcIpAddress", 0),
          ("aclSrcPrefixLegth", 1),
          ("aclDstIpAddress", 2),
          ("aclDstPrefixLegth", 3),
          ("aclDscp", 4),
          ("aclProtocolType", 5),
          ("aclTcpFlags", 6),
          ("aclSrcL4Port", 7),
          ("aclDstL4Port", 8),
          ("aclPacketLength", 9))
    )

_SleAclValidFlags_Type.__name__ = "Bits"
_SleAclValidFlags_Object = MibTableColumn
sleAclValidFlags = _SleAclValidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 12),
    _SleAclValidFlags_Type()
)
sleAclValidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclValidFlags.setStatus("current")


class _SleAclMatchFlags_Type(Bits):
    """Custom type sleAclMatchFlags based on Bits"""
    namedValues = NamedValues(
        *(("aclSrcIpAddress", 0),
          ("aclSrcPrefixLegth", 1),
          ("aclDstIpAddress", 2),
          ("aclDstPrefixLength", 3),
          ("aclDscp", 4),
          ("aclProtocolType", 5),
          ("aclTcpFlag", 6),
          ("aclSrcL4Port", 7),
          ("aclDstL4Port", 8),
          ("aclPacketLength", 9))
    )

_SleAclMatchFlags_Type.__name__ = "Bits"
_SleAclMatchFlags_Object = MibTableColumn
sleAclMatchFlags = _SleAclMatchFlags_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 13),
    _SleAclMatchFlags_Type()
)
sleAclMatchFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclMatchFlags.setStatus("current")


class _SleAclMatchAction_Type(Integer32):
    """Custom type sleAclMatchAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_SleAclMatchAction_Type.__name__ = "Integer32"
_SleAclMatchAction_Object = MibTableColumn
sleAclMatchAction = _SleAclMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 14),
    _SleAclMatchAction_Type()
)
sleAclMatchAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclMatchAction.setStatus("current")


class _SleAclNomatchAction_Type(Integer32):
    """Custom type sleAclNomatchAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_SleAclNomatchAction_Type.__name__ = "Integer32"
_SleAclNomatchAction_Object = MibTableColumn
sleAclNomatchAction = _SleAclNomatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 15),
    _SleAclNomatchAction_Type()
)
sleAclNomatchAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclNomatchAction.setStatus("current")


class _SleAclPriority_Type(Integer32):
    """Custom type sleAclPriority based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
    )


_SleAclPriority_Type.__name__ = "Integer32"
_SleAclPriority_Object = MibTableColumn
sleAclPriority = _SleAclPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 1, 1, 16),
    _SleAclPriority_Type()
)
sleAclPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclPriority.setStatus("current")
_SleAclControl_ObjectIdentity = ObjectIdentity
sleAclControl = _SleAclControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2)
)


class _SleAclControlReqest_Type(Integer32):
    """Custom type sleAclControlReqest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("createAclRule", 1),
          ("destroyAclRule", 2),
          ("setAclClassifierProfile", 3),
          ("setAclMatchAction", 10),
          ("setAclNomatchAction", 11))
    )


_SleAclControlReqest_Type.__name__ = "Integer32"
_SleAclControlReqest_Object = MibScalar
sleAclControlReqest = _SleAclControlReqest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 1),
    _SleAclControlReqest_Type()
)
sleAclControlReqest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlReqest.setStatus("current")
_SleAclControlStatus_Type = SleControlStatusType
_SleAclControlStatus_Object = MibScalar
sleAclControlStatus = _SleAclControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 2),
    _SleAclControlStatus_Type()
)
sleAclControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclControlStatus.setStatus("current")
_SleAclControlTimer_Type = Gauge32
_SleAclControlTimer_Object = MibScalar
sleAclControlTimer = _SleAclControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 3),
    _SleAclControlTimer_Type()
)
sleAclControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlTimer.setStatus("current")
_SleAclControlTimeStamp_Type = TimeStamp
_SleAclControlTimeStamp_Object = MibScalar
sleAclControlTimeStamp = _SleAclControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 4),
    _SleAclControlTimeStamp_Type()
)
sleAclControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclControlTimeStamp.setStatus("current")
_SleAclControlReqResult_Type = SleControlRequestResultType
_SleAclControlReqResult_Object = MibScalar
sleAclControlReqResult = _SleAclControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 5),
    _SleAclControlReqResult_Type()
)
sleAclControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleAclControlReqResult.setStatus("current")


class _SleAclControlName_Type(OctetString):
    """Custom type sleAclControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleAclControlName_Type.__name__ = "OctetString"
_SleAclControlName_Object = MibScalar
sleAclControlName = _SleAclControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 6),
    _SleAclControlName_Type()
)
sleAclControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlName.setStatus("current")
_SleAclControlSrcIpAddr_Type = IpAddress
_SleAclControlSrcIpAddr_Object = MibScalar
sleAclControlSrcIpAddr = _SleAclControlSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 7),
    _SleAclControlSrcIpAddr_Type()
)
sleAclControlSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlSrcIpAddr.setStatus("current")


class _SleAclControlSrcPrefixLength_Type(Integer32):
    """Custom type sleAclControlSrcPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SleAclControlSrcPrefixLength_Type.__name__ = "Integer32"
_SleAclControlSrcPrefixLength_Object = MibScalar
sleAclControlSrcPrefixLength = _SleAclControlSrcPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 8),
    _SleAclControlSrcPrefixLength_Type()
)
sleAclControlSrcPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlSrcPrefixLength.setStatus("current")
_SleAclControlDstIpAddr_Type = IpAddress
_SleAclControlDstIpAddr_Object = MibScalar
sleAclControlDstIpAddr = _SleAclControlDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 9),
    _SleAclControlDstIpAddr_Type()
)
sleAclControlDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlDstIpAddr.setStatus("current")


class _SleAclControlDstPrefixLength_Type(Integer32):
    """Custom type sleAclControlDstPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SleAclControlDstPrefixLength_Type.__name__ = "Integer32"
_SleAclControlDstPrefixLength_Object = MibScalar
sleAclControlDstPrefixLength = _SleAclControlDstPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 10),
    _SleAclControlDstPrefixLength_Type()
)
sleAclControlDstPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlDstPrefixLength.setStatus("current")


class _SleAclControlDscp_Type(Integer32):
    """Custom type sleAclControlDscp based on Integer32"""
    defaultValue = -1


_SleAclControlDscp_Type.__name__ = "Integer32"
_SleAclControlDscp_Object = MibScalar
sleAclControlDscp = _SleAclControlDscp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 11),
    _SleAclControlDscp_Type()
)
sleAclControlDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlDscp.setStatus("current")


class _SleAclControlProtocolType_Type(Integer32):
    """Custom type sleAclControlProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleAclControlProtocolType_Type.__name__ = "Integer32"
_SleAclControlProtocolType_Object = MibScalar
sleAclControlProtocolType = _SleAclControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 12),
    _SleAclControlProtocolType_Type()
)
sleAclControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlProtocolType.setStatus("current")


class _SleAclControlTcpFlag_Type(Bits):
    """Custom type sleAclControlTcpFlag based on Bits"""
    namedValues = NamedValues(
        *(("reserv", 0),
          ("reserv1", 1),
          ("urg", 2),
          ("ack", 3),
          ("psh", 4),
          ("rst", 5),
          ("syn", 6),
          ("fin", 7))
    )

_SleAclControlTcpFlag_Type.__name__ = "Bits"
_SleAclControlTcpFlag_Object = MibScalar
sleAclControlTcpFlag = _SleAclControlTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 13),
    _SleAclControlTcpFlag_Type()
)
sleAclControlTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlTcpFlag.setStatus("current")


class _SleAclControlSrcL4Port_Type(Integer32):
    """Custom type sleAclControlSrcL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleAclControlSrcL4Port_Type.__name__ = "Integer32"
_SleAclControlSrcL4Port_Object = MibScalar
sleAclControlSrcL4Port = _SleAclControlSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 14),
    _SleAclControlSrcL4Port_Type()
)
sleAclControlSrcL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlSrcL4Port.setStatus("current")


class _SleAclControlDstL4Port_Type(Integer32):
    """Custom type sleAclControlDstL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleAclControlDstL4Port_Type.__name__ = "Integer32"
_SleAclControlDstL4Port_Object = MibScalar
sleAclControlDstL4Port = _SleAclControlDstL4Port_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 15),
    _SleAclControlDstL4Port_Type()
)
sleAclControlDstL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlDstL4Port.setStatus("current")


class _SleAclControlPktLen_Type(Integer32):
    """Custom type sleAclControlPktLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 65535),
    )


_SleAclControlPktLen_Type.__name__ = "Integer32"
_SleAclControlPktLen_Object = MibScalar
sleAclControlPktLen = _SleAclControlPktLen_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 16),
    _SleAclControlPktLen_Type()
)
sleAclControlPktLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlPktLen.setStatus("current")


class _SleAclControlValidFlags_Type(Bits):
    """Custom type sleAclControlValidFlags based on Bits"""
    namedValues = NamedValues(
        *(("aclSrcIpAddress", 0),
          ("aclSrcPrefixLength", 1),
          ("aclDstIpAddress", 2),
          ("aclDstPrefixLength", 3),
          ("aclDscp", 4),
          ("aclProtocolType", 5),
          ("aclTcpFlag", 6),
          ("aclSrcL4Port", 7),
          ("aclDstL4Port", 8),
          ("aclPacketLength", 9))
    )

_SleAclControlValidFlags_Type.__name__ = "Bits"
_SleAclControlValidFlags_Object = MibScalar
sleAclControlValidFlags = _SleAclControlValidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 17),
    _SleAclControlValidFlags_Type()
)
sleAclControlValidFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlValidFlags.setStatus("current")


class _SleAclControlMatchFlags_Type(Bits):
    """Custom type sleAclControlMatchFlags based on Bits"""
    namedValues = NamedValues(
        *(("aclSrcIpAddress", 0),
          ("aclSrcPrefixLength", 1),
          ("aclDstIpAddress", 2),
          ("aclDstPrefixLength", 3),
          ("aclDscp", 4),
          ("aclProtocolType", 5),
          ("aclTcpFlag", 6),
          ("aclSrcL4Port", 7),
          ("aclDstL4Port", 8),
          ("aclPacketLength", 9))
    )

_SleAclControlMatchFlags_Type.__name__ = "Bits"
_SleAclControlMatchFlags_Object = MibScalar
sleAclControlMatchFlags = _SleAclControlMatchFlags_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 18),
    _SleAclControlMatchFlags_Type()
)
sleAclControlMatchFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlMatchFlags.setStatus("current")


class _SleAclControlMatchAction_Type(Integer32):
    """Custom type sleAclControlMatchAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("permit", 1),
          ("deny", 2))
    )


_SleAclControlMatchAction_Type.__name__ = "Integer32"
_SleAclControlMatchAction_Object = MibScalar
sleAclControlMatchAction = _SleAclControlMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 19),
    _SleAclControlMatchAction_Type()
)
sleAclControlMatchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlMatchAction.setStatus("current")


class _SleAclControlNomatchAction_Type(Integer32):
    """Custom type sleAclControlNomatchAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("permit", 1),
          ("deny", 2))
    )


_SleAclControlNomatchAction_Type.__name__ = "Integer32"
_SleAclControlNomatchAction_Object = MibScalar
sleAclControlNomatchAction = _SleAclControlNomatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 20),
    _SleAclControlNomatchAction_Type()
)
sleAclControlNomatchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlNomatchAction.setStatus("current")


class _SleAclControlPriority_Type(Integer32):
    """Custom type sleAclControlPriority based on Integer32"""
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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("highest", 4))
    )


_SleAclControlPriority_Type.__name__ = "Integer32"
_SleAclControlPriority_Object = MibScalar
sleAclControlPriority = _SleAclControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 2, 21),
    _SleAclControlPriority_Type()
)
sleAclControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleAclControlPriority.setStatus("current")
_SleAclNotification_ObjectIdentity = ObjectIdentity
sleAclNotification = _SleAclNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 3)
)
_SleDot1xPort_ObjectIdentity = ObjectIdentity
sleDot1xPort = _SleDot1xPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6)
)
_SleDot1xPortTable_Object = MibTable
sleDot1xPortTable = _SleDot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1)
)
if mibBuilder.loadTexts:
    sleDot1xPortTable.setStatus("current")
_SleDot1xPortEntry_Object = MibTableRow
sleDot1xPortEntry = _SleDot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1, 1)
)
sleDot1xPortEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleDot1xPortIndex"),
)
if mibBuilder.loadTexts:
    sleDot1xPortEntry.setStatus("current")
_SleDot1xPortIndex_Type = InterfaceIndex
_SleDot1xPortIndex_Object = MibTableColumn
sleDot1xPortIndex = _SleDot1xPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1, 1, 1),
    _SleDot1xPortIndex_Type()
)
sleDot1xPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortIndex.setStatus("current")


class _SleDot1xPortEnable_Type(Integer32):
    """Custom type sleDot1xPortEnable based on Integer32"""
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
          ("portEnable", 2),
          ("macEnable", 3))
    )


_SleDot1xPortEnable_Type.__name__ = "Integer32"
_SleDot1xPortEnable_Object = MibTableColumn
sleDot1xPortEnable = _SleDot1xPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1, 1, 2),
    _SleDot1xPortEnable_Type()
)
sleDot1xPortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortEnable.setStatus("current")


class _SleDot1xPortMode_Type(Integer32):
    """Custom type sleDot1xPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", -1),
          ("none", 0),
          ("auto", 1),
          ("forceAuthorized", 2),
          ("forceUnauthorized", 3))
    )


_SleDot1xPortMode_Type.__name__ = "Integer32"
_SleDot1xPortMode_Object = MibTableColumn
sleDot1xPortMode = _SleDot1xPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1, 1, 3),
    _SleDot1xPortMode_Type()
)
sleDot1xPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortMode.setStatus("current")


class _SleDot1xPortReauthEnable_Type(Integer32):
    """Custom type sleDot1xPortReauthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDot1xPortReauthEnable_Type.__name__ = "Integer32"
_SleDot1xPortReauthEnable_Object = MibTableColumn
sleDot1xPortReauthEnable = _SleDot1xPortReauthEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1, 1, 4),
    _SleDot1xPortReauthEnable_Type()
)
sleDot1xPortReauthEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortReauthEnable.setStatus("current")


class _SleDot1xPortQuietPeriod_Type(Integer32):
    """Custom type sleDot1xPortQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleDot1xPortQuietPeriod_Type.__name__ = "Integer32"
_SleDot1xPortQuietPeriod_Object = MibTableColumn
sleDot1xPortQuietPeriod = _SleDot1xPortQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1, 1, 5),
    _SleDot1xPortQuietPeriod_Type()
)
sleDot1xPortQuietPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortQuietPeriod.setStatus("current")


class _SleDot1xPortReauthPeriod_Type(Integer32):
    """Custom type sleDot1xPortReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleDot1xPortReauthPeriod_Type.__name__ = "Integer32"
_SleDot1xPortReauthPeriod_Object = MibTableColumn
sleDot1xPortReauthPeriod = _SleDot1xPortReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1, 1, 6),
    _SleDot1xPortReauthPeriod_Type()
)
sleDot1xPortReauthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortReauthPeriod.setStatus("current")


class _SleDot1xPortAuthSuccess_Type(Integer32):
    """Custom type sleDot1xPortAuthSuccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("success", 2))
    )


_SleDot1xPortAuthSuccess_Type.__name__ = "Integer32"
_SleDot1xPortAuthSuccess_Object = MibTableColumn
sleDot1xPortAuthSuccess = _SleDot1xPortAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 1, 1, 7),
    _SleDot1xPortAuthSuccess_Type()
)
sleDot1xPortAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortAuthSuccess.setStatus("current")
_SleDot1xPortControl_ObjectIdentity = ObjectIdentity
sleDot1xPortControl = _SleDot1xPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2)
)


class _SleDot1xPortControlRequest_Type(Integer32):
    """Custom type sleDot1xPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setDot1xPortProfile", 1),
          ("setDot1xPortReauthenticate", 2),
          ("setDot1xPortInittialize", 3))
    )


_SleDot1xPortControlRequest_Type.__name__ = "Integer32"
_SleDot1xPortControlRequest_Object = MibScalar
sleDot1xPortControlRequest = _SleDot1xPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 1),
    _SleDot1xPortControlRequest_Type()
)
sleDot1xPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xPortControlRequest.setStatus("current")
_SleDot1xPortControlStatus_Type = SleControlStatusType
_SleDot1xPortControlStatus_Object = MibScalar
sleDot1xPortControlStatus = _SleDot1xPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 2),
    _SleDot1xPortControlStatus_Type()
)
sleDot1xPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortControlStatus.setStatus("current")
_SleDot1xPortControlTimer_Type = Gauge32
_SleDot1xPortControlTimer_Object = MibScalar
sleDot1xPortControlTimer = _SleDot1xPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 3),
    _SleDot1xPortControlTimer_Type()
)
sleDot1xPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xPortControlTimer.setStatus("current")
_SleDot1xPortControlTimeStamp_Type = TimeStamp
_SleDot1xPortControlTimeStamp_Object = MibScalar
sleDot1xPortControlTimeStamp = _SleDot1xPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 4),
    _SleDot1xPortControlTimeStamp_Type()
)
sleDot1xPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortControlTimeStamp.setStatus("current")
_SleDot1xPortControlReqResult_Type = SleControlRequestResultType
_SleDot1xPortControlReqResult_Object = MibScalar
sleDot1xPortControlReqResult = _SleDot1xPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 5),
    _SleDot1xPortControlReqResult_Type()
)
sleDot1xPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xPortControlReqResult.setStatus("current")
_SleDot1xPortControlIndex_Type = Integer32
_SleDot1xPortControlIndex_Object = MibScalar
sleDot1xPortControlIndex = _SleDot1xPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 6),
    _SleDot1xPortControlIndex_Type()
)
sleDot1xPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xPortControlIndex.setStatus("current")


class _SleDot1xPortControlEnable_Type(Integer32):
    """Custom type sleDot1xPortControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", -1),
          ("disable", 1),
          ("portEnable", 2),
          ("macEnable", 3))
    )


_SleDot1xPortControlEnable_Type.__name__ = "Integer32"
_SleDot1xPortControlEnable_Object = MibScalar
sleDot1xPortControlEnable = _SleDot1xPortControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 7),
    _SleDot1xPortControlEnable_Type()
)
sleDot1xPortControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xPortControlEnable.setStatus("current")


class _SleDot1xPortControlMode_Type(Integer32):
    """Custom type sleDot1xPortControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", -1),
          ("none", 0),
          ("auto", 1),
          ("forceAuthorized", 2),
          ("forceUnauthorized", 3))
    )


_SleDot1xPortControlMode_Type.__name__ = "Integer32"
_SleDot1xPortControlMode_Object = MibScalar
sleDot1xPortControlMode = _SleDot1xPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 8),
    _SleDot1xPortControlMode_Type()
)
sleDot1xPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xPortControlMode.setStatus("current")


class _SleDot1xPortControlReauthEnable_Type(Integer32):
    """Custom type sleDot1xPortControlReauthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", -1),
          ("disable", 0),
          ("enable", 1))
    )


_SleDot1xPortControlReauthEnable_Type.__name__ = "Integer32"
_SleDot1xPortControlReauthEnable_Object = MibScalar
sleDot1xPortControlReauthEnable = _SleDot1xPortControlReauthEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 9),
    _SleDot1xPortControlReauthEnable_Type()
)
sleDot1xPortControlReauthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xPortControlReauthEnable.setStatus("current")


class _SleDot1xPortControlQuietPeriod_Type(Integer32):
    """Custom type sleDot1xPortControlQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )


_SleDot1xPortControlQuietPeriod_Type.__name__ = "Integer32"
_SleDot1xPortControlQuietPeriod_Object = MibScalar
sleDot1xPortControlQuietPeriod = _SleDot1xPortControlQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 10),
    _SleDot1xPortControlQuietPeriod_Type()
)
sleDot1xPortControlQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xPortControlQuietPeriod.setStatus("current")


class _SleDot1xPortControlReauthPeriod_Type(Integer32):
    """Custom type sleDot1xPortControlReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 65535),
    )


_SleDot1xPortControlReauthPeriod_Type.__name__ = "Integer32"
_SleDot1xPortControlReauthPeriod_Object = MibScalar
sleDot1xPortControlReauthPeriod = _SleDot1xPortControlReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 2, 11),
    _SleDot1xPortControlReauthPeriod_Type()
)
sleDot1xPortControlReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xPortControlReauthPeriod.setStatus("current")
_SleDot1xPortNotification_ObjectIdentity = ObjectIdentity
sleDot1xPortNotification = _SleDot1xPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 3)
)
_SleDot1xStatistics_ObjectIdentity = ObjectIdentity
sleDot1xStatistics = _SleDot1xStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7)
)
_SleDot1xStatisticsTable_Object = MibTable
sleDot1xStatisticsTable = _SleDot1xStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1)
)
if mibBuilder.loadTexts:
    sleDot1xStatisticsTable.setStatus("current")
_SleDot1xStatisticsEntry_Object = MibTableRow
sleDot1xStatisticsEntry = _SleDot1xStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1)
)
sleDot1xStatisticsEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleDot1xStatsPortIndex"),
)
if mibBuilder.loadTexts:
    sleDot1xStatisticsEntry.setStatus("current")


class _SleDot1xStatsPortIndex_Type(Integer32):
    """Custom type sleDot1xStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDot1xStatsPortIndex_Type.__name__ = "Integer32"
_SleDot1xStatsPortIndex_Object = MibTableColumn
sleDot1xStatsPortIndex = _SleDot1xStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 1),
    _SleDot1xStatsPortIndex_Type()
)
sleDot1xStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsPortIndex.setStatus("current")
_SleDot1xStatsEapolFramesRx_Type = Counter32
_SleDot1xStatsEapolFramesRx_Object = MibTableColumn
sleDot1xStatsEapolFramesRx = _SleDot1xStatsEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 2),
    _SleDot1xStatsEapolFramesRx_Type()
)
sleDot1xStatsEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapolFramesRx.setStatus("current")
_SleDot1xStatsEapolFramesTx_Type = Counter32
_SleDot1xStatsEapolFramesTx_Object = MibTableColumn
sleDot1xStatsEapolFramesTx = _SleDot1xStatsEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 3),
    _SleDot1xStatsEapolFramesTx_Type()
)
sleDot1xStatsEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapolFramesTx.setStatus("current")
_SleDot1xStatsEapolStartFramesRx_Type = Counter32
_SleDot1xStatsEapolStartFramesRx_Object = MibTableColumn
sleDot1xStatsEapolStartFramesRx = _SleDot1xStatsEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 4),
    _SleDot1xStatsEapolStartFramesRx_Type()
)
sleDot1xStatsEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapolStartFramesRx.setStatus("current")
_SleDot1xStatsEapolLogoffFramesRx_Type = Counter32
_SleDot1xStatsEapolLogoffFramesRx_Object = MibTableColumn
sleDot1xStatsEapolLogoffFramesRx = _SleDot1xStatsEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 5),
    _SleDot1xStatsEapolLogoffFramesRx_Type()
)
sleDot1xStatsEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapolLogoffFramesRx.setStatus("current")
_SleDot1xStatsEapolRespIdFramesRx_Type = Counter32
_SleDot1xStatsEapolRespIdFramesRx_Object = MibTableColumn
sleDot1xStatsEapolRespIdFramesRx = _SleDot1xStatsEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 6),
    _SleDot1xStatsEapolRespIdFramesRx_Type()
)
sleDot1xStatsEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapolRespIdFramesRx.setStatus("current")
_SleDot1xStatsEapolRespFramesRx_Type = Counter32
_SleDot1xStatsEapolRespFramesRx_Object = MibTableColumn
sleDot1xStatsEapolRespFramesRx = _SleDot1xStatsEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 7),
    _SleDot1xStatsEapolRespFramesRx_Type()
)
sleDot1xStatsEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapolRespFramesRx.setStatus("current")
_SleDot1xStatsEapolReqIdFramesTx_Type = Counter32
_SleDot1xStatsEapolReqIdFramesTx_Object = MibTableColumn
sleDot1xStatsEapolReqIdFramesTx = _SleDot1xStatsEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 8),
    _SleDot1xStatsEapolReqIdFramesTx_Type()
)
sleDot1xStatsEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapolReqIdFramesTx.setStatus("current")
_SleDot1xStatsEapolReqFramesTx_Type = Integer32
_SleDot1xStatsEapolReqFramesTx_Object = MibTableColumn
sleDot1xStatsEapolReqFramesTx = _SleDot1xStatsEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 9),
    _SleDot1xStatsEapolReqFramesTx_Type()
)
sleDot1xStatsEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapolReqFramesTx.setStatus("current")
_SleDot1xStatsInvalidEapolFramesRx_Type = Counter32
_SleDot1xStatsInvalidEapolFramesRx_Object = MibTableColumn
sleDot1xStatsInvalidEapolFramesRx = _SleDot1xStatsInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 10),
    _SleDot1xStatsInvalidEapolFramesRx_Type()
)
sleDot1xStatsInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsInvalidEapolFramesRx.setStatus("current")
_SleDot1xStatsEapLengthErrorFramesRx_Type = Counter32
_SleDot1xStatsEapLengthErrorFramesRx_Object = MibTableColumn
sleDot1xStatsEapLengthErrorFramesRx = _SleDot1xStatsEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 11),
    _SleDot1xStatsEapLengthErrorFramesRx_Type()
)
sleDot1xStatsEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsEapLengthErrorFramesRx.setStatus("current")
_SleDot1xStatsLastEapolFrameVersion_Type = Counter32
_SleDot1xStatsLastEapolFrameVersion_Object = MibTableColumn
sleDot1xStatsLastEapolFrameVersion = _SleDot1xStatsLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 12),
    _SleDot1xStatsLastEapolFrameVersion_Type()
)
sleDot1xStatsLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsLastEapolFrameVersion.setStatus("current")
_SleDot1xStatsLastEapolFrameSource_Type = MacAddress
_SleDot1xStatsLastEapolFrameSource_Object = MibTableColumn
sleDot1xStatsLastEapolFrameSource = _SleDot1xStatsLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 1, 1, 13),
    _SleDot1xStatsLastEapolFrameSource_Type()
)
sleDot1xStatsLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsLastEapolFrameSource.setStatus("current")
_SleDot1xStatisticsControl_ObjectIdentity = ObjectIdentity
sleDot1xStatisticsControl = _SleDot1xStatisticsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 2)
)


class _SleDot1xStatsControlRequest_Type(Integer32):
    """Custom type sleDot1xStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearDot1xStatistics", 1)
    )


_SleDot1xStatsControlRequest_Type.__name__ = "Integer32"
_SleDot1xStatsControlRequest_Object = MibScalar
sleDot1xStatsControlRequest = _SleDot1xStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 2, 1),
    _SleDot1xStatsControlRequest_Type()
)
sleDot1xStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xStatsControlRequest.setStatus("current")
_SleDot1xStatsControlStatus_Type = SleControlStatusType
_SleDot1xStatsControlStatus_Object = MibScalar
sleDot1xStatsControlStatus = _SleDot1xStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 2, 2),
    _SleDot1xStatsControlStatus_Type()
)
sleDot1xStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsControlStatus.setStatus("current")
_SleDot1xStatsControlTimer_Type = Gauge32
_SleDot1xStatsControlTimer_Object = MibScalar
sleDot1xStatsControlTimer = _SleDot1xStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 2, 3),
    _SleDot1xStatsControlTimer_Type()
)
sleDot1xStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xStatsControlTimer.setStatus("current")
_SleDot1xStatsControlTimeStamp_Type = TimeTicks
_SleDot1xStatsControlTimeStamp_Object = MibScalar
sleDot1xStatsControlTimeStamp = _SleDot1xStatsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 2, 4),
    _SleDot1xStatsControlTimeStamp_Type()
)
sleDot1xStatsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsControlTimeStamp.setStatus("current")
_SleDot1xStatsControlReqResult_Type = SleControlRequestResultType
_SleDot1xStatsControlReqResult_Object = MibScalar
sleDot1xStatsControlReqResult = _SleDot1xStatsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 2, 5),
    _SleDot1xStatsControlReqResult_Type()
)
sleDot1xStatsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDot1xStatsControlReqResult.setStatus("current")


class _SleDot1xStatsControlPortIndex_Type(Unsigned32):
    """Custom type sleDot1xStatsControlPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDot1xStatsControlPortIndex_Type.__name__ = "Unsigned32"
_SleDot1xStatsControlPortIndex_Object = MibScalar
sleDot1xStatsControlPortIndex = _SleDot1xStatsControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 2, 6),
    _SleDot1xStatsControlPortIndex_Type()
)
sleDot1xStatsControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDot1xStatsControlPortIndex.setStatus("current")
_SleDot1xStatisticsNotification_ObjectIdentity = ObjectIdentity
sleDot1xStatisticsNotification = _SleDot1xStatisticsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 3)
)
_SleArpInspection_ObjectIdentity = ObjectIdentity
sleArpInspection = _SleArpInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8)
)
_SleArpInspectBase_ObjectIdentity = ObjectIdentity
sleArpInspectBase = _SleArpInspectBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1)
)
_SleArpInspectBaseInfo_ObjectIdentity = ObjectIdentity
sleArpInspectBaseInfo = _SleArpInspectBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 1)
)


class _SleArpInspectValidateSrcMac_Type(Integer32):
    """Custom type sleArpInspectValidateSrcMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleArpInspectValidateSrcMac_Type.__name__ = "Integer32"
_SleArpInspectValidateSrcMac_Object = MibScalar
sleArpInspectValidateSrcMac = _SleArpInspectValidateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 1, 1),
    _SleArpInspectValidateSrcMac_Type()
)
sleArpInspectValidateSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectValidateSrcMac.setStatus("current")


class _SleArpInspectValidateDstMac_Type(Integer32):
    """Custom type sleArpInspectValidateDstMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleArpInspectValidateDstMac_Type.__name__ = "Integer32"
_SleArpInspectValidateDstMac_Object = MibScalar
sleArpInspectValidateDstMac = _SleArpInspectValidateDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 1, 2),
    _SleArpInspectValidateDstMac_Type()
)
sleArpInspectValidateDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectValidateDstMac.setStatus("current")


class _SleArpInspectValidateIpAddr_Type(Integer32):
    """Custom type sleArpInspectValidateIpAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleArpInspectValidateIpAddr_Type.__name__ = "Integer32"
_SleArpInspectValidateIpAddr_Object = MibScalar
sleArpInspectValidateIpAddr = _SleArpInspectValidateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 1, 3),
    _SleArpInspectValidateIpAddr_Type()
)
sleArpInspectValidateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectValidateIpAddr.setStatus("current")


class _SleArpInspectLogBufferSize_Type(Integer32):
    """Custom type sleArpInspectLogBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleArpInspectLogBufferSize_Type.__name__ = "Integer32"
_SleArpInspectLogBufferSize_Object = MibScalar
sleArpInspectLogBufferSize = _SleArpInspectLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 1, 4),
    _SleArpInspectLogBufferSize_Type()
)
sleArpInspectLogBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectLogBufferSize.setStatus("current")


class _SleArpInspectLogEntry_Type(Integer32):
    """Custom type sleArpInspectLogEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleArpInspectLogEntry_Type.__name__ = "Integer32"
_SleArpInspectLogEntry_Object = MibScalar
sleArpInspectLogEntry = _SleArpInspectLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 1, 5),
    _SleArpInspectLogEntry_Type()
)
sleArpInspectLogEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectLogEntry.setStatus("current")


class _SleArpInspectLogInterval_Type(Integer32):
    """Custom type sleArpInspectLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SleArpInspectLogInterval_Type.__name__ = "Integer32"
_SleArpInspectLogInterval_Object = MibScalar
sleArpInspectLogInterval = _SleArpInspectLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 1, 6),
    _SleArpInspectLogInterval_Type()
)
sleArpInspectLogInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectLogInterval.setStatus("current")
_SleArpInspectBaseControl_ObjectIdentity = ObjectIdentity
sleArpInspectBaseControl = _SleArpInspectBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2)
)


class _SleArpInspectControlRequest_Type(Integer32):
    """Custom type sleArpInspectControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setArpInspectValidateProfile", 1),
          ("setArpInspectLogBufferSize", 2),
          ("setArpInspectLogRate", 3))
    )


_SleArpInspectControlRequest_Type.__name__ = "Integer32"
_SleArpInspectControlRequest_Object = MibScalar
sleArpInspectControlRequest = _SleArpInspectControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 1),
    _SleArpInspectControlRequest_Type()
)
sleArpInspectControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectControlRequest.setStatus("current")
_SleArpInspectControlStatus_Type = SleControlStatusType
_SleArpInspectControlStatus_Object = MibScalar
sleArpInspectControlStatus = _SleArpInspectControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 2),
    _SleArpInspectControlStatus_Type()
)
sleArpInspectControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectControlStatus.setStatus("current")
_SleArpInspectControlTimer_Type = Gauge32
_SleArpInspectControlTimer_Object = MibScalar
sleArpInspectControlTimer = _SleArpInspectControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 3),
    _SleArpInspectControlTimer_Type()
)
sleArpInspectControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectControlTimer.setStatus("current")
_SleArpInspectControlTimeStamp_Type = TimeTicks
_SleArpInspectControlTimeStamp_Object = MibScalar
sleArpInspectControlTimeStamp = _SleArpInspectControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 4),
    _SleArpInspectControlTimeStamp_Type()
)
sleArpInspectControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectControlTimeStamp.setStatus("current")
_SleArpInspectControlReqResult_Type = SleControlRequestResultType
_SleArpInspectControlReqResult_Object = MibScalar
sleArpInspectControlReqResult = _SleArpInspectControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 5),
    _SleArpInspectControlReqResult_Type()
)
sleArpInspectControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectControlReqResult.setStatus("current")


class _SleArpInspectControlValidateSrcMac_Type(Integer32):
    """Custom type sleArpInspectControlValidateSrcMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleArpInspectControlValidateSrcMac_Type.__name__ = "Integer32"
_SleArpInspectControlValidateSrcMac_Object = MibScalar
sleArpInspectControlValidateSrcMac = _SleArpInspectControlValidateSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 6),
    _SleArpInspectControlValidateSrcMac_Type()
)
sleArpInspectControlValidateSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectControlValidateSrcMac.setStatus("current")


class _SleArpInspectControlValidateDstMac_Type(Integer32):
    """Custom type sleArpInspectControlValidateDstMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleArpInspectControlValidateDstMac_Type.__name__ = "Integer32"
_SleArpInspectControlValidateDstMac_Object = MibScalar
sleArpInspectControlValidateDstMac = _SleArpInspectControlValidateDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 7),
    _SleArpInspectControlValidateDstMac_Type()
)
sleArpInspectControlValidateDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectControlValidateDstMac.setStatus("current")


class _SleArpInspectControlValidateIpAddr_Type(Integer32):
    """Custom type sleArpInspectControlValidateIpAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleArpInspectControlValidateIpAddr_Type.__name__ = "Integer32"
_SleArpInspectControlValidateIpAddr_Object = MibScalar
sleArpInspectControlValidateIpAddr = _SleArpInspectControlValidateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 8),
    _SleArpInspectControlValidateIpAddr_Type()
)
sleArpInspectControlValidateIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectControlValidateIpAddr.setStatus("current")


class _SleArpInspectControlLogBufferSize_Type(Integer32):
    """Custom type sleArpInspectControlLogBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleArpInspectControlLogBufferSize_Type.__name__ = "Integer32"
_SleArpInspectControlLogBufferSize_Object = MibScalar
sleArpInspectControlLogBufferSize = _SleArpInspectControlLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 9),
    _SleArpInspectControlLogBufferSize_Type()
)
sleArpInspectControlLogBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectControlLogBufferSize.setStatus("current")


class _SleArpInspectControlLogEntry_Type(Integer32):
    """Custom type sleArpInspectControlLogEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleArpInspectControlLogEntry_Type.__name__ = "Integer32"
_SleArpInspectControlLogEntry_Object = MibScalar
sleArpInspectControlLogEntry = _SleArpInspectControlLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 10),
    _SleArpInspectControlLogEntry_Type()
)
sleArpInspectControlLogEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectControlLogEntry.setStatus("current")


class _SleArpInspectControlLogInterval_Type(Integer32):
    """Custom type sleArpInspectControlLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SleArpInspectControlLogInterval_Type.__name__ = "Integer32"
_SleArpInspectControlLogInterval_Object = MibScalar
sleArpInspectControlLogInterval = _SleArpInspectControlLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 2, 11),
    _SleArpInspectControlLogInterval_Type()
)
sleArpInspectControlLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectControlLogInterval.setStatus("current")
_SleArpInspectBaseNotifications_ObjectIdentity = ObjectIdentity
sleArpInspectBaseNotifications = _SleArpInspectBaseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 3)
)
_SleArpACL_ObjectIdentity = ObjectIdentity
sleArpACL = _SleArpACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2)
)
_SleArpAclTable_Object = MibTable
sleArpAclTable = _SleArpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    sleArpAclTable.setStatus("current")
_SleArpAclEntry_Object = MibTableRow
sleArpAclEntry = _SleArpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 1, 1)
)
sleArpAclEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleArpAclIndex"),
)
if mibBuilder.loadTexts:
    sleArpAclEntry.setStatus("current")


class _SleArpAclIndex_Type(Integer32):
    """Custom type sleArpAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleArpAclIndex_Type.__name__ = "Integer32"
_SleArpAclIndex_Object = MibTableColumn
sleArpAclIndex = _SleArpAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 1, 1, 1),
    _SleArpAclIndex_Type()
)
sleArpAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclIndex.setStatus("current")


class _SleArpAclName_Type(OctetString):
    """Custom type sleArpAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleArpAclName_Type.__name__ = "OctetString"
_SleArpAclName_Object = MibTableColumn
sleArpAclName = _SleArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 1, 1, 2),
    _SleArpAclName_Type()
)
sleArpAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclName.setStatus("current")


class _SleArpAclNumEntries_Type(Integer32):
    """Custom type sleArpAclNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleArpAclNumEntries_Type.__name__ = "Integer32"
_SleArpAclNumEntries_Object = MibTableColumn
sleArpAclNumEntries = _SleArpAclNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 1, 1, 3),
    _SleArpAclNumEntries_Type()
)
sleArpAclNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclNumEntries.setStatus("current")
_SleArpAclControl_ObjectIdentity = ObjectIdentity
sleArpAclControl = _SleArpAclControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 2)
)


class _SleArpAclControlRequest_Type(Integer32):
    """Custom type sleArpAclControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createArpAcl", 1),
          ("destroyArpAcl", 2))
    )


_SleArpAclControlRequest_Type.__name__ = "Integer32"
_SleArpAclControlRequest_Object = MibScalar
sleArpAclControlRequest = _SleArpAclControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 2, 1),
    _SleArpAclControlRequest_Type()
)
sleArpAclControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclControlRequest.setStatus("current")
_SleArpAclControlStatus_Type = SleControlStatusType
_SleArpAclControlStatus_Object = MibScalar
sleArpAclControlStatus = _SleArpAclControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 2, 2),
    _SleArpAclControlStatus_Type()
)
sleArpAclControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclControlStatus.setStatus("current")
_SleArpAclControlTimer_Type = Gauge32
_SleArpAclControlTimer_Object = MibScalar
sleArpAclControlTimer = _SleArpAclControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 2, 3),
    _SleArpAclControlTimer_Type()
)
sleArpAclControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclControlTimer.setStatus("current")
_SleArpAclControlTimeStamp_Type = TimeTicks
_SleArpAclControlTimeStamp_Object = MibScalar
sleArpAclControlTimeStamp = _SleArpAclControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 2, 4),
    _SleArpAclControlTimeStamp_Type()
)
sleArpAclControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclControlTimeStamp.setStatus("current")
_SleArpAclControlReqResult_Type = SleControlRequestResultType
_SleArpAclControlReqResult_Object = MibScalar
sleArpAclControlReqResult = _SleArpAclControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 2, 5),
    _SleArpAclControlReqResult_Type()
)
sleArpAclControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclControlReqResult.setStatus("current")
_SleArpAclControlIndex_Type = Integer32
_SleArpAclControlIndex_Object = MibScalar
sleArpAclControlIndex = _SleArpAclControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 2, 6),
    _SleArpAclControlIndex_Type()
)
sleArpAclControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclControlIndex.setStatus("current")


class _SleArpAclControlName_Type(OctetString):
    """Custom type sleArpAclControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleArpAclControlName_Type.__name__ = "OctetString"
_SleArpAclControlName_Object = MibScalar
sleArpAclControlName = _SleArpAclControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 2, 7),
    _SleArpAclControlName_Type()
)
sleArpAclControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclControlName.setStatus("current")
_SleArpAclNotifications_ObjectIdentity = ObjectIdentity
sleArpAclNotifications = _SleArpAclNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 3)
)
_SleArpACLRule_ObjectIdentity = ObjectIdentity
sleArpACLRule = _SleArpACLRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3)
)
_SleArpAclRuleTable_Object = MibTable
sleArpAclRuleTable = _SleArpAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1)
)
if mibBuilder.loadTexts:
    sleArpAclRuleTable.setStatus("current")
_SleArpAclRuleEntry_Object = MibTableRow
sleArpAclRuleEntry = _SleArpAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1)
)
sleArpAclRuleEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleArpAclRuleAclIndex"),
    (0, "SLE-SECURITY-MIB", "sleArpAclRuleIndex"),
)
if mibBuilder.loadTexts:
    sleArpAclRuleEntry.setStatus("current")


class _SleArpAclRuleAclIndex_Type(Integer32):
    """Custom type sleArpAclRuleAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleArpAclRuleAclIndex_Type.__name__ = "Integer32"
_SleArpAclRuleAclIndex_Object = MibTableColumn
sleArpAclRuleAclIndex = _SleArpAclRuleAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 1),
    _SleArpAclRuleAclIndex_Type()
)
sleArpAclRuleAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleAclIndex.setStatus("current")


class _SleArpAclRuleIndex_Type(Integer32):
    """Custom type sleArpAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleArpAclRuleIndex_Type.__name__ = "Integer32"
_SleArpAclRuleIndex_Object = MibTableColumn
sleArpAclRuleIndex = _SleArpAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 2),
    _SleArpAclRuleIndex_Type()
)
sleArpAclRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleIndex.setStatus("current")


class _SleArpAclRuleAction_Type(Integer32):
    """Custom type sleArpAclRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SleArpAclRuleAction_Type.__name__ = "Integer32"
_SleArpAclRuleAction_Object = MibTableColumn
sleArpAclRuleAction = _SleArpAclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 3),
    _SleArpAclRuleAction_Type()
)
sleArpAclRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleAction.setStatus("current")


class _SleArpAclRuleType_Type(Integer32):
    """Custom type sleArpAclRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("subnet", 0),
          ("range", 1),
          ("dhcpSnooping", 2))
    )


_SleArpAclRuleType_Type.__name__ = "Integer32"
_SleArpAclRuleType_Object = MibTableColumn
sleArpAclRuleType = _SleArpAclRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 4),
    _SleArpAclRuleType_Type()
)
sleArpAclRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleType.setStatus("current")
_SleArpAclRuleRangeStartIP_Type = IpAddress
_SleArpAclRuleRangeStartIP_Object = MibTableColumn
sleArpAclRuleRangeStartIP = _SleArpAclRuleRangeStartIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 5),
    _SleArpAclRuleRangeStartIP_Type()
)
sleArpAclRuleRangeStartIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleRangeStartIP.setStatus("current")
_SleArpAclRuleRangeEndIP_Type = IpAddress
_SleArpAclRuleRangeEndIP_Object = MibTableColumn
sleArpAclRuleRangeEndIP = _SleArpAclRuleRangeEndIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 6),
    _SleArpAclRuleRangeEndIP_Type()
)
sleArpAclRuleRangeEndIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleRangeEndIP.setStatus("current")
_SleArpAclRuleIPAddress_Type = IpAddress
_SleArpAclRuleIPAddress_Object = MibTableColumn
sleArpAclRuleIPAddress = _SleArpAclRuleIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 7),
    _SleArpAclRuleIPAddress_Type()
)
sleArpAclRuleIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleIPAddress.setStatus("current")


class _SleArpAclRuleIPMask_Type(Integer32):
    """Custom type sleArpAclRuleIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleArpAclRuleIPMask_Type.__name__ = "Integer32"
_SleArpAclRuleIPMask_Object = MibTableColumn
sleArpAclRuleIPMask = _SleArpAclRuleIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 8),
    _SleArpAclRuleIPMask_Type()
)
sleArpAclRuleIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleIPMask.setStatus("current")
_SleArpAclRuleMacAddr_Type = MacAddress
_SleArpAclRuleMacAddr_Object = MibTableColumn
sleArpAclRuleMacAddr = _SleArpAclRuleMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 9),
    _SleArpAclRuleMacAddr_Type()
)
sleArpAclRuleMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleMacAddr.setStatus("current")


class _SleArpAclRuleMacType_Type(Integer32):
    """Custom type sleArpAclRuleMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("host", 1))
    )


_SleArpAclRuleMacType_Type.__name__ = "Integer32"
_SleArpAclRuleMacType_Object = MibTableColumn
sleArpAclRuleMacType = _SleArpAclRuleMacType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 1, 1, 10),
    _SleArpAclRuleMacType_Type()
)
sleArpAclRuleMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleMacType.setStatus("current")
_SleArpAclRuleControl_ObjectIdentity = ObjectIdentity
sleArpAclRuleControl = _SleArpAclRuleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2)
)


class _SleArpAclRuleControlRequest_Type(Integer32):
    """Custom type sleArpAclRuleControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createArpAclRule", 1),
          ("destroyArpAclRule", 2))
    )


_SleArpAclRuleControlRequest_Type.__name__ = "Integer32"
_SleArpAclRuleControlRequest_Object = MibScalar
sleArpAclRuleControlRequest = _SleArpAclRuleControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 1),
    _SleArpAclRuleControlRequest_Type()
)
sleArpAclRuleControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlRequest.setStatus("current")
_SleArpAclRuleControlStatus_Type = SleControlStatusType
_SleArpAclRuleControlStatus_Object = MibScalar
sleArpAclRuleControlStatus = _SleArpAclRuleControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 2),
    _SleArpAclRuleControlStatus_Type()
)
sleArpAclRuleControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleControlStatus.setStatus("current")
_SleArpAclRuleControlTimer_Type = Gauge32
_SleArpAclRuleControlTimer_Object = MibScalar
sleArpAclRuleControlTimer = _SleArpAclRuleControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 3),
    _SleArpAclRuleControlTimer_Type()
)
sleArpAclRuleControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlTimer.setStatus("current")
_SleArpAclRuleControlTimeStamp_Type = TimeTicks
_SleArpAclRuleControlTimeStamp_Object = MibScalar
sleArpAclRuleControlTimeStamp = _SleArpAclRuleControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 4),
    _SleArpAclRuleControlTimeStamp_Type()
)
sleArpAclRuleControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleControlTimeStamp.setStatus("current")
_SleArpAclRuleControlReqResult_Type = SleControlRequestResultType
_SleArpAclRuleControlReqResult_Object = MibScalar
sleArpAclRuleControlReqResult = _SleArpAclRuleControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 5),
    _SleArpAclRuleControlReqResult_Type()
)
sleArpAclRuleControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpAclRuleControlReqResult.setStatus("current")
_SleArpAclRuleControlAclIndex_Type = Integer32
_SleArpAclRuleControlAclIndex_Object = MibScalar
sleArpAclRuleControlAclIndex = _SleArpAclRuleControlAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 6),
    _SleArpAclRuleControlAclIndex_Type()
)
sleArpAclRuleControlAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlAclIndex.setStatus("current")
_SleArpAclRuleControlIndex_Type = Integer32
_SleArpAclRuleControlIndex_Object = MibScalar
sleArpAclRuleControlIndex = _SleArpAclRuleControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 7),
    _SleArpAclRuleControlIndex_Type()
)
sleArpAclRuleControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlIndex.setStatus("current")


class _SleArpAclRuleControlAction_Type(Integer32):
    """Custom type sleArpAclRuleControlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SleArpAclRuleControlAction_Type.__name__ = "Integer32"
_SleArpAclRuleControlAction_Object = MibScalar
sleArpAclRuleControlAction = _SleArpAclRuleControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 8),
    _SleArpAclRuleControlAction_Type()
)
sleArpAclRuleControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlAction.setStatus("current")


class _SleArpAclRuleControlType_Type(Integer32):
    """Custom type sleArpAclRuleControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("subnet", 0),
          ("range", 1),
          ("dhcpSnooping", 2))
    )


_SleArpAclRuleControlType_Type.__name__ = "Integer32"
_SleArpAclRuleControlType_Object = MibScalar
sleArpAclRuleControlType = _SleArpAclRuleControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 9),
    _SleArpAclRuleControlType_Type()
)
sleArpAclRuleControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlType.setStatus("current")
_SleArpAclRuleControlRangeStartIP_Type = IpAddress
_SleArpAclRuleControlRangeStartIP_Object = MibScalar
sleArpAclRuleControlRangeStartIP = _SleArpAclRuleControlRangeStartIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 10),
    _SleArpAclRuleControlRangeStartIP_Type()
)
sleArpAclRuleControlRangeStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlRangeStartIP.setStatus("current")
_SleArpAclRuleControlRangeEndIP_Type = IpAddress
_SleArpAclRuleControlRangeEndIP_Object = MibScalar
sleArpAclRuleControlRangeEndIP = _SleArpAclRuleControlRangeEndIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 11),
    _SleArpAclRuleControlRangeEndIP_Type()
)
sleArpAclRuleControlRangeEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlRangeEndIP.setStatus("current")
_SleArpAclRuleControlIPAddress_Type = IpAddress
_SleArpAclRuleControlIPAddress_Object = MibScalar
sleArpAclRuleControlIPAddress = _SleArpAclRuleControlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 12),
    _SleArpAclRuleControlIPAddress_Type()
)
sleArpAclRuleControlIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlIPAddress.setStatus("current")


class _SleArpAclRuleControlIPMask_Type(Integer32):
    """Custom type sleArpAclRuleControlIPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleArpAclRuleControlIPMask_Type.__name__ = "Integer32"
_SleArpAclRuleControlIPMask_Object = MibScalar
sleArpAclRuleControlIPMask = _SleArpAclRuleControlIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 13),
    _SleArpAclRuleControlIPMask_Type()
)
sleArpAclRuleControlIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlIPMask.setStatus("current")
_SleArpAclRuleControlMacAddr_Type = MacAddress
_SleArpAclRuleControlMacAddr_Object = MibScalar
sleArpAclRuleControlMacAddr = _SleArpAclRuleControlMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 14),
    _SleArpAclRuleControlMacAddr_Type()
)
sleArpAclRuleControlMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlMacAddr.setStatus("current")


class _SleArpAclRuleControlMacType_Type(Integer32):
    """Custom type sleArpAclRuleControlMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("host", 1))
    )


_SleArpAclRuleControlMacType_Type.__name__ = "Integer32"
_SleArpAclRuleControlMacType_Object = MibScalar
sleArpAclRuleControlMacType = _SleArpAclRuleControlMacType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 2, 15),
    _SleArpAclRuleControlMacType_Type()
)
sleArpAclRuleControlMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpAclRuleControlMacType.setStatus("current")
_SleArpAclRuleNotifications_ObjectIdentity = ObjectIdentity
sleArpAclRuleNotifications = _SleArpAclRuleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 3)
)
_SleArpInspectVlan_ObjectIdentity = ObjectIdentity
sleArpInspectVlan = _SleArpInspectVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4)
)
_SleArpInspectVlanTable_Object = MibTable
sleArpInspectVlanTable = _SleArpInspectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1)
)
if mibBuilder.loadTexts:
    sleArpInspectVlanTable.setStatus("current")
_SleArpInspectVlanEntry_Object = MibTableRow
sleArpInspectVlanEntry = _SleArpInspectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1)
)
sleArpInspectVlanEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleArpInspectVlanIndex"),
)
if mibBuilder.loadTexts:
    sleArpInspectVlanEntry.setStatus("current")


class _SleArpInspectVlanIndex_Type(Integer32):
    """Custom type sleArpInspectVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleArpInspectVlanIndex_Type.__name__ = "Integer32"
_SleArpInspectVlanIndex_Object = MibTableColumn
sleArpInspectVlanIndex = _SleArpInspectVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 1),
    _SleArpInspectVlanIndex_Type()
)
sleArpInspectVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanIndex.setStatus("current")


class _SleArpInspectVlanEnable_Type(Integer32):
    """Custom type sleArpInspectVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleArpInspectVlanEnable_Type.__name__ = "Integer32"
_SleArpInspectVlanEnable_Object = MibTableColumn
sleArpInspectVlanEnable = _SleArpInspectVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 2),
    _SleArpInspectVlanEnable_Type()
)
sleArpInspectVlanEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanEnable.setStatus("current")
_SleArpInspectVlanFilterAcl_Type = Integer32
_SleArpInspectVlanFilterAcl_Object = MibTableColumn
sleArpInspectVlanFilterAcl = _SleArpInspectVlanFilterAcl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 3),
    _SleArpInspectVlanFilterAcl_Type()
)
sleArpInspectVlanFilterAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanFilterAcl.setStatus("current")
_SleArpInspectVlanFwdPktCnt_Type = Integer32
_SleArpInspectVlanFwdPktCnt_Object = MibTableColumn
sleArpInspectVlanFwdPktCnt = _SleArpInspectVlanFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 4),
    _SleArpInspectVlanFwdPktCnt_Type()
)
sleArpInspectVlanFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanFwdPktCnt.setStatus("current")
_SleArpInspectVlanDropPktCnt_Type = Integer32
_SleArpInspectVlanDropPktCnt_Object = MibTableColumn
sleArpInspectVlanDropPktCnt = _SleArpInspectVlanDropPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 5),
    _SleArpInspectVlanDropPktCnt_Type()
)
sleArpInspectVlanDropPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanDropPktCnt.setStatus("current")
_SleArpInspectVlanAclPermits_Type = Integer32
_SleArpInspectVlanAclPermits_Object = MibTableColumn
sleArpInspectVlanAclPermits = _SleArpInspectVlanAclPermits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 6),
    _SleArpInspectVlanAclPermits_Type()
)
sleArpInspectVlanAclPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanAclPermits.setStatus("current")
_SleArpInspectVlanAclDrops_Type = Integer32
_SleArpInspectVlanAclDrops_Object = MibTableColumn
sleArpInspectVlanAclDrops = _SleArpInspectVlanAclDrops_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 7),
    _SleArpInspectVlanAclDrops_Type()
)
sleArpInspectVlanAclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanAclDrops.setStatus("current")
_SleArpInspectVlanSrcMacFailurs_Type = Integer32
_SleArpInspectVlanSrcMacFailurs_Object = MibTableColumn
sleArpInspectVlanSrcMacFailurs = _SleArpInspectVlanSrcMacFailurs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 8),
    _SleArpInspectVlanSrcMacFailurs_Type()
)
sleArpInspectVlanSrcMacFailurs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanSrcMacFailurs.setStatus("current")
_SleArpInspectVlanDstMacFailurs_Type = Integer32
_SleArpInspectVlanDstMacFailurs_Object = MibTableColumn
sleArpInspectVlanDstMacFailurs = _SleArpInspectVlanDstMacFailurs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 9),
    _SleArpInspectVlanDstMacFailurs_Type()
)
sleArpInspectVlanDstMacFailurs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanDstMacFailurs.setStatus("current")
_SleArpInspectVlanIpAddrFailurs_Type = Integer32
_SleArpInspectVlanIpAddrFailurs_Object = MibTableColumn
sleArpInspectVlanIpAddrFailurs = _SleArpInspectVlanIpAddrFailurs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 10),
    _SleArpInspectVlanIpAddrFailurs_Type()
)
sleArpInspectVlanIpAddrFailurs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanIpAddrFailurs.setStatus("current")


class _SleArpInspectVlanFilterAclName_Type(OctetString):
    """Custom type sleArpInspectVlanFilterAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleArpInspectVlanFilterAclName_Type.__name__ = "OctetString"
_SleArpInspectVlanFilterAclName_Object = MibTableColumn
sleArpInspectVlanFilterAclName = _SleArpInspectVlanFilterAclName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 1, 1, 11),
    _SleArpInspectVlanFilterAclName_Type()
)
sleArpInspectVlanFilterAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanFilterAclName.setStatus("current")
_SleArpInspectVlanControl_ObjectIdentity = ObjectIdentity
sleArpInspectVlanControl = _SleArpInspectVlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2)
)


class _SleArpInspectVlanControlRequest_Type(Integer32):
    """Custom type sleArpInspectVlanControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setArpInspectVlanProfile", 1),
          ("clearArpInspectVlanStatistics", 2))
    )


_SleArpInspectVlanControlRequest_Type.__name__ = "Integer32"
_SleArpInspectVlanControlRequest_Object = MibScalar
sleArpInspectVlanControlRequest = _SleArpInspectVlanControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2, 1),
    _SleArpInspectVlanControlRequest_Type()
)
sleArpInspectVlanControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectVlanControlRequest.setStatus("current")
_SleArpInspectVlanControlStatus_Type = SleControlStatusType
_SleArpInspectVlanControlStatus_Object = MibScalar
sleArpInspectVlanControlStatus = _SleArpInspectVlanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2, 2),
    _SleArpInspectVlanControlStatus_Type()
)
sleArpInspectVlanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanControlStatus.setStatus("current")
_SleArpInspectVlanControlTimer_Type = Gauge32
_SleArpInspectVlanControlTimer_Object = MibScalar
sleArpInspectVlanControlTimer = _SleArpInspectVlanControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2, 3),
    _SleArpInspectVlanControlTimer_Type()
)
sleArpInspectVlanControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectVlanControlTimer.setStatus("current")
_SleArpInspectVlanControlTimeStamp_Type = TimeTicks
_SleArpInspectVlanControlTimeStamp_Object = MibScalar
sleArpInspectVlanControlTimeStamp = _SleArpInspectVlanControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2, 4),
    _SleArpInspectVlanControlTimeStamp_Type()
)
sleArpInspectVlanControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanControlTimeStamp.setStatus("current")
_SleArpInspectVlanControlReqResult_Type = SleControlRequestResultType
_SleArpInspectVlanControlReqResult_Object = MibScalar
sleArpInspectVlanControlReqResult = _SleArpInspectVlanControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2, 5),
    _SleArpInspectVlanControlReqResult_Type()
)
sleArpInspectVlanControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectVlanControlReqResult.setStatus("current")


class _SleArpInspectVlanControlIndex_Type(Integer32):
    """Custom type sleArpInspectVlanControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleArpInspectVlanControlIndex_Type.__name__ = "Integer32"
_SleArpInspectVlanControlIndex_Object = MibScalar
sleArpInspectVlanControlIndex = _SleArpInspectVlanControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2, 6),
    _SleArpInspectVlanControlIndex_Type()
)
sleArpInspectVlanControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectVlanControlIndex.setStatus("current")


class _SleArpInspectVlanControlEnable_Type(Integer32):
    """Custom type sleArpInspectVlanControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleArpInspectVlanControlEnable_Type.__name__ = "Integer32"
_SleArpInspectVlanControlEnable_Object = MibScalar
sleArpInspectVlanControlEnable = _SleArpInspectVlanControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2, 7),
    _SleArpInspectVlanControlEnable_Type()
)
sleArpInspectVlanControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectVlanControlEnable.setStatus("current")
_SleArpInspectVlanControlFilterAcl_Type = Integer32
_SleArpInspectVlanControlFilterAcl_Object = MibScalar
sleArpInspectVlanControlFilterAcl = _SleArpInspectVlanControlFilterAcl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 2, 8),
    _SleArpInspectVlanControlFilterAcl_Type()
)
sleArpInspectVlanControlFilterAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectVlanControlFilterAcl.setStatus("current")
_SleArpInspectVlanNotifications_ObjectIdentity = ObjectIdentity
sleArpInspectVlanNotifications = _SleArpInspectVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 3)
)
_SleArpInspectPort_ObjectIdentity = ObjectIdentity
sleArpInspectPort = _SleArpInspectPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5)
)
_SleArpInspectPortTable_Object = MibTable
sleArpInspectPortTable = _SleArpInspectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 1)
)
if mibBuilder.loadTexts:
    sleArpInspectPortTable.setStatus("current")
_SleArpInspectPortEntry_Object = MibTableRow
sleArpInspectPortEntry = _SleArpInspectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 1, 1)
)
sleArpInspectPortEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleArpInspectPortIndex"),
)
if mibBuilder.loadTexts:
    sleArpInspectPortEntry.setStatus("current")


class _SleArpInspectPortIndex_Type(Integer32):
    """Custom type sleArpInspectPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleArpInspectPortIndex_Type.__name__ = "Integer32"
_SleArpInspectPortIndex_Object = MibTableColumn
sleArpInspectPortIndex = _SleArpInspectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 1, 1, 1),
    _SleArpInspectPortIndex_Type()
)
sleArpInspectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectPortIndex.setStatus("current")


class _SleArpInspectPortTrust_Type(Integer32):
    """Custom type sleArpInspectPortTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrust", 0),
          ("trust", 1))
    )


_SleArpInspectPortTrust_Type.__name__ = "Integer32"
_SleArpInspectPortTrust_Object = MibTableColumn
sleArpInspectPortTrust = _SleArpInspectPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 1, 1, 2),
    _SleArpInspectPortTrust_Type()
)
sleArpInspectPortTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectPortTrust.setStatus("current")
_SleArpInspectPortControl_ObjectIdentity = ObjectIdentity
sleArpInspectPortControl = _SleArpInspectPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 2)
)


class _SleArpInspectPortControlRequest_Type(Integer32):
    """Custom type sleArpInspectPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setArpInspectTrustPort", 1)
    )


_SleArpInspectPortControlRequest_Type.__name__ = "Integer32"
_SleArpInspectPortControlRequest_Object = MibScalar
sleArpInspectPortControlRequest = _SleArpInspectPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 2, 1),
    _SleArpInspectPortControlRequest_Type()
)
sleArpInspectPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectPortControlRequest.setStatus("current")
_SleArpInspectPortControlStatus_Type = SleControlStatusType
_SleArpInspectPortControlStatus_Object = MibScalar
sleArpInspectPortControlStatus = _SleArpInspectPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 2, 2),
    _SleArpInspectPortControlStatus_Type()
)
sleArpInspectPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectPortControlStatus.setStatus("current")
_SleArpInspectPortControlTimer_Type = Gauge32
_SleArpInspectPortControlTimer_Object = MibScalar
sleArpInspectPortControlTimer = _SleArpInspectPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 2, 3),
    _SleArpInspectPortControlTimer_Type()
)
sleArpInspectPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectPortControlTimer.setStatus("current")
_SleArpInspectPortControlTimeStamp_Type = TimeTicks
_SleArpInspectPortControlTimeStamp_Object = MibScalar
sleArpInspectPortControlTimeStamp = _SleArpInspectPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 2, 4),
    _SleArpInspectPortControlTimeStamp_Type()
)
sleArpInspectPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectPortControlTimeStamp.setStatus("current")
_SleArpInspectPortControlReqResult_Type = SleControlRequestResultType
_SleArpInspectPortControlReqResult_Object = MibScalar
sleArpInspectPortControlReqResult = _SleArpInspectPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 2, 5),
    _SleArpInspectPortControlReqResult_Type()
)
sleArpInspectPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectPortControlReqResult.setStatus("current")


class _SleArpInspectPortControlIndex_Type(Integer32):
    """Custom type sleArpInspectPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleArpInspectPortControlIndex_Type.__name__ = "Integer32"
_SleArpInspectPortControlIndex_Object = MibScalar
sleArpInspectPortControlIndex = _SleArpInspectPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 2, 6),
    _SleArpInspectPortControlIndex_Type()
)
sleArpInspectPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectPortControlIndex.setStatus("current")


class _SleArpInspectPortControlTrust_Type(Integer32):
    """Custom type sleArpInspectPortControlTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrust", 0),
          ("trust", 1))
    )


_SleArpInspectPortControlTrust_Type.__name__ = "Integer32"
_SleArpInspectPortControlTrust_Object = MibScalar
sleArpInspectPortControlTrust = _SleArpInspectPortControlTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 2, 7),
    _SleArpInspectPortControlTrust_Type()
)
sleArpInspectPortControlTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleArpInspectPortControlTrust.setStatus("current")
_SleArpInspectPortNotifications_ObjectIdentity = ObjectIdentity
sleArpInspectPortNotifications = _SleArpInspectPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 3)
)
_SleArpInspectInvalidLog_ObjectIdentity = ObjectIdentity
sleArpInspectInvalidLog = _SleArpInspectInvalidLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6)
)
_SleArpInspectInvalidLogTable_Object = MibTable
sleArpInspectInvalidLogTable = _SleArpInspectInvalidLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1)
)
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogTable.setStatus("current")
_SleArpInspectInvalidLogEntry_Object = MibTableRow
sleArpInspectInvalidLogEntry = _SleArpInspectInvalidLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1)
)
sleArpInspectInvalidLogEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleArpInspectInvalidLogId"),
)
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogEntry.setStatus("current")


class _SleArpInspectInvalidLogId_Type(Integer32):
    """Custom type sleArpInspectInvalidLogId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleArpInspectInvalidLogId_Type.__name__ = "Integer32"
_SleArpInspectInvalidLogId_Object = MibTableColumn
sleArpInspectInvalidLogId = _SleArpInspectInvalidLogId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 1),
    _SleArpInspectInvalidLogId_Type()
)
sleArpInspectInvalidLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogId.setStatus("current")


class _SleArpInspectInvalidLogReason_Type(Integer32):
    """Custom type sleArpInspectInvalidLogReason based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("aliReasonNone", 0),
          ("aliReasonDhcpPermit", 1),
          ("aliReasonDhcpDeny", 2),
          ("aliReasonAclPermit", 3),
          ("aliReasonAclDeny", 4),
          ("aliReasonValidSrcfail", 5),
          ("aliReasonValidDstfail", 6),
          ("aliReasonValidIpfail", 7))
    )


_SleArpInspectInvalidLogReason_Type.__name__ = "Integer32"
_SleArpInspectInvalidLogReason_Object = MibTableColumn
sleArpInspectInvalidLogReason = _SleArpInspectInvalidLogReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 2),
    _SleArpInspectInvalidLogReason_Type()
)
sleArpInspectInvalidLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogReason.setStatus("current")
_SleArpInspectInvalidLogSamePktCnt_Type = Counter32
_SleArpInspectInvalidLogSamePktCnt_Object = MibTableColumn
sleArpInspectInvalidLogSamePktCnt = _SleArpInspectInvalidLogSamePktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 3),
    _SleArpInspectInvalidLogSamePktCnt_Type()
)
sleArpInspectInvalidLogSamePktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogSamePktCnt.setStatus("current")


class _SleArpInspectInvalidLogOpcode_Type(Integer32):
    """Custom type sleArpInspectInvalidLogOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arpopRequest", 1),
          ("arpopReply", 2))
    )


_SleArpInspectInvalidLogOpcode_Type.__name__ = "Integer32"
_SleArpInspectInvalidLogOpcode_Object = MibTableColumn
sleArpInspectInvalidLogOpcode = _SleArpInspectInvalidLogOpcode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 4),
    _SleArpInspectInvalidLogOpcode_Type()
)
sleArpInspectInvalidLogOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogOpcode.setStatus("current")
_SleArpInspectInvalidLogPortNumber_Type = Integer32
_SleArpInspectInvalidLogPortNumber_Object = MibTableColumn
sleArpInspectInvalidLogPortNumber = _SleArpInspectInvalidLogPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 5),
    _SleArpInspectInvalidLogPortNumber_Type()
)
sleArpInspectInvalidLogPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogPortNumber.setStatus("current")
_SleArpInspectInvalidLogVlanId_Type = Integer32
_SleArpInspectInvalidLogVlanId_Object = MibTableColumn
sleArpInspectInvalidLogVlanId = _SleArpInspectInvalidLogVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 6),
    _SleArpInspectInvalidLogVlanId_Type()
)
sleArpInspectInvalidLogVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogVlanId.setStatus("current")


class _SleArpInspectInvalidLogSrcMacAddr_Type(OctetString):
    """Custom type sleArpInspectInvalidLogSrcMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SleArpInspectInvalidLogSrcMacAddr_Type.__name__ = "OctetString"
_SleArpInspectInvalidLogSrcMacAddr_Object = MibTableColumn
sleArpInspectInvalidLogSrcMacAddr = _SleArpInspectInvalidLogSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 7),
    _SleArpInspectInvalidLogSrcMacAddr_Type()
)
sleArpInspectInvalidLogSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogSrcMacAddr.setStatus("current")
_SleArpInspectInvalidLogSrcIpAddr_Type = IpAddress
_SleArpInspectInvalidLogSrcIpAddr_Object = MibTableColumn
sleArpInspectInvalidLogSrcIpAddr = _SleArpInspectInvalidLogSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 8),
    _SleArpInspectInvalidLogSrcIpAddr_Type()
)
sleArpInspectInvalidLogSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogSrcIpAddr.setStatus("current")


class _SleArpInspectInvalidLogDstMacAddr_Type(OctetString):
    """Custom type sleArpInspectInvalidLogDstMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SleArpInspectInvalidLogDstMacAddr_Type.__name__ = "OctetString"
_SleArpInspectInvalidLogDstMacAddr_Object = MibTableColumn
sleArpInspectInvalidLogDstMacAddr = _SleArpInspectInvalidLogDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 9),
    _SleArpInspectInvalidLogDstMacAddr_Type()
)
sleArpInspectInvalidLogDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogDstMacAddr.setStatus("current")
_SleArpInspectInvalidLogDstIpAddr_Type = IpAddress
_SleArpInspectInvalidLogDstIpAddr_Object = MibTableColumn
sleArpInspectInvalidLogDstIpAddr = _SleArpInspectInvalidLogDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 10),
    _SleArpInspectInvalidLogDstIpAddr_Type()
)
sleArpInspectInvalidLogDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogDstIpAddr.setStatus("current")
_SleArpInspectInvalidLogLastRecvTime_Type = OctetString
_SleArpInspectInvalidLogLastRecvTime_Object = MibTableColumn
sleArpInspectInvalidLogLastRecvTime = _SleArpInspectInvalidLogLastRecvTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 6, 1, 1, 11),
    _SleArpInspectInvalidLogLastRecvTime_Type()
)
sleArpInspectInvalidLogLastRecvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleArpInspectInvalidLogLastRecvTime.setStatus("current")
_SleSecurityAttack_ObjectIdentity = ObjectIdentity
sleSecurityAttack = _SleSecurityAttack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9)
)
_SleSecurityAttackBasic_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasic = _SleSecurityAttackBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1)
)
_SleSecurityAttackBasicBase_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBase = _SleSecurityAttackBasicBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1)
)
_SleSecurityAttackBasicBaseInfo_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBaseInfo = _SleSecurityAttackBasicBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 1)
)


class _SleSecurityAttackBasicBaseInfoGlobalStatus_Type(Integer32):
    """Custom type sleSecurityAttackBasicBaseInfoGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackBasicBaseInfoGlobalStatus_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBaseInfoGlobalStatus_Object = MibScalar
sleSecurityAttackBasicBaseInfoGlobalStatus = _SleSecurityAttackBasicBaseInfoGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 1, 1),
    _SleSecurityAttackBasicBaseInfoGlobalStatus_Type()
)
sleSecurityAttackBasicBaseInfoGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseInfoGlobalStatus.setStatus("current")


class _SleSecurityAttackBasicBaseDosStatus_Type(Integer32):
    """Custom type sleSecurityAttackBasicBaseDosStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackBasicBaseDosStatus_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBaseDosStatus_Object = MibScalar
sleSecurityAttackBasicBaseDosStatus = _SleSecurityAttackBasicBaseDosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 1, 2),
    _SleSecurityAttackBasicBaseDosStatus_Type()
)
sleSecurityAttackBasicBaseDosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseDosStatus.setStatus("current")


class _SleSecurityAttackBasicBaseScanStatus_Type(Integer32):
    """Custom type sleSecurityAttackBasicBaseScanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackBasicBaseScanStatus_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBaseScanStatus_Object = MibScalar
sleSecurityAttackBasicBaseScanStatus = _SleSecurityAttackBasicBaseScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 1, 3),
    _SleSecurityAttackBasicBaseScanStatus_Type()
)
sleSecurityAttackBasicBaseScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseScanStatus.setStatus("current")
_SleSecurityAttackBasicBaseCollectInterval_Type = Integer32
_SleSecurityAttackBasicBaseCollectInterval_Object = MibScalar
sleSecurityAttackBasicBaseCollectInterval = _SleSecurityAttackBasicBaseCollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 1, 4),
    _SleSecurityAttackBasicBaseCollectInterval_Type()
)
sleSecurityAttackBasicBaseCollectInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseCollectInterval.setStatus("current")
_SleSecurityAttackBasicBaseControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBaseControl = _SleSecurityAttackBasicBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2)
)


class _SleSecurityAttackBasicBaseControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackBasicBaseControlRequest based on Integer32"""
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
        *(("setSecurityAttackGlobalStatus", 1),
          ("setSecurityAttackDosStatus", 2),
          ("setSecurityAttackScanStatus", 3),
          ("setSecurityAttackCollectInterval", 4),
          ("setSecurityAttackAllConfig", 5))
    )


_SleSecurityAttackBasicBaseControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBaseControlRequest_Object = MibScalar
sleSecurityAttackBasicBaseControlRequest = _SleSecurityAttackBasicBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 1),
    _SleSecurityAttackBasicBaseControlRequest_Type()
)
sleSecurityAttackBasicBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlRequest.setStatus("current")
_SleSecurityAttackBasicBaseControlStatus_Type = SleControlStatusType
_SleSecurityAttackBasicBaseControlStatus_Object = MibScalar
sleSecurityAttackBasicBaseControlStatus = _SleSecurityAttackBasicBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 2),
    _SleSecurityAttackBasicBaseControlStatus_Type()
)
sleSecurityAttackBasicBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlStatus.setStatus("current")
_SleSecurityAttackBasicBaseControlTimer_Type = Gauge32
_SleSecurityAttackBasicBaseControlTimer_Object = MibScalar
sleSecurityAttackBasicBaseControlTimer = _SleSecurityAttackBasicBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 3),
    _SleSecurityAttackBasicBaseControlTimer_Type()
)
sleSecurityAttackBasicBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlTimer.setStatus("current")
_SleSecurityAttackBasicBaseControlTimeStamp_Type = TimeTicks
_SleSecurityAttackBasicBaseControlTimeStamp_Object = MibScalar
sleSecurityAttackBasicBaseControlTimeStamp = _SleSecurityAttackBasicBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 4),
    _SleSecurityAttackBasicBaseControlTimeStamp_Type()
)
sleSecurityAttackBasicBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlTimeStamp.setStatus("current")
_SleSecurityAttackBasicBaseControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackBasicBaseControlReqResult_Object = MibScalar
sleSecurityAttackBasicBaseControlReqResult = _SleSecurityAttackBasicBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 5),
    _SleSecurityAttackBasicBaseControlReqResult_Type()
)
sleSecurityAttackBasicBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlReqResult.setStatus("current")


class _SleSecurityAttackBasicBaseControlGlobalStatus_Type(Integer32):
    """Custom type sleSecurityAttackBasicBaseControlGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackBasicBaseControlGlobalStatus_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBaseControlGlobalStatus_Object = MibScalar
sleSecurityAttackBasicBaseControlGlobalStatus = _SleSecurityAttackBasicBaseControlGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 6),
    _SleSecurityAttackBasicBaseControlGlobalStatus_Type()
)
sleSecurityAttackBasicBaseControlGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlGlobalStatus.setStatus("current")


class _SleSecurityAttackBasicBaseControlDosStatus_Type(Integer32):
    """Custom type sleSecurityAttackBasicBaseControlDosStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackBasicBaseControlDosStatus_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBaseControlDosStatus_Object = MibScalar
sleSecurityAttackBasicBaseControlDosStatus = _SleSecurityAttackBasicBaseControlDosStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 7),
    _SleSecurityAttackBasicBaseControlDosStatus_Type()
)
sleSecurityAttackBasicBaseControlDosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlDosStatus.setStatus("current")


class _SleSecurityAttackBasicBaseControlScanStatus_Type(Integer32):
    """Custom type sleSecurityAttackBasicBaseControlScanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackBasicBaseControlScanStatus_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBaseControlScanStatus_Object = MibScalar
sleSecurityAttackBasicBaseControlScanStatus = _SleSecurityAttackBasicBaseControlScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 8),
    _SleSecurityAttackBasicBaseControlScanStatus_Type()
)
sleSecurityAttackBasicBaseControlScanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlScanStatus.setStatus("current")
_SleSecurityAttackBasicBaseControlCollectInterval_Type = Integer32
_SleSecurityAttackBasicBaseControlCollectInterval_Object = MibScalar
sleSecurityAttackBasicBaseControlCollectInterval = _SleSecurityAttackBasicBaseControlCollectInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 2, 9),
    _SleSecurityAttackBasicBaseControlCollectInterval_Type()
)
sleSecurityAttackBasicBaseControlCollectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseControlCollectInterval.setStatus("current")
_SleSecurityAttackBasicBaseNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBaseNotification = _SleSecurityAttackBasicBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 3)
)
_SleSecurityAttackBasicPolicy_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicPolicy = _SleSecurityAttackBasicPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2)
)
_SleSecurityAttackBasicPolicyInfo_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicPolicyInfo = _SleSecurityAttackBasicPolicyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 1)
)


class _SleSecurityAttackBasicPolicyAttackType_Type(Bits):
    """Custom type sleSecurityAttackBasicPolicyAttackType based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("tcpDosAttack", 1),
          ("udpDosAttack", 2),
          ("icmpDosAttack", 3),
          ("hostScan", 4),
          ("portScan", 5))
    )

_SleSecurityAttackBasicPolicyAttackType_Type.__name__ = "Bits"
_SleSecurityAttackBasicPolicyAttackType_Object = MibScalar
sleSecurityAttackBasicPolicyAttackType = _SleSecurityAttackBasicPolicyAttackType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 1, 1),
    _SleSecurityAttackBasicPolicyAttackType_Type()
)
sleSecurityAttackBasicPolicyAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyAttackType.setStatus("current")
_SleSecurityAttackBasicPolicyBlockTime_Type = OctetString
_SleSecurityAttackBasicPolicyBlockTime_Object = MibScalar
sleSecurityAttackBasicPolicyBlockTime = _SleSecurityAttackBasicPolicyBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 1, 2),
    _SleSecurityAttackBasicPolicyBlockTime_Type()
)
sleSecurityAttackBasicPolicyBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyBlockTime.setStatus("current")
_SleSecurityAttackBasicPolicyThresholdCount_Type = OctetString
_SleSecurityAttackBasicPolicyThresholdCount_Object = MibScalar
sleSecurityAttackBasicPolicyThresholdCount = _SleSecurityAttackBasicPolicyThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 1, 3),
    _SleSecurityAttackBasicPolicyThresholdCount_Type()
)
sleSecurityAttackBasicPolicyThresholdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyThresholdCount.setStatus("current")
_SleSecurityAttackBasicPolicyCollectPorts_Type = OctetString
_SleSecurityAttackBasicPolicyCollectPorts_Object = MibScalar
sleSecurityAttackBasicPolicyCollectPorts = _SleSecurityAttackBasicPolicyCollectPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 1, 4),
    _SleSecurityAttackBasicPolicyCollectPorts_Type()
)
sleSecurityAttackBasicPolicyCollectPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyCollectPorts.setStatus("current")
_SleSecurityAttackBasicPolicyControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicPolicyControl = _SleSecurityAttackBasicPolicyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2)
)


class _SleSecurityAttackBasicPolicyControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackBasicPolicyControlRequest based on Integer32"""
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
        *(("setSecurityAttackBasicPolicyBlockTime", 1),
          ("setSecurityAttackBasicPolicyThresholdCount", 2),
          ("setSecurityAttackBasicPolicyCollectPorts", 3),
          ("setSecurityAttackBasicPolicyAllConfig", 4))
    )


_SleSecurityAttackBasicPolicyControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackBasicPolicyControlRequest_Object = MibScalar
sleSecurityAttackBasicPolicyControlRequest = _SleSecurityAttackBasicPolicyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 1),
    _SleSecurityAttackBasicPolicyControlRequest_Type()
)
sleSecurityAttackBasicPolicyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlRequest.setStatus("current")
_SleSecurityAttackBasicPolicyControlStatus_Type = SleControlStatusType
_SleSecurityAttackBasicPolicyControlStatus_Object = MibScalar
sleSecurityAttackBasicPolicyControlStatus = _SleSecurityAttackBasicPolicyControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 2),
    _SleSecurityAttackBasicPolicyControlStatus_Type()
)
sleSecurityAttackBasicPolicyControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlStatus.setStatus("current")
_SleSecurityAttackBasicPolicyControlTimer_Type = Gauge32
_SleSecurityAttackBasicPolicyControlTimer_Object = MibScalar
sleSecurityAttackBasicPolicyControlTimer = _SleSecurityAttackBasicPolicyControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 3),
    _SleSecurityAttackBasicPolicyControlTimer_Type()
)
sleSecurityAttackBasicPolicyControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlTimer.setStatus("current")
_SleSecurityAttackBasicPolicyControlTimeStamp_Type = TimeTicks
_SleSecurityAttackBasicPolicyControlTimeStamp_Object = MibScalar
sleSecurityAttackBasicPolicyControlTimeStamp = _SleSecurityAttackBasicPolicyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 4),
    _SleSecurityAttackBasicPolicyControlTimeStamp_Type()
)
sleSecurityAttackBasicPolicyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlTimeStamp.setStatus("current")
_SleSecurityAttackBasicPolicyControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackBasicPolicyControlReqResult_Object = MibScalar
sleSecurityAttackBasicPolicyControlReqResult = _SleSecurityAttackBasicPolicyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 5),
    _SleSecurityAttackBasicPolicyControlReqResult_Type()
)
sleSecurityAttackBasicPolicyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlReqResult.setStatus("current")


class _SleSecurityAttackBasicPolicyControlAttackType_Type(Bits):
    """Custom type sleSecurityAttackBasicPolicyControlAttackType based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("tcpDosAttack", 1),
          ("udpDosAttack", 2),
          ("icmpDosAttack", 3),
          ("hostScan", 4),
          ("portScan", 5))
    )

_SleSecurityAttackBasicPolicyControlAttackType_Type.__name__ = "Bits"
_SleSecurityAttackBasicPolicyControlAttackType_Object = MibScalar
sleSecurityAttackBasicPolicyControlAttackType = _SleSecurityAttackBasicPolicyControlAttackType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 6),
    _SleSecurityAttackBasicPolicyControlAttackType_Type()
)
sleSecurityAttackBasicPolicyControlAttackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlAttackType.setStatus("current")
_SleSecurityAttackBasicPolicyControlBlockTime_Type = OctetString
_SleSecurityAttackBasicPolicyControlBlockTime_Object = MibScalar
sleSecurityAttackBasicPolicyControlBlockTime = _SleSecurityAttackBasicPolicyControlBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 7),
    _SleSecurityAttackBasicPolicyControlBlockTime_Type()
)
sleSecurityAttackBasicPolicyControlBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlBlockTime.setStatus("current")
_SleSecurityAttackBasicPolicyControlThresholdCount_Type = OctetString
_SleSecurityAttackBasicPolicyControlThresholdCount_Object = MibScalar
sleSecurityAttackBasicPolicyControlThresholdCount = _SleSecurityAttackBasicPolicyControlThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 8),
    _SleSecurityAttackBasicPolicyControlThresholdCount_Type()
)
sleSecurityAttackBasicPolicyControlThresholdCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlThresholdCount.setStatus("current")
_SleSecurityAttackBasicPolicyControlCollectPorts_Type = OctetString
_SleSecurityAttackBasicPolicyControlCollectPorts_Object = MibScalar
sleSecurityAttackBasicPolicyControlCollectPorts = _SleSecurityAttackBasicPolicyControlCollectPorts_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 2, 9),
    _SleSecurityAttackBasicPolicyControlCollectPorts_Type()
)
sleSecurityAttackBasicPolicyControlCollectPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyControlCollectPorts.setStatus("current")
_SleSecurityAttackBasicPolicyNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicPolicyNotification = _SleSecurityAttackBasicPolicyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 3)
)
_SleSecurityAttackBasicExceptList_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicExceptList = _SleSecurityAttackBasicExceptList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3)
)
_SleSecurityAttackBasicExceptListTable_Object = MibTable
sleSecurityAttackBasicExceptListTable = _SleSecurityAttackBasicExceptListTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListTable.setStatus("current")
_SleSecurityAttackBasicExceptListEntry_Object = MibTableRow
sleSecurityAttackBasicExceptListEntry = _SleSecurityAttackBasicExceptListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 1, 1)
)
sleSecurityAttackBasicExceptListEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListIndex"),
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListEntry.setStatus("current")


class _SleSecurityAttackBasicExceptListIndex_Type(Integer32):
    """Custom type sleSecurityAttackBasicExceptListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackBasicExceptListIndex_Type.__name__ = "Integer32"
_SleSecurityAttackBasicExceptListIndex_Object = MibTableColumn
sleSecurityAttackBasicExceptListIndex = _SleSecurityAttackBasicExceptListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 1, 1, 1),
    _SleSecurityAttackBasicExceptListIndex_Type()
)
sleSecurityAttackBasicExceptListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListIndex.setStatus("current")


class _SleSecurityAttackBasicExceptListProtocolType_Type(Integer32):
    """Custom type sleSecurityAttackBasicExceptListProtocolType based on Integer32"""
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
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2),
          ("icmp", 3))
    )


_SleSecurityAttackBasicExceptListProtocolType_Type.__name__ = "Integer32"
_SleSecurityAttackBasicExceptListProtocolType_Object = MibTableColumn
sleSecurityAttackBasicExceptListProtocolType = _SleSecurityAttackBasicExceptListProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 1, 1, 2),
    _SleSecurityAttackBasicExceptListProtocolType_Type()
)
sleSecurityAttackBasicExceptListProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListProtocolType.setStatus("current")
_SleSecurityAttackBasicExceptListSourceIpAddress_Type = IpAddress
_SleSecurityAttackBasicExceptListSourceIpAddress_Object = MibTableColumn
sleSecurityAttackBasicExceptListSourceIpAddress = _SleSecurityAttackBasicExceptListSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 1, 1, 3),
    _SleSecurityAttackBasicExceptListSourceIpAddress_Type()
)
sleSecurityAttackBasicExceptListSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListSourceIpAddress.setStatus("current")
_SleSecurityAttackBasicExceptListDestinationIpAddress_Type = IpAddress
_SleSecurityAttackBasicExceptListDestinationIpAddress_Object = MibTableColumn
sleSecurityAttackBasicExceptListDestinationIpAddress = _SleSecurityAttackBasicExceptListDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 1, 1, 4),
    _SleSecurityAttackBasicExceptListDestinationIpAddress_Type()
)
sleSecurityAttackBasicExceptListDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListDestinationIpAddress.setStatus("current")


class _SleSecurityAttackBasicExceptListIngressPort_Type(Integer32):
    """Custom type sleSecurityAttackBasicExceptListIngressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackBasicExceptListIngressPort_Type.__name__ = "Integer32"
_SleSecurityAttackBasicExceptListIngressPort_Object = MibTableColumn
sleSecurityAttackBasicExceptListIngressPort = _SleSecurityAttackBasicExceptListIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 1, 1, 5),
    _SleSecurityAttackBasicExceptListIngressPort_Type()
)
sleSecurityAttackBasicExceptListIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListIngressPort.setStatus("current")
_SleSecurityAttackBasicExceptListControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicExceptListControl = _SleSecurityAttackBasicExceptListControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2)
)


class _SleSecurityAttackBasicExceptListControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackBasicExceptListControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createSecurityAttackBasicExceptList", 1),
          ("modifySecurityAttackBasicExceptList", 2),
          ("delSecurityAttackBasicExceptList", 3))
    )


_SleSecurityAttackBasicExceptListControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackBasicExceptListControlRequest_Object = MibScalar
sleSecurityAttackBasicExceptListControlRequest = _SleSecurityAttackBasicExceptListControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 1),
    _SleSecurityAttackBasicExceptListControlRequest_Type()
)
sleSecurityAttackBasicExceptListControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlRequest.setStatus("current")
_SleSecurityAttackBasicExceptListControlStatus_Type = SleControlStatusType
_SleSecurityAttackBasicExceptListControlStatus_Object = MibScalar
sleSecurityAttackBasicExceptListControlStatus = _SleSecurityAttackBasicExceptListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 2),
    _SleSecurityAttackBasicExceptListControlStatus_Type()
)
sleSecurityAttackBasicExceptListControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlStatus.setStatus("current")
_SleSecurityAttackBasicExceptListControlTimer_Type = Gauge32
_SleSecurityAttackBasicExceptListControlTimer_Object = MibScalar
sleSecurityAttackBasicExceptListControlTimer = _SleSecurityAttackBasicExceptListControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 3),
    _SleSecurityAttackBasicExceptListControlTimer_Type()
)
sleSecurityAttackBasicExceptListControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlTimer.setStatus("current")
_SleSecurityAttackBasicExceptListControlTimeStamp_Type = TimeTicks
_SleSecurityAttackBasicExceptListControlTimeStamp_Object = MibScalar
sleSecurityAttackBasicExceptListControlTimeStamp = _SleSecurityAttackBasicExceptListControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 4),
    _SleSecurityAttackBasicExceptListControlTimeStamp_Type()
)
sleSecurityAttackBasicExceptListControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlTimeStamp.setStatus("current")
_SleSecurityAttackBasicExceptListControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackBasicExceptListControlReqResult_Object = MibScalar
sleSecurityAttackBasicExceptListControlReqResult = _SleSecurityAttackBasicExceptListControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 5),
    _SleSecurityAttackBasicExceptListControlReqResult_Type()
)
sleSecurityAttackBasicExceptListControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlReqResult.setStatus("current")
_SleSecurityAttackBasicExceptListControlRuleIndex_Type = Integer32
_SleSecurityAttackBasicExceptListControlRuleIndex_Object = MibScalar
sleSecurityAttackBasicExceptListControlRuleIndex = _SleSecurityAttackBasicExceptListControlRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 6),
    _SleSecurityAttackBasicExceptListControlRuleIndex_Type()
)
sleSecurityAttackBasicExceptListControlRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlRuleIndex.setStatus("current")


class _SleSecurityAttackBasicExceptListControlProtocolType_Type(Integer32):
    """Custom type sleSecurityAttackBasicExceptListControlProtocolType based on Integer32"""
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
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2),
          ("icmp", 3))
    )


_SleSecurityAttackBasicExceptListControlProtocolType_Type.__name__ = "Integer32"
_SleSecurityAttackBasicExceptListControlProtocolType_Object = MibScalar
sleSecurityAttackBasicExceptListControlProtocolType = _SleSecurityAttackBasicExceptListControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 7),
    _SleSecurityAttackBasicExceptListControlProtocolType_Type()
)
sleSecurityAttackBasicExceptListControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlProtocolType.setStatus("current")
_SleSecurityAttackBasicExceptListControlSourceIpAddress_Type = IpAddress
_SleSecurityAttackBasicExceptListControlSourceIpAddress_Object = MibScalar
sleSecurityAttackBasicExceptListControlSourceIpAddress = _SleSecurityAttackBasicExceptListControlSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 8),
    _SleSecurityAttackBasicExceptListControlSourceIpAddress_Type()
)
sleSecurityAttackBasicExceptListControlSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlSourceIpAddress.setStatus("current")
_SleSecurityAttackBasicExceptListControlDestinationIpAddress_Type = IpAddress
_SleSecurityAttackBasicExceptListControlDestinationIpAddress_Object = MibScalar
sleSecurityAttackBasicExceptListControlDestinationIpAddress = _SleSecurityAttackBasicExceptListControlDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 9),
    _SleSecurityAttackBasicExceptListControlDestinationIpAddress_Type()
)
sleSecurityAttackBasicExceptListControlDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlDestinationIpAddress.setStatus("current")
_SleSecurityAttackBasicExceptListControlIngressPort_Type = Integer32
_SleSecurityAttackBasicExceptListControlIngressPort_Object = MibScalar
sleSecurityAttackBasicExceptListControlIngressPort = _SleSecurityAttackBasicExceptListControlIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 2, 10),
    _SleSecurityAttackBasicExceptListControlIngressPort_Type()
)
sleSecurityAttackBasicExceptListControlIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListControlIngressPort.setStatus("current")
_SleSecurityAttackBasicExceptListNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicExceptListNotification = _SleSecurityAttackBasicExceptListNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 3)
)
_SleSecurityAttackBasicBlackList_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBlackList = _SleSecurityAttackBasicBlackList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4)
)
_SleSecurityAttackBasicBlackListTable_Object = MibTable
sleSecurityAttackBasicBlackListTable = _SleSecurityAttackBasicBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListTable.setStatus("current")
_SleSecurityAttackBasicBlackListEntry_Object = MibTableRow
sleSecurityAttackBasicBlackListEntry = _SleSecurityAttackBasicBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 1, 1)
)
sleSecurityAttackBasicBlackListEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListIndex"),
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListEntry.setStatus("current")


class _SleSecurityAttackBasicBlackListIndex_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlackListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackBasicBlackListIndex_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlackListIndex_Object = MibTableColumn
sleSecurityAttackBasicBlackListIndex = _SleSecurityAttackBasicBlackListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 1, 1, 1),
    _SleSecurityAttackBasicBlackListIndex_Type()
)
sleSecurityAttackBasicBlackListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListIndex.setStatus("current")


class _SleSecurityAttackBasicBlackListProtocolType_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlackListProtocolType based on Integer32"""
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
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2),
          ("icmp", 3))
    )


_SleSecurityAttackBasicBlackListProtocolType_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlackListProtocolType_Object = MibTableColumn
sleSecurityAttackBasicBlackListProtocolType = _SleSecurityAttackBasicBlackListProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 1, 1, 2),
    _SleSecurityAttackBasicBlackListProtocolType_Type()
)
sleSecurityAttackBasicBlackListProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListProtocolType.setStatus("current")
_SleSecurityAttackBasicBlackListSourceIpAddress_Type = IpAddress
_SleSecurityAttackBasicBlackListSourceIpAddress_Object = MibTableColumn
sleSecurityAttackBasicBlackListSourceIpAddress = _SleSecurityAttackBasicBlackListSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 1, 1, 3),
    _SleSecurityAttackBasicBlackListSourceIpAddress_Type()
)
sleSecurityAttackBasicBlackListSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListSourceIpAddress.setStatus("current")
_SleSecurityAttackBasicBlackListDestinationIpAddress_Type = IpAddress
_SleSecurityAttackBasicBlackListDestinationIpAddress_Object = MibTableColumn
sleSecurityAttackBasicBlackListDestinationIpAddress = _SleSecurityAttackBasicBlackListDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 1, 1, 4),
    _SleSecurityAttackBasicBlackListDestinationIpAddress_Type()
)
sleSecurityAttackBasicBlackListDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListDestinationIpAddress.setStatus("current")


class _SleSecurityAttackBasicBlackListBlockingStatus_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlackListBlockingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackBasicBlackListBlockingStatus_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlackListBlockingStatus_Object = MibTableColumn
sleSecurityAttackBasicBlackListBlockingStatus = _SleSecurityAttackBasicBlackListBlockingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 1, 1, 5),
    _SleSecurityAttackBasicBlackListBlockingStatus_Type()
)
sleSecurityAttackBasicBlackListBlockingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListBlockingStatus.setStatus("current")
_SleSecurityAttackBasicBlackListIgressPort_Type = Integer32
_SleSecurityAttackBasicBlackListIgressPort_Object = MibTableColumn
sleSecurityAttackBasicBlackListIgressPort = _SleSecurityAttackBasicBlackListIgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 1, 1, 6),
    _SleSecurityAttackBasicBlackListIgressPort_Type()
)
sleSecurityAttackBasicBlackListIgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListIgressPort.setStatus("current")
_SleSecurityAttackBasicBlackListControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBlackListControl = _SleSecurityAttackBasicBlackListControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2)
)


class _SleSecurityAttackBasicBlackListControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlackListControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createSecurityAttackBasicBlackList", 1),
          ("delSecurityAttackBasicBlackList", 2))
    )


_SleSecurityAttackBasicBlackListControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlackListControlRequest_Object = MibScalar
sleSecurityAttackBasicBlackListControlRequest = _SleSecurityAttackBasicBlackListControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 1),
    _SleSecurityAttackBasicBlackListControlRequest_Type()
)
sleSecurityAttackBasicBlackListControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlRequest.setStatus("current")
_SleSecurityAttackBasicBlackListControlStatus_Type = SleControlStatusType
_SleSecurityAttackBasicBlackListControlStatus_Object = MibScalar
sleSecurityAttackBasicBlackListControlStatus = _SleSecurityAttackBasicBlackListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 2),
    _SleSecurityAttackBasicBlackListControlStatus_Type()
)
sleSecurityAttackBasicBlackListControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlStatus.setStatus("current")
_SleSecurityAttackBasicBlackListControlTimer_Type = Gauge32
_SleSecurityAttackBasicBlackListControlTimer_Object = MibScalar
sleSecurityAttackBasicBlackListControlTimer = _SleSecurityAttackBasicBlackListControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 3),
    _SleSecurityAttackBasicBlackListControlTimer_Type()
)
sleSecurityAttackBasicBlackListControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlTimer.setStatus("current")
_SleSecurityAttackBasicBlackListControlTimeStamp_Type = TimeTicks
_SleSecurityAttackBasicBlackListControlTimeStamp_Object = MibScalar
sleSecurityAttackBasicBlackListControlTimeStamp = _SleSecurityAttackBasicBlackListControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 4),
    _SleSecurityAttackBasicBlackListControlTimeStamp_Type()
)
sleSecurityAttackBasicBlackListControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlTimeStamp.setStatus("current")
_SleSecurityAttackBasicBlackListControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackBasicBlackListControlReqResult_Object = MibScalar
sleSecurityAttackBasicBlackListControlReqResult = _SleSecurityAttackBasicBlackListControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 5),
    _SleSecurityAttackBasicBlackListControlReqResult_Type()
)
sleSecurityAttackBasicBlackListControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlReqResult.setStatus("current")
_SleSecurityAttackBasicBlackListControlRuleIndex_Type = Integer32
_SleSecurityAttackBasicBlackListControlRuleIndex_Object = MibScalar
sleSecurityAttackBasicBlackListControlRuleIndex = _SleSecurityAttackBasicBlackListControlRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 6),
    _SleSecurityAttackBasicBlackListControlRuleIndex_Type()
)
sleSecurityAttackBasicBlackListControlRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlRuleIndex.setStatus("current")


class _SleSecurityAttackBasicBlackListControlProtocolType_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlackListControlProtocolType based on Integer32"""
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
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2),
          ("icmp", 3))
    )


_SleSecurityAttackBasicBlackListControlProtocolType_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlackListControlProtocolType_Object = MibScalar
sleSecurityAttackBasicBlackListControlProtocolType = _SleSecurityAttackBasicBlackListControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 7),
    _SleSecurityAttackBasicBlackListControlProtocolType_Type()
)
sleSecurityAttackBasicBlackListControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlProtocolType.setStatus("current")
_SleSecurityAttackBasicBlackListControlSourceIpAddress_Type = IpAddress
_SleSecurityAttackBasicBlackListControlSourceIpAddress_Object = MibScalar
sleSecurityAttackBasicBlackListControlSourceIpAddress = _SleSecurityAttackBasicBlackListControlSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 8),
    _SleSecurityAttackBasicBlackListControlSourceIpAddress_Type()
)
sleSecurityAttackBasicBlackListControlSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlSourceIpAddress.setStatus("current")
_SleSecurityAttackBasicBlackListControlDestinationIpAddress_Type = IpAddress
_SleSecurityAttackBasicBlackListControlDestinationIpAddress_Object = MibScalar
sleSecurityAttackBasicBlackListControlDestinationIpAddress = _SleSecurityAttackBasicBlackListControlDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 9),
    _SleSecurityAttackBasicBlackListControlDestinationIpAddress_Type()
)
sleSecurityAttackBasicBlackListControlDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlDestinationIpAddress.setStatus("current")
_SleSecurityAttackBasicBlackListControlIngressPort_Type = Integer32
_SleSecurityAttackBasicBlackListControlIngressPort_Object = MibScalar
sleSecurityAttackBasicBlackListControlIngressPort = _SleSecurityAttackBasicBlackListControlIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 2, 10),
    _SleSecurityAttackBasicBlackListControlIngressPort_Type()
)
sleSecurityAttackBasicBlackListControlIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListControlIngressPort.setStatus("current")
_SleSecurityAttackBasicBlackListNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBlackListNotification = _SleSecurityAttackBasicBlackListNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 3)
)
_SleSecurityAttackBasicBlockedList_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBlockedList = _SleSecurityAttackBasicBlockedList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5)
)
_SleSecurityAttackBasicBlockedListTable_Object = MibTable
sleSecurityAttackBasicBlockedListTable = _SleSecurityAttackBasicBlockedListTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListTable.setStatus("current")
_SleSecurityAttackBasicBlockedListEntry_Object = MibTableRow
sleSecurityAttackBasicBlockedListEntry = _SleSecurityAttackBasicBlockedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1)
)
sleSecurityAttackBasicBlockedListEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListIndex"),
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListEntry.setStatus("current")


class _SleSecurityAttackBasicBlockedListIndex_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlockedListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackBasicBlockedListIndex_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlockedListIndex_Object = MibTableColumn
sleSecurityAttackBasicBlockedListIndex = _SleSecurityAttackBasicBlockedListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 1),
    _SleSecurityAttackBasicBlockedListIndex_Type()
)
sleSecurityAttackBasicBlockedListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListIndex.setStatus("current")


class _SleSecurityAttackBasicBlockedListAttackType_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlockedListAttackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tcpDosAttack", 1),
          ("udpDosAttack", 2),
          ("icmpDosAttack", 3),
          ("hostScan", 4),
          ("portScan", 5),
          ("staticAttack", 6))
    )


_SleSecurityAttackBasicBlockedListAttackType_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlockedListAttackType_Object = MibTableColumn
sleSecurityAttackBasicBlockedListAttackType = _SleSecurityAttackBasicBlockedListAttackType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 2),
    _SleSecurityAttackBasicBlockedListAttackType_Type()
)
sleSecurityAttackBasicBlockedListAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListAttackType.setStatus("current")
_SleSecurityAttackBasicBlockedListStartTime_Type = OctetString
_SleSecurityAttackBasicBlockedListStartTime_Object = MibTableColumn
sleSecurityAttackBasicBlockedListStartTime = _SleSecurityAttackBasicBlockedListStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 3),
    _SleSecurityAttackBasicBlockedListStartTime_Type()
)
sleSecurityAttackBasicBlockedListStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListStartTime.setStatus("current")
_SleSecurityAttackBasicBlockedListEndTime_Type = OctetString
_SleSecurityAttackBasicBlockedListEndTime_Object = MibTableColumn
sleSecurityAttackBasicBlockedListEndTime = _SleSecurityAttackBasicBlockedListEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 4),
    _SleSecurityAttackBasicBlockedListEndTime_Type()
)
sleSecurityAttackBasicBlockedListEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListEndTime.setStatus("current")
_SleSecurityAttackBasicBlockedListAttackSourceIp_Type = IpAddress
_SleSecurityAttackBasicBlockedListAttackSourceIp_Object = MibTableColumn
sleSecurityAttackBasicBlockedListAttackSourceIp = _SleSecurityAttackBasicBlockedListAttackSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 5),
    _SleSecurityAttackBasicBlockedListAttackSourceIp_Type()
)
sleSecurityAttackBasicBlockedListAttackSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListAttackSourceIp.setStatus("current")
_SleSecurityAttackBasicBlockedListAttackDestinationIp_Type = IpAddress
_SleSecurityAttackBasicBlockedListAttackDestinationIp_Object = MibTableColumn
sleSecurityAttackBasicBlockedListAttackDestinationIp = _SleSecurityAttackBasicBlockedListAttackDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 6),
    _SleSecurityAttackBasicBlockedListAttackDestinationIp_Type()
)
sleSecurityAttackBasicBlockedListAttackDestinationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListAttackDestinationIp.setStatus("current")


class _SleSecurityAttackBasicBlockedListProtocol_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlockedListProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("arp", 4))
    )


_SleSecurityAttackBasicBlockedListProtocol_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlockedListProtocol_Object = MibTableColumn
sleSecurityAttackBasicBlockedListProtocol = _SleSecurityAttackBasicBlockedListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 7),
    _SleSecurityAttackBasicBlockedListProtocol_Type()
)
sleSecurityAttackBasicBlockedListProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListProtocol.setStatus("current")
_SleSecurityAttackBasicBlockedListAttackPktCount_Type = Counter32
_SleSecurityAttackBasicBlockedListAttackPktCount_Object = MibTableColumn
sleSecurityAttackBasicBlockedListAttackPktCount = _SleSecurityAttackBasicBlockedListAttackPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 8),
    _SleSecurityAttackBasicBlockedListAttackPktCount_Type()
)
sleSecurityAttackBasicBlockedListAttackPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListAttackPktCount.setStatus("current")


class _SleSecurityAttackBasicBlockedListAttackBlockTime_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlockedListAttackBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_SleSecurityAttackBasicBlockedListAttackBlockTime_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlockedListAttackBlockTime_Object = MibTableColumn
sleSecurityAttackBasicBlockedListAttackBlockTime = _SleSecurityAttackBasicBlockedListAttackBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 9),
    _SleSecurityAttackBasicBlockedListAttackBlockTime_Type()
)
sleSecurityAttackBasicBlockedListAttackBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListAttackBlockTime.setStatus("current")
_SleSecurityAttackBasicBlockedListBlackListIndex_Type = Integer32
_SleSecurityAttackBasicBlockedListBlackListIndex_Object = MibTableColumn
sleSecurityAttackBasicBlockedListBlackListIndex = _SleSecurityAttackBasicBlockedListBlackListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 10),
    _SleSecurityAttackBasicBlockedListBlackListIndex_Type()
)
sleSecurityAttackBasicBlockedListBlackListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListBlackListIndex.setStatus("current")
_SleSecurityAttackBasicBlockedListIgressPort_Type = Integer32
_SleSecurityAttackBasicBlockedListIgressPort_Object = MibTableColumn
sleSecurityAttackBasicBlockedListIgressPort = _SleSecurityAttackBasicBlockedListIgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 1, 1, 11),
    _SleSecurityAttackBasicBlockedListIgressPort_Type()
)
sleSecurityAttackBasicBlockedListIgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListIgressPort.setStatus("current")
_SleSecurityAttackBasicBlockedListControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBlockedListControl = _SleSecurityAttackBasicBlockedListControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 2)
)


class _SleSecurityAttackBasicBlockedListControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlockedListControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setSecurityAttackBasicBlockTime", 1),
          ("delSecurityAttackBasicBlockList", 2))
    )


_SleSecurityAttackBasicBlockedListControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlockedListControlRequest_Object = MibScalar
sleSecurityAttackBasicBlockedListControlRequest = _SleSecurityAttackBasicBlockedListControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 2, 1),
    _SleSecurityAttackBasicBlockedListControlRequest_Type()
)
sleSecurityAttackBasicBlockedListControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListControlRequest.setStatus("current")
_SleSecurityAttackBasicBlockedListControlStatus_Type = SleControlStatusType
_SleSecurityAttackBasicBlockedListControlStatus_Object = MibScalar
sleSecurityAttackBasicBlockedListControlStatus = _SleSecurityAttackBasicBlockedListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 2, 2),
    _SleSecurityAttackBasicBlockedListControlStatus_Type()
)
sleSecurityAttackBasicBlockedListControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListControlStatus.setStatus("current")
_SleSecurityAttackBasicBlockedListControlTimer_Type = Gauge32
_SleSecurityAttackBasicBlockedListControlTimer_Object = MibScalar
sleSecurityAttackBasicBlockedListControlTimer = _SleSecurityAttackBasicBlockedListControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 2, 3),
    _SleSecurityAttackBasicBlockedListControlTimer_Type()
)
sleSecurityAttackBasicBlockedListControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListControlTimer.setStatus("current")
_SleSecurityAttackBasicBlockedListControlTimeStamp_Type = TimeTicks
_SleSecurityAttackBasicBlockedListControlTimeStamp_Object = MibScalar
sleSecurityAttackBasicBlockedListControlTimeStamp = _SleSecurityAttackBasicBlockedListControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 2, 4),
    _SleSecurityAttackBasicBlockedListControlTimeStamp_Type()
)
sleSecurityAttackBasicBlockedListControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListControlTimeStamp.setStatus("current")
_SleSecurityAttackBasicBlockedListControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackBasicBlockedListControlReqResult_Object = MibScalar
sleSecurityAttackBasicBlockedListControlReqResult = _SleSecurityAttackBasicBlockedListControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 2, 5),
    _SleSecurityAttackBasicBlockedListControlReqResult_Type()
)
sleSecurityAttackBasicBlockedListControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListControlReqResult.setStatus("current")
_SleSecurityAttackBasicBlockedListControlRuleIndex_Type = Integer32
_SleSecurityAttackBasicBlockedListControlRuleIndex_Object = MibScalar
sleSecurityAttackBasicBlockedListControlRuleIndex = _SleSecurityAttackBasicBlockedListControlRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 2, 6),
    _SleSecurityAttackBasicBlockedListControlRuleIndex_Type()
)
sleSecurityAttackBasicBlockedListControlRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListControlRuleIndex.setStatus("current")


class _SleSecurityAttackBasicBlockedListControlBlockTime_Type(Integer32):
    """Custom type sleSecurityAttackBasicBlockedListControlBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 86400),
    )


_SleSecurityAttackBasicBlockedListControlBlockTime_Type.__name__ = "Integer32"
_SleSecurityAttackBasicBlockedListControlBlockTime_Object = MibScalar
sleSecurityAttackBasicBlockedListControlBlockTime = _SleSecurityAttackBasicBlockedListControlBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 2, 7),
    _SleSecurityAttackBasicBlockedListControlBlockTime_Type()
)
sleSecurityAttackBasicBlockedListControlBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListControlBlockTime.setStatus("current")
_SleSecurityAttackBasicBlockedListNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackBasicBlockedListNotification = _SleSecurityAttackBasicBlockedListNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 3)
)
_SleSecurityAttackExpansion_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansion = _SleSecurityAttackExpansion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2)
)
_SleSecurityAttackExpansionBase_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionBase = _SleSecurityAttackExpansionBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1)
)
_SleSecurityAttackExpansionBaseInfo_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionBaseInfo = _SleSecurityAttackExpansionBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 1)
)


class _SleSecurityAttackExpansionBaseGlobalStatus_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBaseGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackExpansionBaseGlobalStatus_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBaseGlobalStatus_Object = MibScalar
sleSecurityAttackExpansionBaseGlobalStatus = _SleSecurityAttackExpansionBaseGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 1, 1),
    _SleSecurityAttackExpansionBaseGlobalStatus_Type()
)
sleSecurityAttackExpansionBaseGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBaseGlobalStatus.setStatus("current")
_SleSecurityAttackExpansionBaseControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionBaseControl = _SleSecurityAttackExpansionBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 2)
)


class _SleSecurityAttackExpansionBaseControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBaseControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setSecurityAttackExpansionGlobalStatus", 1)
    )


_SleSecurityAttackExpansionBaseControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBaseControlRequest_Object = MibScalar
sleSecurityAttackExpansionBaseControlRequest = _SleSecurityAttackExpansionBaseControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 2, 1),
    _SleSecurityAttackExpansionBaseControlRequest_Type()
)
sleSecurityAttackExpansionBaseControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBaseControlRequest.setStatus("current")
_SleSecurityAttackExpansionBaseControlStatus_Type = SleControlStatusType
_SleSecurityAttackExpansionBaseControlStatus_Object = MibScalar
sleSecurityAttackExpansionBaseControlStatus = _SleSecurityAttackExpansionBaseControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 2, 2),
    _SleSecurityAttackExpansionBaseControlStatus_Type()
)
sleSecurityAttackExpansionBaseControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBaseControlStatus.setStatus("current")
_SleSecurityAttackExpansionBaseControlTimer_Type = Gauge32
_SleSecurityAttackExpansionBaseControlTimer_Object = MibScalar
sleSecurityAttackExpansionBaseControlTimer = _SleSecurityAttackExpansionBaseControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 2, 3),
    _SleSecurityAttackExpansionBaseControlTimer_Type()
)
sleSecurityAttackExpansionBaseControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBaseControlTimer.setStatus("current")
_SleSecurityAttackExpansionBaseControlTimeStamp_Type = TimeTicks
_SleSecurityAttackExpansionBaseControlTimeStamp_Object = MibScalar
sleSecurityAttackExpansionBaseControlTimeStamp = _SleSecurityAttackExpansionBaseControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 2, 4),
    _SleSecurityAttackExpansionBaseControlTimeStamp_Type()
)
sleSecurityAttackExpansionBaseControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBaseControlTimeStamp.setStatus("current")
_SleSecurityAttackExpansionBaseControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackExpansionBaseControlReqResult_Object = MibScalar
sleSecurityAttackExpansionBaseControlReqResult = _SleSecurityAttackExpansionBaseControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 2, 5),
    _SleSecurityAttackExpansionBaseControlReqResult_Type()
)
sleSecurityAttackExpansionBaseControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBaseControlReqResult.setStatus("current")


class _SleSecurityAttackExpansionBaseControlGlobalStatus_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBaseControlGlobalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackExpansionBaseControlGlobalStatus_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBaseControlGlobalStatus_Object = MibScalar
sleSecurityAttackExpansionBaseControlGlobalStatus = _SleSecurityAttackExpansionBaseControlGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 2, 6),
    _SleSecurityAttackExpansionBaseControlGlobalStatus_Type()
)
sleSecurityAttackExpansionBaseControlGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBaseControlGlobalStatus.setStatus("current")
_SleSecurityAttackExpansionBaseNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionBaseNotification = _SleSecurityAttackExpansionBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 3)
)
_SleSecurityAttackExpansionPolicy_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionPolicy = _SleSecurityAttackExpansionPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2)
)
_SleSecurityAttackExpansionPolicyTable_Object = MibTable
sleSecurityAttackExpansionPolicyTable = _SleSecurityAttackExpansionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyTable.setStatus("current")
_SleSecurityAttackExpansionPolicyEntry_Object = MibTableRow
sleSecurityAttackExpansionPolicyEntry = _SleSecurityAttackExpansionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 1, 1)
)
sleSecurityAttackExpansionPolicyEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyPortIndex"),
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyEntry.setStatus("current")


class _SleSecurityAttackExpansionPolicyPortIndex_Type(Integer32):
    """Custom type sleSecurityAttackExpansionPolicyPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackExpansionPolicyPortIndex_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionPolicyPortIndex_Object = MibTableColumn
sleSecurityAttackExpansionPolicyPortIndex = _SleSecurityAttackExpansionPolicyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 1, 1, 1),
    _SleSecurityAttackExpansionPolicyPortIndex_Type()
)
sleSecurityAttackExpansionPolicyPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyPortIndex.setStatus("current")


class _SleSecurityAttackExpansionPolicyStatus_Type(Integer32):
    """Custom type sleSecurityAttackExpansionPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleSecurityAttackExpansionPolicyStatus_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionPolicyStatus_Object = MibTableColumn
sleSecurityAttackExpansionPolicyStatus = _SleSecurityAttackExpansionPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 1, 1, 2),
    _SleSecurityAttackExpansionPolicyStatus_Type()
)
sleSecurityAttackExpansionPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyStatus.setStatus("current")


class _SleSecurityAttackExpansionPolicyAttackType_Type(Bits):
    """Custom type sleSecurityAttackExpansionPolicyAttackType based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("tcpDosAttack", 1),
          ("tcpPortFlooding", 2),
          ("tcpHostRandomFlooding", 3),
          ("tcpHostScanning", 4),
          ("ipSppfing", 5),
          ("udpDosAttack", 6),
          ("udpPortFlooding", 7),
          ("udpHostRandomFlooding", 8),
          ("udpHostScanning", 9),
          ("udpIPSppfing", 10),
          ("icmpDosAttack", 11),
          ("icmpIPSppfing", 12),
          ("icmpHostScanning", 13),
          ("arpMacFlooding", 14),
          ("arpSpoofing", 15),
          ("decoySnare", 16),
          ("hostScan", 17),
          ("portScan", 18),
          ("tcpPortScanning", 19),
          ("udpPortScanning", 20),
          ("staticAttack", 21))
    )

_SleSecurityAttackExpansionPolicyAttackType_Type.__name__ = "Bits"
_SleSecurityAttackExpansionPolicyAttackType_Object = MibTableColumn
sleSecurityAttackExpansionPolicyAttackType = _SleSecurityAttackExpansionPolicyAttackType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 1, 1, 3),
    _SleSecurityAttackExpansionPolicyAttackType_Type()
)
sleSecurityAttackExpansionPolicyAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyAttackType.setStatus("current")
_SleSecurityAttackExpansionPolicyBlockTime_Type = OctetString
_SleSecurityAttackExpansionPolicyBlockTime_Object = MibTableColumn
sleSecurityAttackExpansionPolicyBlockTime = _SleSecurityAttackExpansionPolicyBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 1, 1, 4),
    _SleSecurityAttackExpansionPolicyBlockTime_Type()
)
sleSecurityAttackExpansionPolicyBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyBlockTime.setStatus("current")
_SleSecurityAttackExpansionPolicyControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionPolicyControl = _SleSecurityAttackExpansionPolicyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2)
)


class _SleSecurityAttackExpansionPolicyControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackExpansionPolicyControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setSecurityAttackExpansionPolicy", 1)
    )


_SleSecurityAttackExpansionPolicyControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionPolicyControlRequest_Object = MibScalar
sleSecurityAttackExpansionPolicyControlRequest = _SleSecurityAttackExpansionPolicyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2, 1),
    _SleSecurityAttackExpansionPolicyControlRequest_Type()
)
sleSecurityAttackExpansionPolicyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyControlRequest.setStatus("current")
_SleSecurityAttackExpansionPolicyControlStatus_Type = SleControlStatusType
_SleSecurityAttackExpansionPolicyControlStatus_Object = MibScalar
sleSecurityAttackExpansionPolicyControlStatus = _SleSecurityAttackExpansionPolicyControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2, 2),
    _SleSecurityAttackExpansionPolicyControlStatus_Type()
)
sleSecurityAttackExpansionPolicyControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyControlStatus.setStatus("current")
_SleSecurityAttackExpansionPolicyControlTimer_Type = Gauge32
_SleSecurityAttackExpansionPolicyControlTimer_Object = MibScalar
sleSecurityAttackExpansionPolicyControlTimer = _SleSecurityAttackExpansionPolicyControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2, 3),
    _SleSecurityAttackExpansionPolicyControlTimer_Type()
)
sleSecurityAttackExpansionPolicyControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyControlTimer.setStatus("current")
_SleSecurityAttackExpansionPolicyControlTimeStamp_Type = TimeTicks
_SleSecurityAttackExpansionPolicyControlTimeStamp_Object = MibScalar
sleSecurityAttackExpansionPolicyControlTimeStamp = _SleSecurityAttackExpansionPolicyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2, 4),
    _SleSecurityAttackExpansionPolicyControlTimeStamp_Type()
)
sleSecurityAttackExpansionPolicyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyControlTimeStamp.setStatus("current")
_SleSecurityAttackExpansionPolicyControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackExpansionPolicyControlReqResult_Object = MibScalar
sleSecurityAttackExpansionPolicyControlReqResult = _SleSecurityAttackExpansionPolicyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2, 5),
    _SleSecurityAttackExpansionPolicyControlReqResult_Type()
)
sleSecurityAttackExpansionPolicyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyControlReqResult.setStatus("current")
_SleSecurityAttackExpansionPolicyControlPortIndex_Type = Integer32
_SleSecurityAttackExpansionPolicyControlPortIndex_Object = MibScalar
sleSecurityAttackExpansionPolicyControlPortIndex = _SleSecurityAttackExpansionPolicyControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2, 6),
    _SleSecurityAttackExpansionPolicyControlPortIndex_Type()
)
sleSecurityAttackExpansionPolicyControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyControlPortIndex.setStatus("current")


class _SleSecurityAttackExpansionPolicyControlAttackType_Type(Bits):
    """Custom type sleSecurityAttackExpansionPolicyControlAttackType based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("tcpDosAttack", 1),
          ("tcpPortFlooding", 2),
          ("tcpHostRandomFlooding", 3),
          ("tcpHostScanning", 4),
          ("ipSppfing", 5),
          ("udpDosAttack", 6),
          ("udpPortFlooding", 7),
          ("udpHostRandomFlooding", 8),
          ("udpHostScanning", 9),
          ("udpIPSppfing", 10),
          ("icmpDosAttack", 11),
          ("icmpIPSppfing", 12),
          ("icmpHostScanning", 13),
          ("arpMacFlooding", 14),
          ("arpSpoofing", 15),
          ("decoySnare", 16),
          ("hostScan", 17),
          ("portScan", 18),
          ("tcpPortScanning", 19),
          ("udpPortScanning", 20),
          ("staticAttack", 21))
    )

_SleSecurityAttackExpansionPolicyControlAttackType_Type.__name__ = "Bits"
_SleSecurityAttackExpansionPolicyControlAttackType_Object = MibScalar
sleSecurityAttackExpansionPolicyControlAttackType = _SleSecurityAttackExpansionPolicyControlAttackType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2, 7),
    _SleSecurityAttackExpansionPolicyControlAttackType_Type()
)
sleSecurityAttackExpansionPolicyControlAttackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyControlAttackType.setStatus("current")
_SleSecurityAttackExpansionPolicyControlBlockTime_Type = OctetString
_SleSecurityAttackExpansionPolicyControlBlockTime_Object = MibScalar
sleSecurityAttackExpansionPolicyControlBlockTime = _SleSecurityAttackExpansionPolicyControlBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 2, 8),
    _SleSecurityAttackExpansionPolicyControlBlockTime_Type()
)
sleSecurityAttackExpansionPolicyControlBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyControlBlockTime.setStatus("current")
_SleSecurityAttackExpansionPolicyNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionPolicyNotification = _SleSecurityAttackExpansionPolicyNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 3)
)
_SleSecurityAttackExpansionExceptList_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionExceptList = _SleSecurityAttackExpansionExceptList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3)
)
_SleSecurityAttackExpansionExceptListTable_Object = MibTable
sleSecurityAttackExpansionExceptListTable = _SleSecurityAttackExpansionExceptListTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListTable.setStatus("current")
_SleSecurityAttackExpansionExceptListEntry_Object = MibTableRow
sleSecurityAttackExpansionExceptListEntry = _SleSecurityAttackExpansionExceptListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1)
)
sleSecurityAttackExpansionExceptListEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListPortIndex"),
    (0, "SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListIndex"),
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListEntry.setStatus("current")


class _SleSecurityAttackExpansionExceptListPortIndex_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackExpansionExceptListPortIndex_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListPortIndex_Object = MibTableColumn
sleSecurityAttackExpansionExceptListPortIndex = _SleSecurityAttackExpansionExceptListPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 1),
    _SleSecurityAttackExpansionExceptListPortIndex_Type()
)
sleSecurityAttackExpansionExceptListPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListPortIndex.setStatus("current")


class _SleSecurityAttackExpansionExceptListIndex_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackExpansionExceptListIndex_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListIndex_Object = MibTableColumn
sleSecurityAttackExpansionExceptListIndex = _SleSecurityAttackExpansionExceptListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 2),
    _SleSecurityAttackExpansionExceptListIndex_Type()
)
sleSecurityAttackExpansionExceptListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListIndex.setStatus("current")
_SleSecurityAttackExpansionExceptListRuleIndex_Type = Integer32
_SleSecurityAttackExpansionExceptListRuleIndex_Object = MibTableColumn
sleSecurityAttackExpansionExceptListRuleIndex = _SleSecurityAttackExpansionExceptListRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 3),
    _SleSecurityAttackExpansionExceptListRuleIndex_Type()
)
sleSecurityAttackExpansionExceptListRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListRuleIndex.setStatus("current")


class _SleSecurityAttackExpansionExceptListProtocolType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("arp", 4))
    )


_SleSecurityAttackExpansionExceptListProtocolType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListProtocolType_Object = MibTableColumn
sleSecurityAttackExpansionExceptListProtocolType = _SleSecurityAttackExpansionExceptListProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 4),
    _SleSecurityAttackExpansionExceptListProtocolType_Type()
)
sleSecurityAttackExpansionExceptListProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListProtocolType.setStatus("current")


class _SleSecurityAttackExpansionExceptListSourceType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("ip", 1),
          ("mac", 2))
    )


_SleSecurityAttackExpansionExceptListSourceType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListSourceType_Object = MibTableColumn
sleSecurityAttackExpansionExceptListSourceType = _SleSecurityAttackExpansionExceptListSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 5),
    _SleSecurityAttackExpansionExceptListSourceType_Type()
)
sleSecurityAttackExpansionExceptListSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListSourceType.setStatus("current")
_SleSecurityAttackExpansionExceptListSourceIpAddress_Type = IpAddress
_SleSecurityAttackExpansionExceptListSourceIpAddress_Object = MibTableColumn
sleSecurityAttackExpansionExceptListSourceIpAddress = _SleSecurityAttackExpansionExceptListSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 6),
    _SleSecurityAttackExpansionExceptListSourceIpAddress_Type()
)
sleSecurityAttackExpansionExceptListSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListSourceIpAddress.setStatus("current")
_SleSecurityAttackExpansionExceptListSourceIpMask_Type = Integer32
_SleSecurityAttackExpansionExceptListSourceIpMask_Object = MibTableColumn
sleSecurityAttackExpansionExceptListSourceIpMask = _SleSecurityAttackExpansionExceptListSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 7),
    _SleSecurityAttackExpansionExceptListSourceIpMask_Type()
)
sleSecurityAttackExpansionExceptListSourceIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListSourceIpMask.setStatus("current")
_SleSecurityAttackExpansionExceptListSourceMac_Type = OctetString
_SleSecurityAttackExpansionExceptListSourceMac_Object = MibTableColumn
sleSecurityAttackExpansionExceptListSourceMac = _SleSecurityAttackExpansionExceptListSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 8),
    _SleSecurityAttackExpansionExceptListSourceMac_Type()
)
sleSecurityAttackExpansionExceptListSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListSourceMac.setStatus("current")


class _SleSecurityAttackExpansionExceptListSourcePortType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListSourcePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("equal", 1),
          ("range", 2))
    )


_SleSecurityAttackExpansionExceptListSourcePortType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListSourcePortType_Object = MibTableColumn
sleSecurityAttackExpansionExceptListSourcePortType = _SleSecurityAttackExpansionExceptListSourcePortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 9),
    _SleSecurityAttackExpansionExceptListSourcePortType_Type()
)
sleSecurityAttackExpansionExceptListSourcePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListSourcePortType.setStatus("current")
_SleSecurityAttackExpansionExceptListSourcePortFrom_Type = Integer32
_SleSecurityAttackExpansionExceptListSourcePortFrom_Object = MibTableColumn
sleSecurityAttackExpansionExceptListSourcePortFrom = _SleSecurityAttackExpansionExceptListSourcePortFrom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 10),
    _SleSecurityAttackExpansionExceptListSourcePortFrom_Type()
)
sleSecurityAttackExpansionExceptListSourcePortFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListSourcePortFrom.setStatus("current")
_SleSecurityAttackExpansionExceptListSourcePortTo_Type = Integer32
_SleSecurityAttackExpansionExceptListSourcePortTo_Object = MibTableColumn
sleSecurityAttackExpansionExceptListSourcePortTo = _SleSecurityAttackExpansionExceptListSourcePortTo_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 11),
    _SleSecurityAttackExpansionExceptListSourcePortTo_Type()
)
sleSecurityAttackExpansionExceptListSourcePortTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListSourcePortTo.setStatus("current")


class _SleSecurityAttackExpansionExceptListDestinationType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListDestinationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("ip", 1),
          ("mac", 2))
    )


_SleSecurityAttackExpansionExceptListDestinationType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListDestinationType_Object = MibTableColumn
sleSecurityAttackExpansionExceptListDestinationType = _SleSecurityAttackExpansionExceptListDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 12),
    _SleSecurityAttackExpansionExceptListDestinationType_Type()
)
sleSecurityAttackExpansionExceptListDestinationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListDestinationType.setStatus("current")
_SleSecurityAttackExpansionExceptListDestinationIpAddress_Type = IpAddress
_SleSecurityAttackExpansionExceptListDestinationIpAddress_Object = MibTableColumn
sleSecurityAttackExpansionExceptListDestinationIpAddress = _SleSecurityAttackExpansionExceptListDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 13),
    _SleSecurityAttackExpansionExceptListDestinationIpAddress_Type()
)
sleSecurityAttackExpansionExceptListDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListDestinationIpAddress.setStatus("current")
_SleSecurityAttackExpansionExceptListDestinationIpMask_Type = Integer32
_SleSecurityAttackExpansionExceptListDestinationIpMask_Object = MibTableColumn
sleSecurityAttackExpansionExceptListDestinationIpMask = _SleSecurityAttackExpansionExceptListDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 14),
    _SleSecurityAttackExpansionExceptListDestinationIpMask_Type()
)
sleSecurityAttackExpansionExceptListDestinationIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListDestinationIpMask.setStatus("current")
_SleSecurityAttackExpansionExceptListDestinationMac_Type = OctetString
_SleSecurityAttackExpansionExceptListDestinationMac_Object = MibTableColumn
sleSecurityAttackExpansionExceptListDestinationMac = _SleSecurityAttackExpansionExceptListDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 15),
    _SleSecurityAttackExpansionExceptListDestinationMac_Type()
)
sleSecurityAttackExpansionExceptListDestinationMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListDestinationMac.setStatus("current")


class _SleSecurityAttackExpansionExceptListDestinationPortType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListDestinationPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("equal", 1),
          ("range", 2))
    )


_SleSecurityAttackExpansionExceptListDestinationPortType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListDestinationPortType_Object = MibTableColumn
sleSecurityAttackExpansionExceptListDestinationPortType = _SleSecurityAttackExpansionExceptListDestinationPortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 16),
    _SleSecurityAttackExpansionExceptListDestinationPortType_Type()
)
sleSecurityAttackExpansionExceptListDestinationPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListDestinationPortType.setStatus("current")
_SleSecurityAttackExpansionExceptListDestinationPortFrom_Type = Integer32
_SleSecurityAttackExpansionExceptListDestinationPortFrom_Object = MibTableColumn
sleSecurityAttackExpansionExceptListDestinationPortFrom = _SleSecurityAttackExpansionExceptListDestinationPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 17),
    _SleSecurityAttackExpansionExceptListDestinationPortFrom_Type()
)
sleSecurityAttackExpansionExceptListDestinationPortFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListDestinationPortFrom.setStatus("current")
_SleSecurityAttackExpansionExceptListDestinationPortTo_Type = Integer32
_SleSecurityAttackExpansionExceptListDestinationPortTo_Object = MibTableColumn
sleSecurityAttackExpansionExceptListDestinationPortTo = _SleSecurityAttackExpansionExceptListDestinationPortTo_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 1, 1, 18),
    _SleSecurityAttackExpansionExceptListDestinationPortTo_Type()
)
sleSecurityAttackExpansionExceptListDestinationPortTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListDestinationPortTo.setStatus("current")
_SleSecurityAttackExpansionExceptListControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionExceptListControl = _SleSecurityAttackExpansionExceptListControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2)
)


class _SleSecurityAttackExpansionExceptListControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createSecurityAttackExpansionExceptList", 1),
          ("modifyPortAttackExpansionExceptList", 2),
          ("delPortAttackExpansionExceptList", 3))
    )


_SleSecurityAttackExpansionExceptListControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListControlRequest_Object = MibScalar
sleSecurityAttackExpansionExceptListControlRequest = _SleSecurityAttackExpansionExceptListControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 1),
    _SleSecurityAttackExpansionExceptListControlRequest_Type()
)
sleSecurityAttackExpansionExceptListControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlRequest.setStatus("current")
_SleSecurityAttackExpansionExceptListControlStatus_Type = SleControlStatusType
_SleSecurityAttackExpansionExceptListControlStatus_Object = MibScalar
sleSecurityAttackExpansionExceptListControlStatus = _SleSecurityAttackExpansionExceptListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 2),
    _SleSecurityAttackExpansionExceptListControlStatus_Type()
)
sleSecurityAttackExpansionExceptListControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlStatus.setStatus("current")
_SleSecurityAttackExpansionExceptListControlTimer_Type = Gauge32
_SleSecurityAttackExpansionExceptListControlTimer_Object = MibScalar
sleSecurityAttackExpansionExceptListControlTimer = _SleSecurityAttackExpansionExceptListControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 3),
    _SleSecurityAttackExpansionExceptListControlTimer_Type()
)
sleSecurityAttackExpansionExceptListControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlTimer.setStatus("current")
_SleSecurityAttackExpansionExceptListControlTimeStamp_Type = TimeTicks
_SleSecurityAttackExpansionExceptListControlTimeStamp_Object = MibScalar
sleSecurityAttackExpansionExceptListControlTimeStamp = _SleSecurityAttackExpansionExceptListControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 4),
    _SleSecurityAttackExpansionExceptListControlTimeStamp_Type()
)
sleSecurityAttackExpansionExceptListControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlTimeStamp.setStatus("current")
_SleSecurityAttackExpansionExceptListControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackExpansionExceptListControlReqResult_Object = MibScalar
sleSecurityAttackExpansionExceptListControlReqResult = _SleSecurityAttackExpansionExceptListControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 5),
    _SleSecurityAttackExpansionExceptListControlReqResult_Type()
)
sleSecurityAttackExpansionExceptListControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlReqResult.setStatus("current")
_SleSecurityAttackExpansionExceptListControlPortIndex_Type = Integer32
_SleSecurityAttackExpansionExceptListControlPortIndex_Object = MibScalar
sleSecurityAttackExpansionExceptListControlPortIndex = _SleSecurityAttackExpansionExceptListControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 6),
    _SleSecurityAttackExpansionExceptListControlPortIndex_Type()
)
sleSecurityAttackExpansionExceptListControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlPortIndex.setStatus("current")
_SleSecurityAttackExpansionExceptListControlRuleIndex_Type = Integer32
_SleSecurityAttackExpansionExceptListControlRuleIndex_Object = MibScalar
sleSecurityAttackExpansionExceptListControlRuleIndex = _SleSecurityAttackExpansionExceptListControlRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 7),
    _SleSecurityAttackExpansionExceptListControlRuleIndex_Type()
)
sleSecurityAttackExpansionExceptListControlRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlRuleIndex.setStatus("current")


class _SleSecurityAttackExpansionExceptListControlProtocolType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListControlProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("arp", 4))
    )


_SleSecurityAttackExpansionExceptListControlProtocolType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListControlProtocolType_Object = MibScalar
sleSecurityAttackExpansionExceptListControlProtocolType = _SleSecurityAttackExpansionExceptListControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 8),
    _SleSecurityAttackExpansionExceptListControlProtocolType_Type()
)
sleSecurityAttackExpansionExceptListControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlProtocolType.setStatus("current")


class _SleSecurityAttackExpansionExceptListControlSourceType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListControlSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("ip", 1),
          ("mac", 2))
    )


_SleSecurityAttackExpansionExceptListControlSourceType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListControlSourceType_Object = MibScalar
sleSecurityAttackExpansionExceptListControlSourceType = _SleSecurityAttackExpansionExceptListControlSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 9),
    _SleSecurityAttackExpansionExceptListControlSourceType_Type()
)
sleSecurityAttackExpansionExceptListControlSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlSourceType.setStatus("current")
_SleSecurityAttackExpansionExceptListControlSourceIpAddress_Type = IpAddress
_SleSecurityAttackExpansionExceptListControlSourceIpAddress_Object = MibScalar
sleSecurityAttackExpansionExceptListControlSourceIpAddress = _SleSecurityAttackExpansionExceptListControlSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 10),
    _SleSecurityAttackExpansionExceptListControlSourceIpAddress_Type()
)
sleSecurityAttackExpansionExceptListControlSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlSourceIpAddress.setStatus("current")
_SleSecurityAttackExpansionExceptListControlSourceIpMask_Type = Integer32
_SleSecurityAttackExpansionExceptListControlSourceIpMask_Object = MibScalar
sleSecurityAttackExpansionExceptListControlSourceIpMask = _SleSecurityAttackExpansionExceptListControlSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 11),
    _SleSecurityAttackExpansionExceptListControlSourceIpMask_Type()
)
sleSecurityAttackExpansionExceptListControlSourceIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlSourceIpMask.setStatus("current")
_SleSecurityAttackExpansionExceptListControlSourceMac_Type = OctetString
_SleSecurityAttackExpansionExceptListControlSourceMac_Object = MibScalar
sleSecurityAttackExpansionExceptListControlSourceMac = _SleSecurityAttackExpansionExceptListControlSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 12),
    _SleSecurityAttackExpansionExceptListControlSourceMac_Type()
)
sleSecurityAttackExpansionExceptListControlSourceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlSourceMac.setStatus("current")


class _SleSecurityAttackExpansionExceptListControlSourcePortType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListControlSourcePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("equal", 1),
          ("range", 2))
    )


_SleSecurityAttackExpansionExceptListControlSourcePortType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListControlSourcePortType_Object = MibScalar
sleSecurityAttackExpansionExceptListControlSourcePortType = _SleSecurityAttackExpansionExceptListControlSourcePortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 13),
    _SleSecurityAttackExpansionExceptListControlSourcePortType_Type()
)
sleSecurityAttackExpansionExceptListControlSourcePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlSourcePortType.setStatus("current")
_SleSecurityAttackExpansionExceptListControlSourcePortFrom_Type = Integer32
_SleSecurityAttackExpansionExceptListControlSourcePortFrom_Object = MibScalar
sleSecurityAttackExpansionExceptListControlSourcePortFrom = _SleSecurityAttackExpansionExceptListControlSourcePortFrom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 14),
    _SleSecurityAttackExpansionExceptListControlSourcePortFrom_Type()
)
sleSecurityAttackExpansionExceptListControlSourcePortFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlSourcePortFrom.setStatus("current")
_SleSecurityAttackExpansionExceptListControlSourcePortTo_Type = Integer32
_SleSecurityAttackExpansionExceptListControlSourcePortTo_Object = MibScalar
sleSecurityAttackExpansionExceptListControlSourcePortTo = _SleSecurityAttackExpansionExceptListControlSourcePortTo_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 15),
    _SleSecurityAttackExpansionExceptListControlSourcePortTo_Type()
)
sleSecurityAttackExpansionExceptListControlSourcePortTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlSourcePortTo.setStatus("current")


class _SleSecurityAttackExpansionExceptListControlDestinationType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListControlDestinationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("ip", 1),
          ("mac", 2))
    )


_SleSecurityAttackExpansionExceptListControlDestinationType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListControlDestinationType_Object = MibScalar
sleSecurityAttackExpansionExceptListControlDestinationType = _SleSecurityAttackExpansionExceptListControlDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 16),
    _SleSecurityAttackExpansionExceptListControlDestinationType_Type()
)
sleSecurityAttackExpansionExceptListControlDestinationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlDestinationType.setStatus("current")
_SleSecurityAttackExpansionExceptListControlDestinationIpAddress_Type = IpAddress
_SleSecurityAttackExpansionExceptListControlDestinationIpAddress_Object = MibScalar
sleSecurityAttackExpansionExceptListControlDestinationIpAddress = _SleSecurityAttackExpansionExceptListControlDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 17),
    _SleSecurityAttackExpansionExceptListControlDestinationIpAddress_Type()
)
sleSecurityAttackExpansionExceptListControlDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlDestinationIpAddress.setStatus("current")
_SleSecurityAttackExpansionExceptListControlDestinationIpMask_Type = Integer32
_SleSecurityAttackExpansionExceptListControlDestinationIpMask_Object = MibScalar
sleSecurityAttackExpansionExceptListControlDestinationIpMask = _SleSecurityAttackExpansionExceptListControlDestinationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 18),
    _SleSecurityAttackExpansionExceptListControlDestinationIpMask_Type()
)
sleSecurityAttackExpansionExceptListControlDestinationIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlDestinationIpMask.setStatus("current")
_SleSecurityAttackExpansionExceptListControlDestinationMac_Type = Integer32
_SleSecurityAttackExpansionExceptListControlDestinationMac_Object = MibScalar
sleSecurityAttackExpansionExceptListControlDestinationMac = _SleSecurityAttackExpansionExceptListControlDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 19),
    _SleSecurityAttackExpansionExceptListControlDestinationMac_Type()
)
sleSecurityAttackExpansionExceptListControlDestinationMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlDestinationMac.setStatus("current")


class _SleSecurityAttackExpansionExceptListControlDestinationPortType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionExceptListControlDestinationPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("equal", 1),
          ("range", 2))
    )


_SleSecurityAttackExpansionExceptListControlDestinationPortType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionExceptListControlDestinationPortType_Object = MibScalar
sleSecurityAttackExpansionExceptListControlDestinationPortType = _SleSecurityAttackExpansionExceptListControlDestinationPortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 20),
    _SleSecurityAttackExpansionExceptListControlDestinationPortType_Type()
)
sleSecurityAttackExpansionExceptListControlDestinationPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlDestinationPortType.setStatus("current")
_SleSecurityAttackExpansionExceptListControlDestinationPortFrom_Type = Integer32
_SleSecurityAttackExpansionExceptListControlDestinationPortFrom_Object = MibScalar
sleSecurityAttackExpansionExceptListControlDestinationPortFrom = _SleSecurityAttackExpansionExceptListControlDestinationPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 21),
    _SleSecurityAttackExpansionExceptListControlDestinationPortFrom_Type()
)
sleSecurityAttackExpansionExceptListControlDestinationPortFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlDestinationPortFrom.setStatus("current")
_SleSecurityAttackExpansionExceptListControlDestinationPortTo_Type = Integer32
_SleSecurityAttackExpansionExceptListControlDestinationPortTo_Object = MibScalar
sleSecurityAttackExpansionExceptListControlDestinationPortTo = _SleSecurityAttackExpansionExceptListControlDestinationPortTo_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 2, 22),
    _SleSecurityAttackExpansionExceptListControlDestinationPortTo_Type()
)
sleSecurityAttackExpansionExceptListControlDestinationPortTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListControlDestinationPortTo.setStatus("current")
_SleSecurityAttackExpansionExceptListNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionExceptListNotification = _SleSecurityAttackExpansionExceptListNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 3)
)
_SleSecurityAttackExpansionBlockedList_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionBlockedList = _SleSecurityAttackExpansionBlockedList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4)
)
_SleSecurityAttackExpansionBlockedListTable_Object = MibTable
sleSecurityAttackExpansionBlockedListTable = _SleSecurityAttackExpansionBlockedListTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListTable.setStatus("current")
_SleSecurityAttackExpansionBlockedListEntry_Object = MibTableRow
sleSecurityAttackExpansionBlockedListEntry = _SleSecurityAttackExpansionBlockedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1)
)
sleSecurityAttackExpansionBlockedListEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListPortIndex"),
    (0, "SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListIndex"),
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListEntry.setStatus("current")


class _SleSecurityAttackExpansionBlockedListPortIndex_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackExpansionBlockedListPortIndex_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListPortIndex_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListPortIndex = _SleSecurityAttackExpansionBlockedListPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 1),
    _SleSecurityAttackExpansionBlockedListPortIndex_Type()
)
sleSecurityAttackExpansionBlockedListPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListPortIndex.setStatus("current")


class _SleSecurityAttackExpansionBlockedListIndex_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleSecurityAttackExpansionBlockedListIndex_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListIndex_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListIndex = _SleSecurityAttackExpansionBlockedListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 2),
    _SleSecurityAttackExpansionBlockedListIndex_Type()
)
sleSecurityAttackExpansionBlockedListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListIndex.setStatus("current")
_SleSecurityAttackExpansionBlockedListRuleIndex_Type = Integer32
_SleSecurityAttackExpansionBlockedListRuleIndex_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListRuleIndex = _SleSecurityAttackExpansionBlockedListRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 3),
    _SleSecurityAttackExpansionBlockedListRuleIndex_Type()
)
sleSecurityAttackExpansionBlockedListRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListRuleIndex.setStatus("current")


class _SleSecurityAttackExpansionBlockedListAttackType_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListAttackType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tcpDosAttack", 1),
          ("tcpPortFlooding", 2),
          ("tcpHostRandomFlooding", 3),
          ("tcpHostScanning", 4),
          ("ipSppfing", 5),
          ("udpDosAttack", 6),
          ("udpPortFlooding", 7),
          ("udpHostRandomFlooding", 8),
          ("udpHostScanning", 9),
          ("udpIPSppfing", 10),
          ("icmpDosAttack", 11),
          ("icmpIPSppfing", 12),
          ("icmpHostScanning", 13),
          ("arpMacFlooding", 14),
          ("arpSpoofing", 15),
          ("decoySnare", 16),
          ("hostScan", 17),
          ("portScan", 18),
          ("tcpPortScanning", 19),
          ("udpPortScanning", 20),
          ("staticAttack", 21))
    )


_SleSecurityAttackExpansionBlockedListAttackType_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListAttackType_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListAttackType = _SleSecurityAttackExpansionBlockedListAttackType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 4),
    _SleSecurityAttackExpansionBlockedListAttackType_Type()
)
sleSecurityAttackExpansionBlockedListAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListAttackType.setStatus("current")


class _SleSecurityAttackExpansionBlockedListAttackBlockType_Type(Bits):
    """Custom type sleSecurityAttackExpansionBlockedListAttackBlockType based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("sourceIp", 1),
          ("sourceMac", 2),
          ("sourcePort", 3),
          ("destinationIp", 4),
          ("destinationPort", 5))
    )

_SleSecurityAttackExpansionBlockedListAttackBlockType_Type.__name__ = "Bits"
_SleSecurityAttackExpansionBlockedListAttackBlockType_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListAttackBlockType = _SleSecurityAttackExpansionBlockedListAttackBlockType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 5),
    _SleSecurityAttackExpansionBlockedListAttackBlockType_Type()
)
sleSecurityAttackExpansionBlockedListAttackBlockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListAttackBlockType.setStatus("current")
_SleSecurityAttackExpansionBlockedListStartTime_Type = OctetString
_SleSecurityAttackExpansionBlockedListStartTime_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListStartTime = _SleSecurityAttackExpansionBlockedListStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 6),
    _SleSecurityAttackExpansionBlockedListStartTime_Type()
)
sleSecurityAttackExpansionBlockedListStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListStartTime.setStatus("current")
_SleSecurityAttackExpansionBlockedListEndTime_Type = OctetString
_SleSecurityAttackExpansionBlockedListEndTime_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListEndTime = _SleSecurityAttackExpansionBlockedListEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 7),
    _SleSecurityAttackExpansionBlockedListEndTime_Type()
)
sleSecurityAttackExpansionBlockedListEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListEndTime.setStatus("current")
_SleSecurityAttackExpansionBlockedListAttackSourceIp_Type = IpAddress
_SleSecurityAttackExpansionBlockedListAttackSourceIp_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListAttackSourceIp = _SleSecurityAttackExpansionBlockedListAttackSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 8),
    _SleSecurityAttackExpansionBlockedListAttackSourceIp_Type()
)
sleSecurityAttackExpansionBlockedListAttackSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListAttackSourceIp.setStatus("current")
_SleSecurityAttackExpansionBlockedListSourceMac_Type = OctetString
_SleSecurityAttackExpansionBlockedListSourceMac_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListSourceMac = _SleSecurityAttackExpansionBlockedListSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 9),
    _SleSecurityAttackExpansionBlockedListSourceMac_Type()
)
sleSecurityAttackExpansionBlockedListSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListSourceMac.setStatus("current")
_SleSecurityAttackExpansionBlockedListAttackDestinationIp_Type = IpAddress
_SleSecurityAttackExpansionBlockedListAttackDestinationIp_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListAttackDestinationIp = _SleSecurityAttackExpansionBlockedListAttackDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 10),
    _SleSecurityAttackExpansionBlockedListAttackDestinationIp_Type()
)
sleSecurityAttackExpansionBlockedListAttackDestinationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListAttackDestinationIp.setStatus("current")


class _SleSecurityAttackExpansionBlockedListProtocol_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("arp", 4))
    )


_SleSecurityAttackExpansionBlockedListProtocol_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListProtocol_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListProtocol = _SleSecurityAttackExpansionBlockedListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 11),
    _SleSecurityAttackExpansionBlockedListProtocol_Type()
)
sleSecurityAttackExpansionBlockedListProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListProtocol.setStatus("current")


class _SleSecurityAttackExpansionBlockedListSourcePort_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSecurityAttackExpansionBlockedListSourcePort_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListSourcePort_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListSourcePort = _SleSecurityAttackExpansionBlockedListSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 12),
    _SleSecurityAttackExpansionBlockedListSourcePort_Type()
)
sleSecurityAttackExpansionBlockedListSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListSourcePort.setStatus("current")


class _SleSecurityAttackExpansionBlockedListDestinationPort_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleSecurityAttackExpansionBlockedListDestinationPort_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListDestinationPort_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListDestinationPort = _SleSecurityAttackExpansionBlockedListDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 13),
    _SleSecurityAttackExpansionBlockedListDestinationPort_Type()
)
sleSecurityAttackExpansionBlockedListDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListDestinationPort.setStatus("current")
_SleSecurityAttackExpansionBlockedListAttackPktCount_Type = Counter32
_SleSecurityAttackExpansionBlockedListAttackPktCount_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListAttackPktCount = _SleSecurityAttackExpansionBlockedListAttackPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 14),
    _SleSecurityAttackExpansionBlockedListAttackPktCount_Type()
)
sleSecurityAttackExpansionBlockedListAttackPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListAttackPktCount.setStatus("current")


class _SleSecurityAttackExpansionBlockedListAttackBlockTime_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListAttackBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 86400),
    )


_SleSecurityAttackExpansionBlockedListAttackBlockTime_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListAttackBlockTime_Object = MibTableColumn
sleSecurityAttackExpansionBlockedListAttackBlockTime = _SleSecurityAttackExpansionBlockedListAttackBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 1, 1, 15),
    _SleSecurityAttackExpansionBlockedListAttackBlockTime_Type()
)
sleSecurityAttackExpansionBlockedListAttackBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListAttackBlockTime.setStatus("current")
_SleSecurityAttackExpansionBlockedListControl_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionBlockedListControl = _SleSecurityAttackExpansionBlockedListControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 2)
)


class _SleSecurityAttackExpansionBlockedListControlRequest_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setPortAttackExpansionBlockTime", 1)
    )


_SleSecurityAttackExpansionBlockedListControlRequest_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListControlRequest_Object = MibScalar
sleSecurityAttackExpansionBlockedListControlRequest = _SleSecurityAttackExpansionBlockedListControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 2, 1),
    _SleSecurityAttackExpansionBlockedListControlRequest_Type()
)
sleSecurityAttackExpansionBlockedListControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListControlRequest.setStatus("current")
_SleSecurityAttackExpansionBlockedListControlStatus_Type = SleControlStatusType
_SleSecurityAttackExpansionBlockedListControlStatus_Object = MibScalar
sleSecurityAttackExpansionBlockedListControlStatus = _SleSecurityAttackExpansionBlockedListControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 2, 2),
    _SleSecurityAttackExpansionBlockedListControlStatus_Type()
)
sleSecurityAttackExpansionBlockedListControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListControlStatus.setStatus("current")
_SleSecurityAttackExpansionBlockedListControlTimer_Type = Gauge32
_SleSecurityAttackExpansionBlockedListControlTimer_Object = MibScalar
sleSecurityAttackExpansionBlockedListControlTimer = _SleSecurityAttackExpansionBlockedListControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 2, 3),
    _SleSecurityAttackExpansionBlockedListControlTimer_Type()
)
sleSecurityAttackExpansionBlockedListControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListControlTimer.setStatus("current")
_SleSecurityAttackExpansionBlockedListControlTimeStamp_Type = TimeTicks
_SleSecurityAttackExpansionBlockedListControlTimeStamp_Object = MibScalar
sleSecurityAttackExpansionBlockedListControlTimeStamp = _SleSecurityAttackExpansionBlockedListControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 2, 4),
    _SleSecurityAttackExpansionBlockedListControlTimeStamp_Type()
)
sleSecurityAttackExpansionBlockedListControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListControlTimeStamp.setStatus("current")
_SleSecurityAttackExpansionBlockedListControlReqResult_Type = SleControlRequestResultType
_SleSecurityAttackExpansionBlockedListControlReqResult_Object = MibScalar
sleSecurityAttackExpansionBlockedListControlReqResult = _SleSecurityAttackExpansionBlockedListControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 2, 5),
    _SleSecurityAttackExpansionBlockedListControlReqResult_Type()
)
sleSecurityAttackExpansionBlockedListControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListControlReqResult.setStatus("current")
_SleSecurityAttackExpansionBlockedListControlRuleIndex_Type = Integer32
_SleSecurityAttackExpansionBlockedListControlRuleIndex_Object = MibScalar
sleSecurityAttackExpansionBlockedListControlRuleIndex = _SleSecurityAttackExpansionBlockedListControlRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 2, 6),
    _SleSecurityAttackExpansionBlockedListControlRuleIndex_Type()
)
sleSecurityAttackExpansionBlockedListControlRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListControlRuleIndex.setStatus("current")


class _SleSecurityAttackExpansionBlockedListControlBlockTime_Type(Integer32):
    """Custom type sleSecurityAttackExpansionBlockedListControlBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 86400),
    )


_SleSecurityAttackExpansionBlockedListControlBlockTime_Type.__name__ = "Integer32"
_SleSecurityAttackExpansionBlockedListControlBlockTime_Object = MibScalar
sleSecurityAttackExpansionBlockedListControlBlockTime = _SleSecurityAttackExpansionBlockedListControlBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 2, 7),
    _SleSecurityAttackExpansionBlockedListControlBlockTime_Type()
)
sleSecurityAttackExpansionBlockedListControlBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListControlBlockTime.setStatus("current")
_SleSecurityAttackExpansionBlockedListNotification_ObjectIdentity = ObjectIdentity
sleSecurityAttackExpansionBlockedListNotification = _SleSecurityAttackExpansionBlockedListNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 3)
)
_SleNDInspection_ObjectIdentity = ObjectIdentity
sleNDInspection = _SleNDInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12)
)
_SleNDInspectBase_ObjectIdentity = ObjectIdentity
sleNDInspectBase = _SleNDInspectBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1)
)
_SleNDInspectBaseInfo_ObjectIdentity = ObjectIdentity
sleNDInspectBaseInfo = _SleNDInspectBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 1)
)


class _SleNDInspectLogBufferSize_Type(Integer32):
    """Custom type sleNDInspectLogBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleNDInspectLogBufferSize_Type.__name__ = "Integer32"
_SleNDInspectLogBufferSize_Object = MibScalar
sleNDInspectLogBufferSize = _SleNDInspectLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 1, 1),
    _SleNDInspectLogBufferSize_Type()
)
sleNDInspectLogBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectLogBufferSize.setStatus("current")


class _SleNDInspectLogEntry_Type(Integer32):
    """Custom type sleNDInspectLogEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleNDInspectLogEntry_Type.__name__ = "Integer32"
_SleNDInspectLogEntry_Object = MibScalar
sleNDInspectLogEntry = _SleNDInspectLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 1, 2),
    _SleNDInspectLogEntry_Type()
)
sleNDInspectLogEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectLogEntry.setStatus("current")


class _SleNDInspectLogInterval_Type(Integer32):
    """Custom type sleNDInspectLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SleNDInspectLogInterval_Type.__name__ = "Integer32"
_SleNDInspectLogInterval_Object = MibScalar
sleNDInspectLogInterval = _SleNDInspectLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 1, 3),
    _SleNDInspectLogInterval_Type()
)
sleNDInspectLogInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectLogInterval.setStatus("current")
_SleNDInspectBaseControl_ObjectIdentity = ObjectIdentity
sleNDInspectBaseControl = _SleNDInspectBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2)
)


class _SleNDInspectControlRequest_Type(Integer32):
    """Custom type sleNDInspectControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setNDInspectLogBufferSize", 1),
          ("setNDInspectLogRate", 2))
    )


_SleNDInspectControlRequest_Type.__name__ = "Integer32"
_SleNDInspectControlRequest_Object = MibScalar
sleNDInspectControlRequest = _SleNDInspectControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2, 1),
    _SleNDInspectControlRequest_Type()
)
sleNDInspectControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectControlRequest.setStatus("current")
_SleNDInspectControlStatus_Type = SleControlStatusType
_SleNDInspectControlStatus_Object = MibScalar
sleNDInspectControlStatus = _SleNDInspectControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2, 2),
    _SleNDInspectControlStatus_Type()
)
sleNDInspectControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectControlStatus.setStatus("current")
_SleNDInspectControlTimer_Type = Gauge32
_SleNDInspectControlTimer_Object = MibScalar
sleNDInspectControlTimer = _SleNDInspectControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2, 3),
    _SleNDInspectControlTimer_Type()
)
sleNDInspectControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectControlTimer.setStatus("current")
_SleNDInspectControlTimeStamp_Type = TimeTicks
_SleNDInspectControlTimeStamp_Object = MibScalar
sleNDInspectControlTimeStamp = _SleNDInspectControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2, 4),
    _SleNDInspectControlTimeStamp_Type()
)
sleNDInspectControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectControlTimeStamp.setStatus("current")
_SleNDInspectControlReqResult_Type = SleControlRequestResultType
_SleNDInspectControlReqResult_Object = MibScalar
sleNDInspectControlReqResult = _SleNDInspectControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2, 5),
    _SleNDInspectControlReqResult_Type()
)
sleNDInspectControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectControlReqResult.setStatus("current")


class _SleNDInspectControlLogBufferSize_Type(Integer32):
    """Custom type sleNDInspectControlLogBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleNDInspectControlLogBufferSize_Type.__name__ = "Integer32"
_SleNDInspectControlLogBufferSize_Object = MibScalar
sleNDInspectControlLogBufferSize = _SleNDInspectControlLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2, 6),
    _SleNDInspectControlLogBufferSize_Type()
)
sleNDInspectControlLogBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectControlLogBufferSize.setStatus("current")


class _SleNDInspectControlLogEntry_Type(Integer32):
    """Custom type sleNDInspectControlLogEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_SleNDInspectControlLogEntry_Type.__name__ = "Integer32"
_SleNDInspectControlLogEntry_Object = MibScalar
sleNDInspectControlLogEntry = _SleNDInspectControlLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2, 7),
    _SleNDInspectControlLogEntry_Type()
)
sleNDInspectControlLogEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectControlLogEntry.setStatus("current")


class _SleNDInspectControlLogInterval_Type(Integer32):
    """Custom type sleNDInspectControlLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_SleNDInspectControlLogInterval_Type.__name__ = "Integer32"
_SleNDInspectControlLogInterval_Object = MibScalar
sleNDInspectControlLogInterval = _SleNDInspectControlLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 2, 8),
    _SleNDInspectControlLogInterval_Type()
)
sleNDInspectControlLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectControlLogInterval.setStatus("current")
_SleNDInspectBaseNotifications_ObjectIdentity = ObjectIdentity
sleNDInspectBaseNotifications = _SleNDInspectBaseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 3)
)
_SleNDACL_ObjectIdentity = ObjectIdentity
sleNDACL = _SleNDACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2)
)
_SleNDAclTable_Object = MibTable
sleNDAclTable = _SleNDAclTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 1)
)
if mibBuilder.loadTexts:
    sleNDAclTable.setStatus("current")
_SleNDAclEntry_Object = MibTableRow
sleNDAclEntry = _SleNDAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 1, 1)
)
sleNDAclEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleNDAclIndex"),
)
if mibBuilder.loadTexts:
    sleNDAclEntry.setStatus("current")


class _SleNDAclIndex_Type(Integer32):
    """Custom type sleNDAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleNDAclIndex_Type.__name__ = "Integer32"
_SleNDAclIndex_Object = MibTableColumn
sleNDAclIndex = _SleNDAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 1, 1, 1),
    _SleNDAclIndex_Type()
)
sleNDAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclIndex.setStatus("current")


class _SleNDAclName_Type(OctetString):
    """Custom type sleNDAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleNDAclName_Type.__name__ = "OctetString"
_SleNDAclName_Object = MibTableColumn
sleNDAclName = _SleNDAclName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 1, 1, 2),
    _SleNDAclName_Type()
)
sleNDAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclName.setStatus("current")


class _SleNDAclNumEntries_Type(Integer32):
    """Custom type sleNDAclNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleNDAclNumEntries_Type.__name__ = "Integer32"
_SleNDAclNumEntries_Object = MibTableColumn
sleNDAclNumEntries = _SleNDAclNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 1, 1, 3),
    _SleNDAclNumEntries_Type()
)
sleNDAclNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclNumEntries.setStatus("current")
_SleNDAclControl_ObjectIdentity = ObjectIdentity
sleNDAclControl = _SleNDAclControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 2)
)


class _SleNDAclControlRequest_Type(Integer32):
    """Custom type sleNDAclControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createNDAcl", 1),
          ("destroyNDAcl", 2))
    )


_SleNDAclControlRequest_Type.__name__ = "Integer32"
_SleNDAclControlRequest_Object = MibScalar
sleNDAclControlRequest = _SleNDAclControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 2, 1),
    _SleNDAclControlRequest_Type()
)
sleNDAclControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclControlRequest.setStatus("current")
_SleNDAclControlStatus_Type = SleControlStatusType
_SleNDAclControlStatus_Object = MibScalar
sleNDAclControlStatus = _SleNDAclControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 2, 2),
    _SleNDAclControlStatus_Type()
)
sleNDAclControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclControlStatus.setStatus("current")
_SleNDAclControlTimer_Type = Gauge32
_SleNDAclControlTimer_Object = MibScalar
sleNDAclControlTimer = _SleNDAclControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 2, 3),
    _SleNDAclControlTimer_Type()
)
sleNDAclControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclControlTimer.setStatus("current")
_SleNDAclControlTimeStamp_Type = TimeTicks
_SleNDAclControlTimeStamp_Object = MibScalar
sleNDAclControlTimeStamp = _SleNDAclControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 2, 4),
    _SleNDAclControlTimeStamp_Type()
)
sleNDAclControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclControlTimeStamp.setStatus("current")
_SleNDAclControlReqResult_Type = SleControlRequestResultType
_SleNDAclControlReqResult_Object = MibScalar
sleNDAclControlReqResult = _SleNDAclControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 2, 5),
    _SleNDAclControlReqResult_Type()
)
sleNDAclControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclControlReqResult.setStatus("current")
_SleNDAclControlIndex_Type = Integer32
_SleNDAclControlIndex_Object = MibScalar
sleNDAclControlIndex = _SleNDAclControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 2, 6),
    _SleNDAclControlIndex_Type()
)
sleNDAclControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclControlIndex.setStatus("current")


class _SleNDAclControlName_Type(OctetString):
    """Custom type sleNDAclControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleNDAclControlName_Type.__name__ = "OctetString"
_SleNDAclControlName_Object = MibScalar
sleNDAclControlName = _SleNDAclControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 2, 7),
    _SleNDAclControlName_Type()
)
sleNDAclControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclControlName.setStatus("current")
_SleNDAclNotifications_ObjectIdentity = ObjectIdentity
sleNDAclNotifications = _SleNDAclNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 3)
)
_SleNDACLRule_ObjectIdentity = ObjectIdentity
sleNDACLRule = _SleNDACLRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3)
)
_SleNDAclRuleTable_Object = MibTable
sleNDAclRuleTable = _SleNDAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1)
)
if mibBuilder.loadTexts:
    sleNDAclRuleTable.setStatus("current")
_SleNDAclRuleEntry_Object = MibTableRow
sleNDAclRuleEntry = _SleNDAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1)
)
sleNDAclRuleEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleNDAclIndex"),
    (0, "SLE-SECURITY-MIB", "sleNDAclRuleIndex"),
)
if mibBuilder.loadTexts:
    sleNDAclRuleEntry.setStatus("current")


class _SleNDAclRuleAclIndex_Type(Integer32):
    """Custom type sleNDAclRuleAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleNDAclRuleAclIndex_Type.__name__ = "Integer32"
_SleNDAclRuleAclIndex_Object = MibTableColumn
sleNDAclRuleAclIndex = _SleNDAclRuleAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 1),
    _SleNDAclRuleAclIndex_Type()
)
sleNDAclRuleAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleAclIndex.setStatus("current")


class _SleNDAclRuleIndex_Type(Integer32):
    """Custom type sleNDAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleNDAclRuleIndex_Type.__name__ = "Integer32"
_SleNDAclRuleIndex_Object = MibTableColumn
sleNDAclRuleIndex = _SleNDAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 2),
    _SleNDAclRuleIndex_Type()
)
sleNDAclRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleIndex.setStatus("current")


class _SleNDAclRuleAction_Type(Integer32):
    """Custom type sleNDAclRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SleNDAclRuleAction_Type.__name__ = "Integer32"
_SleNDAclRuleAction_Object = MibTableColumn
sleNDAclRuleAction = _SleNDAclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 3),
    _SleNDAclRuleAction_Type()
)
sleNDAclRuleAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleAction.setStatus("current")


class _SleNDAclRuleType_Type(Integer32):
    """Custom type sleNDAclRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("subnet", 1),
          ("range", 2),
          ("dhcpv6Snooping", 3))
    )


_SleNDAclRuleType_Type.__name__ = "Integer32"
_SleNDAclRuleType_Object = MibTableColumn
sleNDAclRuleType = _SleNDAclRuleType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 4),
    _SleNDAclRuleType_Type()
)
sleNDAclRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleType.setStatus("current")
_SleNDAclRuleRangeStartIPv6_Type = InetAddressIPv6
_SleNDAclRuleRangeStartIPv6_Object = MibTableColumn
sleNDAclRuleRangeStartIPv6 = _SleNDAclRuleRangeStartIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 5),
    _SleNDAclRuleRangeStartIPv6_Type()
)
sleNDAclRuleRangeStartIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleRangeStartIPv6.setStatus("current")
_SleNDAclRuleRangeEndIPv6_Type = InetAddressIPv6
_SleNDAclRuleRangeEndIPv6_Object = MibTableColumn
sleNDAclRuleRangeEndIPv6 = _SleNDAclRuleRangeEndIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 6),
    _SleNDAclRuleRangeEndIPv6_Type()
)
sleNDAclRuleRangeEndIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleRangeEndIPv6.setStatus("current")
_SleNDAclRuleIPv6Address_Type = InetAddressIPv6
_SleNDAclRuleIPv6Address_Object = MibTableColumn
sleNDAclRuleIPv6Address = _SleNDAclRuleIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 7),
    _SleNDAclRuleIPv6Address_Type()
)
sleNDAclRuleIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleIPv6Address.setStatus("current")


class _SleNDAclRuleIPv6Mask_Type(Integer32):
    """Custom type sleNDAclRuleIPv6Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SleNDAclRuleIPv6Mask_Type.__name__ = "Integer32"
_SleNDAclRuleIPv6Mask_Object = MibTableColumn
sleNDAclRuleIPv6Mask = _SleNDAclRuleIPv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 8),
    _SleNDAclRuleIPv6Mask_Type()
)
sleNDAclRuleIPv6Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleIPv6Mask.setStatus("current")
_SleNDAclRuleMacAddr_Type = MacAddress
_SleNDAclRuleMacAddr_Object = MibTableColumn
sleNDAclRuleMacAddr = _SleNDAclRuleMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 9),
    _SleNDAclRuleMacAddr_Type()
)
sleNDAclRuleMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleMacAddr.setStatus("current")


class _SleNDAclRuleMacType_Type(Integer32):
    """Custom type sleNDAclRuleMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("host", 1),
          ("pattern", 2))
    )


_SleNDAclRuleMacType_Type.__name__ = "Integer32"
_SleNDAclRuleMacType_Object = MibTableColumn
sleNDAclRuleMacType = _SleNDAclRuleMacType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 1, 1, 10),
    _SleNDAclRuleMacType_Type()
)
sleNDAclRuleMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleMacType.setStatus("current")
_SleNDAclRuleControl_ObjectIdentity = ObjectIdentity
sleNDAclRuleControl = _SleNDAclRuleControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2)
)


class _SleNDAclRuleControlRequest_Type(Integer32):
    """Custom type sleNDAclRuleControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createNDAclRule", 1),
          ("destroyNDAclRule", 2))
    )


_SleNDAclRuleControlRequest_Type.__name__ = "Integer32"
_SleNDAclRuleControlRequest_Object = MibScalar
sleNDAclRuleControlRequest = _SleNDAclRuleControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 1),
    _SleNDAclRuleControlRequest_Type()
)
sleNDAclRuleControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlRequest.setStatus("current")
_SleNDAclRuleControlStatus_Type = SleControlStatusType
_SleNDAclRuleControlStatus_Object = MibScalar
sleNDAclRuleControlStatus = _SleNDAclRuleControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 2),
    _SleNDAclRuleControlStatus_Type()
)
sleNDAclRuleControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleControlStatus.setStatus("current")
_SleNDAclRuleControlTimer_Type = Gauge32
_SleNDAclRuleControlTimer_Object = MibScalar
sleNDAclRuleControlTimer = _SleNDAclRuleControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 3),
    _SleNDAclRuleControlTimer_Type()
)
sleNDAclRuleControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlTimer.setStatus("current")
_SleNDAclRuleControlTimeStamp_Type = TimeTicks
_SleNDAclRuleControlTimeStamp_Object = MibScalar
sleNDAclRuleControlTimeStamp = _SleNDAclRuleControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 4),
    _SleNDAclRuleControlTimeStamp_Type()
)
sleNDAclRuleControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleControlTimeStamp.setStatus("current")
_SleNDAclRuleControlReqResult_Type = SleControlRequestResultType
_SleNDAclRuleControlReqResult_Object = MibScalar
sleNDAclRuleControlReqResult = _SleNDAclRuleControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 5),
    _SleNDAclRuleControlReqResult_Type()
)
sleNDAclRuleControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDAclRuleControlReqResult.setStatus("current")
_SleNDAclRuleControlAclIndex_Type = Integer32
_SleNDAclRuleControlAclIndex_Object = MibScalar
sleNDAclRuleControlAclIndex = _SleNDAclRuleControlAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 6),
    _SleNDAclRuleControlAclIndex_Type()
)
sleNDAclRuleControlAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlAclIndex.setStatus("current")
_SleNDAclRuleControlIndex_Type = Integer32
_SleNDAclRuleControlIndex_Object = MibScalar
sleNDAclRuleControlIndex = _SleNDAclRuleControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 7),
    _SleNDAclRuleControlIndex_Type()
)
sleNDAclRuleControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlIndex.setStatus("current")


class _SleNDAclRuleControlAction_Type(Integer32):
    """Custom type sleNDAclRuleControlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SleNDAclRuleControlAction_Type.__name__ = "Integer32"
_SleNDAclRuleControlAction_Object = MibScalar
sleNDAclRuleControlAction = _SleNDAclRuleControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 8),
    _SleNDAclRuleControlAction_Type()
)
sleNDAclRuleControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlAction.setStatus("current")


class _SleNDAclRuleControlType_Type(Integer32):
    """Custom type sleNDAclRuleControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("subnet", 1),
          ("range", 2),
          ("dhcpSnooping", 3))
    )


_SleNDAclRuleControlType_Type.__name__ = "Integer32"
_SleNDAclRuleControlType_Object = MibScalar
sleNDAclRuleControlType = _SleNDAclRuleControlType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 9),
    _SleNDAclRuleControlType_Type()
)
sleNDAclRuleControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlType.setStatus("current")
_SleNDAclRuleControlRangeStartIPv6_Type = InetAddressIPv6
_SleNDAclRuleControlRangeStartIPv6_Object = MibScalar
sleNDAclRuleControlRangeStartIPv6 = _SleNDAclRuleControlRangeStartIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 10),
    _SleNDAclRuleControlRangeStartIPv6_Type()
)
sleNDAclRuleControlRangeStartIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlRangeStartIPv6.setStatus("current")
_SleNDAclRuleControlRangeEndIPv6_Type = InetAddressIPv6
_SleNDAclRuleControlRangeEndIPv6_Object = MibScalar
sleNDAclRuleControlRangeEndIPv6 = _SleNDAclRuleControlRangeEndIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 11),
    _SleNDAclRuleControlRangeEndIPv6_Type()
)
sleNDAclRuleControlRangeEndIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlRangeEndIPv6.setStatus("current")
_SleNDAclRuleControlIPv6Address_Type = InetAddressIPv6
_SleNDAclRuleControlIPv6Address_Object = MibScalar
sleNDAclRuleControlIPv6Address = _SleNDAclRuleControlIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 12),
    _SleNDAclRuleControlIPv6Address_Type()
)
sleNDAclRuleControlIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlIPv6Address.setStatus("current")


class _SleNDAclRuleControlIPv6Mask_Type(Integer32):
    """Custom type sleNDAclRuleControlIPv6Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SleNDAclRuleControlIPv6Mask_Type.__name__ = "Integer32"
_SleNDAclRuleControlIPv6Mask_Object = MibScalar
sleNDAclRuleControlIPv6Mask = _SleNDAclRuleControlIPv6Mask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 13),
    _SleNDAclRuleControlIPv6Mask_Type()
)
sleNDAclRuleControlIPv6Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlIPv6Mask.setStatus("current")
_SleNDAclRuleControlMacAddr_Type = MacAddress
_SleNDAclRuleControlMacAddr_Object = MibScalar
sleNDAclRuleControlMacAddr = _SleNDAclRuleControlMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 14),
    _SleNDAclRuleControlMacAddr_Type()
)
sleNDAclRuleControlMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlMacAddr.setStatus("current")


class _SleNDAclRuleControlMacType_Type(Integer32):
    """Custom type sleNDAclRuleControlMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("host", 1),
          ("pattern", 2))
    )


_SleNDAclRuleControlMacType_Type.__name__ = "Integer32"
_SleNDAclRuleControlMacType_Object = MibScalar
sleNDAclRuleControlMacType = _SleNDAclRuleControlMacType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 2, 15),
    _SleNDAclRuleControlMacType_Type()
)
sleNDAclRuleControlMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDAclRuleControlMacType.setStatus("current")
_SleNDAclRuleNotifications_ObjectIdentity = ObjectIdentity
sleNDAclRuleNotifications = _SleNDAclRuleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 3)
)
_SleNDInspectVlan_ObjectIdentity = ObjectIdentity
sleNDInspectVlan = _SleNDInspectVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4)
)
_SleNDInspectVlanTable_Object = MibTable
sleNDInspectVlanTable = _SleNDInspectVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1)
)
if mibBuilder.loadTexts:
    sleNDInspectVlanTable.setStatus("current")
_SleNDInspectVlanEntry_Object = MibTableRow
sleNDInspectVlanEntry = _SleNDInspectVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1)
)
sleNDInspectVlanEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleNDInspectVlanIndex"),
)
if mibBuilder.loadTexts:
    sleNDInspectVlanEntry.setStatus("current")


class _SleNDInspectVlanIndex_Type(Integer32):
    """Custom type sleNDInspectVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleNDInspectVlanIndex_Type.__name__ = "Integer32"
_SleNDInspectVlanIndex_Object = MibTableColumn
sleNDInspectVlanIndex = _SleNDInspectVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 1),
    _SleNDInspectVlanIndex_Type()
)
sleNDInspectVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanIndex.setStatus("current")


class _SleNDInspectVlanEnable_Type(Integer32):
    """Custom type sleNDInspectVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNDInspectVlanEnable_Type.__name__ = "Integer32"
_SleNDInspectVlanEnable_Object = MibTableColumn
sleNDInspectVlanEnable = _SleNDInspectVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 2),
    _SleNDInspectVlanEnable_Type()
)
sleNDInspectVlanEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanEnable.setStatus("current")
_SleNDInspectVlanFilterAclIndex_Type = Integer32
_SleNDInspectVlanFilterAclIndex_Object = MibTableColumn
sleNDInspectVlanFilterAclIndex = _SleNDInspectVlanFilterAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 3),
    _SleNDInspectVlanFilterAclIndex_Type()
)
sleNDInspectVlanFilterAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanFilterAclIndex.setStatus("current")
_SleNDInspectVlanFwdPktCnt_Type = Integer32
_SleNDInspectVlanFwdPktCnt_Object = MibTableColumn
sleNDInspectVlanFwdPktCnt = _SleNDInspectVlanFwdPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 4),
    _SleNDInspectVlanFwdPktCnt_Type()
)
sleNDInspectVlanFwdPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanFwdPktCnt.setStatus("current")
_SleNDInspectVlanDropPktCnt_Type = Integer32
_SleNDInspectVlanDropPktCnt_Object = MibTableColumn
sleNDInspectVlanDropPktCnt = _SleNDInspectVlanDropPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 5),
    _SleNDInspectVlanDropPktCnt_Type()
)
sleNDInspectVlanDropPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanDropPktCnt.setStatus("current")
_SleNDInspectVlanAclPermits_Type = Integer32
_SleNDInspectVlanAclPermits_Object = MibTableColumn
sleNDInspectVlanAclPermits = _SleNDInspectVlanAclPermits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 6),
    _SleNDInspectVlanAclPermits_Type()
)
sleNDInspectVlanAclPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanAclPermits.setStatus("current")
_SleNDInspectVlanAclDrops_Type = Integer32
_SleNDInspectVlanAclDrops_Object = MibTableColumn
sleNDInspectVlanAclDrops = _SleNDInspectVlanAclDrops_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 7),
    _SleNDInspectVlanAclDrops_Type()
)
sleNDInspectVlanAclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanAclDrops.setStatus("current")
_SleNDInspectVlanDhcpv6Permits_Type = Integer32
_SleNDInspectVlanDhcpv6Permits_Object = MibTableColumn
sleNDInspectVlanDhcpv6Permits = _SleNDInspectVlanDhcpv6Permits_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 8),
    _SleNDInspectVlanDhcpv6Permits_Type()
)
sleNDInspectVlanDhcpv6Permits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanDhcpv6Permits.setStatus("current")
_SleNDInspectVlanDhcpv6Denys_Type = Integer32
_SleNDInspectVlanDhcpv6Denys_Object = MibTableColumn
sleNDInspectVlanDhcpv6Denys = _SleNDInspectVlanDhcpv6Denys_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 9),
    _SleNDInspectVlanDhcpv6Denys_Type()
)
sleNDInspectVlanDhcpv6Denys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanDhcpv6Denys.setStatus("current")
_SleNDInspectVlanLocalIpv6Denys_Type = Integer32
_SleNDInspectVlanLocalIpv6Denys_Object = MibTableColumn
sleNDInspectVlanLocalIpv6Denys = _SleNDInspectVlanLocalIpv6Denys_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 10),
    _SleNDInspectVlanLocalIpv6Denys_Type()
)
sleNDInspectVlanLocalIpv6Denys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanLocalIpv6Denys.setStatus("current")


class _SleNDInspectVlanFilterAclName_Type(OctetString):
    """Custom type sleNDInspectVlanFilterAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleNDInspectVlanFilterAclName_Type.__name__ = "OctetString"
_SleNDInspectVlanFilterAclName_Object = MibTableColumn
sleNDInspectVlanFilterAclName = _SleNDInspectVlanFilterAclName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 1, 1, 11),
    _SleNDInspectVlanFilterAclName_Type()
)
sleNDInspectVlanFilterAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanFilterAclName.setStatus("current")
_SleNDInspectVlanControl_ObjectIdentity = ObjectIdentity
sleNDInspectVlanControl = _SleNDInspectVlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2)
)


class _SleNDInspectVlanControlRequest_Type(Integer32):
    """Custom type sleNDInspectVlanControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setNDInspectVlanProfile", 1),
          ("clearNDInspectVlanStatistics", 2))
    )


_SleNDInspectVlanControlRequest_Type.__name__ = "Integer32"
_SleNDInspectVlanControlRequest_Object = MibScalar
sleNDInspectVlanControlRequest = _SleNDInspectVlanControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2, 1),
    _SleNDInspectVlanControlRequest_Type()
)
sleNDInspectVlanControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectVlanControlRequest.setStatus("current")
_SleNDInspectVlanControlStatus_Type = SleControlStatusType
_SleNDInspectVlanControlStatus_Object = MibScalar
sleNDInspectVlanControlStatus = _SleNDInspectVlanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2, 2),
    _SleNDInspectVlanControlStatus_Type()
)
sleNDInspectVlanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanControlStatus.setStatus("current")
_SleNDInspectVlanControlTimer_Type = Gauge32
_SleNDInspectVlanControlTimer_Object = MibScalar
sleNDInspectVlanControlTimer = _SleNDInspectVlanControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2, 3),
    _SleNDInspectVlanControlTimer_Type()
)
sleNDInspectVlanControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectVlanControlTimer.setStatus("current")
_SleNDInspectVlanControlTimeStamp_Type = TimeTicks
_SleNDInspectVlanControlTimeStamp_Object = MibScalar
sleNDInspectVlanControlTimeStamp = _SleNDInspectVlanControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2, 4),
    _SleNDInspectVlanControlTimeStamp_Type()
)
sleNDInspectVlanControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanControlTimeStamp.setStatus("current")
_SleNDInspectVlanControlReqResult_Type = SleControlRequestResultType
_SleNDInspectVlanControlReqResult_Object = MibScalar
sleNDInspectVlanControlReqResult = _SleNDInspectVlanControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2, 5),
    _SleNDInspectVlanControlReqResult_Type()
)
sleNDInspectVlanControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectVlanControlReqResult.setStatus("current")


class _SleNDInspectVlanControlIndex_Type(Integer32):
    """Custom type sleNDInspectVlanControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleNDInspectVlanControlIndex_Type.__name__ = "Integer32"
_SleNDInspectVlanControlIndex_Object = MibScalar
sleNDInspectVlanControlIndex = _SleNDInspectVlanControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2, 6),
    _SleNDInspectVlanControlIndex_Type()
)
sleNDInspectVlanControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectVlanControlIndex.setStatus("current")


class _SleNDInspectVlanControlEnable_Type(Integer32):
    """Custom type sleNDInspectVlanControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleNDInspectVlanControlEnable_Type.__name__ = "Integer32"
_SleNDInspectVlanControlEnable_Object = MibScalar
sleNDInspectVlanControlEnable = _SleNDInspectVlanControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2, 7),
    _SleNDInspectVlanControlEnable_Type()
)
sleNDInspectVlanControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectVlanControlEnable.setStatus("current")
_SleNDInspectVlanControlFilterAclIndex_Type = Integer32
_SleNDInspectVlanControlFilterAclIndex_Object = MibScalar
sleNDInspectVlanControlFilterAclIndex = _SleNDInspectVlanControlFilterAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 2, 8),
    _SleNDInspectVlanControlFilterAclIndex_Type()
)
sleNDInspectVlanControlFilterAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectVlanControlFilterAclIndex.setStatus("current")
_SleNDInspectVlanNotifications_ObjectIdentity = ObjectIdentity
sleNDInspectVlanNotifications = _SleNDInspectVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 3)
)
_SleNDInspectPort_ObjectIdentity = ObjectIdentity
sleNDInspectPort = _SleNDInspectPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5)
)
_SleNDInspectPortTable_Object = MibTable
sleNDInspectPortTable = _SleNDInspectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 1)
)
if mibBuilder.loadTexts:
    sleNDInspectPortTable.setStatus("current")
_SleNDInspectPortEntry_Object = MibTableRow
sleNDInspectPortEntry = _SleNDInspectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 1, 1)
)
sleNDInspectPortEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleNDInspectPortIndex"),
)
if mibBuilder.loadTexts:
    sleNDInspectPortEntry.setStatus("current")


class _SleNDInspectPortIndex_Type(Integer32):
    """Custom type sleNDInspectPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleNDInspectPortIndex_Type.__name__ = "Integer32"
_SleNDInspectPortIndex_Object = MibTableColumn
sleNDInspectPortIndex = _SleNDInspectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 1, 1, 1),
    _SleNDInspectPortIndex_Type()
)
sleNDInspectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectPortIndex.setStatus("current")


class _SleNDInspectPortTrust_Type(Integer32):
    """Custom type sleNDInspectPortTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrust", 0),
          ("trust", 1))
    )


_SleNDInspectPortTrust_Type.__name__ = "Integer32"
_SleNDInspectPortTrust_Object = MibTableColumn
sleNDInspectPortTrust = _SleNDInspectPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 1, 1, 2),
    _SleNDInspectPortTrust_Type()
)
sleNDInspectPortTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectPortTrust.setStatus("current")
_SleNDInspectPortControl_ObjectIdentity = ObjectIdentity
sleNDInspectPortControl = _SleNDInspectPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 2)
)


class _SleNDInspectPortControlRequest_Type(Integer32):
    """Custom type sleNDInspectPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setNDInspectTrustPort", 1)
    )


_SleNDInspectPortControlRequest_Type.__name__ = "Integer32"
_SleNDInspectPortControlRequest_Object = MibScalar
sleNDInspectPortControlRequest = _SleNDInspectPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 2, 1),
    _SleNDInspectPortControlRequest_Type()
)
sleNDInspectPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectPortControlRequest.setStatus("current")
_SleNDInspectPortControlStatus_Type = SleControlStatusType
_SleNDInspectPortControlStatus_Object = MibScalar
sleNDInspectPortControlStatus = _SleNDInspectPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 2, 2),
    _SleNDInspectPortControlStatus_Type()
)
sleNDInspectPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectPortControlStatus.setStatus("current")
_SleNDInspectPortControlTimer_Type = Gauge32
_SleNDInspectPortControlTimer_Object = MibScalar
sleNDInspectPortControlTimer = _SleNDInspectPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 2, 3),
    _SleNDInspectPortControlTimer_Type()
)
sleNDInspectPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectPortControlTimer.setStatus("current")
_SleNDInspectPortControlTimeStamp_Type = TimeTicks
_SleNDInspectPortControlTimeStamp_Object = MibScalar
sleNDInspectPortControlTimeStamp = _SleNDInspectPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 2, 4),
    _SleNDInspectPortControlTimeStamp_Type()
)
sleNDInspectPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectPortControlTimeStamp.setStatus("current")
_SleNDInspectPortControlReqResult_Type = SleControlRequestResultType
_SleNDInspectPortControlReqResult_Object = MibScalar
sleNDInspectPortControlReqResult = _SleNDInspectPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 2, 5),
    _SleNDInspectPortControlReqResult_Type()
)
sleNDInspectPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectPortControlReqResult.setStatus("current")


class _SleNDInspectPortControlIndex_Type(Integer32):
    """Custom type sleNDInspectPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleNDInspectPortControlIndex_Type.__name__ = "Integer32"
_SleNDInspectPortControlIndex_Object = MibScalar
sleNDInspectPortControlIndex = _SleNDInspectPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 2, 6),
    _SleNDInspectPortControlIndex_Type()
)
sleNDInspectPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectPortControlIndex.setStatus("current")


class _SleNDInspectPortControlTrust_Type(Integer32):
    """Custom type sleNDInspectPortControlTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrust", 0),
          ("trust", 1))
    )


_SleNDInspectPortControlTrust_Type.__name__ = "Integer32"
_SleNDInspectPortControlTrust_Object = MibScalar
sleNDInspectPortControlTrust = _SleNDInspectPortControlTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 2, 7),
    _SleNDInspectPortControlTrust_Type()
)
sleNDInspectPortControlTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleNDInspectPortControlTrust.setStatus("current")
_SleNDInspectPortNotifications_ObjectIdentity = ObjectIdentity
sleNDInspectPortNotifications = _SleNDInspectPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 3)
)
_SleNDInspectInvalidLog_ObjectIdentity = ObjectIdentity
sleNDInspectInvalidLog = _SleNDInspectInvalidLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6)
)
_SleNDInspectInvalidLogTable_Object = MibTable
sleNDInspectInvalidLogTable = _SleNDInspectInvalidLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1)
)
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogTable.setStatus("current")
_SleNDInspectInvalidLogEntry_Object = MibTableRow
sleNDInspectInvalidLogEntry = _SleNDInspectInvalidLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1)
)
sleNDInspectInvalidLogEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleArpInspectInvalidLogId"),
)
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogEntry.setStatus("current")


class _SleNDInspectInvalidLogId_Type(Integer32):
    """Custom type sleNDInspectInvalidLogId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleNDInspectInvalidLogId_Type.__name__ = "Integer32"
_SleNDInspectInvalidLogId_Object = MibTableColumn
sleNDInspectInvalidLogId = _SleNDInspectInvalidLogId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 1),
    _SleNDInspectInvalidLogId_Type()
)
sleNDInspectInvalidLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogId.setStatus("current")


class _SleNDInspectInvalidLogReason_Type(Integer32):
    """Custom type sleNDInspectInvalidLogReason based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("aliReasonNone", 0),
          ("aliiReasonDhcpv6Permit", 1),
          ("aliReasonDhcpv6Deny", 2),
          ("aliReasonAclPermit", 3),
          ("aliReasonAclDeny", 4),
          ("aliReasonLocalIpv6Deny", 5),
          ("aliReasonRAguardPermit", 6),
          ("aliReasonRAguardDeny", 7))
    )


_SleNDInspectInvalidLogReason_Type.__name__ = "Integer32"
_SleNDInspectInvalidLogReason_Object = MibTableColumn
sleNDInspectInvalidLogReason = _SleNDInspectInvalidLogReason_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 2),
    _SleNDInspectInvalidLogReason_Type()
)
sleNDInspectInvalidLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogReason.setStatus("current")
_SleNDInspectInvalidLogSamePktCnt_Type = Counter32
_SleNDInspectInvalidLogSamePktCnt_Object = MibTableColumn
sleNDInspectInvalidLogSamePktCnt = _SleNDInspectInvalidLogSamePktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 3),
    _SleNDInspectInvalidLogSamePktCnt_Type()
)
sleNDInspectInvalidLogSamePktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogSamePktCnt.setStatus("current")
_SleNDInspectInvalidLogPortNumber_Type = Integer32
_SleNDInspectInvalidLogPortNumber_Object = MibTableColumn
sleNDInspectInvalidLogPortNumber = _SleNDInspectInvalidLogPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 4),
    _SleNDInspectInvalidLogPortNumber_Type()
)
sleNDInspectInvalidLogPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogPortNumber.setStatus("current")
_SleNDInspectInvalidLogVlanId_Type = Integer32
_SleNDInspectInvalidLogVlanId_Object = MibTableColumn
sleNDInspectInvalidLogVlanId = _SleNDInspectInvalidLogVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 5),
    _SleNDInspectInvalidLogVlanId_Type()
)
sleNDInspectInvalidLogVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogVlanId.setStatus("current")


class _SleNDInspectInvalidLogSenderMacAddr_Type(OctetString):
    """Custom type sleNDInspectInvalidLogSenderMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SleNDInspectInvalidLogSenderMacAddr_Type.__name__ = "OctetString"
_SleNDInspectInvalidLogSenderMacAddr_Object = MibTableColumn
sleNDInspectInvalidLogSenderMacAddr = _SleNDInspectInvalidLogSenderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 6),
    _SleNDInspectInvalidLogSenderMacAddr_Type()
)
sleNDInspectInvalidLogSenderMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogSenderMacAddr.setStatus("current")


class _SleNDInspectInvalidLogSrcMacAddr_Type(OctetString):
    """Custom type sleNDInspectInvalidLogSrcMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SleNDInspectInvalidLogSrcMacAddr_Type.__name__ = "OctetString"
_SleNDInspectInvalidLogSrcMacAddr_Object = MibTableColumn
sleNDInspectInvalidLogSrcMacAddr = _SleNDInspectInvalidLogSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 7),
    _SleNDInspectInvalidLogSrcMacAddr_Type()
)
sleNDInspectInvalidLogSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogSrcMacAddr.setStatus("current")
_SleNDInspectInvalidLogSenderIpv6Addr_Type = InetAddressIPv6
_SleNDInspectInvalidLogSenderIpv6Addr_Object = MibTableColumn
sleNDInspectInvalidLogSenderIpv6Addr = _SleNDInspectInvalidLogSenderIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 8),
    _SleNDInspectInvalidLogSenderIpv6Addr_Type()
)
sleNDInspectInvalidLogSenderIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogSenderIpv6Addr.setStatus("current")
_SleNDInspectInvalidLogDstIpv6Addr_Type = InetAddressIPv6
_SleNDInspectInvalidLogDstIpv6Addr_Object = MibTableColumn
sleNDInspectInvalidLogDstIpv6Addr = _SleNDInspectInvalidLogDstIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 9),
    _SleNDInspectInvalidLogDstIpv6Addr_Type()
)
sleNDInspectInvalidLogDstIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogDstIpv6Addr.setStatus("current")
_SleNDInspectInvalidLogLastRecvTime_Type = OctetString
_SleNDInspectInvalidLogLastRecvTime_Object = MibTableColumn
sleNDInspectInvalidLogLastRecvTime = _SleNDInspectInvalidLogLastRecvTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 10),
    _SleNDInspectInvalidLogLastRecvTime_Type()
)
sleNDInspectInvalidLogLastRecvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogLastRecvTime.setStatus("current")


class _SleNDInspectInvalidLogNDType_Type(Integer32):
    """Custom type sleNDInspectInvalidLogNDType based on Integer32"""
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
        *(("ndiscRouterSolicitation", 1),
          ("ndiscRouteradvertisemetn", 2),
          ("ndiscNeighbourSolicitation", 3),
          ("ndiscNeighbourAdvertisement", 4))
    )


_SleNDInspectInvalidLogNDType_Type.__name__ = "Integer32"
_SleNDInspectInvalidLogNDType_Object = MibTableColumn
sleNDInspectInvalidLogNDType = _SleNDInspectInvalidLogNDType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 6, 1, 1, 11),
    _SleNDInspectInvalidLogNDType_Type()
)
sleNDInspectInvalidLogNDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNDInspectInvalidLogNDType.setStatus("current")
_SleRAGuard_ObjectIdentity = ObjectIdentity
sleRAGuard = _SleRAGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13)
)
_SleRAGuardPolicy_ObjectIdentity = ObjectIdentity
sleRAGuardPolicy = _SleRAGuardPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1)
)
_SleRAGuardPolicyTable_Object = MibTable
sleRAGuardPolicyTable = _SleRAGuardPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1)
)
if mibBuilder.loadTexts:
    sleRAGuardPolicyTable.setStatus("current")
_SleRAGuardPolicyEntry_Object = MibTableRow
sleRAGuardPolicyEntry = _SleRAGuardPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1)
)
sleRAGuardPolicyEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleRAGuardPolicyIndex"),
)
if mibBuilder.loadTexts:
    sleRAGuardPolicyEntry.setStatus("current")


class _SleRAGuardPolicyIndex_Type(Integer32):
    """Custom type sleRAGuardPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SleRAGuardPolicyIndex_Type.__name__ = "Integer32"
_SleRAGuardPolicyIndex_Object = MibTableColumn
sleRAGuardPolicyIndex = _SleRAGuardPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 1),
    _SleRAGuardPolicyIndex_Type()
)
sleRAGuardPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyIndex.setStatus("current")


class _SleRAGuardPolicyName_Type(OctetString):
    """Custom type sleRAGuardPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleRAGuardPolicyName_Type.__name__ = "OctetString"
_SleRAGuardPolicyName_Object = MibTableColumn
sleRAGuardPolicyName = _SleRAGuardPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 2),
    _SleRAGuardPolicyName_Type()
)
sleRAGuardPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyName.setStatus("current")


class _SleRAGuardPolicyHoplimitMin_Type(Integer32):
    """Custom type sleRAGuardPolicyHoplimitMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleRAGuardPolicyHoplimitMin_Type.__name__ = "Integer32"
_SleRAGuardPolicyHoplimitMin_Object = MibTableColumn
sleRAGuardPolicyHoplimitMin = _SleRAGuardPolicyHoplimitMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 3),
    _SleRAGuardPolicyHoplimitMin_Type()
)
sleRAGuardPolicyHoplimitMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyHoplimitMin.setStatus("current")


class _SleRAGuardPolicyHoplimitMax_Type(Integer32):
    """Custom type sleRAGuardPolicyHoplimitMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleRAGuardPolicyHoplimitMax_Type.__name__ = "Integer32"
_SleRAGuardPolicyHoplimitMax_Object = MibTableColumn
sleRAGuardPolicyHoplimitMax = _SleRAGuardPolicyHoplimitMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 4),
    _SleRAGuardPolicyHoplimitMax_Type()
)
sleRAGuardPolicyHoplimitMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyHoplimitMax.setStatus("current")


class _SleRAGuardPolicyManagedFlag_Type(Integer32):
    """Custom type sleRAGuardPolicyManagedFlag based on Integer32"""
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


_SleRAGuardPolicyManagedFlag_Type.__name__ = "Integer32"
_SleRAGuardPolicyManagedFlag_Object = MibTableColumn
sleRAGuardPolicyManagedFlag = _SleRAGuardPolicyManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 5),
    _SleRAGuardPolicyManagedFlag_Type()
)
sleRAGuardPolicyManagedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyManagedFlag.setStatus("current")


class _SleRAGuardPolicyOtherFlag_Type(Integer32):
    """Custom type sleRAGuardPolicyOtherFlag based on Integer32"""
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


_SleRAGuardPolicyOtherFlag_Type.__name__ = "Integer32"
_SleRAGuardPolicyOtherFlag_Object = MibTableColumn
sleRAGuardPolicyOtherFlag = _SleRAGuardPolicyOtherFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 6),
    _SleRAGuardPolicyOtherFlag_Type()
)
sleRAGuardPolicyOtherFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyOtherFlag.setStatus("current")


class _SleRAGuardPolicyRouterPreference_Type(Integer32):
    """Custom type sleRAGuardPolicyRouterPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("medium", 0),
          ("high", 1),
          ("low", 3))
    )


_SleRAGuardPolicyRouterPreference_Type.__name__ = "Integer32"
_SleRAGuardPolicyRouterPreference_Object = MibTableColumn
sleRAGuardPolicyRouterPreference = _SleRAGuardPolicyRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 7),
    _SleRAGuardPolicyRouterPreference_Type()
)
sleRAGuardPolicyRouterPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyRouterPreference.setStatus("current")


class _SleRAGuardPolicyMatchACLName_Type(OctetString):
    """Custom type sleRAGuardPolicyMatchACLName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleRAGuardPolicyMatchACLName_Type.__name__ = "OctetString"
_SleRAGuardPolicyMatchACLName_Object = MibTableColumn
sleRAGuardPolicyMatchACLName = _SleRAGuardPolicyMatchACLName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 8),
    _SleRAGuardPolicyMatchACLName_Type()
)
sleRAGuardPolicyMatchACLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyMatchACLName.setStatus("current")


class _SleRAGuardPolicyMatchPrefixName_Type(OctetString):
    """Custom type sleRAGuardPolicyMatchPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleRAGuardPolicyMatchPrefixName_Type.__name__ = "OctetString"
_SleRAGuardPolicyMatchPrefixName_Object = MibTableColumn
sleRAGuardPolicyMatchPrefixName = _SleRAGuardPolicyMatchPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 1, 1, 9),
    _SleRAGuardPolicyMatchPrefixName_Type()
)
sleRAGuardPolicyMatchPrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyMatchPrefixName.setStatus("current")
_SleRAGuardPolicyControl_ObjectIdentity = ObjectIdentity
sleRAGuardPolicyControl = _SleRAGuardPolicyControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2)
)


class _SleRAGuardPolicyControlRequest_Type(Integer32):
    """Custom type sleRAGuardPolicyControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createRAGuardPolicy", 1),
          ("destroyRAGuardPolicy", 2),
          ("changeRAGuardPolicy", 3))
    )


_SleRAGuardPolicyControlRequest_Type.__name__ = "Integer32"
_SleRAGuardPolicyControlRequest_Object = MibScalar
sleRAGuardPolicyControlRequest = _SleRAGuardPolicyControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 1),
    _SleRAGuardPolicyControlRequest_Type()
)
sleRAGuardPolicyControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlRequest.setStatus("current")
_SleRAGuardPolicyControlStatus_Type = SleControlStatusType
_SleRAGuardPolicyControlStatus_Object = MibScalar
sleRAGuardPolicyControlStatus = _SleRAGuardPolicyControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 2),
    _SleRAGuardPolicyControlStatus_Type()
)
sleRAGuardPolicyControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlStatus.setStatus("current")
_SleRAGuardPolicyControlTimer_Type = Gauge32
_SleRAGuardPolicyControlTimer_Object = MibScalar
sleRAGuardPolicyControlTimer = _SleRAGuardPolicyControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 3),
    _SleRAGuardPolicyControlTimer_Type()
)
sleRAGuardPolicyControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlTimer.setStatus("current")
_SleRAGuardPolicyControlTimeStamp_Type = TimeTicks
_SleRAGuardPolicyControlTimeStamp_Object = MibScalar
sleRAGuardPolicyControlTimeStamp = _SleRAGuardPolicyControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 4),
    _SleRAGuardPolicyControlTimeStamp_Type()
)
sleRAGuardPolicyControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlTimeStamp.setStatus("current")
_SleRAGuardPolicyControlReqResult_Type = SleControlRequestResultType
_SleRAGuardPolicyControlReqResult_Object = MibScalar
sleRAGuardPolicyControlReqResult = _SleRAGuardPolicyControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 5),
    _SleRAGuardPolicyControlReqResult_Type()
)
sleRAGuardPolicyControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlReqResult.setStatus("current")
_SleRAGuardPolicyControlIndex_Type = Integer32
_SleRAGuardPolicyControlIndex_Object = MibScalar
sleRAGuardPolicyControlIndex = _SleRAGuardPolicyControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 6),
    _SleRAGuardPolicyControlIndex_Type()
)
sleRAGuardPolicyControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlIndex.setStatus("current")


class _SleRAGuardPolicyControlName_Type(OctetString):
    """Custom type sleRAGuardPolicyControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleRAGuardPolicyControlName_Type.__name__ = "OctetString"
_SleRAGuardPolicyControlName_Object = MibScalar
sleRAGuardPolicyControlName = _SleRAGuardPolicyControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 7),
    _SleRAGuardPolicyControlName_Type()
)
sleRAGuardPolicyControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlName.setStatus("current")


class _SleRAGuardPolicyControlHoplimitMin_Type(Integer32):
    """Custom type sleRAGuardPolicyControlHoplimitMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleRAGuardPolicyControlHoplimitMin_Type.__name__ = "Integer32"
_SleRAGuardPolicyControlHoplimitMin_Object = MibScalar
sleRAGuardPolicyControlHoplimitMin = _SleRAGuardPolicyControlHoplimitMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 8),
    _SleRAGuardPolicyControlHoplimitMin_Type()
)
sleRAGuardPolicyControlHoplimitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlHoplimitMin.setStatus("current")


class _SleRAGuardPolicyControlHoplimitMax_Type(Integer32):
    """Custom type sleRAGuardPolicyControlHoplimitMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleRAGuardPolicyControlHoplimitMax_Type.__name__ = "Integer32"
_SleRAGuardPolicyControlHoplimitMax_Object = MibScalar
sleRAGuardPolicyControlHoplimitMax = _SleRAGuardPolicyControlHoplimitMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 9),
    _SleRAGuardPolicyControlHoplimitMax_Type()
)
sleRAGuardPolicyControlHoplimitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlHoplimitMax.setStatus("current")


class _SleRAGuardPolicyControlManagedFlag_Type(Integer32):
    """Custom type sleRAGuardPolicyControlManagedFlag based on Integer32"""
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


_SleRAGuardPolicyControlManagedFlag_Type.__name__ = "Integer32"
_SleRAGuardPolicyControlManagedFlag_Object = MibScalar
sleRAGuardPolicyControlManagedFlag = _SleRAGuardPolicyControlManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 10),
    _SleRAGuardPolicyControlManagedFlag_Type()
)
sleRAGuardPolicyControlManagedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlManagedFlag.setStatus("current")


class _SleRAGuardPolicyControlOtherFlag_Type(Integer32):
    """Custom type sleRAGuardPolicyControlOtherFlag based on Integer32"""
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


_SleRAGuardPolicyControlOtherFlag_Type.__name__ = "Integer32"
_SleRAGuardPolicyControlOtherFlag_Object = MibScalar
sleRAGuardPolicyControlOtherFlag = _SleRAGuardPolicyControlOtherFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 11),
    _SleRAGuardPolicyControlOtherFlag_Type()
)
sleRAGuardPolicyControlOtherFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlOtherFlag.setStatus("current")


class _SleRAGuardPolicyControlRouterPreference_Type(Integer32):
    """Custom type sleRAGuardPolicyControlRouterPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("medium", 0),
          ("high", 1),
          ("low", 3))
    )


_SleRAGuardPolicyControlRouterPreference_Type.__name__ = "Integer32"
_SleRAGuardPolicyControlRouterPreference_Object = MibScalar
sleRAGuardPolicyControlRouterPreference = _SleRAGuardPolicyControlRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 12),
    _SleRAGuardPolicyControlRouterPreference_Type()
)
sleRAGuardPolicyControlRouterPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlRouterPreference.setStatus("current")


class _SleRAGuardPolicyControlMatchACLName_Type(OctetString):
    """Custom type sleRAGuardPolicyControlMatchACLName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleRAGuardPolicyControlMatchACLName_Type.__name__ = "OctetString"
_SleRAGuardPolicyControlMatchACLName_Object = MibScalar
sleRAGuardPolicyControlMatchACLName = _SleRAGuardPolicyControlMatchACLName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 13),
    _SleRAGuardPolicyControlMatchACLName_Type()
)
sleRAGuardPolicyControlMatchACLName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlMatchACLName.setStatus("current")


class _SleRAGuardPolicyControlMatchPrefixName_Type(OctetString):
    """Custom type sleRAGuardPolicyControlMatchPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleRAGuardPolicyControlMatchPrefixName_Type.__name__ = "OctetString"
_SleRAGuardPolicyControlMatchPrefixName_Object = MibScalar
sleRAGuardPolicyControlMatchPrefixName = _SleRAGuardPolicyControlMatchPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 2, 14),
    _SleRAGuardPolicyControlMatchPrefixName_Type()
)
sleRAGuardPolicyControlMatchPrefixName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPolicyControlMatchPrefixName.setStatus("current")
_SleRAGuardPolicyNotifications_ObjectIdentity = ObjectIdentity
sleRAGuardPolicyNotifications = _SleRAGuardPolicyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 3)
)
_SleRAGuardVlan_ObjectIdentity = ObjectIdentity
sleRAGuardVlan = _SleRAGuardVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2)
)
_SleRAGuardVlanTable_Object = MibTable
sleRAGuardVlanTable = _SleRAGuardVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 1)
)
if mibBuilder.loadTexts:
    sleRAGuardVlanTable.setStatus("current")
_SleRAGuardVlanEntry_Object = MibTableRow
sleRAGuardVlanEntry = _SleRAGuardVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 1, 1)
)
sleRAGuardVlanEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleRAGuardVlanIndex"),
)
if mibBuilder.loadTexts:
    sleRAGuardVlanEntry.setStatus("current")


class _SleRAGuardVlanIndex_Type(Integer32):
    """Custom type sleRAGuardVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleRAGuardVlanIndex_Type.__name__ = "Integer32"
_SleRAGuardVlanIndex_Object = MibTableColumn
sleRAGuardVlanIndex = _SleRAGuardVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 1, 1, 1),
    _SleRAGuardVlanIndex_Type()
)
sleRAGuardVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardVlanIndex.setStatus("current")


class _SleRAGuardVlanEnable_Type(Integer32):
    """Custom type sleRAGuardVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleRAGuardVlanEnable_Type.__name__ = "Integer32"
_SleRAGuardVlanEnable_Object = MibTableColumn
sleRAGuardVlanEnable = _SleRAGuardVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 1, 1, 2),
    _SleRAGuardVlanEnable_Type()
)
sleRAGuardVlanEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardVlanEnable.setStatus("current")
_SleRAGuardVlanFilterPolicy_Type = Integer32
_SleRAGuardVlanFilterPolicy_Object = MibTableColumn
sleRAGuardVlanFilterPolicy = _SleRAGuardVlanFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 1, 1, 3),
    _SleRAGuardVlanFilterPolicy_Type()
)
sleRAGuardVlanFilterPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardVlanFilterPolicy.setStatus("current")


class _SleRAGuardVlanFilterAclName_Type(OctetString):
    """Custom type sleRAGuardVlanFilterAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SleRAGuardVlanFilterAclName_Type.__name__ = "OctetString"
_SleRAGuardVlanFilterAclName_Object = MibTableColumn
sleRAGuardVlanFilterAclName = _SleRAGuardVlanFilterAclName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 1, 1, 4),
    _SleRAGuardVlanFilterAclName_Type()
)
sleRAGuardVlanFilterAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardVlanFilterAclName.setStatus("current")
_SleRAGuardVlanControl_ObjectIdentity = ObjectIdentity
sleRAGuardVlanControl = _SleRAGuardVlanControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2)
)


class _SleRAGuardVlanControlRequest_Type(Integer32):
    """Custom type sleRAGuardVlanControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setRAGuardtVlanProfile", 1)
    )


_SleRAGuardVlanControlRequest_Type.__name__ = "Integer32"
_SleRAGuardVlanControlRequest_Object = MibScalar
sleRAGuardVlanControlRequest = _SleRAGuardVlanControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2, 1),
    _SleRAGuardVlanControlRequest_Type()
)
sleRAGuardVlanControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardVlanControlRequest.setStatus("current")
_SleRAGuardVlanControlStatus_Type = SleControlStatusType
_SleRAGuardVlanControlStatus_Object = MibScalar
sleRAGuardVlanControlStatus = _SleRAGuardVlanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2, 2),
    _SleRAGuardVlanControlStatus_Type()
)
sleRAGuardVlanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardVlanControlStatus.setStatus("current")
_SleRAGuardVlanControlTimer_Type = Gauge32
_SleRAGuardVlanControlTimer_Object = MibScalar
sleRAGuardVlanControlTimer = _SleRAGuardVlanControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2, 3),
    _SleRAGuardVlanControlTimer_Type()
)
sleRAGuardVlanControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardVlanControlTimer.setStatus("current")
_SleRAGuardVlanControlTimeStamp_Type = TimeTicks
_SleRAGuardVlanControlTimeStamp_Object = MibScalar
sleRAGuardVlanControlTimeStamp = _SleRAGuardVlanControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2, 4),
    _SleRAGuardVlanControlTimeStamp_Type()
)
sleRAGuardVlanControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardVlanControlTimeStamp.setStatus("current")
_SleRAGuardVlanControlReqResult_Type = SleControlRequestResultType
_SleRAGuardVlanControlReqResult_Object = MibScalar
sleRAGuardVlanControlReqResult = _SleRAGuardVlanControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2, 5),
    _SleRAGuardVlanControlReqResult_Type()
)
sleRAGuardVlanControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardVlanControlReqResult.setStatus("current")


class _SleRAGuardVlanControlIndex_Type(Integer32):
    """Custom type sleRAGuardVlanControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleRAGuardVlanControlIndex_Type.__name__ = "Integer32"
_SleRAGuardVlanControlIndex_Object = MibScalar
sleRAGuardVlanControlIndex = _SleRAGuardVlanControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2, 6),
    _SleRAGuardVlanControlIndex_Type()
)
sleRAGuardVlanControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardVlanControlIndex.setStatus("current")


class _SleRAGuardVlanControlEnable_Type(Integer32):
    """Custom type sleRAGuardVlanControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleRAGuardVlanControlEnable_Type.__name__ = "Integer32"
_SleRAGuardVlanControlEnable_Object = MibScalar
sleRAGuardVlanControlEnable = _SleRAGuardVlanControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2, 7),
    _SleRAGuardVlanControlEnable_Type()
)
sleRAGuardVlanControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardVlanControlEnable.setStatus("current")
_SleRAGuardVlanControlFilterPolicy_Type = Integer32
_SleRAGuardVlanControlFilterPolicy_Object = MibScalar
sleRAGuardVlanControlFilterPolicy = _SleRAGuardVlanControlFilterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 2, 8),
    _SleRAGuardVlanControlFilterPolicy_Type()
)
sleRAGuardVlanControlFilterPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardVlanControlFilterPolicy.setStatus("current")
_SleRAGuardVlanNotifications_ObjectIdentity = ObjectIdentity
sleRAGuardVlanNotifications = _SleRAGuardVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 3)
)
_SleRAGuardPort_ObjectIdentity = ObjectIdentity
sleRAGuardPort = _SleRAGuardPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3)
)
_SleRAGuardPortTable_Object = MibTable
sleRAGuardPortTable = _SleRAGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 1)
)
if mibBuilder.loadTexts:
    sleRAGuardPortTable.setStatus("current")
_SleRAGuardPortEntry_Object = MibTableRow
sleRAGuardPortEntry = _SleRAGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 1, 1)
)
sleRAGuardPortEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleRAGuardPortIndex"),
)
if mibBuilder.loadTexts:
    sleRAGuardPortEntry.setStatus("current")


class _SleRAGuardPortIndex_Type(Integer32):
    """Custom type sleRAGuardPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SleRAGuardPortIndex_Type.__name__ = "Integer32"
_SleRAGuardPortIndex_Object = MibTableColumn
sleRAGuardPortIndex = _SleRAGuardPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 1, 1, 1),
    _SleRAGuardPortIndex_Type()
)
sleRAGuardPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPortIndex.setStatus("current")


class _SleRAGuardPortTrust_Type(Integer32):
    """Custom type sleRAGuardPortTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("trust", 1),
          ("untrust", 2))
    )


_SleRAGuardPortTrust_Type.__name__ = "Integer32"
_SleRAGuardPortTrust_Object = MibTableColumn
sleRAGuardPortTrust = _SleRAGuardPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 1, 1, 2),
    _SleRAGuardPortTrust_Type()
)
sleRAGuardPortTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPortTrust.setStatus("current")
_SleRAGuardPortControl_ObjectIdentity = ObjectIdentity
sleRAGuardPortControl = _SleRAGuardPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 2)
)


class _SleRAGuardPortControlRequest_Type(Integer32):
    """Custom type sleRAGuardPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setdRAGuardTrustPort", 1)
    )


_SleRAGuardPortControlRequest_Type.__name__ = "Integer32"
_SleRAGuardPortControlRequest_Object = MibScalar
sleRAGuardPortControlRequest = _SleRAGuardPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 2, 1),
    _SleRAGuardPortControlRequest_Type()
)
sleRAGuardPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPortControlRequest.setStatus("current")
_SleRAGuardPortControlStatus_Type = SleControlStatusType
_SleRAGuardPortControlStatus_Object = MibScalar
sleRAGuardPortControlStatus = _SleRAGuardPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 2, 2),
    _SleRAGuardPortControlStatus_Type()
)
sleRAGuardPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPortControlStatus.setStatus("current")
_SleRAGuardPortControlTimer_Type = Gauge32
_SleRAGuardPortControlTimer_Object = MibScalar
sleRAGuardPortControlTimer = _SleRAGuardPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 2, 3),
    _SleRAGuardPortControlTimer_Type()
)
sleRAGuardPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPortControlTimer.setStatus("current")
_SleRAGuardPortControlTimeStamp_Type = TimeTicks
_SleRAGuardPortControlTimeStamp_Object = MibScalar
sleRAGuardPortControlTimeStamp = _SleRAGuardPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 2, 4),
    _SleRAGuardPortControlTimeStamp_Type()
)
sleRAGuardPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPortControlTimeStamp.setStatus("current")
_SleRAGuardPortControlReqResult_Type = SleControlRequestResultType
_SleRAGuardPortControlReqResult_Object = MibScalar
sleRAGuardPortControlReqResult = _SleRAGuardPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 2, 5),
    _SleRAGuardPortControlReqResult_Type()
)
sleRAGuardPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRAGuardPortControlReqResult.setStatus("current")


class _SleRAGuardPortControlIndex_Type(Integer32):
    """Custom type sleRAGuardPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SleRAGuardPortControlIndex_Type.__name__ = "Integer32"
_SleRAGuardPortControlIndex_Object = MibScalar
sleRAGuardPortControlIndex = _SleRAGuardPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 2, 6),
    _SleRAGuardPortControlIndex_Type()
)
sleRAGuardPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPortControlIndex.setStatus("current")


class _SleRAGuardPortControlTrust_Type(Integer32):
    """Custom type sleRAGuardPortControlTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("trust", 1),
          ("untrust", 2))
    )


_SleRAGuardPortControlTrust_Type.__name__ = "Integer32"
_SleRAGuardPortControlTrust_Object = MibScalar
sleRAGuardPortControlTrust = _SleRAGuardPortControlTrust_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 2, 7),
    _SleRAGuardPortControlTrust_Type()
)
sleRAGuardPortControlTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRAGuardPortControlTrust.setStatus("current")
_SleRAGuardPortNotifications_ObjectIdentity = ObjectIdentity
sleRAGuardPortNotifications = _SleRAGuardPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 3)
)
_SleRadiusServerDot1x_ObjectIdentity = ObjectIdentity
sleRadiusServerDot1x = _SleRadiusServerDot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14)
)
_SleRadiusServerDot1xTable_Object = MibTable
sleRadiusServerDot1xTable = _SleRadiusServerDot1xTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 1)
)
if mibBuilder.loadTexts:
    sleRadiusServerDot1xTable.setStatus("current")
_SleRadiusServerDot1xEntry_Object = MibTableRow
sleRadiusServerDot1xEntry = _SleRadiusServerDot1xEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 1, 1)
)
sleRadiusServerDot1xEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleRadiusServerDot1xAddress"),
    (0, "SLE-SECURITY-MIB", "sleRadiusServerDot1xAuthPort"),
)
if mibBuilder.loadTexts:
    sleRadiusServerDot1xEntry.setStatus("current")
_SleRadiusServerDot1xAddress_Type = IpAddress
_SleRadiusServerDot1xAddress_Object = MibTableColumn
sleRadiusServerDot1xAddress = _SleRadiusServerDot1xAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 1, 1, 1),
    _SleRadiusServerDot1xAddress_Type()
)
sleRadiusServerDot1xAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xAddress.setStatus("current")


class _SleRadiusServerDot1xAuthPort_Type(Integer32):
    """Custom type sleRadiusServerDot1xAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRadiusServerDot1xAuthPort_Type.__name__ = "Integer32"
_SleRadiusServerDot1xAuthPort_Object = MibTableColumn
sleRadiusServerDot1xAuthPort = _SleRadiusServerDot1xAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 1, 1, 2),
    _SleRadiusServerDot1xAuthPort_Type()
)
sleRadiusServerDot1xAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xAuthPort.setStatus("current")


class _SleRadiusServerDot1xTimeout_Type(Integer32):
    """Custom type sleRadiusServerDot1xTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SleRadiusServerDot1xTimeout_Type.__name__ = "Integer32"
_SleRadiusServerDot1xTimeout_Object = MibTableColumn
sleRadiusServerDot1xTimeout = _SleRadiusServerDot1xTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 1, 1, 3),
    _SleRadiusServerDot1xTimeout_Type()
)
sleRadiusServerDot1xTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xTimeout.setStatus("current")


class _SleRadiusServerDot1xRetransmit_Type(Integer32):
    """Custom type sleRadiusServerDot1xRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleRadiusServerDot1xRetransmit_Type.__name__ = "Integer32"
_SleRadiusServerDot1xRetransmit_Object = MibTableColumn
sleRadiusServerDot1xRetransmit = _SleRadiusServerDot1xRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 1, 1, 4),
    _SleRadiusServerDot1xRetransmit_Type()
)
sleRadiusServerDot1xRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xRetransmit.setStatus("current")


class _SleRadiusServerDot1xClientKey_Type(OctetString):
    """Custom type sleRadiusServerDot1xClientKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleRadiusServerDot1xClientKey_Type.__name__ = "OctetString"
_SleRadiusServerDot1xClientKey_Object = MibTableColumn
sleRadiusServerDot1xClientKey = _SleRadiusServerDot1xClientKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 1, 1, 5),
    _SleRadiusServerDot1xClientKey_Type()
)
sleRadiusServerDot1xClientKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xClientKey.setStatus("current")
_SleRadiusServerDot1xControl_ObjectIdentity = ObjectIdentity
sleRadiusServerDot1xControl = _SleRadiusServerDot1xControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2)
)


class _SleRadiusServerDot1xControlRequest_Type(Integer32):
    """Custom type sleRadiusServerDot1xControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createRadiusServerDot1x", 1),
          ("destroyRadiusServerDot1x", 2),
          ("setRadiusServerDot1xProfile", 3))
    )


_SleRadiusServerDot1xControlRequest_Type.__name__ = "Integer32"
_SleRadiusServerDot1xControlRequest_Object = MibScalar
sleRadiusServerDot1xControlRequest = _SleRadiusServerDot1xControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 1),
    _SleRadiusServerDot1xControlRequest_Type()
)
sleRadiusServerDot1xControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlRequest.setStatus("current")
_SleRadiusServerDot1xControlStatus_Type = SleControlStatusType
_SleRadiusServerDot1xControlStatus_Object = MibScalar
sleRadiusServerDot1xControlStatus = _SleRadiusServerDot1xControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 2),
    _SleRadiusServerDot1xControlStatus_Type()
)
sleRadiusServerDot1xControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlStatus.setStatus("current")
_SleRadiusServerDot1xControlTimer_Type = Gauge32
_SleRadiusServerDot1xControlTimer_Object = MibScalar
sleRadiusServerDot1xControlTimer = _SleRadiusServerDot1xControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 3),
    _SleRadiusServerDot1xControlTimer_Type()
)
sleRadiusServerDot1xControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlTimer.setStatus("current")
_SleRadiusServerDot1xControlTimeStamp_Type = TimeStamp
_SleRadiusServerDot1xControlTimeStamp_Object = MibScalar
sleRadiusServerDot1xControlTimeStamp = _SleRadiusServerDot1xControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 4),
    _SleRadiusServerDot1xControlTimeStamp_Type()
)
sleRadiusServerDot1xControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlTimeStamp.setStatus("current")
_SleRadiusServerDot1xControlReqResult_Type = SleControlRequestResultType
_SleRadiusServerDot1xControlReqResult_Object = MibScalar
sleRadiusServerDot1xControlReqResult = _SleRadiusServerDot1xControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 5),
    _SleRadiusServerDot1xControlReqResult_Type()
)
sleRadiusServerDot1xControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlReqResult.setStatus("current")
_SleRadiusServerDot1xControlAddress_Type = IpAddress
_SleRadiusServerDot1xControlAddress_Object = MibScalar
sleRadiusServerDot1xControlAddress = _SleRadiusServerDot1xControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 6),
    _SleRadiusServerDot1xControlAddress_Type()
)
sleRadiusServerDot1xControlAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlAddress.setStatus("current")


class _SleRadiusServerDot1xControlAuthPort_Type(Integer32):
    """Custom type sleRadiusServerDot1xControlAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleRadiusServerDot1xControlAuthPort_Type.__name__ = "Integer32"
_SleRadiusServerDot1xControlAuthPort_Object = MibScalar
sleRadiusServerDot1xControlAuthPort = _SleRadiusServerDot1xControlAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 7),
    _SleRadiusServerDot1xControlAuthPort_Type()
)
sleRadiusServerDot1xControlAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlAuthPort.setStatus("current")


class _SleRadiusServerDot1xControlTimeout_Type(Integer32):
    """Custom type sleRadiusServerDot1xControlTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SleRadiusServerDot1xControlTimeout_Type.__name__ = "Integer32"
_SleRadiusServerDot1xControlTimeout_Object = MibScalar
sleRadiusServerDot1xControlTimeout = _SleRadiusServerDot1xControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 8),
    _SleRadiusServerDot1xControlTimeout_Type()
)
sleRadiusServerDot1xControlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlTimeout.setStatus("current")


class _SleRadiusServerDot1xControlRetransmit_Type(Integer32):
    """Custom type sleRadiusServerDot1xControlRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SleRadiusServerDot1xControlRetransmit_Type.__name__ = "Integer32"
_SleRadiusServerDot1xControlRetransmit_Object = MibScalar
sleRadiusServerDot1xControlRetransmit = _SleRadiusServerDot1xControlRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 9),
    _SleRadiusServerDot1xControlRetransmit_Type()
)
sleRadiusServerDot1xControlRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlRetransmit.setStatus("current")


class _SleRadiusServerDot1xControlClientKey_Type(OctetString):
    """Custom type sleRadiusServerDot1xControlClientKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleRadiusServerDot1xControlClientKey_Type.__name__ = "OctetString"
_SleRadiusServerDot1xControlClientKey_Object = MibScalar
sleRadiusServerDot1xControlClientKey = _SleRadiusServerDot1xControlClientKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 14, 2, 10),
    _SleRadiusServerDot1xControlClientKey_Type()
)
sleRadiusServerDot1xControlClientKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRadiusServerDot1xControlClientKey.setStatus("current")
_SleKeyChain_ObjectIdentity = ObjectIdentity
sleKeyChain = _SleKeyChain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15)
)
_SleKeyChainTable_Object = MibTable
sleKeyChainTable = _SleKeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1)
)
if mibBuilder.loadTexts:
    sleKeyChainTable.setStatus("current")
_SleKeyChainEntry_Object = MibTableRow
sleKeyChainEntry = _SleKeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1)
)
sleKeyChainEntry.setIndexNames(
    (0, "SLE-SECURITY-MIB", "sleKeyChainName"),
    (0, "SLE-SECURITY-MIB", "sleKeyChainKeyId"),
)
if mibBuilder.loadTexts:
    sleKeyChainEntry.setStatus("current")
_SleKeyChainName_Type = OctetString
_SleKeyChainName_Object = MibTableColumn
sleKeyChainName = _SleKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 1),
    _SleKeyChainName_Type()
)
sleKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainName.setStatus("current")


class _SleKeyChainKeyId_Type(Integer32):
    """Custom type sleKeyChainKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleKeyChainKeyId_Type.__name__ = "Integer32"
_SleKeyChainKeyId_Object = MibTableColumn
sleKeyChainKeyId = _SleKeyChainKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 2),
    _SleKeyChainKeyId_Type()
)
sleKeyChainKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyId.setStatus("current")
_SleKeyChainKeyString_Type = OctetString
_SleKeyChainKeyString_Object = MibTableColumn
sleKeyChainKeyString = _SleKeyChainKeyString_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 3),
    _SleKeyChainKeyString_Type()
)
sleKeyChainKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyString.setStatus("current")
_SleKeyChainKeyAccepLifeTimeStartTime_Type = OctetString
_SleKeyChainKeyAccepLifeTimeStartTime_Object = MibTableColumn
sleKeyChainKeyAccepLifeTimeStartTime = _SleKeyChainKeyAccepLifeTimeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 4),
    _SleKeyChainKeyAccepLifeTimeStartTime_Type()
)
sleKeyChainKeyAccepLifeTimeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAccepLifeTimeStartTime.setStatus("current")


class _SleKeyChainKeyAcceptLifeTimeStartDay_Type(Integer32):
    """Custom type sleKeyChainKeyAcceptLifeTimeStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SleKeyChainKeyAcceptLifeTimeStartDay_Type.__name__ = "Integer32"
_SleKeyChainKeyAcceptLifeTimeStartDay_Object = MibTableColumn
sleKeyChainKeyAcceptLifeTimeStartDay = _SleKeyChainKeyAcceptLifeTimeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 5),
    _SleKeyChainKeyAcceptLifeTimeStartDay_Type()
)
sleKeyChainKeyAcceptLifeTimeStartDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAcceptLifeTimeStartDay.setStatus("current")


class _SleKeyChainKeyAcceptLifeTimeStartMonth_Type(Integer32):
    """Custom type sleKeyChainKeyAcceptLifeTimeStartMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SleKeyChainKeyAcceptLifeTimeStartMonth_Type.__name__ = "Integer32"
_SleKeyChainKeyAcceptLifeTimeStartMonth_Object = MibTableColumn
sleKeyChainKeyAcceptLifeTimeStartMonth = _SleKeyChainKeyAcceptLifeTimeStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 6),
    _SleKeyChainKeyAcceptLifeTimeStartMonth_Type()
)
sleKeyChainKeyAcceptLifeTimeStartMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAcceptLifeTimeStartMonth.setStatus("current")


class _SleKeyChainKeyAcceptLifeTimeStartYear_Type(Integer32):
    """Custom type sleKeyChainKeyAcceptLifeTimeStartYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1993, 2035),
    )


_SleKeyChainKeyAcceptLifeTimeStartYear_Type.__name__ = "Integer32"
_SleKeyChainKeyAcceptLifeTimeStartYear_Object = MibTableColumn
sleKeyChainKeyAcceptLifeTimeStartYear = _SleKeyChainKeyAcceptLifeTimeStartYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 7),
    _SleKeyChainKeyAcceptLifeTimeStartYear_Type()
)
sleKeyChainKeyAcceptLifeTimeStartYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAcceptLifeTimeStartYear.setStatus("current")


class _SleKeyChainKeyAcceptLifeTimeExpireType_Type(Integer32):
    """Custom type sleKeyChainKeyAcceptLifeTimeExpireType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("expire", 0),
          ("neverexpire", 1))
    )


_SleKeyChainKeyAcceptLifeTimeExpireType_Type.__name__ = "Integer32"
_SleKeyChainKeyAcceptLifeTimeExpireType_Object = MibTableColumn
sleKeyChainKeyAcceptLifeTimeExpireType = _SleKeyChainKeyAcceptLifeTimeExpireType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 8),
    _SleKeyChainKeyAcceptLifeTimeExpireType_Type()
)
sleKeyChainKeyAcceptLifeTimeExpireType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAcceptLifeTimeExpireType.setStatus("current")
_SleKeyChainKeyAcceptLifeTimeExpireTime_Type = OctetString
_SleKeyChainKeyAcceptLifeTimeExpireTime_Object = MibTableColumn
sleKeyChainKeyAcceptLifeTimeExpireTime = _SleKeyChainKeyAcceptLifeTimeExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 9),
    _SleKeyChainKeyAcceptLifeTimeExpireTime_Type()
)
sleKeyChainKeyAcceptLifeTimeExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAcceptLifeTimeExpireTime.setStatus("current")


class _SleKeyChainKeyAcceptLifeTimeExpireDay_Type(Integer32):
    """Custom type sleKeyChainKeyAcceptLifeTimeExpireDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SleKeyChainKeyAcceptLifeTimeExpireDay_Type.__name__ = "Integer32"
_SleKeyChainKeyAcceptLifeTimeExpireDay_Object = MibTableColumn
sleKeyChainKeyAcceptLifeTimeExpireDay = _SleKeyChainKeyAcceptLifeTimeExpireDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 10),
    _SleKeyChainKeyAcceptLifeTimeExpireDay_Type()
)
sleKeyChainKeyAcceptLifeTimeExpireDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAcceptLifeTimeExpireDay.setStatus("current")


class _SleKeyChainKeyAcceptLifeTimeExpireMonth_Type(Integer32):
    """Custom type sleKeyChainKeyAcceptLifeTimeExpireMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SleKeyChainKeyAcceptLifeTimeExpireMonth_Type.__name__ = "Integer32"
_SleKeyChainKeyAcceptLifeTimeExpireMonth_Object = MibTableColumn
sleKeyChainKeyAcceptLifeTimeExpireMonth = _SleKeyChainKeyAcceptLifeTimeExpireMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 11),
    _SleKeyChainKeyAcceptLifeTimeExpireMonth_Type()
)
sleKeyChainKeyAcceptLifeTimeExpireMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAcceptLifeTimeExpireMonth.setStatus("current")


class _SleKeyChainKeyAcceptLifeTimeExpireYear_Type(Integer32):
    """Custom type sleKeyChainKeyAcceptLifeTimeExpireYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1993, 2035),
    )


_SleKeyChainKeyAcceptLifeTimeExpireYear_Type.__name__ = "Integer32"
_SleKeyChainKeyAcceptLifeTimeExpireYear_Object = MibTableColumn
sleKeyChainKeyAcceptLifeTimeExpireYear = _SleKeyChainKeyAcceptLifeTimeExpireYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 12),
    _SleKeyChainKeyAcceptLifeTimeExpireYear_Type()
)
sleKeyChainKeyAcceptLifeTimeExpireYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeyAcceptLifeTimeExpireYear.setStatus("current")
_SleKeyChainKeySendLifeTimeStartTime_Type = OctetString
_SleKeyChainKeySendLifeTimeStartTime_Object = MibTableColumn
sleKeyChainKeySendLifeTimeStartTime = _SleKeyChainKeySendLifeTimeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 13),
    _SleKeyChainKeySendLifeTimeStartTime_Type()
)
sleKeyChainKeySendLifeTimeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeStartTime.setStatus("current")


class _SleKeyChainKeySendLifeTimeStartDay_Type(Integer32):
    """Custom type sleKeyChainKeySendLifeTimeStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SleKeyChainKeySendLifeTimeStartDay_Type.__name__ = "Integer32"
_SleKeyChainKeySendLifeTimeStartDay_Object = MibTableColumn
sleKeyChainKeySendLifeTimeStartDay = _SleKeyChainKeySendLifeTimeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 14),
    _SleKeyChainKeySendLifeTimeStartDay_Type()
)
sleKeyChainKeySendLifeTimeStartDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeStartDay.setStatus("current")


class _SleKeyChainKeySendLifeTimeStartMonth_Type(Integer32):
    """Custom type sleKeyChainKeySendLifeTimeStartMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SleKeyChainKeySendLifeTimeStartMonth_Type.__name__ = "Integer32"
_SleKeyChainKeySendLifeTimeStartMonth_Object = MibTableColumn
sleKeyChainKeySendLifeTimeStartMonth = _SleKeyChainKeySendLifeTimeStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 15),
    _SleKeyChainKeySendLifeTimeStartMonth_Type()
)
sleKeyChainKeySendLifeTimeStartMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeStartMonth.setStatus("current")


class _SleKeyChainKeySendLifeTimeStartYear_Type(Integer32):
    """Custom type sleKeyChainKeySendLifeTimeStartYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1993, 2035),
    )


_SleKeyChainKeySendLifeTimeStartYear_Type.__name__ = "Integer32"
_SleKeyChainKeySendLifeTimeStartYear_Object = MibTableColumn
sleKeyChainKeySendLifeTimeStartYear = _SleKeyChainKeySendLifeTimeStartYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 16),
    _SleKeyChainKeySendLifeTimeStartYear_Type()
)
sleKeyChainKeySendLifeTimeStartYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeStartYear.setStatus("current")


class _SleKeyChainKeySendLifeTimeExpireType_Type(Integer32):
    """Custom type sleKeyChainKeySendLifeTimeExpireType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("expire", 0),
          ("neverexpire", 1))
    )


_SleKeyChainKeySendLifeTimeExpireType_Type.__name__ = "Integer32"
_SleKeyChainKeySendLifeTimeExpireType_Object = MibTableColumn
sleKeyChainKeySendLifeTimeExpireType = _SleKeyChainKeySendLifeTimeExpireType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 17),
    _SleKeyChainKeySendLifeTimeExpireType_Type()
)
sleKeyChainKeySendLifeTimeExpireType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeExpireType.setStatus("current")
_SleKeyChainKeySendLifeTimeExpireTime_Type = OctetString
_SleKeyChainKeySendLifeTimeExpireTime_Object = MibTableColumn
sleKeyChainKeySendLifeTimeExpireTime = _SleKeyChainKeySendLifeTimeExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 18),
    _SleKeyChainKeySendLifeTimeExpireTime_Type()
)
sleKeyChainKeySendLifeTimeExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeExpireTime.setStatus("current")


class _SleKeyChainKeySendLifeTimeExpireDay_Type(Integer32):
    """Custom type sleKeyChainKeySendLifeTimeExpireDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SleKeyChainKeySendLifeTimeExpireDay_Type.__name__ = "Integer32"
_SleKeyChainKeySendLifeTimeExpireDay_Object = MibTableColumn
sleKeyChainKeySendLifeTimeExpireDay = _SleKeyChainKeySendLifeTimeExpireDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 19),
    _SleKeyChainKeySendLifeTimeExpireDay_Type()
)
sleKeyChainKeySendLifeTimeExpireDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeExpireDay.setStatus("current")


class _SleKeyChainKeySendLifeTimeExpireMonth_Type(Integer32):
    """Custom type sleKeyChainKeySendLifeTimeExpireMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SleKeyChainKeySendLifeTimeExpireMonth_Type.__name__ = "Integer32"
_SleKeyChainKeySendLifeTimeExpireMonth_Object = MibTableColumn
sleKeyChainKeySendLifeTimeExpireMonth = _SleKeyChainKeySendLifeTimeExpireMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 20),
    _SleKeyChainKeySendLifeTimeExpireMonth_Type()
)
sleKeyChainKeySendLifeTimeExpireMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeExpireMonth.setStatus("current")


class _SleKeyChainKeySendLifeTimeExpireYear_Type(Integer32):
    """Custom type sleKeyChainKeySendLifeTimeExpireYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1993, 2035),
    )


_SleKeyChainKeySendLifeTimeExpireYear_Type.__name__ = "Integer32"
_SleKeyChainKeySendLifeTimeExpireYear_Object = MibTableColumn
sleKeyChainKeySendLifeTimeExpireYear = _SleKeyChainKeySendLifeTimeExpireYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 1, 1, 21),
    _SleKeyChainKeySendLifeTimeExpireYear_Type()
)
sleKeyChainKeySendLifeTimeExpireYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainKeySendLifeTimeExpireYear.setStatus("current")
_SleKeyChainControl_ObjectIdentity = ObjectIdentity
sleKeyChainControl = _SleKeyChainControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2)
)


class _SleKeyChainControlRequest_Type(Integer32):
    """Custom type sleKeyChainControlRequest based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("createKeyChain", 1),
          ("deleteKeyChain", 2),
          ("createKeyChainKey", 3),
          ("deleteKeyChainKey", 4),
          ("setKeyChainKeyString", 5),
          ("deleteKeyChainKeyString", 6),
          ("setKeyChainKeyAcceptLifeTimeProfile", 7),
          ("deleteKeyChainKeyAcceptLifeTime", 8),
          ("setKeyChainKeySendLifeTimeProfile", 9),
          ("deleteKeyChainKeySendLifeTime", 10))
    )


_SleKeyChainControlRequest_Type.__name__ = "Integer32"
_SleKeyChainControlRequest_Object = MibScalar
sleKeyChainControlRequest = _SleKeyChainControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 1),
    _SleKeyChainControlRequest_Type()
)
sleKeyChainControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlRequest.setStatus("current")
_SleKeyChainControlStatus_Type = SleControlStatusType
_SleKeyChainControlStatus_Object = MibScalar
sleKeyChainControlStatus = _SleKeyChainControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 2),
    _SleKeyChainControlStatus_Type()
)
sleKeyChainControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainControlStatus.setStatus("current")
_SleKeyChainControlTimer_Type = Gauge32
_SleKeyChainControlTimer_Object = MibScalar
sleKeyChainControlTimer = _SleKeyChainControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 3),
    _SleKeyChainControlTimer_Type()
)
sleKeyChainControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlTimer.setStatus("current")
_SleKeyChainControlTimeStamp_Type = TimeTicks
_SleKeyChainControlTimeStamp_Object = MibScalar
sleKeyChainControlTimeStamp = _SleKeyChainControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 4),
    _SleKeyChainControlTimeStamp_Type()
)
sleKeyChainControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainControlTimeStamp.setStatus("current")
_SleKeyChainControlReqResult_Type = SleControlRequestResultType
_SleKeyChainControlReqResult_Object = MibScalar
sleKeyChainControlReqResult = _SleKeyChainControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 5),
    _SleKeyChainControlReqResult_Type()
)
sleKeyChainControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleKeyChainControlReqResult.setStatus("current")
_SleKeyChainControlName_Type = OctetString
_SleKeyChainControlName_Object = MibScalar
sleKeyChainControlName = _SleKeyChainControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 6),
    _SleKeyChainControlName_Type()
)
sleKeyChainControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlName.setStatus("current")


class _SleKeyChainControlKeyId_Type(Integer32):
    """Custom type sleKeyChainControlKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleKeyChainControlKeyId_Type.__name__ = "Integer32"
_SleKeyChainControlKeyId_Object = MibScalar
sleKeyChainControlKeyId = _SleKeyChainControlKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 7),
    _SleKeyChainControlKeyId_Type()
)
sleKeyChainControlKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyId.setStatus("current")
_SleKeyChainControlKeyString_Type = OctetString
_SleKeyChainControlKeyString_Object = MibScalar
sleKeyChainControlKeyString = _SleKeyChainControlKeyString_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 8),
    _SleKeyChainControlKeyString_Type()
)
sleKeyChainControlKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyString.setStatus("current")
_SleKeyChainControlKeyAcceptLifeTimeStartTime_Type = OctetString
_SleKeyChainControlKeyAcceptLifeTimeStartTime_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeStartTime = _SleKeyChainControlKeyAcceptLifeTimeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 9),
    _SleKeyChainControlKeyAcceptLifeTimeStartTime_Type()
)
sleKeyChainControlKeyAcceptLifeTimeStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeStartTime.setStatus("current")


class _SleKeyChainControlKeyAcceptLifeTimeStartDay_Type(Integer32):
    """Custom type sleKeyChainControlKeyAcceptLifeTimeStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SleKeyChainControlKeyAcceptLifeTimeStartDay_Type.__name__ = "Integer32"
_SleKeyChainControlKeyAcceptLifeTimeStartDay_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeStartDay = _SleKeyChainControlKeyAcceptLifeTimeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 10),
    _SleKeyChainControlKeyAcceptLifeTimeStartDay_Type()
)
sleKeyChainControlKeyAcceptLifeTimeStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeStartDay.setStatus("current")


class _SleKeyChainControlKeyAcceptLifeTimeStartMonth_Type(Integer32):
    """Custom type sleKeyChainControlKeyAcceptLifeTimeStartMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SleKeyChainControlKeyAcceptLifeTimeStartMonth_Type.__name__ = "Integer32"
_SleKeyChainControlKeyAcceptLifeTimeStartMonth_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeStartMonth = _SleKeyChainControlKeyAcceptLifeTimeStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 11),
    _SleKeyChainControlKeyAcceptLifeTimeStartMonth_Type()
)
sleKeyChainControlKeyAcceptLifeTimeStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeStartMonth.setStatus("current")


class _SleKeyChainControlKeyAcceptLifeTimeStartYear_Type(Integer32):
    """Custom type sleKeyChainControlKeyAcceptLifeTimeStartYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1993, 2035),
    )


_SleKeyChainControlKeyAcceptLifeTimeStartYear_Type.__name__ = "Integer32"
_SleKeyChainControlKeyAcceptLifeTimeStartYear_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeStartYear = _SleKeyChainControlKeyAcceptLifeTimeStartYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 12),
    _SleKeyChainControlKeyAcceptLifeTimeStartYear_Type()
)
sleKeyChainControlKeyAcceptLifeTimeStartYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeStartYear.setStatus("current")


class _SleKeyChainControlKeyAcceptLifeTimeExpireType_Type(Integer32):
    """Custom type sleKeyChainControlKeyAcceptLifeTimeExpireType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("expire", 0),
          ("neverexpire", 1))
    )


_SleKeyChainControlKeyAcceptLifeTimeExpireType_Type.__name__ = "Integer32"
_SleKeyChainControlKeyAcceptLifeTimeExpireType_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeExpireType = _SleKeyChainControlKeyAcceptLifeTimeExpireType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 13),
    _SleKeyChainControlKeyAcceptLifeTimeExpireType_Type()
)
sleKeyChainControlKeyAcceptLifeTimeExpireType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeExpireType.setStatus("current")
_SleKeyChainControlKeyAcceptLifeTimeExpireTime_Type = OctetString
_SleKeyChainControlKeyAcceptLifeTimeExpireTime_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeExpireTime = _SleKeyChainControlKeyAcceptLifeTimeExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 14),
    _SleKeyChainControlKeyAcceptLifeTimeExpireTime_Type()
)
sleKeyChainControlKeyAcceptLifeTimeExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeExpireTime.setStatus("current")


class _SleKeyChainControlKeyAcceptLifeTimeExpireDay_Type(Integer32):
    """Custom type sleKeyChainControlKeyAcceptLifeTimeExpireDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SleKeyChainControlKeyAcceptLifeTimeExpireDay_Type.__name__ = "Integer32"
_SleKeyChainControlKeyAcceptLifeTimeExpireDay_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeExpireDay = _SleKeyChainControlKeyAcceptLifeTimeExpireDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 15),
    _SleKeyChainControlKeyAcceptLifeTimeExpireDay_Type()
)
sleKeyChainControlKeyAcceptLifeTimeExpireDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeExpireDay.setStatus("current")


class _SleKeyChainControlKeyAcceptLifeTimeExpireMonth_Type(Integer32):
    """Custom type sleKeyChainControlKeyAcceptLifeTimeExpireMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SleKeyChainControlKeyAcceptLifeTimeExpireMonth_Type.__name__ = "Integer32"
_SleKeyChainControlKeyAcceptLifeTimeExpireMonth_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeExpireMonth = _SleKeyChainControlKeyAcceptLifeTimeExpireMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 16),
    _SleKeyChainControlKeyAcceptLifeTimeExpireMonth_Type()
)
sleKeyChainControlKeyAcceptLifeTimeExpireMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeExpireMonth.setStatus("current")


class _SleKeyChainControlKeyAcceptLifeTimeExpireYear_Type(Integer32):
    """Custom type sleKeyChainControlKeyAcceptLifeTimeExpireYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1993, 2035),
    )


_SleKeyChainControlKeyAcceptLifeTimeExpireYear_Type.__name__ = "Integer32"
_SleKeyChainControlKeyAcceptLifeTimeExpireYear_Object = MibScalar
sleKeyChainControlKeyAcceptLifeTimeExpireYear = _SleKeyChainControlKeyAcceptLifeTimeExpireYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 17),
    _SleKeyChainControlKeyAcceptLifeTimeExpireYear_Type()
)
sleKeyChainControlKeyAcceptLifeTimeExpireYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeyAcceptLifeTimeExpireYear.setStatus("current")
_SleKeyChainControlKeySendLifeTimeStartTime_Type = OctetString
_SleKeyChainControlKeySendLifeTimeStartTime_Object = MibScalar
sleKeyChainControlKeySendLifeTimeStartTime = _SleKeyChainControlKeySendLifeTimeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 18),
    _SleKeyChainControlKeySendLifeTimeStartTime_Type()
)
sleKeyChainControlKeySendLifeTimeStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeStartTime.setStatus("current")


class _SleKeyChainControlKeySendLifeTimeStartDay_Type(Integer32):
    """Custom type sleKeyChainControlKeySendLifeTimeStartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SleKeyChainControlKeySendLifeTimeStartDay_Type.__name__ = "Integer32"
_SleKeyChainControlKeySendLifeTimeStartDay_Object = MibScalar
sleKeyChainControlKeySendLifeTimeStartDay = _SleKeyChainControlKeySendLifeTimeStartDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 19),
    _SleKeyChainControlKeySendLifeTimeStartDay_Type()
)
sleKeyChainControlKeySendLifeTimeStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeStartDay.setStatus("current")


class _SleKeyChainControlKeySendLifeTimeStartMonth_Type(Integer32):
    """Custom type sleKeyChainControlKeySendLifeTimeStartMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SleKeyChainControlKeySendLifeTimeStartMonth_Type.__name__ = "Integer32"
_SleKeyChainControlKeySendLifeTimeStartMonth_Object = MibScalar
sleKeyChainControlKeySendLifeTimeStartMonth = _SleKeyChainControlKeySendLifeTimeStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 20),
    _SleKeyChainControlKeySendLifeTimeStartMonth_Type()
)
sleKeyChainControlKeySendLifeTimeStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeStartMonth.setStatus("current")


class _SleKeyChainControlKeySendLifeTimeStartYear_Type(Integer32):
    """Custom type sleKeyChainControlKeySendLifeTimeStartYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1993, 2035),
    )


_SleKeyChainControlKeySendLifeTimeStartYear_Type.__name__ = "Integer32"
_SleKeyChainControlKeySendLifeTimeStartYear_Object = MibScalar
sleKeyChainControlKeySendLifeTimeStartYear = _SleKeyChainControlKeySendLifeTimeStartYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 21),
    _SleKeyChainControlKeySendLifeTimeStartYear_Type()
)
sleKeyChainControlKeySendLifeTimeStartYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeStartYear.setStatus("current")


class _SleKeyChainControlKeySendLifeTimeExpireType_Type(Integer32):
    """Custom type sleKeyChainControlKeySendLifeTimeExpireType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("expire", 0),
          ("neverexpire", 1))
    )


_SleKeyChainControlKeySendLifeTimeExpireType_Type.__name__ = "Integer32"
_SleKeyChainControlKeySendLifeTimeExpireType_Object = MibScalar
sleKeyChainControlKeySendLifeTimeExpireType = _SleKeyChainControlKeySendLifeTimeExpireType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 22),
    _SleKeyChainControlKeySendLifeTimeExpireType_Type()
)
sleKeyChainControlKeySendLifeTimeExpireType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeExpireType.setStatus("current")
_SleKeyChainControlKeySendLifeTimeExpireTime_Type = OctetString
_SleKeyChainControlKeySendLifeTimeExpireTime_Object = MibScalar
sleKeyChainControlKeySendLifeTimeExpireTime = _SleKeyChainControlKeySendLifeTimeExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 23),
    _SleKeyChainControlKeySendLifeTimeExpireTime_Type()
)
sleKeyChainControlKeySendLifeTimeExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeExpireTime.setStatus("current")


class _SleKeyChainControlKeySendLifeTimeExpireDay_Type(Integer32):
    """Custom type sleKeyChainControlKeySendLifeTimeExpireDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_SleKeyChainControlKeySendLifeTimeExpireDay_Type.__name__ = "Integer32"
_SleKeyChainControlKeySendLifeTimeExpireDay_Object = MibScalar
sleKeyChainControlKeySendLifeTimeExpireDay = _SleKeyChainControlKeySendLifeTimeExpireDay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 24),
    _SleKeyChainControlKeySendLifeTimeExpireDay_Type()
)
sleKeyChainControlKeySendLifeTimeExpireDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeExpireDay.setStatus("current")


class _SleKeyChainControlKeySendLifeTimeExpireMonth_Type(Integer32):
    """Custom type sleKeyChainControlKeySendLifeTimeExpireMonth based on Integer32"""
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
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SleKeyChainControlKeySendLifeTimeExpireMonth_Type.__name__ = "Integer32"
_SleKeyChainControlKeySendLifeTimeExpireMonth_Object = MibScalar
sleKeyChainControlKeySendLifeTimeExpireMonth = _SleKeyChainControlKeySendLifeTimeExpireMonth_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 25),
    _SleKeyChainControlKeySendLifeTimeExpireMonth_Type()
)
sleKeyChainControlKeySendLifeTimeExpireMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeExpireMonth.setStatus("current")


class _SleKeyChainControlKeySendLifeTimeExpireYear_Type(Integer32):
    """Custom type sleKeyChainControlKeySendLifeTimeExpireYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1993, 2035),
    )


_SleKeyChainControlKeySendLifeTimeExpireYear_Type.__name__ = "Integer32"
_SleKeyChainControlKeySendLifeTimeExpireYear_Object = MibScalar
sleKeyChainControlKeySendLifeTimeExpireYear = _SleKeyChainControlKeySendLifeTimeExpireYear_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 15, 2, 26),
    _SleKeyChainControlKeySendLifeTimeExpireYear_Type()
)
sleKeyChainControlKeySendLifeTimeExpireYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleKeyChainControlKeySendLifeTimeExpireYear.setStatus("current")

# Managed Objects groups

sleSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 16)
)
sleSecurityGroup.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityRadiusRetransmissions"),
        ("SLE-SECURITY-MIB", "sleSecurityRadiusTimeouts"),
        ("SLE-SECURITY-MIB", "sleSecurityRadiusInterfaceName"),
        ("SLE-SECURITY-MIB", "sleSecurityRadiusInterfaceAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsInterfaceName"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsInterfaceAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsPort"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsAuthType"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsTimeouts"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsPriorityLevel"),
        ("SLE-SECURITY-MIB", "sleSecurityDot1xActivity"),
        ("SLE-SECURITY-MIB", "sleSecurityLoginLimits"),
        ("SLE-SECURITY-MIB", "sleSecurityControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityControlRadiusRetransmissions"),
        ("SLE-SECURITY-MIB", "sleSecurityControlRadiusTimeouts"),
        ("SLE-SECURITY-MIB", "sleSecurityControlRadiusInterfaceName"),
        ("SLE-SECURITY-MIB", "sleSecurityControlRadiusInterfaceAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTacacsInterfaceName"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTacacsInterfaceAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTacacsPort"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTacacsAuthType"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTacacsTimeouts"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTacacsPriorityLevel"),
        ("SLE-SECURITY-MIB", "sleSecurityControlDot1xActivity"),
        ("SLE-SECURITY-MIB", "sleSecurityControlLoginLimits"),
        ("SLE-SECURITY-MIB", "sleAaaSession"),
        ("SLE-SECURITY-MIB", "sleAaaAuthen"),
        ("SLE-SECURITY-MIB", "sleAaaEnable"),
        ("SLE-SECURITY-MIB", "sleAaaPrimarySequence"),
        ("SLE-SECURITY-MIB", "sleAaaControlRequest"),
        ("SLE-SECURITY-MIB", "sleAaaControlStatus"),
        ("SLE-SECURITY-MIB", "sleAaaControlTimer"),
        ("SLE-SECURITY-MIB", "sleAaaControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleAaaControlReqResult"),
        ("SLE-SECURITY-MIB", "sleAaaControlSession"),
        ("SLE-SECURITY-MIB", "sleAaaControlAuthen"),
        ("SLE-SECURITY-MIB", "sleAaaControlEnable"),
        ("SLE-SECURITY-MIB", "sleAaaControlPrimaryFlag"),
        ("SLE-SECURITY-MIB", "sleRadiusServerAddress"),
        ("SLE-SECURITY-MIB", "sleRadiusServerClientKey"),
        ("SLE-SECURITY-MIB", "sleRadiusServerAuthPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerAccPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerMode"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlRequest"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlStatus"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlTimer"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlAddress"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlClientKey"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlAuthPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlAccPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlMode"),
        ("SLE-SECURITY-MIB", "sleTacacsServerAddress"),
        ("SLE-SECURITY-MIB", "sleTacacsServerClientKey"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlRequest"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlStatus"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlTimer"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlReqResult"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlAddress"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlClientKey"),
        ("SLE-SECURITY-MIB", "sleAclName"),
        ("SLE-SECURITY-MIB", "sleAclSrcIpAddr"),
        ("SLE-SECURITY-MIB", "sleAclSrcPrefixLength"),
        ("SLE-SECURITY-MIB", "sleAclDstIpAddr"),
        ("SLE-SECURITY-MIB", "sleAclDstPrefixLength"),
        ("SLE-SECURITY-MIB", "sleAclDscp"),
        ("SLE-SECURITY-MIB", "sleAclProtocolType"),
        ("SLE-SECURITY-MIB", "sleAclTcpFlag"),
        ("SLE-SECURITY-MIB", "sleAclSrcL4Port"),
        ("SLE-SECURITY-MIB", "sleAclDstL4Port"),
        ("SLE-SECURITY-MIB", "sleAclPktLen"),
        ("SLE-SECURITY-MIB", "sleAclValidFlags"),
        ("SLE-SECURITY-MIB", "sleAclMatchFlags"),
        ("SLE-SECURITY-MIB", "sleAclMatchAction"),
        ("SLE-SECURITY-MIB", "sleAclNomatchAction"),
        ("SLE-SECURITY-MIB", "sleAclPriority"),
        ("SLE-SECURITY-MIB", "sleAclControlReqest"),
        ("SLE-SECURITY-MIB", "sleAclControlStatus"),
        ("SLE-SECURITY-MIB", "sleAclControlTimer"),
        ("SLE-SECURITY-MIB", "sleAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleAclControlName"),
        ("SLE-SECURITY-MIB", "sleAclControlSrcIpAddr"),
        ("SLE-SECURITY-MIB", "sleAclControlSrcPrefixLength"),
        ("SLE-SECURITY-MIB", "sleAclControlDstIpAddr"),
        ("SLE-SECURITY-MIB", "sleAclControlDstPrefixLength"),
        ("SLE-SECURITY-MIB", "sleAclControlDscp"),
        ("SLE-SECURITY-MIB", "sleAclControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleAclControlTcpFlag"),
        ("SLE-SECURITY-MIB", "sleAclControlSrcL4Port"),
        ("SLE-SECURITY-MIB", "sleAclControlDstL4Port"),
        ("SLE-SECURITY-MIB", "sleAclControlPktLen"),
        ("SLE-SECURITY-MIB", "sleAclControlValidFlags"),
        ("SLE-SECURITY-MIB", "sleAclControlMatchFlags"),
        ("SLE-SECURITY-MIB", "sleAclControlMatchAction"),
        ("SLE-SECURITY-MIB", "sleAclControlNomatchAction"),
        ("SLE-SECURITY-MIB", "sleAclControlPriority"),
        ("SLE-SECURITY-MIB", "sleDot1xPortIndex"),
        ("SLE-SECURITY-MIB", "sleDot1xPortEnable"),
        ("SLE-SECURITY-MIB", "sleDot1xPortMode"),
        ("SLE-SECURITY-MIB", "sleDot1xPortReauthEnable"),
        ("SLE-SECURITY-MIB", "sleDot1xPortQuietPeriod"),
        ("SLE-SECURITY-MIB", "sleDot1xPortReauthPeriod"),
        ("SLE-SECURITY-MIB", "sleDot1xPortAuthSuccess"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlStatus"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlTimer"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlReqResult"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlIndex"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlEnable"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlMode"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlReauthEnable"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlQuietPeriod"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlReauthPeriod"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsPortIndex"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapolFramesRx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapolFramesTx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapolStartFramesRx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapolLogoffFramesRx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapolRespIdFramesRx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapolRespFramesRx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapolReqIdFramesTx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapolReqFramesTx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsInvalidEapolFramesRx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsEapLengthErrorFramesRx"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsLastEapolFrameVersion"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsLastEapolFrameSource"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlRequest"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlStatus"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlTimer"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlReqResult"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlPortIndex"),
        ("SLE-SECURITY-MIB", "sleArpInspectValidateSrcMac"),
        ("SLE-SECURITY-MIB", "sleArpInspectValidateDstMac"),
        ("SLE-SECURITY-MIB", "sleArpInspectValidateIpAddr"),
        ("SLE-SECURITY-MIB", "sleArpInspectLogBufferSize"),
        ("SLE-SECURITY-MIB", "sleArpInspectLogEntry"),
        ("SLE-SECURITY-MIB", "sleArpInspectLogInterval"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlStatus"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlTimer"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlValidateSrcMac"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlValidateDstMac"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlValidateIpAddr"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlLogBufferSize"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlLogEntry"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlLogInterval"),
        ("SLE-SECURITY-MIB", "sleArpAclIndex"),
        ("SLE-SECURITY-MIB", "sleArpAclName"),
        ("SLE-SECURITY-MIB", "sleArpAclNumEntries"),
        ("SLE-SECURITY-MIB", "sleArpAclControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpAclControlStatus"),
        ("SLE-SECURITY-MIB", "sleArpAclControlTimer"),
        ("SLE-SECURITY-MIB", "sleArpAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpAclControlIndex"),
        ("SLE-SECURITY-MIB", "sleArpAclControlName"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleAclIndex"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleIndex"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleAction"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleType"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleRangeStartIP"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleRangeEndIP"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleIPAddress"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleIPMask"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleMacAddr"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleMacType"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlStatus"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlTimer"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlAclIndex"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlIndex"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlAction"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlType"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlRangeStartIP"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlRangeEndIP"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlIPAddress"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlIPMask"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlMacAddr"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlMacType"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanIndex"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanEnable"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanFilterAcl"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanFwdPktCnt"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanDropPktCnt"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanAclPermits"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanAclDrops"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanSrcMacFailurs"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanDstMacFailurs"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanIpAddrFailurs"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanFilterAclName"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlStatus"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlTimer"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlIndex"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlEnable"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlFilterAcl"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortIndex"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortTrust"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlStatus"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlTimer"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlIndex"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlTrust"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogId"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogReason"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogSamePktCnt"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogOpcode"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogPortNumber"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogVlanId"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogSrcMacAddr"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogSrcIpAddr"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogDstMacAddr"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogDstIpAddr"),
        ("SLE-SECURITY-MIB", "sleArpInspectInvalidLogLastRecvTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseInfoGlobalStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlGlobalStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListStartTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListEndTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListAttackSourceIp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListAttackDestinationIp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListProtocol"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListAttackPktCount"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListAttackBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseGlobalStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlGlobalStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyPortIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlPortIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListPortIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListSourceType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListSourceIpMask"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListSourceMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListSourcePortType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListSourcePortFrom"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListSourcePortTo"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListDestinationType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListDestinationIpMask"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListDestinationMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListDestinationPortType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListDestinationPortFrom"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListDestinationPortTo"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlPortIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceIpMask"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortFrom"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortTo"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationIpMask"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortFrom"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortTo"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListPortIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListAttackBlockType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListStartTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListEndTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListAttackSourceIp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListSourceMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListAttackDestinationIp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListProtocol"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListSourcePort"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListDestinationPort"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListAttackPktCount"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListAttackBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseDosStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseScanStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseCollectInterval"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlDosStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlScanStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlCollectInterval"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyThresholdCount"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlThresholdCount"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListBlockingStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlTimer"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityLoginLockDelayTime"),
        ("SLE-SECURITY-MIB", "sleSecurityControlLoginLockDelayTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyCollectPorts"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlCollectPorts"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListIngressPort"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlIngressPort"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListIgressPort"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlIngressPort"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListBlackListIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityLoginAccountingMode"),
        ("SLE-SECURITY-MIB", "sleSecurityControlLoginAccountingMode"),
        ("SLE-SECURITY-MIB", "sleNDInspectLogBufferSize"),
        ("SLE-SECURITY-MIB", "sleNDInspectLogEntry"),
        ("SLE-SECURITY-MIB", "sleNDInspectLogInterval"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlStatus"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlTimer"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlLogBufferSize"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlLogEntry"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlLogInterval"),
        ("SLE-SECURITY-MIB", "sleNDAclIndex"),
        ("SLE-SECURITY-MIB", "sleNDAclName"),
        ("SLE-SECURITY-MIB", "sleNDAclNumEntries"),
        ("SLE-SECURITY-MIB", "sleNDAclControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDAclControlStatus"),
        ("SLE-SECURITY-MIB", "sleNDAclControlTimer"),
        ("SLE-SECURITY-MIB", "sleNDAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDAclControlIndex"),
        ("SLE-SECURITY-MIB", "sleNDAclControlName"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleAclIndex"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleIndex"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleAction"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleType"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleRangeStartIPv6"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleRangeEndIPv6"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleIPv6Address"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleIPv6Mask"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleMacAddr"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleMacType"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlStatus"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlTimer"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlAclIndex"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlIndex"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlAction"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlType"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlRangeStartIPv6"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlRangeEndIPv6"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlIPv6Address"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlIPv6Mask"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlMacAddr"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlMacType"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanIndex"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanEnable"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanFilterAclIndex"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanFwdPktCnt"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanDropPktCnt"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanAclPermits"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanAclDrops"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanDhcpv6Permits"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanDhcpv6Denys"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanLocalIpv6Denys"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanFilterAclName"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlStatus"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlTimer"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlIndex"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlEnable"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlFilterAclIndex"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortIndex"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortTrust"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlStatus"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlTimer"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlIndex"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlTrust"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogId"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogReason"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogSamePktCnt"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogPortNumber"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogVlanId"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogSenderMacAddr"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogSrcMacAddr"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogSenderIpv6Addr"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogDstIpv6Addr"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogLastRecvTime"),
        ("SLE-SECURITY-MIB", "sleNDInspectInvalidLogNDType"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyIndex"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyName"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyHoplimitMin"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyHoplimitMax"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyManagedFlag"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyOtherFlag"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyRouterPreference"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyMatchACLName"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyMatchPrefixName"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlStatus"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlTimer"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlIndex"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlName"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlHoplimitMin"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlHoplimitMax"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlManagedFlag"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlOtherFlag"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlRouterPreference"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlMatchACLName"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlMatchPrefixName"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanIndex"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanEnable"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanFilterPolicy"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanFilterAclName"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlRequest"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlStatus"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlTimer"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlIndex"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlEnable"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlFilterPolicy"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortIndex"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortTrust"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlStatus"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlTimer"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlIndex"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlTrust"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xAddress"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xAuthPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xTimeout"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xRetransmit"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xClientKey"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlRequest"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlStatus"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlTimer"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlAddress"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlAuthPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlTimeout"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlRetransmit"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDot1xControlClientKey"),
        ("SLE-SECURITY-MIB", "sleKeyChainName"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyId"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyString"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAccepLifeTimeStartTime"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAcceptLifeTimeStartDay"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAcceptLifeTimeStartMonth"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAcceptLifeTimeStartYear"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAcceptLifeTimeExpireType"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAcceptLifeTimeExpireTime"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAcceptLifeTimeExpireDay"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAcceptLifeTimeExpireMonth"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeyAcceptLifeTimeExpireYear"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeStartTime"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeStartDay"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeStartMonth"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeStartYear"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeExpireType"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeExpireTime"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeExpireDay"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeExpireMonth"),
        ("SLE-SECURITY-MIB", "sleKeyChainKeySendLifeTimeExpireYear"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlRequest"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlStatus"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlTimer"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlReqResult"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlName"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyId"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyString"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeStartTime"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeStartDay"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeStartMonth"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeStartYear"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeExpireType"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeExpireTime"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeExpireDay"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeExpireMonth"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeyAcceptLifeTimeExpireYear"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeStartTime"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeStartDay"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeStartMonth"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeStartYear"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeExpireType"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeExpireTime"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeExpireDay"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeExpireMonth"),
        ("SLE-SECURITY-MIB", "sleKeyChainControlKeySendLifeTimeExpireYear"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListIgressPort"),
        ("SLE-SECURITY-MIB", "sleSecurityLoginLockAttemptsCount"),
        ("SLE-SECURITY-MIB", "sleSecurityControlLoginLockAttemptsCount"))
)
if mibBuilder.loadTexts:
    sleSecurityGroup.setStatus("current")


# Notification objects

sleSecurityRadiusProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 3, 1)
)
sleSecurityRadiusProfileChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityRadiusRetransmissions"),
        ("SLE-SECURITY-MIB", "sleSecurityRadiusTimeouts"),
        ("SLE-SECURITY-MIB", "sleSecurityRadiusInterfaceName"),
        ("SLE-SECURITY-MIB", "sleSecurityRadiusInterfaceAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSecurityRadiusProfileChanged.setStatus(
        "current"
    )

sleSecurityTacacsProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 3, 2)
)
sleSecurityTacacsProfileChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityTacacsInterfaceName"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsInterfaceAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsPort"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsAuthType"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsTimeouts"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsPriorityLevel"),
        ("SLE-SECURITY-MIB", "sleSecurityControlStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSecurityTacacsProfileChanged.setStatus(
        "current"
    )

sleSecurityDot1xActivityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 3, 3)
)
sleSecurityDot1xActivityChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityDot1xActivity"),
        ("SLE-SECURITY-MIB", "sleSecurityControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSecurityDot1xActivityChanged.setStatus(
        "current"
    )

sleSecurityBaseLoginLimitsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 3, 4)
)
sleSecurityBaseLoginLimitsChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityControlLoginLimits"))
)
if mibBuilder.loadTexts:
    sleSecurityBaseLoginLimitsChanged.setStatus(
        "current"
    )

sleSecurityBaseLoginLockConfChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 3, 5)
)
sleSecurityBaseLoginLockConfChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityControlLoginLockAttemptsCount"),
        ("SLE-SECURITY-MIB", "sleSecurityControlLoginLockDelayTime"))
)
if mibBuilder.loadTexts:
    sleSecurityBaseLoginLockConfChanged.setStatus(
        "current"
    )

sleSecurityBaseLoginLockConfDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 3, 6)
)
sleSecurityBaseLoginLockConfDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSecurityBaseLoginLockConfDestroyed.setStatus(
        "current"
    )

sleSecurityLoginAccountingModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 1, 3, 7)
)
sleSecurityLoginAccountingModeChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityControlLoginAccountingMode"))
)
if mibBuilder.loadTexts:
    sleSecurityLoginAccountingModeChanged.setStatus(
        "current"
    )

sleAaaProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 2, 3, 1)
)
sleAaaProfileChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleAaaControlRequest"),
        ("SLE-SECURITY-MIB", "sleAaaControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleAaaControlReqResult"),
        ("SLE-SECURITY-MIB", "sleAaaEnable"),
        ("SLE-SECURITY-MIB", "sleAaaPrimarySequence"))
)
if mibBuilder.loadTexts:
    sleAaaProfileChanged.setStatus(
        "current"
    )

sleRadiusServerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 3, 1)
)
sleRadiusServerCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleRadiusServerControlRequest"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRadiusServerClientKey"),
        ("SLE-SECURITY-MIB", "sleRadiusServerAccPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerAuthPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerMode"))
)
if mibBuilder.loadTexts:
    sleRadiusServerCreated.setStatus(
        "current"
    )

sleRadiusServerDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 3, 2)
)
sleRadiusServerDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleRadiusServerControlRequest"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlAddress"))
)
if mibBuilder.loadTexts:
    sleRadiusServerDestroyed.setStatus(
        "current"
    )

sleRadiusServerProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 3, 3, 3)
)
sleRadiusServerProfileChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleRadiusServerControlRequest"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRadiusServerControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRadiusServerClientKey"),
        ("SLE-SECURITY-MIB", "sleRadiusServerAuthPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerAccPort"),
        ("SLE-SECURITY-MIB", "sleRadiusServerMode"))
)
if mibBuilder.loadTexts:
    sleRadiusServerProfileChanged.setStatus(
        "current"
    )

sleTacacsServerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 3, 1)
)
sleTacacsServerCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleTacacsServerControlRequest"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlReqResult"),
        ("SLE-SECURITY-MIB", "sleTacacsServerClientKey"))
)
if mibBuilder.loadTexts:
    sleTacacsServerCreated.setStatus(
        "current"
    )

sleTacacsServerDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 3, 2)
)
sleTacacsServerDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleTacacsServerControlRequest"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlReqResult"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlAddress"))
)
if mibBuilder.loadTexts:
    sleTacacsServerDestroyed.setStatus(
        "current"
    )

sleTacacsServerClientKeyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 4, 3, 3)
)
sleTacacsServerClientKeyChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleTacacsServerControlRequest"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleTacacsServerControlReqResult"),
        ("SLE-SECURITY-MIB", "sleTacacsServerClientKey"))
)
if mibBuilder.loadTexts:
    sleTacacsServerClientKeyChanged.setStatus(
        "current"
    )

sleAclCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 3, 1)
)
sleAclCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleAclControlReqest"),
        ("SLE-SECURITY-MIB", "sleAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleAclSrcIpAddr"),
        ("SLE-SECURITY-MIB", "sleAclSrcPrefixLength"),
        ("SLE-SECURITY-MIB", "sleAclDstIpAddr"),
        ("SLE-SECURITY-MIB", "sleAclDstPrefixLength"),
        ("SLE-SECURITY-MIB", "sleAclDscp"),
        ("SLE-SECURITY-MIB", "sleAclProtocolType"),
        ("SLE-SECURITY-MIB", "sleAclTcpFlag"),
        ("SLE-SECURITY-MIB", "sleAclSrcL4Port"),
        ("SLE-SECURITY-MIB", "sleAclDstL4Port"),
        ("SLE-SECURITY-MIB", "sleAclPktLen"),
        ("SLE-SECURITY-MIB", "sleAclValidFlags"),
        ("SLE-SECURITY-MIB", "sleAclMatchFlags"),
        ("SLE-SECURITY-MIB", "sleAclMatchAction"),
        ("SLE-SECURITY-MIB", "sleAclNomatchAction"),
        ("SLE-SECURITY-MIB", "sleAclPriority"))
)
if mibBuilder.loadTexts:
    sleAclCreated.setStatus(
        "current"
    )

sleAclDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 3, 2)
)
sleAclDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleAclControlReqest"),
        ("SLE-SECURITY-MIB", "sleAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleAclControlName"))
)
if mibBuilder.loadTexts:
    sleAclDestroyed.setStatus(
        "current"
    )

sleAclClassifierProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 3, 3)
)
sleAclClassifierProfileChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleAclControlReqest"),
        ("SLE-SECURITY-MIB", "sleAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleAclSrcIpAddr"),
        ("SLE-SECURITY-MIB", "sleAclSrcPrefixLength"),
        ("SLE-SECURITY-MIB", "sleAclDstIpAddr"),
        ("SLE-SECURITY-MIB", "sleAclDstPrefixLength"),
        ("SLE-SECURITY-MIB", "sleAclDscp"),
        ("SLE-SECURITY-MIB", "sleAclProtocolType"),
        ("SLE-SECURITY-MIB", "sleAclTcpFlag"),
        ("SLE-SECURITY-MIB", "sleAclSrcL4Port"),
        ("SLE-SECURITY-MIB", "sleAclDstL4Port"),
        ("SLE-SECURITY-MIB", "sleAclPktLen"),
        ("SLE-SECURITY-MIB", "sleAclValidFlags"),
        ("SLE-SECURITY-MIB", "sleAclMatchFlags"))
)
if mibBuilder.loadTexts:
    sleAclClassifierProfileChanged.setStatus(
        "current"
    )

sleAclMatchActionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 3, 4)
)
sleAclMatchActionChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleAclControlReqest"),
        ("SLE-SECURITY-MIB", "sleAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleAclMatchAction"))
)
if mibBuilder.loadTexts:
    sleAclMatchActionChanged.setStatus(
        "current"
    )

sleAclNomatchActionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 5, 3, 5)
)
sleAclNomatchActionChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleAclControlReqest"),
        ("SLE-SECURITY-MIB", "sleAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleAclNomatchAction"))
)
if mibBuilder.loadTexts:
    sleAclNomatchActionChanged.setStatus(
        "current"
    )

sleDot1xPortProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 3, 1)
)
sleDot1xPortProfileChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleDot1xPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlReqResult"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleDot1xPortEnable"),
        ("SLE-SECURITY-MIB", "sleDot1xPortMode"),
        ("SLE-SECURITY-MIB", "sleDot1xPortReauthEnable"),
        ("SLE-SECURITY-MIB", "sleDot1xPortQuietPeriod"),
        ("SLE-SECURITY-MIB", "sleDot1xPortReauthPeriod"))
)
if mibBuilder.loadTexts:
    sleDot1xPortProfileChanged.setStatus(
        "current"
    )

sleDot1xPortAuthSuccessChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 6, 3, 2)
)
sleDot1xPortAuthSuccessChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleDot1xPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleDot1xPortControlReqResult"),
        ("SLE-SECURITY-MIB", "sleDot1xPortAuthSuccess"))
)
if mibBuilder.loadTexts:
    sleDot1xPortAuthSuccessChanged.setStatus(
        "current"
    )

sleDot1xStatisticsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 7, 3, 1)
)
sleDot1xStatisticsCleared.setObjects(
      *(("SLE-SECURITY-MIB", "sleDot1xStatsControlRequest"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlReqResult"),
        ("SLE-SECURITY-MIB", "sleDot1xStatsControlPortIndex"))
)
if mibBuilder.loadTexts:
    sleDot1xStatisticsCleared.setStatus(
        "current"
    )

sleArpInspectValidateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 3, 1)
)
sleArpInspectValidateChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpInspectControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlValidateSrcMac"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlValidateDstMac"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlValidateIpAddr"))
)
if mibBuilder.loadTexts:
    sleArpInspectValidateChanged.setStatus(
        "current"
    )

sleArpInspectLogBufferSizeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 3, 2)
)
sleArpInspectLogBufferSizeChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpInspectControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlLogBufferSize"))
)
if mibBuilder.loadTexts:
    sleArpInspectLogBufferSizeChanged.setStatus(
        "current"
    )

sleArpInspectLogRateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 1, 3, 3)
)
sleArpInspectLogRateChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpInspectControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlLogEntry"),
        ("SLE-SECURITY-MIB", "sleArpInspectControlLogInterval"))
)
if mibBuilder.loadTexts:
    sleArpInspectLogRateChanged.setStatus(
        "current"
    )

sleArpAclCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 3, 1)
)
sleArpAclCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpAclControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpAclName"))
)
if mibBuilder.loadTexts:
    sleArpAclCreated.setStatus(
        "current"
    )

sleArpAclDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 2, 3, 2)
)
sleArpAclDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpAclControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpAclControlIndex"))
)
if mibBuilder.loadTexts:
    sleArpAclDestroyed.setStatus(
        "current"
    )

sleArpAclRuleCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 3, 1)
)
sleArpAclRuleCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpAclRuleControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleAction"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleType"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleRangeStartIP"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleRangeEndIP"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleIPAddress"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleIPMask"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleMacAddr"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleMacType"))
)
if mibBuilder.loadTexts:
    sleArpAclRuleCreated.setStatus(
        "current"
    )

sleArpAclRuleDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 3, 3, 2)
)
sleArpAclRuleDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpAclRuleControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlAclIndex"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleControlIndex"))
)
if mibBuilder.loadTexts:
    sleArpAclRuleDestroyed.setStatus(
        "current"
    )

sleArpInspectVlanChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 4, 3, 1)
)
sleArpInspectVlanChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpInspectVlanControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanControlReqResult"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanEnable"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanFilterAcl"))
)
if mibBuilder.loadTexts:
    sleArpInspectVlanChanged.setStatus(
        "current"
    )

sleArpInspectPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 8, 5, 3, 1)
)
sleArpInspectPortChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpInspectPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlTrust"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortControlReqResult"))
)
if mibBuilder.loadTexts:
    sleArpInspectPortChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicBaseGlobalStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 3, 1)
)
sleSecurityAttackBasicBaseGlobalStatusChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlGlobalStatus"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseGlobalStatusChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicBaseDosStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 3, 2)
)
sleSecurityAttackBasicBaseDosStatusChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlDosStatus"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseDosStatusChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicBaseScanStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 3, 3)
)
sleSecurityAttackBasicBaseScanStatusChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlScanStatus"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseScanStatusChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicBaseCollectIntervalChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 3, 4)
)
sleSecurityAttackBasicBaseCollectIntervalChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlCollectInterval"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseCollectIntervalChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicBaseAllConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 1, 3, 5)
)
sleSecurityAttackBasicBaseAllConfigChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlGlobalStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlDosStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlScanStatus"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseControlCollectInterval"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBaseAllConfigChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicPolicyBlockTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 3, 1)
)
sleSecurityAttackBasicPolicyBlockTimeChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlBlockTime"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyBlockTimeChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicPolicyThresholdCountChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 3, 2)
)
sleSecurityAttackBasicPolicyThresholdCountChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlThresholdCount"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyThresholdCountChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicPolicyCollectPortsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 3, 3)
)
sleSecurityAttackBasicPolicyCollectPortsChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlCollectPorts"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicPolicyCollectPortsChanged.setStatus(
        "current"
    )

setSecurityAttackBasicPolicyAllConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 2, 3, 4)
)
setSecurityAttackBasicPolicyAllConfigChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlBlockTime"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlThresholdCount"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyControlCollectPorts"))
)
if mibBuilder.loadTexts:
    setSecurityAttackBasicPolicyAllConfigChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicExceptListCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 3, 1)
)
sleSecurityAttackBasicExceptListCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlIngressPort"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListCreated.setStatus(
        "current"
    )

sleSecurityAttackBasicExceptListChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 3, 2)
)
sleSecurityAttackBasicExceptListChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlIngressPort"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicExceptListDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 3, 3, 3)
)
sleSecurityAttackBasicExceptListDeleted.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListControlRuleIndex"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicExceptListDeleted.setStatus(
        "current"
    )

sleSecurityAttackBasicBlackListCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 3, 1)
)
sleSecurityAttackBasicBlackListCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlIngressPort"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListCreated.setStatus(
        "current"
    )

sleSecurityAttackBasicBlackListDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 4, 3, 2)
)
sleSecurityAttackBasicBlackListDeleted.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListControlRuleIndex"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlackListDeleted.setStatus(
        "current"
    )

sleSecurityAttackBasicBlockedListBlockTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 3, 1)
)
sleSecurityAttackBasicBlockedListBlockTimeChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlBlockTime"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListBlockTimeChanged.setStatus(
        "current"
    )

sleSecurityAttackBasicBlockedListDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 1, 5, 3, 2)
)
sleSecurityAttackBasicBlockedListDeleted.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListControlRuleIndex"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackBasicBlockedListDeleted.setStatus(
        "current"
    )

sleSecurityAttackExpansionBaseGlobalStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 1, 3, 1)
)
sleSecurityAttackExpansionBaseGlobalStatusChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseControlGlobalStatus"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBaseGlobalStatusChanged.setStatus(
        "current"
    )

sleSecurityAttackExpansionPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 2, 3, 1)
)
sleSecurityAttackExpansionPolicyChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlPortIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlAttackType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyControlBlockTime"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionPolicyChanged.setStatus(
        "current"
    )

sleSecurityAttackExpansionExceptListCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 3, 1)
)
sleSecurityAttackExpansionExceptListCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlPortIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceIpMask"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortFrom"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortTo"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationIpMask"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortFrom"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortTo"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListCreated.setStatus(
        "current"
    )

sleSecurityAttackExpansionExceptListChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 3, 2)
)
sleSecurityAttackExpansionExceptListChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlProtocolType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceIpMask"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourceMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortFrom"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlSourcePortTo"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationIpAddress"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationIpMask"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationMac"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortType"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortFrom"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlDestinationPortTo"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListChanged.setStatus(
        "current"
    )

sleSecurityAttackExpansionExceptListDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 3, 3, 3)
)
sleSecurityAttackExpansionExceptListDeleted.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListControlRuleIndex"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionExceptListDeleted.setStatus(
        "current"
    )

sleSecurityAttackExpansionBlockedListBlockTimeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 9, 2, 4, 3, 1)
)
sleSecurityAttackExpansionBlockedListBlockTimeChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlRequest"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlReqResult"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlRuleIndex"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListControlBlockTime"))
)
if mibBuilder.loadTexts:
    sleSecurityAttackExpansionBlockedListBlockTimeChanged.setStatus(
        "current"
    )

sleNDInspectLogBufferSizeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 3, 1)
)
sleNDInspectLogBufferSizeChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDInspectControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlLogBufferSize"))
)
if mibBuilder.loadTexts:
    sleNDInspectLogBufferSizeChanged.setStatus(
        "current"
    )

sleNDInspectLogRateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 1, 3, 2)
)
sleNDInspectLogRateChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDInspectControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlLogEntry"),
        ("SLE-SECURITY-MIB", "sleNDInspectControlLogInterval"))
)
if mibBuilder.loadTexts:
    sleNDInspectLogRateChanged.setStatus(
        "current"
    )

sleNDAclCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 3, 1)
)
sleNDAclCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDAclControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDAclControlName"))
)
if mibBuilder.loadTexts:
    sleNDAclCreated.setStatus(
        "current"
    )

sleNDAclDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 2, 3, 2)
)
sleNDAclDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDAclControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDAclControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDAclControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDAclControlIndex"))
)
if mibBuilder.loadTexts:
    sleNDAclDestroyed.setStatus(
        "current"
    )

sleNDAclRuleCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 3, 1)
)
sleNDAclRuleCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDAclRuleControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleAction"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleType"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleRangeStartIPv6"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleRangeEndIPv6"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleIPv6Address"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleIPv6Mask"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleMacAddr"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleMacType"))
)
if mibBuilder.loadTexts:
    sleNDAclRuleCreated.setStatus(
        "current"
    )

sleNDAclRuleDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 3, 3, 2)
)
sleNDAclRuleDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDAclRuleControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlAclIndex"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleControlIndex"))
)
if mibBuilder.loadTexts:
    sleNDAclRuleDestroyed.setStatus(
        "current"
    )

sleNDInspectVlanChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 3, 1)
)
sleNDInspectVlanChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDInspectVlanControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanEnable"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanFilterAclIndex"))
)
if mibBuilder.loadTexts:
    sleNDInspectVlanChanged.setStatus(
        "current"
    )

sleNDInspectVlanStatsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 4, 3, 2)
)
sleNDInspectVlanStatsCleared.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDInspectVlanControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanControlIndex"))
)
if mibBuilder.loadTexts:
    sleNDInspectVlanStatsCleared.setStatus(
        "current"
    )

sleNDInspectPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 12, 5, 3, 1)
)
sleNDInspectPortChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleNDInspectPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlReqResult"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortControlTrust"))
)
if mibBuilder.loadTexts:
    sleNDInspectPortChanged.setStatus(
        "current"
    )

sleRAGuardPolicyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 3, 1)
)
sleRAGuardPolicyCreated.setObjects(
      *(("SLE-SECURITY-MIB", "sleRAGuardPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlName"))
)
if mibBuilder.loadTexts:
    sleRAGuardPolicyCreated.setStatus(
        "current"
    )

sleRAGuardPolicyDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 3, 2)
)
sleRAGuardPolicyDestroyed.setObjects(
      *(("SLE-SECURITY-MIB", "sleRAGuardPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlIndex"))
)
if mibBuilder.loadTexts:
    sleRAGuardPolicyDestroyed.setStatus(
        "current"
    )

sleRAGuardPolicyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 1, 3, 3)
)
sleRAGuardPolicyChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleRAGuardPolicyControlRequest"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlName"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlHoplimitMin"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlHoplimitMax"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlManagedFlag"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlOtherFlag"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlRouterPreference"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlMatchACLName"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyControlMatchPrefixName"))
)
if mibBuilder.loadTexts:
    sleRAGuardPolicyChanged.setStatus(
        "current"
    )

sleRAGuardVlanChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 2, 3, 1)
)
sleRAGuardVlanChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleRAGuardVlanControlRequest"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlEnable"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanControlFilterPolicy"))
)
if mibBuilder.loadTexts:
    sleRAGuardVlanChanged.setStatus(
        "current"
    )

sleRAGuardPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 13, 3, 3, 1)
)
sleRAGuardPortChanged.setObjects(
      *(("SLE-SECURITY-MIB", "sleRAGuardPortControlRequest"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlTimeStamp"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlReqResult"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortControlTrust"))
)
if mibBuilder.loadTexts:
    sleRAGuardPortChanged.setStatus(
        "current"
    )


# Notifications groups

sleSecurityNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 7, 17)
)
sleSecurityNotificationGroup.setObjects(
      *(("SLE-SECURITY-MIB", "sleArpAclCreated"),
        ("SLE-SECURITY-MIB", "sleArpAclDestroyed"),
        ("SLE-SECURITY-MIB", "sleArpInspectVlanChanged"),
        ("SLE-SECURITY-MIB", "sleArpInspectLogBufferSizeChanged"),
        ("SLE-SECURITY-MIB", "sleArpInspectLogRateChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityBaseLoginLimitsChanged"),
        ("SLE-SECURITY-MIB", "sleArpInspectPortChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityRadiusProfileChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityTacacsProfileChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityDot1xActivityChanged"),
        ("SLE-SECURITY-MIB", "sleAaaProfileChanged"),
        ("SLE-SECURITY-MIB", "sleRadiusServerCreated"),
        ("SLE-SECURITY-MIB", "sleRadiusServerDestroyed"),
        ("SLE-SECURITY-MIB", "sleRadiusServerProfileChanged"),
        ("SLE-SECURITY-MIB", "sleTacacsServerCreated"),
        ("SLE-SECURITY-MIB", "sleTacacsServerDestroyed"),
        ("SLE-SECURITY-MIB", "sleTacacsServerClientKeyChanged"),
        ("SLE-SECURITY-MIB", "sleAclCreated"),
        ("SLE-SECURITY-MIB", "sleAclDestroyed"),
        ("SLE-SECURITY-MIB", "sleAclClassifierProfileChanged"),
        ("SLE-SECURITY-MIB", "sleAclMatchActionChanged"),
        ("SLE-SECURITY-MIB", "sleAclNomatchActionChanged"),
        ("SLE-SECURITY-MIB", "sleDot1xPortProfileChanged"),
        ("SLE-SECURITY-MIB", "sleDot1xPortAuthSuccessChanged"),
        ("SLE-SECURITY-MIB", "sleDot1xStatisticsCleared"),
        ("SLE-SECURITY-MIB", "sleArpInspectValidateChanged"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleCreated"),
        ("SLE-SECURITY-MIB", "sleArpAclRuleDestroyed"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseGlobalStatusChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListCreated"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicExceptListDeleted"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBaseGlobalStatusChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionPolicyChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListCreated"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionExceptListDeleted"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackExpansionBlockedListBlockTimeChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseDosStatusChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseScanStatusChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseCollectIntervalChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyThresholdCountChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListDeleted"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListBlockTimeChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyBlockTimeChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicPolicyCollectPortsChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityBaseLoginLockConfChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityBaseLoginLockConfDestroyed"),
        ("SLE-SECURITY-MIB", "sleSecurityLoginAccountingModeChanged"),
        ("SLE-SECURITY-MIB", "sleNDInspectLogBufferSizeChanged"),
        ("SLE-SECURITY-MIB", "sleNDInspectLogRateChanged"),
        ("SLE-SECURITY-MIB", "sleNDAclCreated"),
        ("SLE-SECURITY-MIB", "sleNDAclDestroyed"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleCreated"),
        ("SLE-SECURITY-MIB", "sleNDAclRuleDestroyed"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanChanged"),
        ("SLE-SECURITY-MIB", "sleNDInspectVlanStatsCleared"),
        ("SLE-SECURITY-MIB", "sleNDInspectPortChanged"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyCreated"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyDestroyed"),
        ("SLE-SECURITY-MIB", "sleRAGuardPolicyChanged"),
        ("SLE-SECURITY-MIB", "sleRAGuardVlanChanged"),
        ("SLE-SECURITY-MIB", "sleRAGuardPortChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlockedListDeleted"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBaseAllConfigChanged"),
        ("SLE-SECURITY-MIB", "setSecurityAttackBasicPolicyAllConfigChanged"),
        ("SLE-SECURITY-MIB", "sleSecurityAttackBasicBlackListCreated"))
)
if mibBuilder.loadTexts:
    sleSecurityNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-SECURITY-MIB",
    **{"sleSecurity": sleSecurity,
       "sleSecurityBase": sleSecurityBase,
       "sleSecurityBaseInfo": sleSecurityBaseInfo,
       "sleSecurityRadiusRetransmissions": sleSecurityRadiusRetransmissions,
       "sleSecurityRadiusTimeouts": sleSecurityRadiusTimeouts,
       "sleSecurityRadiusInterfaceName": sleSecurityRadiusInterfaceName,
       "sleSecurityRadiusInterfaceAddress": sleSecurityRadiusInterfaceAddress,
       "sleSecurityTacacsInterfaceName": sleSecurityTacacsInterfaceName,
       "sleSecurityTacacsInterfaceAddress": sleSecurityTacacsInterfaceAddress,
       "sleSecurityTacacsPort": sleSecurityTacacsPort,
       "sleSecurityTacacsAuthType": sleSecurityTacacsAuthType,
       "sleSecurityTacacsTimeouts": sleSecurityTacacsTimeouts,
       "sleSecurityTacacsPriorityLevel": sleSecurityTacacsPriorityLevel,
       "sleSecurityDot1xActivity": sleSecurityDot1xActivity,
       "sleSecurityLoginLimits": sleSecurityLoginLimits,
       "sleSecurityLoginLockAttemptsCount": sleSecurityLoginLockAttemptsCount,
       "sleSecurityLoginLockDelayTime": sleSecurityLoginLockDelayTime,
       "sleSecurityLoginAccountingMode": sleSecurityLoginAccountingMode,
       "sleSecurityBaseControl": sleSecurityBaseControl,
       "sleSecurityControlRequest": sleSecurityControlRequest,
       "sleSecurityControlStatus": sleSecurityControlStatus,
       "sleSecurityControlTimer": sleSecurityControlTimer,
       "sleSecurityControlTimeStamp": sleSecurityControlTimeStamp,
       "sleSecurityControlReqResult": sleSecurityControlReqResult,
       "sleSecurityControlRadiusRetransmissions": sleSecurityControlRadiusRetransmissions,
       "sleSecurityControlRadiusTimeouts": sleSecurityControlRadiusTimeouts,
       "sleSecurityControlRadiusInterfaceName": sleSecurityControlRadiusInterfaceName,
       "sleSecurityControlRadiusInterfaceAddress": sleSecurityControlRadiusInterfaceAddress,
       "sleSecurityControlTacacsInterfaceName": sleSecurityControlTacacsInterfaceName,
       "sleSecurityControlTacacsInterfaceAddress": sleSecurityControlTacacsInterfaceAddress,
       "sleSecurityControlTacacsPort": sleSecurityControlTacacsPort,
       "sleSecurityControlTacacsAuthType": sleSecurityControlTacacsAuthType,
       "sleSecurityControlTacacsTimeouts": sleSecurityControlTacacsTimeouts,
       "sleSecurityControlTacacsPriorityLevel": sleSecurityControlTacacsPriorityLevel,
       "sleSecurityControlDot1xActivity": sleSecurityControlDot1xActivity,
       "sleSecurityControlLoginLimits": sleSecurityControlLoginLimits,
       "sleSecurityControlLoginLockAttemptsCount": sleSecurityControlLoginLockAttemptsCount,
       "sleSecurityControlLoginLockDelayTime": sleSecurityControlLoginLockDelayTime,
       "sleSecurityControlLoginAccountingMode": sleSecurityControlLoginAccountingMode,
       "sleSecurityBaseNotification": sleSecurityBaseNotification,
       "sleSecurityRadiusProfileChanged": sleSecurityRadiusProfileChanged,
       "sleSecurityTacacsProfileChanged": sleSecurityTacacsProfileChanged,
       "sleSecurityDot1xActivityChanged": sleSecurityDot1xActivityChanged,
       "sleSecurityBaseLoginLimitsChanged": sleSecurityBaseLoginLimitsChanged,
       "sleSecurityBaseLoginLockConfChanged": sleSecurityBaseLoginLockConfChanged,
       "sleSecurityBaseLoginLockConfDestroyed": sleSecurityBaseLoginLockConfDestroyed,
       "sleSecurityLoginAccountingModeChanged": sleSecurityLoginAccountingModeChanged,
       "sleAAA": sleAAA,
       "sleAaaTable": sleAaaTable,
       "sleAaaEntry": sleAaaEntry,
       "sleAaaSession": sleAaaSession,
       "sleAaaAuthen": sleAaaAuthen,
       "sleAaaEnable": sleAaaEnable,
       "sleAaaPrimarySequence": sleAaaPrimarySequence,
       "sleAaaControl": sleAaaControl,
       "sleAaaControlRequest": sleAaaControlRequest,
       "sleAaaControlStatus": sleAaaControlStatus,
       "sleAaaControlTimer": sleAaaControlTimer,
       "sleAaaControlTimeStamp": sleAaaControlTimeStamp,
       "sleAaaControlReqResult": sleAaaControlReqResult,
       "sleAaaControlSession": sleAaaControlSession,
       "sleAaaControlAuthen": sleAaaControlAuthen,
       "sleAaaControlEnable": sleAaaControlEnable,
       "sleAaaControlPrimaryFlag": sleAaaControlPrimaryFlag,
       "sleAaaNotification": sleAaaNotification,
       "sleAaaProfileChanged": sleAaaProfileChanged,
       "sleRadiusServer": sleRadiusServer,
       "sleRadiusServerTable": sleRadiusServerTable,
       "sleRadiusServerEntry": sleRadiusServerEntry,
       "sleRadiusServerAddress": sleRadiusServerAddress,
       "sleRadiusServerClientKey": sleRadiusServerClientKey,
       "sleRadiusServerAuthPort": sleRadiusServerAuthPort,
       "sleRadiusServerAccPort": sleRadiusServerAccPort,
       "sleRadiusServerMode": sleRadiusServerMode,
       "sleRadiusServerControl": sleRadiusServerControl,
       "sleRadiusServerControlRequest": sleRadiusServerControlRequest,
       "sleRadiusServerControlStatus": sleRadiusServerControlStatus,
       "sleRadiusServerControlTimer": sleRadiusServerControlTimer,
       "sleRadiusServerControlTimeStamp": sleRadiusServerControlTimeStamp,
       "sleRadiusServerControlReqResult": sleRadiusServerControlReqResult,
       "sleRadiusServerControlAddress": sleRadiusServerControlAddress,
       "sleRadiusServerControlClientKey": sleRadiusServerControlClientKey,
       "sleRadiusServerControlAuthPort": sleRadiusServerControlAuthPort,
       "sleRadiusServerControlAccPort": sleRadiusServerControlAccPort,
       "sleRadiusServerControlMode": sleRadiusServerControlMode,
       "sleRadiusServerNotification": sleRadiusServerNotification,
       "sleRadiusServerCreated": sleRadiusServerCreated,
       "sleRadiusServerDestroyed": sleRadiusServerDestroyed,
       "sleRadiusServerProfileChanged": sleRadiusServerProfileChanged,
       "sleTacacsServer": sleTacacsServer,
       "sleTacacsServerTable": sleTacacsServerTable,
       "sleTacacsServerEntry": sleTacacsServerEntry,
       "sleTacacsServerAddress": sleTacacsServerAddress,
       "sleTacacsServerClientKey": sleTacacsServerClientKey,
       "sleTacacsServerControl": sleTacacsServerControl,
       "sleTacacsServerControlRequest": sleTacacsServerControlRequest,
       "sleTacacsServerControlStatus": sleTacacsServerControlStatus,
       "sleTacacsServerControlTimer": sleTacacsServerControlTimer,
       "sleTacacsServerControlTimeStamp": sleTacacsServerControlTimeStamp,
       "sleTacacsServerControlReqResult": sleTacacsServerControlReqResult,
       "sleTacacsServerControlAddress": sleTacacsServerControlAddress,
       "sleTacacsServerControlClientKey": sleTacacsServerControlClientKey,
       "sleTacacsServerNotification": sleTacacsServerNotification,
       "sleTacacsServerCreated": sleTacacsServerCreated,
       "sleTacacsServerDestroyed": sleTacacsServerDestroyed,
       "sleTacacsServerClientKeyChanged": sleTacacsServerClientKeyChanged,
       "sleAcl": sleAcl,
       "sleAclTable": sleAclTable,
       "sleAclEntry": sleAclEntry,
       "sleAclName": sleAclName,
       "sleAclSrcIpAddr": sleAclSrcIpAddr,
       "sleAclSrcPrefixLength": sleAclSrcPrefixLength,
       "sleAclDstIpAddr": sleAclDstIpAddr,
       "sleAclDstPrefixLength": sleAclDstPrefixLength,
       "sleAclDscp": sleAclDscp,
       "sleAclProtocolType": sleAclProtocolType,
       "sleAclTcpFlag": sleAclTcpFlag,
       "sleAclSrcL4Port": sleAclSrcL4Port,
       "sleAclDstL4Port": sleAclDstL4Port,
       "sleAclPktLen": sleAclPktLen,
       "sleAclValidFlags": sleAclValidFlags,
       "sleAclMatchFlags": sleAclMatchFlags,
       "sleAclMatchAction": sleAclMatchAction,
       "sleAclNomatchAction": sleAclNomatchAction,
       "sleAclPriority": sleAclPriority,
       "sleAclControl": sleAclControl,
       "sleAclControlReqest": sleAclControlReqest,
       "sleAclControlStatus": sleAclControlStatus,
       "sleAclControlTimer": sleAclControlTimer,
       "sleAclControlTimeStamp": sleAclControlTimeStamp,
       "sleAclControlReqResult": sleAclControlReqResult,
       "sleAclControlName": sleAclControlName,
       "sleAclControlSrcIpAddr": sleAclControlSrcIpAddr,
       "sleAclControlSrcPrefixLength": sleAclControlSrcPrefixLength,
       "sleAclControlDstIpAddr": sleAclControlDstIpAddr,
       "sleAclControlDstPrefixLength": sleAclControlDstPrefixLength,
       "sleAclControlDscp": sleAclControlDscp,
       "sleAclControlProtocolType": sleAclControlProtocolType,
       "sleAclControlTcpFlag": sleAclControlTcpFlag,
       "sleAclControlSrcL4Port": sleAclControlSrcL4Port,
       "sleAclControlDstL4Port": sleAclControlDstL4Port,
       "sleAclControlPktLen": sleAclControlPktLen,
       "sleAclControlValidFlags": sleAclControlValidFlags,
       "sleAclControlMatchFlags": sleAclControlMatchFlags,
       "sleAclControlMatchAction": sleAclControlMatchAction,
       "sleAclControlNomatchAction": sleAclControlNomatchAction,
       "sleAclControlPriority": sleAclControlPriority,
       "sleAclNotification": sleAclNotification,
       "sleAclCreated": sleAclCreated,
       "sleAclDestroyed": sleAclDestroyed,
       "sleAclClassifierProfileChanged": sleAclClassifierProfileChanged,
       "sleAclMatchActionChanged": sleAclMatchActionChanged,
       "sleAclNomatchActionChanged": sleAclNomatchActionChanged,
       "sleDot1xPort": sleDot1xPort,
       "sleDot1xPortTable": sleDot1xPortTable,
       "sleDot1xPortEntry": sleDot1xPortEntry,
       "sleDot1xPortIndex": sleDot1xPortIndex,
       "sleDot1xPortEnable": sleDot1xPortEnable,
       "sleDot1xPortMode": sleDot1xPortMode,
       "sleDot1xPortReauthEnable": sleDot1xPortReauthEnable,
       "sleDot1xPortQuietPeriod": sleDot1xPortQuietPeriod,
       "sleDot1xPortReauthPeriod": sleDot1xPortReauthPeriod,
       "sleDot1xPortAuthSuccess": sleDot1xPortAuthSuccess,
       "sleDot1xPortControl": sleDot1xPortControl,
       "sleDot1xPortControlRequest": sleDot1xPortControlRequest,
       "sleDot1xPortControlStatus": sleDot1xPortControlStatus,
       "sleDot1xPortControlTimer": sleDot1xPortControlTimer,
       "sleDot1xPortControlTimeStamp": sleDot1xPortControlTimeStamp,
       "sleDot1xPortControlReqResult": sleDot1xPortControlReqResult,
       "sleDot1xPortControlIndex": sleDot1xPortControlIndex,
       "sleDot1xPortControlEnable": sleDot1xPortControlEnable,
       "sleDot1xPortControlMode": sleDot1xPortControlMode,
       "sleDot1xPortControlReauthEnable": sleDot1xPortControlReauthEnable,
       "sleDot1xPortControlQuietPeriod": sleDot1xPortControlQuietPeriod,
       "sleDot1xPortControlReauthPeriod": sleDot1xPortControlReauthPeriod,
       "sleDot1xPortNotification": sleDot1xPortNotification,
       "sleDot1xPortProfileChanged": sleDot1xPortProfileChanged,
       "sleDot1xPortAuthSuccessChanged": sleDot1xPortAuthSuccessChanged,
       "sleDot1xStatistics": sleDot1xStatistics,
       "sleDot1xStatisticsTable": sleDot1xStatisticsTable,
       "sleDot1xStatisticsEntry": sleDot1xStatisticsEntry,
       "sleDot1xStatsPortIndex": sleDot1xStatsPortIndex,
       "sleDot1xStatsEapolFramesRx": sleDot1xStatsEapolFramesRx,
       "sleDot1xStatsEapolFramesTx": sleDot1xStatsEapolFramesTx,
       "sleDot1xStatsEapolStartFramesRx": sleDot1xStatsEapolStartFramesRx,
       "sleDot1xStatsEapolLogoffFramesRx": sleDot1xStatsEapolLogoffFramesRx,
       "sleDot1xStatsEapolRespIdFramesRx": sleDot1xStatsEapolRespIdFramesRx,
       "sleDot1xStatsEapolRespFramesRx": sleDot1xStatsEapolRespFramesRx,
       "sleDot1xStatsEapolReqIdFramesTx": sleDot1xStatsEapolReqIdFramesTx,
       "sleDot1xStatsEapolReqFramesTx": sleDot1xStatsEapolReqFramesTx,
       "sleDot1xStatsInvalidEapolFramesRx": sleDot1xStatsInvalidEapolFramesRx,
       "sleDot1xStatsEapLengthErrorFramesRx": sleDot1xStatsEapLengthErrorFramesRx,
       "sleDot1xStatsLastEapolFrameVersion": sleDot1xStatsLastEapolFrameVersion,
       "sleDot1xStatsLastEapolFrameSource": sleDot1xStatsLastEapolFrameSource,
       "sleDot1xStatisticsControl": sleDot1xStatisticsControl,
       "sleDot1xStatsControlRequest": sleDot1xStatsControlRequest,
       "sleDot1xStatsControlStatus": sleDot1xStatsControlStatus,
       "sleDot1xStatsControlTimer": sleDot1xStatsControlTimer,
       "sleDot1xStatsControlTimeStamp": sleDot1xStatsControlTimeStamp,
       "sleDot1xStatsControlReqResult": sleDot1xStatsControlReqResult,
       "sleDot1xStatsControlPortIndex": sleDot1xStatsControlPortIndex,
       "sleDot1xStatisticsNotification": sleDot1xStatisticsNotification,
       "sleDot1xStatisticsCleared": sleDot1xStatisticsCleared,
       "sleArpInspection": sleArpInspection,
       "sleArpInspectBase": sleArpInspectBase,
       "sleArpInspectBaseInfo": sleArpInspectBaseInfo,
       "sleArpInspectValidateSrcMac": sleArpInspectValidateSrcMac,
       "sleArpInspectValidateDstMac": sleArpInspectValidateDstMac,
       "sleArpInspectValidateIpAddr": sleArpInspectValidateIpAddr,
       "sleArpInspectLogBufferSize": sleArpInspectLogBufferSize,
       "sleArpInspectLogEntry": sleArpInspectLogEntry,
       "sleArpInspectLogInterval": sleArpInspectLogInterval,
       "sleArpInspectBaseControl": sleArpInspectBaseControl,
       "sleArpInspectControlRequest": sleArpInspectControlRequest,
       "sleArpInspectControlStatus": sleArpInspectControlStatus,
       "sleArpInspectControlTimer": sleArpInspectControlTimer,
       "sleArpInspectControlTimeStamp": sleArpInspectControlTimeStamp,
       "sleArpInspectControlReqResult": sleArpInspectControlReqResult,
       "sleArpInspectControlValidateSrcMac": sleArpInspectControlValidateSrcMac,
       "sleArpInspectControlValidateDstMac": sleArpInspectControlValidateDstMac,
       "sleArpInspectControlValidateIpAddr": sleArpInspectControlValidateIpAddr,
       "sleArpInspectControlLogBufferSize": sleArpInspectControlLogBufferSize,
       "sleArpInspectControlLogEntry": sleArpInspectControlLogEntry,
       "sleArpInspectControlLogInterval": sleArpInspectControlLogInterval,
       "sleArpInspectBaseNotifications": sleArpInspectBaseNotifications,
       "sleArpInspectValidateChanged": sleArpInspectValidateChanged,
       "sleArpInspectLogBufferSizeChanged": sleArpInspectLogBufferSizeChanged,
       "sleArpInspectLogRateChanged": sleArpInspectLogRateChanged,
       "sleArpACL": sleArpACL,
       "sleArpAclTable": sleArpAclTable,
       "sleArpAclEntry": sleArpAclEntry,
       "sleArpAclIndex": sleArpAclIndex,
       "sleArpAclName": sleArpAclName,
       "sleArpAclNumEntries": sleArpAclNumEntries,
       "sleArpAclControl": sleArpAclControl,
       "sleArpAclControlRequest": sleArpAclControlRequest,
       "sleArpAclControlStatus": sleArpAclControlStatus,
       "sleArpAclControlTimer": sleArpAclControlTimer,
       "sleArpAclControlTimeStamp": sleArpAclControlTimeStamp,
       "sleArpAclControlReqResult": sleArpAclControlReqResult,
       "sleArpAclControlIndex": sleArpAclControlIndex,
       "sleArpAclControlName": sleArpAclControlName,
       "sleArpAclNotifications": sleArpAclNotifications,
       "sleArpAclCreated": sleArpAclCreated,
       "sleArpAclDestroyed": sleArpAclDestroyed,
       "sleArpACLRule": sleArpACLRule,
       "sleArpAclRuleTable": sleArpAclRuleTable,
       "sleArpAclRuleEntry": sleArpAclRuleEntry,
       "sleArpAclRuleAclIndex": sleArpAclRuleAclIndex,
       "sleArpAclRuleIndex": sleArpAclRuleIndex,
       "sleArpAclRuleAction": sleArpAclRuleAction,
       "sleArpAclRuleType": sleArpAclRuleType,
       "sleArpAclRuleRangeStartIP": sleArpAclRuleRangeStartIP,
       "sleArpAclRuleRangeEndIP": sleArpAclRuleRangeEndIP,
       "sleArpAclRuleIPAddress": sleArpAclRuleIPAddress,
       "sleArpAclRuleIPMask": sleArpAclRuleIPMask,
       "sleArpAclRuleMacAddr": sleArpAclRuleMacAddr,
       "sleArpAclRuleMacType": sleArpAclRuleMacType,
       "sleArpAclRuleControl": sleArpAclRuleControl,
       "sleArpAclRuleControlRequest": sleArpAclRuleControlRequest,
       "sleArpAclRuleControlStatus": sleArpAclRuleControlStatus,
       "sleArpAclRuleControlTimer": sleArpAclRuleControlTimer,
       "sleArpAclRuleControlTimeStamp": sleArpAclRuleControlTimeStamp,
       "sleArpAclRuleControlReqResult": sleArpAclRuleControlReqResult,
       "sleArpAclRuleControlAclIndex": sleArpAclRuleControlAclIndex,
       "sleArpAclRuleControlIndex": sleArpAclRuleControlIndex,
       "sleArpAclRuleControlAction": sleArpAclRuleControlAction,
       "sleArpAclRuleControlType": sleArpAclRuleControlType,
       "sleArpAclRuleControlRangeStartIP": sleArpAclRuleControlRangeStartIP,
       "sleArpAclRuleControlRangeEndIP": sleArpAclRuleControlRangeEndIP,
       "sleArpAclRuleControlIPAddress": sleArpAclRuleControlIPAddress,
       "sleArpAclRuleControlIPMask": sleArpAclRuleControlIPMask,
       "sleArpAclRuleControlMacAddr": sleArpAclRuleControlMacAddr,
       "sleArpAclRuleControlMacType": sleArpAclRuleControlMacType,
       "sleArpAclRuleNotifications": sleArpAclRuleNotifications,
       "sleArpAclRuleCreated": sleArpAclRuleCreated,
       "sleArpAclRuleDestroyed": sleArpAclRuleDestroyed,
       "sleArpInspectVlan": sleArpInspectVlan,
       "sleArpInspectVlanTable": sleArpInspectVlanTable,
       "sleArpInspectVlanEntry": sleArpInspectVlanEntry,
       "sleArpInspectVlanIndex": sleArpInspectVlanIndex,
       "sleArpInspectVlanEnable": sleArpInspectVlanEnable,
       "sleArpInspectVlanFilterAcl": sleArpInspectVlanFilterAcl,
       "sleArpInspectVlanFwdPktCnt": sleArpInspectVlanFwdPktCnt,
       "sleArpInspectVlanDropPktCnt": sleArpInspectVlanDropPktCnt,
       "sleArpInspectVlanAclPermits": sleArpInspectVlanAclPermits,
       "sleArpInspectVlanAclDrops": sleArpInspectVlanAclDrops,
       "sleArpInspectVlanSrcMacFailurs": sleArpInspectVlanSrcMacFailurs,
       "sleArpInspectVlanDstMacFailurs": sleArpInspectVlanDstMacFailurs,
       "sleArpInspectVlanIpAddrFailurs": sleArpInspectVlanIpAddrFailurs,
       "sleArpInspectVlanFilterAclName": sleArpInspectVlanFilterAclName,
       "sleArpInspectVlanControl": sleArpInspectVlanControl,
       "sleArpInspectVlanControlRequest": sleArpInspectVlanControlRequest,
       "sleArpInspectVlanControlStatus": sleArpInspectVlanControlStatus,
       "sleArpInspectVlanControlTimer": sleArpInspectVlanControlTimer,
       "sleArpInspectVlanControlTimeStamp": sleArpInspectVlanControlTimeStamp,
       "sleArpInspectVlanControlReqResult": sleArpInspectVlanControlReqResult,
       "sleArpInspectVlanControlIndex": sleArpInspectVlanControlIndex,
       "sleArpInspectVlanControlEnable": sleArpInspectVlanControlEnable,
       "sleArpInspectVlanControlFilterAcl": sleArpInspectVlanControlFilterAcl,
       "sleArpInspectVlanNotifications": sleArpInspectVlanNotifications,
       "sleArpInspectVlanChanged": sleArpInspectVlanChanged,
       "sleArpInspectPort": sleArpInspectPort,
       "sleArpInspectPortTable": sleArpInspectPortTable,
       "sleArpInspectPortEntry": sleArpInspectPortEntry,
       "sleArpInspectPortIndex": sleArpInspectPortIndex,
       "sleArpInspectPortTrust": sleArpInspectPortTrust,
       "sleArpInspectPortControl": sleArpInspectPortControl,
       "sleArpInspectPortControlRequest": sleArpInspectPortControlRequest,
       "sleArpInspectPortControlStatus": sleArpInspectPortControlStatus,
       "sleArpInspectPortControlTimer": sleArpInspectPortControlTimer,
       "sleArpInspectPortControlTimeStamp": sleArpInspectPortControlTimeStamp,
       "sleArpInspectPortControlReqResult": sleArpInspectPortControlReqResult,
       "sleArpInspectPortControlIndex": sleArpInspectPortControlIndex,
       "sleArpInspectPortControlTrust": sleArpInspectPortControlTrust,
       "sleArpInspectPortNotifications": sleArpInspectPortNotifications,
       "sleArpInspectPortChanged": sleArpInspectPortChanged,
       "sleArpInspectInvalidLog": sleArpInspectInvalidLog,
       "sleArpInspectInvalidLogTable": sleArpInspectInvalidLogTable,
       "sleArpInspectInvalidLogEntry": sleArpInspectInvalidLogEntry,
       "sleArpInspectInvalidLogId": sleArpInspectInvalidLogId,
       "sleArpInspectInvalidLogReason": sleArpInspectInvalidLogReason,
       "sleArpInspectInvalidLogSamePktCnt": sleArpInspectInvalidLogSamePktCnt,
       "sleArpInspectInvalidLogOpcode": sleArpInspectInvalidLogOpcode,
       "sleArpInspectInvalidLogPortNumber": sleArpInspectInvalidLogPortNumber,
       "sleArpInspectInvalidLogVlanId": sleArpInspectInvalidLogVlanId,
       "sleArpInspectInvalidLogSrcMacAddr": sleArpInspectInvalidLogSrcMacAddr,
       "sleArpInspectInvalidLogSrcIpAddr": sleArpInspectInvalidLogSrcIpAddr,
       "sleArpInspectInvalidLogDstMacAddr": sleArpInspectInvalidLogDstMacAddr,
       "sleArpInspectInvalidLogDstIpAddr": sleArpInspectInvalidLogDstIpAddr,
       "sleArpInspectInvalidLogLastRecvTime": sleArpInspectInvalidLogLastRecvTime,
       "sleSecurityAttack": sleSecurityAttack,
       "sleSecurityAttackBasic": sleSecurityAttackBasic,
       "sleSecurityAttackBasicBase": sleSecurityAttackBasicBase,
       "sleSecurityAttackBasicBaseInfo": sleSecurityAttackBasicBaseInfo,
       "sleSecurityAttackBasicBaseInfoGlobalStatus": sleSecurityAttackBasicBaseInfoGlobalStatus,
       "sleSecurityAttackBasicBaseDosStatus": sleSecurityAttackBasicBaseDosStatus,
       "sleSecurityAttackBasicBaseScanStatus": sleSecurityAttackBasicBaseScanStatus,
       "sleSecurityAttackBasicBaseCollectInterval": sleSecurityAttackBasicBaseCollectInterval,
       "sleSecurityAttackBasicBaseControl": sleSecurityAttackBasicBaseControl,
       "sleSecurityAttackBasicBaseControlRequest": sleSecurityAttackBasicBaseControlRequest,
       "sleSecurityAttackBasicBaseControlStatus": sleSecurityAttackBasicBaseControlStatus,
       "sleSecurityAttackBasicBaseControlTimer": sleSecurityAttackBasicBaseControlTimer,
       "sleSecurityAttackBasicBaseControlTimeStamp": sleSecurityAttackBasicBaseControlTimeStamp,
       "sleSecurityAttackBasicBaseControlReqResult": sleSecurityAttackBasicBaseControlReqResult,
       "sleSecurityAttackBasicBaseControlGlobalStatus": sleSecurityAttackBasicBaseControlGlobalStatus,
       "sleSecurityAttackBasicBaseControlDosStatus": sleSecurityAttackBasicBaseControlDosStatus,
       "sleSecurityAttackBasicBaseControlScanStatus": sleSecurityAttackBasicBaseControlScanStatus,
       "sleSecurityAttackBasicBaseControlCollectInterval": sleSecurityAttackBasicBaseControlCollectInterval,
       "sleSecurityAttackBasicBaseNotification": sleSecurityAttackBasicBaseNotification,
       "sleSecurityAttackBasicBaseGlobalStatusChanged": sleSecurityAttackBasicBaseGlobalStatusChanged,
       "sleSecurityAttackBasicBaseDosStatusChanged": sleSecurityAttackBasicBaseDosStatusChanged,
       "sleSecurityAttackBasicBaseScanStatusChanged": sleSecurityAttackBasicBaseScanStatusChanged,
       "sleSecurityAttackBasicBaseCollectIntervalChanged": sleSecurityAttackBasicBaseCollectIntervalChanged,
       "sleSecurityAttackBasicBaseAllConfigChanged": sleSecurityAttackBasicBaseAllConfigChanged,
       "sleSecurityAttackBasicPolicy": sleSecurityAttackBasicPolicy,
       "sleSecurityAttackBasicPolicyInfo": sleSecurityAttackBasicPolicyInfo,
       "sleSecurityAttackBasicPolicyAttackType": sleSecurityAttackBasicPolicyAttackType,
       "sleSecurityAttackBasicPolicyBlockTime": sleSecurityAttackBasicPolicyBlockTime,
       "sleSecurityAttackBasicPolicyThresholdCount": sleSecurityAttackBasicPolicyThresholdCount,
       "sleSecurityAttackBasicPolicyCollectPorts": sleSecurityAttackBasicPolicyCollectPorts,
       "sleSecurityAttackBasicPolicyControl": sleSecurityAttackBasicPolicyControl,
       "sleSecurityAttackBasicPolicyControlRequest": sleSecurityAttackBasicPolicyControlRequest,
       "sleSecurityAttackBasicPolicyControlStatus": sleSecurityAttackBasicPolicyControlStatus,
       "sleSecurityAttackBasicPolicyControlTimer": sleSecurityAttackBasicPolicyControlTimer,
       "sleSecurityAttackBasicPolicyControlTimeStamp": sleSecurityAttackBasicPolicyControlTimeStamp,
       "sleSecurityAttackBasicPolicyControlReqResult": sleSecurityAttackBasicPolicyControlReqResult,
       "sleSecurityAttackBasicPolicyControlAttackType": sleSecurityAttackBasicPolicyControlAttackType,
       "sleSecurityAttackBasicPolicyControlBlockTime": sleSecurityAttackBasicPolicyControlBlockTime,
       "sleSecurityAttackBasicPolicyControlThresholdCount": sleSecurityAttackBasicPolicyControlThresholdCount,
       "sleSecurityAttackBasicPolicyControlCollectPorts": sleSecurityAttackBasicPolicyControlCollectPorts,
       "sleSecurityAttackBasicPolicyNotification": sleSecurityAttackBasicPolicyNotification,
       "sleSecurityAttackBasicPolicyBlockTimeChanged": sleSecurityAttackBasicPolicyBlockTimeChanged,
       "sleSecurityAttackBasicPolicyThresholdCountChanged": sleSecurityAttackBasicPolicyThresholdCountChanged,
       "sleSecurityAttackBasicPolicyCollectPortsChanged": sleSecurityAttackBasicPolicyCollectPortsChanged,
       "setSecurityAttackBasicPolicyAllConfigChanged": setSecurityAttackBasicPolicyAllConfigChanged,
       "sleSecurityAttackBasicExceptList": sleSecurityAttackBasicExceptList,
       "sleSecurityAttackBasicExceptListTable": sleSecurityAttackBasicExceptListTable,
       "sleSecurityAttackBasicExceptListEntry": sleSecurityAttackBasicExceptListEntry,
       "sleSecurityAttackBasicExceptListIndex": sleSecurityAttackBasicExceptListIndex,
       "sleSecurityAttackBasicExceptListProtocolType": sleSecurityAttackBasicExceptListProtocolType,
       "sleSecurityAttackBasicExceptListSourceIpAddress": sleSecurityAttackBasicExceptListSourceIpAddress,
       "sleSecurityAttackBasicExceptListDestinationIpAddress": sleSecurityAttackBasicExceptListDestinationIpAddress,
       "sleSecurityAttackBasicExceptListIngressPort": sleSecurityAttackBasicExceptListIngressPort,
       "sleSecurityAttackBasicExceptListControl": sleSecurityAttackBasicExceptListControl,
       "sleSecurityAttackBasicExceptListControlRequest": sleSecurityAttackBasicExceptListControlRequest,
       "sleSecurityAttackBasicExceptListControlStatus": sleSecurityAttackBasicExceptListControlStatus,
       "sleSecurityAttackBasicExceptListControlTimer": sleSecurityAttackBasicExceptListControlTimer,
       "sleSecurityAttackBasicExceptListControlTimeStamp": sleSecurityAttackBasicExceptListControlTimeStamp,
       "sleSecurityAttackBasicExceptListControlReqResult": sleSecurityAttackBasicExceptListControlReqResult,
       "sleSecurityAttackBasicExceptListControlRuleIndex": sleSecurityAttackBasicExceptListControlRuleIndex,
       "sleSecurityAttackBasicExceptListControlProtocolType": sleSecurityAttackBasicExceptListControlProtocolType,
       "sleSecurityAttackBasicExceptListControlSourceIpAddress": sleSecurityAttackBasicExceptListControlSourceIpAddress,
       "sleSecurityAttackBasicExceptListControlDestinationIpAddress": sleSecurityAttackBasicExceptListControlDestinationIpAddress,
       "sleSecurityAttackBasicExceptListControlIngressPort": sleSecurityAttackBasicExceptListControlIngressPort,
       "sleSecurityAttackBasicExceptListNotification": sleSecurityAttackBasicExceptListNotification,
       "sleSecurityAttackBasicExceptListCreated": sleSecurityAttackBasicExceptListCreated,
       "sleSecurityAttackBasicExceptListChanged": sleSecurityAttackBasicExceptListChanged,
       "sleSecurityAttackBasicExceptListDeleted": sleSecurityAttackBasicExceptListDeleted,
       "sleSecurityAttackBasicBlackList": sleSecurityAttackBasicBlackList,
       "sleSecurityAttackBasicBlackListTable": sleSecurityAttackBasicBlackListTable,
       "sleSecurityAttackBasicBlackListEntry": sleSecurityAttackBasicBlackListEntry,
       "sleSecurityAttackBasicBlackListIndex": sleSecurityAttackBasicBlackListIndex,
       "sleSecurityAttackBasicBlackListProtocolType": sleSecurityAttackBasicBlackListProtocolType,
       "sleSecurityAttackBasicBlackListSourceIpAddress": sleSecurityAttackBasicBlackListSourceIpAddress,
       "sleSecurityAttackBasicBlackListDestinationIpAddress": sleSecurityAttackBasicBlackListDestinationIpAddress,
       "sleSecurityAttackBasicBlackListBlockingStatus": sleSecurityAttackBasicBlackListBlockingStatus,
       "sleSecurityAttackBasicBlackListIgressPort": sleSecurityAttackBasicBlackListIgressPort,
       "sleSecurityAttackBasicBlackListControl": sleSecurityAttackBasicBlackListControl,
       "sleSecurityAttackBasicBlackListControlRequest": sleSecurityAttackBasicBlackListControlRequest,
       "sleSecurityAttackBasicBlackListControlStatus": sleSecurityAttackBasicBlackListControlStatus,
       "sleSecurityAttackBasicBlackListControlTimer": sleSecurityAttackBasicBlackListControlTimer,
       "sleSecurityAttackBasicBlackListControlTimeStamp": sleSecurityAttackBasicBlackListControlTimeStamp,
       "sleSecurityAttackBasicBlackListControlReqResult": sleSecurityAttackBasicBlackListControlReqResult,
       "sleSecurityAttackBasicBlackListControlRuleIndex": sleSecurityAttackBasicBlackListControlRuleIndex,
       "sleSecurityAttackBasicBlackListControlProtocolType": sleSecurityAttackBasicBlackListControlProtocolType,
       "sleSecurityAttackBasicBlackListControlSourceIpAddress": sleSecurityAttackBasicBlackListControlSourceIpAddress,
       "sleSecurityAttackBasicBlackListControlDestinationIpAddress": sleSecurityAttackBasicBlackListControlDestinationIpAddress,
       "sleSecurityAttackBasicBlackListControlIngressPort": sleSecurityAttackBasicBlackListControlIngressPort,
       "sleSecurityAttackBasicBlackListNotification": sleSecurityAttackBasicBlackListNotification,
       "sleSecurityAttackBasicBlackListCreated": sleSecurityAttackBasicBlackListCreated,
       "sleSecurityAttackBasicBlackListDeleted": sleSecurityAttackBasicBlackListDeleted,
       "sleSecurityAttackBasicBlockedList": sleSecurityAttackBasicBlockedList,
       "sleSecurityAttackBasicBlockedListTable": sleSecurityAttackBasicBlockedListTable,
       "sleSecurityAttackBasicBlockedListEntry": sleSecurityAttackBasicBlockedListEntry,
       "sleSecurityAttackBasicBlockedListIndex": sleSecurityAttackBasicBlockedListIndex,
       "sleSecurityAttackBasicBlockedListAttackType": sleSecurityAttackBasicBlockedListAttackType,
       "sleSecurityAttackBasicBlockedListStartTime": sleSecurityAttackBasicBlockedListStartTime,
       "sleSecurityAttackBasicBlockedListEndTime": sleSecurityAttackBasicBlockedListEndTime,
       "sleSecurityAttackBasicBlockedListAttackSourceIp": sleSecurityAttackBasicBlockedListAttackSourceIp,
       "sleSecurityAttackBasicBlockedListAttackDestinationIp": sleSecurityAttackBasicBlockedListAttackDestinationIp,
       "sleSecurityAttackBasicBlockedListProtocol": sleSecurityAttackBasicBlockedListProtocol,
       "sleSecurityAttackBasicBlockedListAttackPktCount": sleSecurityAttackBasicBlockedListAttackPktCount,
       "sleSecurityAttackBasicBlockedListAttackBlockTime": sleSecurityAttackBasicBlockedListAttackBlockTime,
       "sleSecurityAttackBasicBlockedListBlackListIndex": sleSecurityAttackBasicBlockedListBlackListIndex,
       "sleSecurityAttackBasicBlockedListIgressPort": sleSecurityAttackBasicBlockedListIgressPort,
       "sleSecurityAttackBasicBlockedListControl": sleSecurityAttackBasicBlockedListControl,
       "sleSecurityAttackBasicBlockedListControlRequest": sleSecurityAttackBasicBlockedListControlRequest,
       "sleSecurityAttackBasicBlockedListControlStatus": sleSecurityAttackBasicBlockedListControlStatus,
       "sleSecurityAttackBasicBlockedListControlTimer": sleSecurityAttackBasicBlockedListControlTimer,
       "sleSecurityAttackBasicBlockedListControlTimeStamp": sleSecurityAttackBasicBlockedListControlTimeStamp,
       "sleSecurityAttackBasicBlockedListControlReqResult": sleSecurityAttackBasicBlockedListControlReqResult,
       "sleSecurityAttackBasicBlockedListControlRuleIndex": sleSecurityAttackBasicBlockedListControlRuleIndex,
       "sleSecurityAttackBasicBlockedListControlBlockTime": sleSecurityAttackBasicBlockedListControlBlockTime,
       "sleSecurityAttackBasicBlockedListNotification": sleSecurityAttackBasicBlockedListNotification,
       "sleSecurityAttackBasicBlockedListBlockTimeChanged": sleSecurityAttackBasicBlockedListBlockTimeChanged,
       "sleSecurityAttackBasicBlockedListDeleted": sleSecurityAttackBasicBlockedListDeleted,
       "sleSecurityAttackExpansion": sleSecurityAttackExpansion,
       "sleSecurityAttackExpansionBase": sleSecurityAttackExpansionBase,
       "sleSecurityAttackExpansionBaseInfo": sleSecurityAttackExpansionBaseInfo,
       "sleSecurityAttackExpansionBaseGlobalStatus": sleSecurityAttackExpansionBaseGlobalStatus,
       "sleSecurityAttackExpansionBaseControl": sleSecurityAttackExpansionBaseControl,
       "sleSecurityAttackExpansionBaseControlRequest": sleSecurityAttackExpansionBaseControlRequest,
       "sleSecurityAttackExpansionBaseControlStatus": sleSecurityAttackExpansionBaseControlStatus,
       "sleSecurityAttackExpansionBaseControlTimer": sleSecurityAttackExpansionBaseControlTimer,
       "sleSecurityAttackExpansionBaseControlTimeStamp": sleSecurityAttackExpansionBaseControlTimeStamp,
       "sleSecurityAttackExpansionBaseControlReqResult": sleSecurityAttackExpansionBaseControlReqResult,
       "sleSecurityAttackExpansionBaseControlGlobalStatus": sleSecurityAttackExpansionBaseControlGlobalStatus,
       "sleSecurityAttackExpansionBaseNotification": sleSecurityAttackExpansionBaseNotification,
       "sleSecurityAttackExpansionBaseGlobalStatusChanged": sleSecurityAttackExpansionBaseGlobalStatusChanged,
       "sleSecurityAttackExpansionPolicy": sleSecurityAttackExpansionPolicy,
       "sleSecurityAttackExpansionPolicyTable": sleSecurityAttackExpansionPolicyTable,
       "sleSecurityAttackExpansionPolicyEntry": sleSecurityAttackExpansionPolicyEntry,
       "sleSecurityAttackExpansionPolicyPortIndex": sleSecurityAttackExpansionPolicyPortIndex,
       "sleSecurityAttackExpansionPolicyStatus": sleSecurityAttackExpansionPolicyStatus,
       "sleSecurityAttackExpansionPolicyAttackType": sleSecurityAttackExpansionPolicyAttackType,
       "sleSecurityAttackExpansionPolicyBlockTime": sleSecurityAttackExpansionPolicyBlockTime,
       "sleSecurityAttackExpansionPolicyControl": sleSecurityAttackExpansionPolicyControl,
       "sleSecurityAttackExpansionPolicyControlRequest": sleSecurityAttackExpansionPolicyControlRequest,
       "sleSecurityAttackExpansionPolicyControlStatus": sleSecurityAttackExpansionPolicyControlStatus,
       "sleSecurityAttackExpansionPolicyControlTimer": sleSecurityAttackExpansionPolicyControlTimer,
       "sleSecurityAttackExpansionPolicyControlTimeStamp": sleSecurityAttackExpansionPolicyControlTimeStamp,
       "sleSecurityAttackExpansionPolicyControlReqResult": sleSecurityAttackExpansionPolicyControlReqResult,
       "sleSecurityAttackExpansionPolicyControlPortIndex": sleSecurityAttackExpansionPolicyControlPortIndex,
       "sleSecurityAttackExpansionPolicyControlAttackType": sleSecurityAttackExpansionPolicyControlAttackType,
       "sleSecurityAttackExpansionPolicyControlBlockTime": sleSecurityAttackExpansionPolicyControlBlockTime,
       "sleSecurityAttackExpansionPolicyNotification": sleSecurityAttackExpansionPolicyNotification,
       "sleSecurityAttackExpansionPolicyChanged": sleSecurityAttackExpansionPolicyChanged,
       "sleSecurityAttackExpansionExceptList": sleSecurityAttackExpansionExceptList,
       "sleSecurityAttackExpansionExceptListTable": sleSecurityAttackExpansionExceptListTable,
       "sleSecurityAttackExpansionExceptListEntry": sleSecurityAttackExpansionExceptListEntry,
       "sleSecurityAttackExpansionExceptListPortIndex": sleSecurityAttackExpansionExceptListPortIndex,
       "sleSecurityAttackExpansionExceptListIndex": sleSecurityAttackExpansionExceptListIndex,
       "sleSecurityAttackExpansionExceptListRuleIndex": sleSecurityAttackExpansionExceptListRuleIndex,
       "sleSecurityAttackExpansionExceptListProtocolType": sleSecurityAttackExpansionExceptListProtocolType,
       "sleSecurityAttackExpansionExceptListSourceType": sleSecurityAttackExpansionExceptListSourceType,
       "sleSecurityAttackExpansionExceptListSourceIpAddress": sleSecurityAttackExpansionExceptListSourceIpAddress,
       "sleSecurityAttackExpansionExceptListSourceIpMask": sleSecurityAttackExpansionExceptListSourceIpMask,
       "sleSecurityAttackExpansionExceptListSourceMac": sleSecurityAttackExpansionExceptListSourceMac,
       "sleSecurityAttackExpansionExceptListSourcePortType": sleSecurityAttackExpansionExceptListSourcePortType,
       "sleSecurityAttackExpansionExceptListSourcePortFrom": sleSecurityAttackExpansionExceptListSourcePortFrom,
       "sleSecurityAttackExpansionExceptListSourcePortTo": sleSecurityAttackExpansionExceptListSourcePortTo,
       "sleSecurityAttackExpansionExceptListDestinationType": sleSecurityAttackExpansionExceptListDestinationType,
       "sleSecurityAttackExpansionExceptListDestinationIpAddress": sleSecurityAttackExpansionExceptListDestinationIpAddress,
       "sleSecurityAttackExpansionExceptListDestinationIpMask": sleSecurityAttackExpansionExceptListDestinationIpMask,
       "sleSecurityAttackExpansionExceptListDestinationMac": sleSecurityAttackExpansionExceptListDestinationMac,
       "sleSecurityAttackExpansionExceptListDestinationPortType": sleSecurityAttackExpansionExceptListDestinationPortType,
       "sleSecurityAttackExpansionExceptListDestinationPortFrom": sleSecurityAttackExpansionExceptListDestinationPortFrom,
       "sleSecurityAttackExpansionExceptListDestinationPortTo": sleSecurityAttackExpansionExceptListDestinationPortTo,
       "sleSecurityAttackExpansionExceptListControl": sleSecurityAttackExpansionExceptListControl,
       "sleSecurityAttackExpansionExceptListControlRequest": sleSecurityAttackExpansionExceptListControlRequest,
       "sleSecurityAttackExpansionExceptListControlStatus": sleSecurityAttackExpansionExceptListControlStatus,
       "sleSecurityAttackExpansionExceptListControlTimer": sleSecurityAttackExpansionExceptListControlTimer,
       "sleSecurityAttackExpansionExceptListControlTimeStamp": sleSecurityAttackExpansionExceptListControlTimeStamp,
       "sleSecurityAttackExpansionExceptListControlReqResult": sleSecurityAttackExpansionExceptListControlReqResult,
       "sleSecurityAttackExpansionExceptListControlPortIndex": sleSecurityAttackExpansionExceptListControlPortIndex,
       "sleSecurityAttackExpansionExceptListControlRuleIndex": sleSecurityAttackExpansionExceptListControlRuleIndex,
       "sleSecurityAttackExpansionExceptListControlProtocolType": sleSecurityAttackExpansionExceptListControlProtocolType,
       "sleSecurityAttackExpansionExceptListControlSourceType": sleSecurityAttackExpansionExceptListControlSourceType,
       "sleSecurityAttackExpansionExceptListControlSourceIpAddress": sleSecurityAttackExpansionExceptListControlSourceIpAddress,
       "sleSecurityAttackExpansionExceptListControlSourceIpMask": sleSecurityAttackExpansionExceptListControlSourceIpMask,
       "sleSecurityAttackExpansionExceptListControlSourceMac": sleSecurityAttackExpansionExceptListControlSourceMac,
       "sleSecurityAttackExpansionExceptListControlSourcePortType": sleSecurityAttackExpansionExceptListControlSourcePortType,
       "sleSecurityAttackExpansionExceptListControlSourcePortFrom": sleSecurityAttackExpansionExceptListControlSourcePortFrom,
       "sleSecurityAttackExpansionExceptListControlSourcePortTo": sleSecurityAttackExpansionExceptListControlSourcePortTo,
       "sleSecurityAttackExpansionExceptListControlDestinationType": sleSecurityAttackExpansionExceptListControlDestinationType,
       "sleSecurityAttackExpansionExceptListControlDestinationIpAddress": sleSecurityAttackExpansionExceptListControlDestinationIpAddress,
       "sleSecurityAttackExpansionExceptListControlDestinationIpMask": sleSecurityAttackExpansionExceptListControlDestinationIpMask,
       "sleSecurityAttackExpansionExceptListControlDestinationMac": sleSecurityAttackExpansionExceptListControlDestinationMac,
       "sleSecurityAttackExpansionExceptListControlDestinationPortType": sleSecurityAttackExpansionExceptListControlDestinationPortType,
       "sleSecurityAttackExpansionExceptListControlDestinationPortFrom": sleSecurityAttackExpansionExceptListControlDestinationPortFrom,
       "sleSecurityAttackExpansionExceptListControlDestinationPortTo": sleSecurityAttackExpansionExceptListControlDestinationPortTo,
       "sleSecurityAttackExpansionExceptListNotification": sleSecurityAttackExpansionExceptListNotification,
       "sleSecurityAttackExpansionExceptListCreated": sleSecurityAttackExpansionExceptListCreated,
       "sleSecurityAttackExpansionExceptListChanged": sleSecurityAttackExpansionExceptListChanged,
       "sleSecurityAttackExpansionExceptListDeleted": sleSecurityAttackExpansionExceptListDeleted,
       "sleSecurityAttackExpansionBlockedList": sleSecurityAttackExpansionBlockedList,
       "sleSecurityAttackExpansionBlockedListTable": sleSecurityAttackExpansionBlockedListTable,
       "sleSecurityAttackExpansionBlockedListEntry": sleSecurityAttackExpansionBlockedListEntry,
       "sleSecurityAttackExpansionBlockedListPortIndex": sleSecurityAttackExpansionBlockedListPortIndex,
       "sleSecurityAttackExpansionBlockedListIndex": sleSecurityAttackExpansionBlockedListIndex,
       "sleSecurityAttackExpansionBlockedListRuleIndex": sleSecurityAttackExpansionBlockedListRuleIndex,
       "sleSecurityAttackExpansionBlockedListAttackType": sleSecurityAttackExpansionBlockedListAttackType,
       "sleSecurityAttackExpansionBlockedListAttackBlockType": sleSecurityAttackExpansionBlockedListAttackBlockType,
       "sleSecurityAttackExpansionBlockedListStartTime": sleSecurityAttackExpansionBlockedListStartTime,
       "sleSecurityAttackExpansionBlockedListEndTime": sleSecurityAttackExpansionBlockedListEndTime,
       "sleSecurityAttackExpansionBlockedListAttackSourceIp": sleSecurityAttackExpansionBlockedListAttackSourceIp,
       "sleSecurityAttackExpansionBlockedListSourceMac": sleSecurityAttackExpansionBlockedListSourceMac,
       "sleSecurityAttackExpansionBlockedListAttackDestinationIp": sleSecurityAttackExpansionBlockedListAttackDestinationIp,
       "sleSecurityAttackExpansionBlockedListProtocol": sleSecurityAttackExpansionBlockedListProtocol,
       "sleSecurityAttackExpansionBlockedListSourcePort": sleSecurityAttackExpansionBlockedListSourcePort,
       "sleSecurityAttackExpansionBlockedListDestinationPort": sleSecurityAttackExpansionBlockedListDestinationPort,
       "sleSecurityAttackExpansionBlockedListAttackPktCount": sleSecurityAttackExpansionBlockedListAttackPktCount,
       "sleSecurityAttackExpansionBlockedListAttackBlockTime": sleSecurityAttackExpansionBlockedListAttackBlockTime,
       "sleSecurityAttackExpansionBlockedListControl": sleSecurityAttackExpansionBlockedListControl,
       "sleSecurityAttackExpansionBlockedListControlRequest": sleSecurityAttackExpansionBlockedListControlRequest,
       "sleSecurityAttackExpansionBlockedListControlStatus": sleSecurityAttackExpansionBlockedListControlStatus,
       "sleSecurityAttackExpansionBlockedListControlTimer": sleSecurityAttackExpansionBlockedListControlTimer,
       "sleSecurityAttackExpansionBlockedListControlTimeStamp": sleSecurityAttackExpansionBlockedListControlTimeStamp,
       "sleSecurityAttackExpansionBlockedListControlReqResult": sleSecurityAttackExpansionBlockedListControlReqResult,
       "sleSecurityAttackExpansionBlockedListControlRuleIndex": sleSecurityAttackExpansionBlockedListControlRuleIndex,
       "sleSecurityAttackExpansionBlockedListControlBlockTime": sleSecurityAttackExpansionBlockedListControlBlockTime,
       "sleSecurityAttackExpansionBlockedListNotification": sleSecurityAttackExpansionBlockedListNotification,
       "sleSecurityAttackExpansionBlockedListBlockTimeChanged": sleSecurityAttackExpansionBlockedListBlockTimeChanged,
       "sleNDInspection": sleNDInspection,
       "sleNDInspectBase": sleNDInspectBase,
       "sleNDInspectBaseInfo": sleNDInspectBaseInfo,
       "sleNDInspectLogBufferSize": sleNDInspectLogBufferSize,
       "sleNDInspectLogEntry": sleNDInspectLogEntry,
       "sleNDInspectLogInterval": sleNDInspectLogInterval,
       "sleNDInspectBaseControl": sleNDInspectBaseControl,
       "sleNDInspectControlRequest": sleNDInspectControlRequest,
       "sleNDInspectControlStatus": sleNDInspectControlStatus,
       "sleNDInspectControlTimer": sleNDInspectControlTimer,
       "sleNDInspectControlTimeStamp": sleNDInspectControlTimeStamp,
       "sleNDInspectControlReqResult": sleNDInspectControlReqResult,
       "sleNDInspectControlLogBufferSize": sleNDInspectControlLogBufferSize,
       "sleNDInspectControlLogEntry": sleNDInspectControlLogEntry,
       "sleNDInspectControlLogInterval": sleNDInspectControlLogInterval,
       "sleNDInspectBaseNotifications": sleNDInspectBaseNotifications,
       "sleNDInspectLogBufferSizeChanged": sleNDInspectLogBufferSizeChanged,
       "sleNDInspectLogRateChanged": sleNDInspectLogRateChanged,
       "sleNDACL": sleNDACL,
       "sleNDAclTable": sleNDAclTable,
       "sleNDAclEntry": sleNDAclEntry,
       "sleNDAclIndex": sleNDAclIndex,
       "sleNDAclName": sleNDAclName,
       "sleNDAclNumEntries": sleNDAclNumEntries,
       "sleNDAclControl": sleNDAclControl,
       "sleNDAclControlRequest": sleNDAclControlRequest,
       "sleNDAclControlStatus": sleNDAclControlStatus,
       "sleNDAclControlTimer": sleNDAclControlTimer,
       "sleNDAclControlTimeStamp": sleNDAclControlTimeStamp,
       "sleNDAclControlReqResult": sleNDAclControlReqResult,
       "sleNDAclControlIndex": sleNDAclControlIndex,
       "sleNDAclControlName": sleNDAclControlName,
       "sleNDAclNotifications": sleNDAclNotifications,
       "sleNDAclCreated": sleNDAclCreated,
       "sleNDAclDestroyed": sleNDAclDestroyed,
       "sleNDACLRule": sleNDACLRule,
       "sleNDAclRuleTable": sleNDAclRuleTable,
       "sleNDAclRuleEntry": sleNDAclRuleEntry,
       "sleNDAclRuleAclIndex": sleNDAclRuleAclIndex,
       "sleNDAclRuleIndex": sleNDAclRuleIndex,
       "sleNDAclRuleAction": sleNDAclRuleAction,
       "sleNDAclRuleType": sleNDAclRuleType,
       "sleNDAclRuleRangeStartIPv6": sleNDAclRuleRangeStartIPv6,
       "sleNDAclRuleRangeEndIPv6": sleNDAclRuleRangeEndIPv6,
       "sleNDAclRuleIPv6Address": sleNDAclRuleIPv6Address,
       "sleNDAclRuleIPv6Mask": sleNDAclRuleIPv6Mask,
       "sleNDAclRuleMacAddr": sleNDAclRuleMacAddr,
       "sleNDAclRuleMacType": sleNDAclRuleMacType,
       "sleNDAclRuleControl": sleNDAclRuleControl,
       "sleNDAclRuleControlRequest": sleNDAclRuleControlRequest,
       "sleNDAclRuleControlStatus": sleNDAclRuleControlStatus,
       "sleNDAclRuleControlTimer": sleNDAclRuleControlTimer,
       "sleNDAclRuleControlTimeStamp": sleNDAclRuleControlTimeStamp,
       "sleNDAclRuleControlReqResult": sleNDAclRuleControlReqResult,
       "sleNDAclRuleControlAclIndex": sleNDAclRuleControlAclIndex,
       "sleNDAclRuleControlIndex": sleNDAclRuleControlIndex,
       "sleNDAclRuleControlAction": sleNDAclRuleControlAction,
       "sleNDAclRuleControlType": sleNDAclRuleControlType,
       "sleNDAclRuleControlRangeStartIPv6": sleNDAclRuleControlRangeStartIPv6,
       "sleNDAclRuleControlRangeEndIPv6": sleNDAclRuleControlRangeEndIPv6,
       "sleNDAclRuleControlIPv6Address": sleNDAclRuleControlIPv6Address,
       "sleNDAclRuleControlIPv6Mask": sleNDAclRuleControlIPv6Mask,
       "sleNDAclRuleControlMacAddr": sleNDAclRuleControlMacAddr,
       "sleNDAclRuleControlMacType": sleNDAclRuleControlMacType,
       "sleNDAclRuleNotifications": sleNDAclRuleNotifications,
       "sleNDAclRuleCreated": sleNDAclRuleCreated,
       "sleNDAclRuleDestroyed": sleNDAclRuleDestroyed,
       "sleNDInspectVlan": sleNDInspectVlan,
       "sleNDInspectVlanTable": sleNDInspectVlanTable,
       "sleNDInspectVlanEntry": sleNDInspectVlanEntry,
       "sleNDInspectVlanIndex": sleNDInspectVlanIndex,
       "sleNDInspectVlanEnable": sleNDInspectVlanEnable,
       "sleNDInspectVlanFilterAclIndex": sleNDInspectVlanFilterAclIndex,
       "sleNDInspectVlanFwdPktCnt": sleNDInspectVlanFwdPktCnt,
       "sleNDInspectVlanDropPktCnt": sleNDInspectVlanDropPktCnt,
       "sleNDInspectVlanAclPermits": sleNDInspectVlanAclPermits,
       "sleNDInspectVlanAclDrops": sleNDInspectVlanAclDrops,
       "sleNDInspectVlanDhcpv6Permits": sleNDInspectVlanDhcpv6Permits,
       "sleNDInspectVlanDhcpv6Denys": sleNDInspectVlanDhcpv6Denys,
       "sleNDInspectVlanLocalIpv6Denys": sleNDInspectVlanLocalIpv6Denys,
       "sleNDInspectVlanFilterAclName": sleNDInspectVlanFilterAclName,
       "sleNDInspectVlanControl": sleNDInspectVlanControl,
       "sleNDInspectVlanControlRequest": sleNDInspectVlanControlRequest,
       "sleNDInspectVlanControlStatus": sleNDInspectVlanControlStatus,
       "sleNDInspectVlanControlTimer": sleNDInspectVlanControlTimer,
       "sleNDInspectVlanControlTimeStamp": sleNDInspectVlanControlTimeStamp,
       "sleNDInspectVlanControlReqResult": sleNDInspectVlanControlReqResult,
       "sleNDInspectVlanControlIndex": sleNDInspectVlanControlIndex,
       "sleNDInspectVlanControlEnable": sleNDInspectVlanControlEnable,
       "sleNDInspectVlanControlFilterAclIndex": sleNDInspectVlanControlFilterAclIndex,
       "sleNDInspectVlanNotifications": sleNDInspectVlanNotifications,
       "sleNDInspectVlanChanged": sleNDInspectVlanChanged,
       "sleNDInspectVlanStatsCleared": sleNDInspectVlanStatsCleared,
       "sleNDInspectPort": sleNDInspectPort,
       "sleNDInspectPortTable": sleNDInspectPortTable,
       "sleNDInspectPortEntry": sleNDInspectPortEntry,
       "sleNDInspectPortIndex": sleNDInspectPortIndex,
       "sleNDInspectPortTrust": sleNDInspectPortTrust,
       "sleNDInspectPortControl": sleNDInspectPortControl,
       "sleNDInspectPortControlRequest": sleNDInspectPortControlRequest,
       "sleNDInspectPortControlStatus": sleNDInspectPortControlStatus,
       "sleNDInspectPortControlTimer": sleNDInspectPortControlTimer,
       "sleNDInspectPortControlTimeStamp": sleNDInspectPortControlTimeStamp,
       "sleNDInspectPortControlReqResult": sleNDInspectPortControlReqResult,
       "sleNDInspectPortControlIndex": sleNDInspectPortControlIndex,
       "sleNDInspectPortControlTrust": sleNDInspectPortControlTrust,
       "sleNDInspectPortNotifications": sleNDInspectPortNotifications,
       "sleNDInspectPortChanged": sleNDInspectPortChanged,
       "sleNDInspectInvalidLog": sleNDInspectInvalidLog,
       "sleNDInspectInvalidLogTable": sleNDInspectInvalidLogTable,
       "sleNDInspectInvalidLogEntry": sleNDInspectInvalidLogEntry,
       "sleNDInspectInvalidLogId": sleNDInspectInvalidLogId,
       "sleNDInspectInvalidLogReason": sleNDInspectInvalidLogReason,
       "sleNDInspectInvalidLogSamePktCnt": sleNDInspectInvalidLogSamePktCnt,
       "sleNDInspectInvalidLogPortNumber": sleNDInspectInvalidLogPortNumber,
       "sleNDInspectInvalidLogVlanId": sleNDInspectInvalidLogVlanId,
       "sleNDInspectInvalidLogSenderMacAddr": sleNDInspectInvalidLogSenderMacAddr,
       "sleNDInspectInvalidLogSrcMacAddr": sleNDInspectInvalidLogSrcMacAddr,
       "sleNDInspectInvalidLogSenderIpv6Addr": sleNDInspectInvalidLogSenderIpv6Addr,
       "sleNDInspectInvalidLogDstIpv6Addr": sleNDInspectInvalidLogDstIpv6Addr,
       "sleNDInspectInvalidLogLastRecvTime": sleNDInspectInvalidLogLastRecvTime,
       "sleNDInspectInvalidLogNDType": sleNDInspectInvalidLogNDType,
       "sleRAGuard": sleRAGuard,
       "sleRAGuardPolicy": sleRAGuardPolicy,
       "sleRAGuardPolicyTable": sleRAGuardPolicyTable,
       "sleRAGuardPolicyEntry": sleRAGuardPolicyEntry,
       "sleRAGuardPolicyIndex": sleRAGuardPolicyIndex,
       "sleRAGuardPolicyName": sleRAGuardPolicyName,
       "sleRAGuardPolicyHoplimitMin": sleRAGuardPolicyHoplimitMin,
       "sleRAGuardPolicyHoplimitMax": sleRAGuardPolicyHoplimitMax,
       "sleRAGuardPolicyManagedFlag": sleRAGuardPolicyManagedFlag,
       "sleRAGuardPolicyOtherFlag": sleRAGuardPolicyOtherFlag,
       "sleRAGuardPolicyRouterPreference": sleRAGuardPolicyRouterPreference,
       "sleRAGuardPolicyMatchACLName": sleRAGuardPolicyMatchACLName,
       "sleRAGuardPolicyMatchPrefixName": sleRAGuardPolicyMatchPrefixName,
       "sleRAGuardPolicyControl": sleRAGuardPolicyControl,
       "sleRAGuardPolicyControlRequest": sleRAGuardPolicyControlRequest,
       "sleRAGuardPolicyControlStatus": sleRAGuardPolicyControlStatus,
       "sleRAGuardPolicyControlTimer": sleRAGuardPolicyControlTimer,
       "sleRAGuardPolicyControlTimeStamp": sleRAGuardPolicyControlTimeStamp,
       "sleRAGuardPolicyControlReqResult": sleRAGuardPolicyControlReqResult,
       "sleRAGuardPolicyControlIndex": sleRAGuardPolicyControlIndex,
       "sleRAGuardPolicyControlName": sleRAGuardPolicyControlName,
       "sleRAGuardPolicyControlHoplimitMin": sleRAGuardPolicyControlHoplimitMin,
       "sleRAGuardPolicyControlHoplimitMax": sleRAGuardPolicyControlHoplimitMax,
       "sleRAGuardPolicyControlManagedFlag": sleRAGuardPolicyControlManagedFlag,
       "sleRAGuardPolicyControlOtherFlag": sleRAGuardPolicyControlOtherFlag,
       "sleRAGuardPolicyControlRouterPreference": sleRAGuardPolicyControlRouterPreference,
       "sleRAGuardPolicyControlMatchACLName": sleRAGuardPolicyControlMatchACLName,
       "sleRAGuardPolicyControlMatchPrefixName": sleRAGuardPolicyControlMatchPrefixName,
       "sleRAGuardPolicyNotifications": sleRAGuardPolicyNotifications,
       "sleRAGuardPolicyCreated": sleRAGuardPolicyCreated,
       "sleRAGuardPolicyDestroyed": sleRAGuardPolicyDestroyed,
       "sleRAGuardPolicyChanged": sleRAGuardPolicyChanged,
       "sleRAGuardVlan": sleRAGuardVlan,
       "sleRAGuardVlanTable": sleRAGuardVlanTable,
       "sleRAGuardVlanEntry": sleRAGuardVlanEntry,
       "sleRAGuardVlanIndex": sleRAGuardVlanIndex,
       "sleRAGuardVlanEnable": sleRAGuardVlanEnable,
       "sleRAGuardVlanFilterPolicy": sleRAGuardVlanFilterPolicy,
       "sleRAGuardVlanFilterAclName": sleRAGuardVlanFilterAclName,
       "sleRAGuardVlanControl": sleRAGuardVlanControl,
       "sleRAGuardVlanControlRequest": sleRAGuardVlanControlRequest,
       "sleRAGuardVlanControlStatus": sleRAGuardVlanControlStatus,
       "sleRAGuardVlanControlTimer": sleRAGuardVlanControlTimer,
       "sleRAGuardVlanControlTimeStamp": sleRAGuardVlanControlTimeStamp,
       "sleRAGuardVlanControlReqResult": sleRAGuardVlanControlReqResult,
       "sleRAGuardVlanControlIndex": sleRAGuardVlanControlIndex,
       "sleRAGuardVlanControlEnable": sleRAGuardVlanControlEnable,
       "sleRAGuardVlanControlFilterPolicy": sleRAGuardVlanControlFilterPolicy,
       "sleRAGuardVlanNotifications": sleRAGuardVlanNotifications,
       "sleRAGuardVlanChanged": sleRAGuardVlanChanged,
       "sleRAGuardPort": sleRAGuardPort,
       "sleRAGuardPortTable": sleRAGuardPortTable,
       "sleRAGuardPortEntry": sleRAGuardPortEntry,
       "sleRAGuardPortIndex": sleRAGuardPortIndex,
       "sleRAGuardPortTrust": sleRAGuardPortTrust,
       "sleRAGuardPortControl": sleRAGuardPortControl,
       "sleRAGuardPortControlRequest": sleRAGuardPortControlRequest,
       "sleRAGuardPortControlStatus": sleRAGuardPortControlStatus,
       "sleRAGuardPortControlTimer": sleRAGuardPortControlTimer,
       "sleRAGuardPortControlTimeStamp": sleRAGuardPortControlTimeStamp,
       "sleRAGuardPortControlReqResult": sleRAGuardPortControlReqResult,
       "sleRAGuardPortControlIndex": sleRAGuardPortControlIndex,
       "sleRAGuardPortControlTrust": sleRAGuardPortControlTrust,
       "sleRAGuardPortNotifications": sleRAGuardPortNotifications,
       "sleRAGuardPortChanged": sleRAGuardPortChanged,
       "sleRadiusServerDot1x": sleRadiusServerDot1x,
       "sleRadiusServerDot1xTable": sleRadiusServerDot1xTable,
       "sleRadiusServerDot1xEntry": sleRadiusServerDot1xEntry,
       "sleRadiusServerDot1xAddress": sleRadiusServerDot1xAddress,
       "sleRadiusServerDot1xAuthPort": sleRadiusServerDot1xAuthPort,
       "sleRadiusServerDot1xTimeout": sleRadiusServerDot1xTimeout,
       "sleRadiusServerDot1xRetransmit": sleRadiusServerDot1xRetransmit,
       "sleRadiusServerDot1xClientKey": sleRadiusServerDot1xClientKey,
       "sleRadiusServerDot1xControl": sleRadiusServerDot1xControl,
       "sleRadiusServerDot1xControlRequest": sleRadiusServerDot1xControlRequest,
       "sleRadiusServerDot1xControlStatus": sleRadiusServerDot1xControlStatus,
       "sleRadiusServerDot1xControlTimer": sleRadiusServerDot1xControlTimer,
       "sleRadiusServerDot1xControlTimeStamp": sleRadiusServerDot1xControlTimeStamp,
       "sleRadiusServerDot1xControlReqResult": sleRadiusServerDot1xControlReqResult,
       "sleRadiusServerDot1xControlAddress": sleRadiusServerDot1xControlAddress,
       "sleRadiusServerDot1xControlAuthPort": sleRadiusServerDot1xControlAuthPort,
       "sleRadiusServerDot1xControlTimeout": sleRadiusServerDot1xControlTimeout,
       "sleRadiusServerDot1xControlRetransmit": sleRadiusServerDot1xControlRetransmit,
       "sleRadiusServerDot1xControlClientKey": sleRadiusServerDot1xControlClientKey,
       "sleKeyChain": sleKeyChain,
       "sleKeyChainTable": sleKeyChainTable,
       "sleKeyChainEntry": sleKeyChainEntry,
       "sleKeyChainName": sleKeyChainName,
       "sleKeyChainKeyId": sleKeyChainKeyId,
       "sleKeyChainKeyString": sleKeyChainKeyString,
       "sleKeyChainKeyAccepLifeTimeStartTime": sleKeyChainKeyAccepLifeTimeStartTime,
       "sleKeyChainKeyAcceptLifeTimeStartDay": sleKeyChainKeyAcceptLifeTimeStartDay,
       "sleKeyChainKeyAcceptLifeTimeStartMonth": sleKeyChainKeyAcceptLifeTimeStartMonth,
       "sleKeyChainKeyAcceptLifeTimeStartYear": sleKeyChainKeyAcceptLifeTimeStartYear,
       "sleKeyChainKeyAcceptLifeTimeExpireType": sleKeyChainKeyAcceptLifeTimeExpireType,
       "sleKeyChainKeyAcceptLifeTimeExpireTime": sleKeyChainKeyAcceptLifeTimeExpireTime,
       "sleKeyChainKeyAcceptLifeTimeExpireDay": sleKeyChainKeyAcceptLifeTimeExpireDay,
       "sleKeyChainKeyAcceptLifeTimeExpireMonth": sleKeyChainKeyAcceptLifeTimeExpireMonth,
       "sleKeyChainKeyAcceptLifeTimeExpireYear": sleKeyChainKeyAcceptLifeTimeExpireYear,
       "sleKeyChainKeySendLifeTimeStartTime": sleKeyChainKeySendLifeTimeStartTime,
       "sleKeyChainKeySendLifeTimeStartDay": sleKeyChainKeySendLifeTimeStartDay,
       "sleKeyChainKeySendLifeTimeStartMonth": sleKeyChainKeySendLifeTimeStartMonth,
       "sleKeyChainKeySendLifeTimeStartYear": sleKeyChainKeySendLifeTimeStartYear,
       "sleKeyChainKeySendLifeTimeExpireType": sleKeyChainKeySendLifeTimeExpireType,
       "sleKeyChainKeySendLifeTimeExpireTime": sleKeyChainKeySendLifeTimeExpireTime,
       "sleKeyChainKeySendLifeTimeExpireDay": sleKeyChainKeySendLifeTimeExpireDay,
       "sleKeyChainKeySendLifeTimeExpireMonth": sleKeyChainKeySendLifeTimeExpireMonth,
       "sleKeyChainKeySendLifeTimeExpireYear": sleKeyChainKeySendLifeTimeExpireYear,
       "sleKeyChainControl": sleKeyChainControl,
       "sleKeyChainControlRequest": sleKeyChainControlRequest,
       "sleKeyChainControlStatus": sleKeyChainControlStatus,
       "sleKeyChainControlTimer": sleKeyChainControlTimer,
       "sleKeyChainControlTimeStamp": sleKeyChainControlTimeStamp,
       "sleKeyChainControlReqResult": sleKeyChainControlReqResult,
       "sleKeyChainControlName": sleKeyChainControlName,
       "sleKeyChainControlKeyId": sleKeyChainControlKeyId,
       "sleKeyChainControlKeyString": sleKeyChainControlKeyString,
       "sleKeyChainControlKeyAcceptLifeTimeStartTime": sleKeyChainControlKeyAcceptLifeTimeStartTime,
       "sleKeyChainControlKeyAcceptLifeTimeStartDay": sleKeyChainControlKeyAcceptLifeTimeStartDay,
       "sleKeyChainControlKeyAcceptLifeTimeStartMonth": sleKeyChainControlKeyAcceptLifeTimeStartMonth,
       "sleKeyChainControlKeyAcceptLifeTimeStartYear": sleKeyChainControlKeyAcceptLifeTimeStartYear,
       "sleKeyChainControlKeyAcceptLifeTimeExpireType": sleKeyChainControlKeyAcceptLifeTimeExpireType,
       "sleKeyChainControlKeyAcceptLifeTimeExpireTime": sleKeyChainControlKeyAcceptLifeTimeExpireTime,
       "sleKeyChainControlKeyAcceptLifeTimeExpireDay": sleKeyChainControlKeyAcceptLifeTimeExpireDay,
       "sleKeyChainControlKeyAcceptLifeTimeExpireMonth": sleKeyChainControlKeyAcceptLifeTimeExpireMonth,
       "sleKeyChainControlKeyAcceptLifeTimeExpireYear": sleKeyChainControlKeyAcceptLifeTimeExpireYear,
       "sleKeyChainControlKeySendLifeTimeStartTime": sleKeyChainControlKeySendLifeTimeStartTime,
       "sleKeyChainControlKeySendLifeTimeStartDay": sleKeyChainControlKeySendLifeTimeStartDay,
       "sleKeyChainControlKeySendLifeTimeStartMonth": sleKeyChainControlKeySendLifeTimeStartMonth,
       "sleKeyChainControlKeySendLifeTimeStartYear": sleKeyChainControlKeySendLifeTimeStartYear,
       "sleKeyChainControlKeySendLifeTimeExpireType": sleKeyChainControlKeySendLifeTimeExpireType,
       "sleKeyChainControlKeySendLifeTimeExpireTime": sleKeyChainControlKeySendLifeTimeExpireTime,
       "sleKeyChainControlKeySendLifeTimeExpireDay": sleKeyChainControlKeySendLifeTimeExpireDay,
       "sleKeyChainControlKeySendLifeTimeExpireMonth": sleKeyChainControlKeySendLifeTimeExpireMonth,
       "sleKeyChainControlKeySendLifeTimeExpireYear": sleKeyChainControlKeySendLifeTimeExpireYear,
       "sleSecurityGroup": sleSecurityGroup,
       "sleSecurityNotificationGroup": sleSecurityNotificationGroup}
)
