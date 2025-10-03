# SNMP MIB module (SLE-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:26 2025
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

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleDhcpSnooping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12)
)
if mibBuilder.loadTexts:
    sleDhcpSnooping.setRevisions(
        ("2005-07-29 14:25",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleGlobal_ObjectIdentity = ObjectIdentity
sleGlobal = _SleGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1)
)
_SleGlobalInfo_ObjectIdentity = ObjectIdentity
sleGlobalInfo = _SleGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 1)
)


class _SleFeatureEnable_Type(Integer32):
    """Custom type sleFeatureEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SleFeatureEnable_Type.__name__ = "Integer32"
_SleFeatureEnable_Object = MibScalar
sleFeatureEnable = _SleFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 1, 1),
    _SleFeatureEnable_Type()
)
sleFeatureEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFeatureEnable.setStatus("current")
_SleGlobalControl_ObjectIdentity = ObjectIdentity
sleGlobalControl = _SleGlobalControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 2)
)


class _SleGlobalControlRequest_Type(Integer32):
    """Custom type sleGlobalControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setSnoopingEnable", 1)
    )


_SleGlobalControlRequest_Type.__name__ = "Integer32"
_SleGlobalControlRequest_Object = MibScalar
sleGlobalControlRequest = _SleGlobalControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 2, 1),
    _SleGlobalControlRequest_Type()
)
sleGlobalControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleGlobalControlRequest.setStatus("current")
_SleGlobalControlStatus_Type = SleControlStatusType
_SleGlobalControlStatus_Object = MibScalar
sleGlobalControlStatus = _SleGlobalControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 2, 2),
    _SleGlobalControlStatus_Type()
)
sleGlobalControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleGlobalControlStatus.setStatus("current")
_SleGlobalControlTimer_Type = Gauge32
_SleGlobalControlTimer_Object = MibScalar
sleGlobalControlTimer = _SleGlobalControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 2, 3),
    _SleGlobalControlTimer_Type()
)
sleGlobalControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleGlobalControlTimer.setStatus("current")
_SleGlobalControlTimeStamp_Type = TimeTicks
_SleGlobalControlTimeStamp_Object = MibScalar
sleGlobalControlTimeStamp = _SleGlobalControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 2, 4),
    _SleGlobalControlTimeStamp_Type()
)
sleGlobalControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleGlobalControlTimeStamp.setStatus("current")
_SleGlobalControlReqResult_Type = SleControlRequestResultType
_SleGlobalControlReqResult_Object = MibScalar
sleGlobalControlReqResult = _SleGlobalControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 2, 5),
    _SleGlobalControlReqResult_Type()
)
sleGlobalControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleGlobalControlReqResult.setStatus("current")


class _SleGlobalControlFeatureEnable_Type(Integer32):
    """Custom type sleGlobalControlFeatureEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_SleGlobalControlFeatureEnable_Type.__name__ = "Integer32"
_SleGlobalControlFeatureEnable_Object = MibScalar
sleGlobalControlFeatureEnable = _SleGlobalControlFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 2, 6),
    _SleGlobalControlFeatureEnable_Type()
)
sleGlobalControlFeatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleGlobalControlFeatureEnable.setStatus("current")
_SleGlobalNotification_ObjectIdentity = ObjectIdentity
sleGlobalNotification = _SleGlobalNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 3)
)
_SlePortSrcGuard_ObjectIdentity = ObjectIdentity
slePortSrcGuard = _SlePortSrcGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2)
)
_SlePortSrcGuardConfig_ObjectIdentity = ObjectIdentity
slePortSrcGuardConfig = _SlePortSrcGuardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1)
)
_SlePortSrcGuardConfigTable_Object = MibTable
slePortSrcGuardConfigTable = _SlePortSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    slePortSrcGuardConfigTable.setStatus("current")
_SlePortSrcGuardConfigEntry_Object = MibTableRow
slePortSrcGuardConfigEntry = _SlePortSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 1, 1)
)
slePortSrcGuardConfigEntry.setIndexNames(
    (0, "SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardIndex"),
)
if mibBuilder.loadTexts:
    slePortSrcGuardConfigEntry.setStatus("current")
_SlePortSrcGuardIndex_Type = Integer32
_SlePortSrcGuardIndex_Object = MibTableColumn
slePortSrcGuardIndex = _SlePortSrcGuardIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 1, 1, 1),
    _SlePortSrcGuardIndex_Type()
)
slePortSrcGuardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardIndex.setStatus("current")


class _SlePortSrcGuardEnable_Type(Integer32):
    """Custom type slePortSrcGuardEnable based on Integer32"""
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


_SlePortSrcGuardEnable_Type.__name__ = "Integer32"
_SlePortSrcGuardEnable_Object = MibTableColumn
slePortSrcGuardEnable = _SlePortSrcGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 1, 1, 2),
    _SlePortSrcGuardEnable_Type()
)
slePortSrcGuardEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardEnable.setStatus("current")
_SlePortSrcGuardConfigControl_ObjectIdentity = ObjectIdentity
slePortSrcGuardConfigControl = _SlePortSrcGuardConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 2)
)


class _SlePortSrcGuardConfigControlRequest_Type(Integer32):
    """Custom type slePortSrcGuardConfigControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setPortSrcGuardConfig", 1)
    )


_SlePortSrcGuardConfigControlRequest_Type.__name__ = "Integer32"
_SlePortSrcGuardConfigControlRequest_Object = MibScalar
slePortSrcGuardConfigControlRequest = _SlePortSrcGuardConfigControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 2, 1),
    _SlePortSrcGuardConfigControlRequest_Type()
)
slePortSrcGuardConfigControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardConfigControlRequest.setStatus("current")
_SlePortSrcGuardConfigControlStatus_Type = SleControlStatusType
_SlePortSrcGuardConfigControlStatus_Object = MibScalar
slePortSrcGuardConfigControlStatus = _SlePortSrcGuardConfigControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 2, 2),
    _SlePortSrcGuardConfigControlStatus_Type()
)
slePortSrcGuardConfigControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardConfigControlStatus.setStatus("current")
_SlePortSrcGuardConfigControlTimer_Type = Gauge32
_SlePortSrcGuardConfigControlTimer_Object = MibScalar
slePortSrcGuardConfigControlTimer = _SlePortSrcGuardConfigControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 2, 3),
    _SlePortSrcGuardConfigControlTimer_Type()
)
slePortSrcGuardConfigControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardConfigControlTimer.setStatus("current")
_SlePortSrcGuardConfigControlTimeStamp_Type = TimeTicks
_SlePortSrcGuardConfigControlTimeStamp_Object = MibScalar
slePortSrcGuardConfigControlTimeStamp = _SlePortSrcGuardConfigControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 2, 4),
    _SlePortSrcGuardConfigControlTimeStamp_Type()
)
slePortSrcGuardConfigControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardConfigControlTimeStamp.setStatus("current")
_SlePortSrcGuardConfigControlReqResult_Type = SleControlRequestResultType
_SlePortSrcGuardConfigControlReqResult_Object = MibScalar
slePortSrcGuardConfigControlReqResult = _SlePortSrcGuardConfigControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 2, 5),
    _SlePortSrcGuardConfigControlReqResult_Type()
)
slePortSrcGuardConfigControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardConfigControlReqResult.setStatus("current")
_SlePortSrcGuardConfigControlIndex_Type = Integer32
_SlePortSrcGuardConfigControlIndex_Object = MibScalar
slePortSrcGuardConfigControlIndex = _SlePortSrcGuardConfigControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 2, 6),
    _SlePortSrcGuardConfigControlIndex_Type()
)
slePortSrcGuardConfigControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardConfigControlIndex.setStatus("current")


class _SlePortSrcGuardConfigControlEnable_Type(Integer32):
    """Custom type slePortSrcGuardConfigControlEnable based on Integer32"""
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


_SlePortSrcGuardConfigControlEnable_Type.__name__ = "Integer32"
_SlePortSrcGuardConfigControlEnable_Object = MibScalar
slePortSrcGuardConfigControlEnable = _SlePortSrcGuardConfigControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 2, 7),
    _SlePortSrcGuardConfigControlEnable_Type()
)
slePortSrcGuardConfigControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardConfigControlEnable.setStatus("current")
_SlePortSrcGuardConfigNotification_ObjectIdentity = ObjectIdentity
slePortSrcGuardConfigNotification = _SlePortSrcGuardConfigNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 3)
)
_SlePortSrcGuardAddress_ObjectIdentity = ObjectIdentity
slePortSrcGuardAddress = _SlePortSrcGuardAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2)
)
_SlePortSrcGuardAddressTable_Object = MibTable
slePortSrcGuardAddressTable = _SlePortSrcGuardAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    slePortSrcGuardAddressTable.setStatus("current")
_SlePortSrcGuardAddressEntry_Object = MibTableRow
slePortSrcGuardAddressEntry = _SlePortSrcGuardAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 1, 1)
)
slePortSrcGuardAddressEntry.setIndexNames(
    (0, "SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardIndex"),
    (0, "SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressIp"),
)
if mibBuilder.loadTexts:
    slePortSrcGuardAddressEntry.setStatus("current")
_SlePortSrcGuardAddressIp_Type = IpAddress
_SlePortSrcGuardAddressIp_Object = MibTableColumn
slePortSrcGuardAddressIp = _SlePortSrcGuardAddressIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 1, 1, 1),
    _SlePortSrcGuardAddressIp_Type()
)
slePortSrcGuardAddressIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressIp.setStatus("current")
_SlePortSrcGuardAddressMask_Type = IpAddress
_SlePortSrcGuardAddressMask_Object = MibTableColumn
slePortSrcGuardAddressMask = _SlePortSrcGuardAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 1, 1, 2),
    _SlePortSrcGuardAddressMask_Type()
)
slePortSrcGuardAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressMask.setStatus("current")
_SlePortSrcGuardAddressMac_Type = MacAddress
_SlePortSrcGuardAddressMac_Object = MibTableColumn
slePortSrcGuardAddressMac = _SlePortSrcGuardAddressMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 1, 1, 3),
    _SlePortSrcGuardAddressMac_Type()
)
slePortSrcGuardAddressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressMac.setStatus("current")
_SlePortSrcGuardAddressLease_Type = Integer32
_SlePortSrcGuardAddressLease_Object = MibTableColumn
slePortSrcGuardAddressLease = _SlePortSrcGuardAddressLease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 1, 1, 4),
    _SlePortSrcGuardAddressLease_Type()
)
slePortSrcGuardAddressLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressLease.setStatus("current")
_SlePortSrcGuardAddressControl_ObjectIdentity = ObjectIdentity
slePortSrcGuardAddressControl = _SlePortSrcGuardAddressControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2)
)


class _SlePortSrcGuardAddressControlRequest_Type(Integer32):
    """Custom type slePortSrcGuardAddressControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createPortSrcGuardAddress", 1),
          ("destroyPortSrcGuardAddress", 2))
    )


_SlePortSrcGuardAddressControlRequest_Type.__name__ = "Integer32"
_SlePortSrcGuardAddressControlRequest_Object = MibScalar
slePortSrcGuardAddressControlRequest = _SlePortSrcGuardAddressControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2, 1),
    _SlePortSrcGuardAddressControlRequest_Type()
)
slePortSrcGuardAddressControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressControlRequest.setStatus("current")
_SlePortSrcGuardAddressControlStatus_Type = SleControlStatusType
_SlePortSrcGuardAddressControlStatus_Object = MibScalar
slePortSrcGuardAddressControlStatus = _SlePortSrcGuardAddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2, 2),
    _SlePortSrcGuardAddressControlStatus_Type()
)
slePortSrcGuardAddressControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressControlStatus.setStatus("current")
_SlePortSrcGuardAddressControlTimer_Type = Gauge32
_SlePortSrcGuardAddressControlTimer_Object = MibScalar
slePortSrcGuardAddressControlTimer = _SlePortSrcGuardAddressControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2, 3),
    _SlePortSrcGuardAddressControlTimer_Type()
)
slePortSrcGuardAddressControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressControlTimer.setStatus("current")
_SlePortSrcGuardAddressControlTimeStamp_Type = TimeTicks
_SlePortSrcGuardAddressControlTimeStamp_Object = MibScalar
slePortSrcGuardAddressControlTimeStamp = _SlePortSrcGuardAddressControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2, 4),
    _SlePortSrcGuardAddressControlTimeStamp_Type()
)
slePortSrcGuardAddressControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressControlTimeStamp.setStatus("current")
_SlePortSrcGuardAddressControlReqResult_Type = SleControlRequestResultType
_SlePortSrcGuardAddressControlReqResult_Object = MibScalar
slePortSrcGuardAddressControlReqResult = _SlePortSrcGuardAddressControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2, 5),
    _SlePortSrcGuardAddressControlReqResult_Type()
)
slePortSrcGuardAddressControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressControlReqResult.setStatus("current")
_SlePortSrcGuardAddressControlIndex_Type = InterfaceIndex
_SlePortSrcGuardAddressControlIndex_Object = MibScalar
slePortSrcGuardAddressControlIndex = _SlePortSrcGuardAddressControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2, 6),
    _SlePortSrcGuardAddressControlIndex_Type()
)
slePortSrcGuardAddressControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressControlIndex.setStatus("current")
_SlePortSrcGuardAddressControlIp_Type = IpAddress
_SlePortSrcGuardAddressControlIp_Object = MibScalar
slePortSrcGuardAddressControlIp = _SlePortSrcGuardAddressControlIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2, 7),
    _SlePortSrcGuardAddressControlIp_Type()
)
slePortSrcGuardAddressControlIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressControlIp.setStatus("current")
_SlePortSrcGuardAddressControlMask_Type = IpAddress
_SlePortSrcGuardAddressControlMask_Object = MibScalar
slePortSrcGuardAddressControlMask = _SlePortSrcGuardAddressControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 2, 8),
    _SlePortSrcGuardAddressControlMask_Type()
)
slePortSrcGuardAddressControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePortSrcGuardAddressControlMask.setStatus("current")
_SlePortSrcGuardAddressNotification_ObjectIdentity = ObjectIdentity
slePortSrcGuardAddressNotification = _SlePortSrcGuardAddressNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 3)
)

# Managed Objects groups


# Notification objects

sleGlobalFeatureEnableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 1, 3, 1)
)
sleGlobalFeatureEnableChanged.setObjects(
      *(("SLE-DHCP-SNOOPING-MIB", "sleGlobalControlRequest"),
        ("SLE-DHCP-SNOOPING-MIB", "sleGlobalControlTimeStamp"),
        ("SLE-DHCP-SNOOPING-MIB", "sleGlobalControlReqResult"),
        ("SLE-DHCP-SNOOPING-MIB", "sleFeatureEnable"))
)
if mibBuilder.loadTexts:
    sleGlobalFeatureEnableChanged.setStatus(
        "current"
    )

slePortSrcGuardConfigEnableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 1, 3, 1)
)
slePortSrcGuardConfigEnableChanged.setObjects(
      *(("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardConfigControlRequest"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardConfigControlTImeStamp"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardConfigControlReqResult"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardEnable"))
)
if mibBuilder.loadTexts:
    slePortSrcGuardConfigEnableChanged.setStatus(
        "current"
    )

slePortSrcGuardAddressCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 3, 1)
)
slePortSrcGuardAddressCreated.setObjects(
      *(("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressControlRequest"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressControlTImeStamp"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressControlReqResult"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressIp"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressMask"))
)
if mibBuilder.loadTexts:
    slePortSrcGuardAddressCreated.setStatus(
        "current"
    )

slePortSrcGuardAddressDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 12, 2, 2, 3, 2)
)
slePortSrcGuardAddressDestroyed.setObjects(
      *(("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressControlRequest"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressControlTImeStamp"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressControlReqResult"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressIp"),
        ("SLE-DHCP-SNOOPING-MIB", "slePortSrcGuardAddressMask"))
)
if mibBuilder.loadTexts:
    slePortSrcGuardAddressDestroyed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-DHCP-SNOOPING-MIB",
    **{"sleDhcpSnooping": sleDhcpSnooping,
       "sleGlobal": sleGlobal,
       "sleGlobalInfo": sleGlobalInfo,
       "sleFeatureEnable": sleFeatureEnable,
       "sleGlobalControl": sleGlobalControl,
       "sleGlobalControlRequest": sleGlobalControlRequest,
       "sleGlobalControlStatus": sleGlobalControlStatus,
       "sleGlobalControlTimer": sleGlobalControlTimer,
       "sleGlobalControlTimeStamp": sleGlobalControlTimeStamp,
       "sleGlobalControlReqResult": sleGlobalControlReqResult,
       "sleGlobalControlFeatureEnable": sleGlobalControlFeatureEnable,
       "sleGlobalNotification": sleGlobalNotification,
       "sleGlobalFeatureEnableChanged": sleGlobalFeatureEnableChanged,
       "slePortSrcGuard": slePortSrcGuard,
       "slePortSrcGuardConfig": slePortSrcGuardConfig,
       "slePortSrcGuardConfigTable": slePortSrcGuardConfigTable,
       "slePortSrcGuardConfigEntry": slePortSrcGuardConfigEntry,
       "slePortSrcGuardIndex": slePortSrcGuardIndex,
       "slePortSrcGuardEnable": slePortSrcGuardEnable,
       "slePortSrcGuardConfigControl": slePortSrcGuardConfigControl,
       "slePortSrcGuardConfigControlRequest": slePortSrcGuardConfigControlRequest,
       "slePortSrcGuardConfigControlStatus": slePortSrcGuardConfigControlStatus,
       "slePortSrcGuardConfigControlTimer": slePortSrcGuardConfigControlTimer,
       "slePortSrcGuardConfigControlTimeStamp": slePortSrcGuardConfigControlTimeStamp,
       "slePortSrcGuardConfigControlReqResult": slePortSrcGuardConfigControlReqResult,
       "slePortSrcGuardConfigControlIndex": slePortSrcGuardConfigControlIndex,
       "slePortSrcGuardConfigControlEnable": slePortSrcGuardConfigControlEnable,
       "slePortSrcGuardConfigNotification": slePortSrcGuardConfigNotification,
       "slePortSrcGuardConfigEnableChanged": slePortSrcGuardConfigEnableChanged,
       "slePortSrcGuardAddress": slePortSrcGuardAddress,
       "slePortSrcGuardAddressTable": slePortSrcGuardAddressTable,
       "slePortSrcGuardAddressEntry": slePortSrcGuardAddressEntry,
       "slePortSrcGuardAddressIp": slePortSrcGuardAddressIp,
       "slePortSrcGuardAddressMask": slePortSrcGuardAddressMask,
       "slePortSrcGuardAddressMac": slePortSrcGuardAddressMac,
       "slePortSrcGuardAddressLease": slePortSrcGuardAddressLease,
       "slePortSrcGuardAddressControl": slePortSrcGuardAddressControl,
       "slePortSrcGuardAddressControlRequest": slePortSrcGuardAddressControlRequest,
       "slePortSrcGuardAddressControlStatus": slePortSrcGuardAddressControlStatus,
       "slePortSrcGuardAddressControlTimer": slePortSrcGuardAddressControlTimer,
       "slePortSrcGuardAddressControlTimeStamp": slePortSrcGuardAddressControlTimeStamp,
       "slePortSrcGuardAddressControlReqResult": slePortSrcGuardAddressControlReqResult,
       "slePortSrcGuardAddressControlIndex": slePortSrcGuardAddressControlIndex,
       "slePortSrcGuardAddressControlIp": slePortSrcGuardAddressControlIp,
       "slePortSrcGuardAddressControlMask": slePortSrcGuardAddressControlMask,
       "slePortSrcGuardAddressNotification": slePortSrcGuardAddressNotification,
       "slePortSrcGuardAddressCreated": slePortSrcGuardAddressCreated,
       "slePortSrcGuardAddressDestroyed": slePortSrcGuardAddressDestroyed}
)
