# SNMP MIB module (DLINKSW-DAI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DAI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:45 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(Dlink2kVlanList,) = mibBuilder.importSymbols(
    "DLINKSW-TC-MIB",
    "Dlink2kVlanList")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwDynamicArpInspectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130)
)
if mibBuilder.loadTexts:
    dlinkSwDynamicArpInspectionMIB.setRevisions(
        ("2013-07-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DaiRuleType(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_DDaiNotifications_ObjectIdentity = ObjectIdentity
dDaiNotifications = _DDaiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 0)
)
_DDaiObjects_ObjectIdentity = ObjectIdentity
dDaiObjects = _DDaiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1)
)
_DDaiGlobal_ObjectIdentity = ObjectIdentity
dDaiGlobal = _DDaiGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1)
)


class _DDaiAddressValidate_Type(Bits):
    """Custom type dDaiAddressValidate based on Bits"""
    namedValues = NamedValues(
        *(("srcMacAddress", 0),
          ("dstMacAddress", 1),
          ("ip", 2))
    )

_DDaiAddressValidate_Type.__name__ = "Bits"
_DDaiAddressValidate_Object = MibScalar
dDaiAddressValidate = _DDaiAddressValidate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 1),
    _DDaiAddressValidate_Type()
)
dDaiAddressValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiAddressValidate.setStatus("current")
_DDaiLogBufferSize_Type = Unsigned32
_DDaiLogBufferSize_Object = MibScalar
dDaiLogBufferSize = _DDaiLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 2),
    _DDaiLogBufferSize_Type()
)
dDaiLogBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiLogBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    dDaiLogBufferSize.setUnits("entries")


class _DDaiClearLogBuffer_Type(Integer32):
    """Custom type dDaiClearLogBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DDaiClearLogBuffer_Type.__name__ = "Integer32"
_DDaiClearLogBuffer_Object = MibScalar
dDaiClearLogBuffer = _DDaiClearLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 3),
    _DDaiClearLogBuffer_Type()
)
dDaiClearLogBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiClearLogBuffer.setStatus("current")
_DDaiLogBufferTable_Object = MibTable
dDaiLogBufferTable = _DDaiLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dDaiLogBufferTable.setStatus("current")
_DDaiLogBufferEntry_Object = MibTableRow
dDaiLogBufferEntry = _DDaiLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4, 1)
)
dDaiLogBufferEntry.setIndexNames(
    (0, "DLINKSW-DAI-MIB", "dDaiLogBufferIndex"),
)
if mibBuilder.loadTexts:
    dDaiLogBufferEntry.setStatus("current")


class _DDaiLogBufferIndex_Type(Unsigned32):
    """Custom type dDaiLogBufferIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DDaiLogBufferIndex_Type.__name__ = "Unsigned32"
_DDaiLogBufferIndex_Object = MibTableColumn
dDaiLogBufferIndex = _DDaiLogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4, 1, 1),
    _DDaiLogBufferIndex_Type()
)
dDaiLogBufferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDaiLogBufferIndex.setStatus("current")
_DDaiLogBufferInterface_Type = InterfaceIndex
_DDaiLogBufferInterface_Object = MibTableColumn
dDaiLogBufferInterface = _DDaiLogBufferInterface_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4, 1, 2),
    _DDaiLogBufferInterface_Type()
)
dDaiLogBufferInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiLogBufferInterface.setStatus("current")
_DDaiLogBufferVlan_Type = VlanIdOrNone
_DDaiLogBufferVlan_Object = MibTableColumn
dDaiLogBufferVlan = _DDaiLogBufferVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4, 1, 3),
    _DDaiLogBufferVlan_Type()
)
dDaiLogBufferVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiLogBufferVlan.setStatus("current")
_DDaiLogBufferSenderMacAddress_Type = MacAddress
_DDaiLogBufferSenderMacAddress_Object = MibTableColumn
dDaiLogBufferSenderMacAddress = _DDaiLogBufferSenderMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4, 1, 4),
    _DDaiLogBufferSenderMacAddress_Type()
)
dDaiLogBufferSenderMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiLogBufferSenderMacAddress.setStatus("current")
_DDaiLogBufferSenderIpAddress_Type = InetAddressIPv4
_DDaiLogBufferSenderIpAddress_Object = MibTableColumn
dDaiLogBufferSenderIpAddress = _DDaiLogBufferSenderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4, 1, 5),
    _DDaiLogBufferSenderIpAddress_Type()
)
dDaiLogBufferSenderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiLogBufferSenderIpAddress.setStatus("current")
_DDaiLogBufferLastUpdate_Type = DateAndTime
_DDaiLogBufferLastUpdate_Object = MibTableColumn
dDaiLogBufferLastUpdate = _DDaiLogBufferLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4, 1, 6),
    _DDaiLogBufferLastUpdate_Type()
)
dDaiLogBufferLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiLogBufferLastUpdate.setStatus("current")
_DDaiLogBufferPacketsCount_Type = Gauge32
_DDaiLogBufferPacketsCount_Object = MibTableColumn
dDaiLogBufferPacketsCount = _DDaiLogBufferPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 1, 4, 1, 7),
    _DDaiLogBufferPacketsCount_Type()
)
dDaiLogBufferPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiLogBufferPacketsCount.setStatus("current")
_DDaiVlan_ObjectIdentity = ObjectIdentity
dDaiVlan = _DDaiVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2)
)
_DDaiVlanCrlFirst2K_Type = Dlink2kVlanList
_DDaiVlanCrlFirst2K_Object = MibScalar
dDaiVlanCrlFirst2K = _DDaiVlanCrlFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 1),
    _DDaiVlanCrlFirst2K_Type()
)
dDaiVlanCrlFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiVlanCrlFirst2K.setStatus("current")
_DDaiVlanCrlSecond2K_Type = Dlink2kVlanList
_DDaiVlanCrlSecond2K_Object = MibScalar
dDaiVlanCrlSecond2K = _DDaiVlanCrlSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 2),
    _DDaiVlanCrlSecond2K_Type()
)
dDaiVlanCrlSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiVlanCrlSecond2K.setStatus("current")
_DDaiVlanCfgTable_Object = MibTable
dDaiVlanCfgTable = _DDaiVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dDaiVlanCfgTable.setStatus("current")
_DDaiVlanCfgEntry_Object = MibTableRow
dDaiVlanCfgEntry = _DDaiVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 3, 1)
)
dDaiVlanCfgEntry.setIndexNames(
    (0, "DLINKSW-DAI-MIB", "dDaiVlanCfgId"),
)
if mibBuilder.loadTexts:
    dDaiVlanCfgEntry.setStatus("current")
_DDaiVlanCfgId_Type = VlanId
_DDaiVlanCfgId_Object = MibTableColumn
dDaiVlanCfgId = _DDaiVlanCfgId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 3, 1, 1),
    _DDaiVlanCfgId_Type()
)
dDaiVlanCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDaiVlanCfgId.setStatus("current")


class _DDaiVlanFilterArpAclName_Type(DisplayString):
    """Custom type dDaiVlanFilterArpAclName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDaiVlanFilterArpAclName_Type.__name__ = "DisplayString"
_DDaiVlanFilterArpAclName_Object = MibTableColumn
dDaiVlanFilterArpAclName = _DDaiVlanFilterArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 3, 1, 2),
    _DDaiVlanFilterArpAclName_Type()
)
dDaiVlanFilterArpAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiVlanFilterArpAclName.setStatus("current")


class _DDaiVlanFilterArpAclStatic_Type(TruthValue):
    """Custom type dDaiVlanFilterArpAclStatic based on TruthValue"""
    defaultValue = 2


_DDaiVlanFilterArpAclStatic_Type.__name__ = "TruthValue"
_DDaiVlanFilterArpAclStatic_Object = MibTableColumn
dDaiVlanFilterArpAclStatic = _DDaiVlanFilterArpAclStatic_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 3, 1, 3),
    _DDaiVlanFilterArpAclStatic_Type()
)
dDaiVlanFilterArpAclStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiVlanFilterArpAclStatic.setStatus("current")


class _DDaiVlanAclLogging_Type(Bits):
    """Custom type dDaiVlanAclLogging based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )

_DDaiVlanAclLogging_Type.__name__ = "Bits"
_DDaiVlanAclLogging_Object = MibTableColumn
dDaiVlanAclLogging = _DDaiVlanAclLogging_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 3, 1, 4),
    _DDaiVlanAclLogging_Type()
)
dDaiVlanAclLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiVlanAclLogging.setStatus("current")


class _DDaiVlanDhcpBindingLogging_Type(Bits):
    """Custom type dDaiVlanDhcpBindingLogging based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )

_DDaiVlanDhcpBindingLogging_Type.__name__ = "Bits"
_DDaiVlanDhcpBindingLogging_Object = MibTableColumn
dDaiVlanDhcpBindingLogging = _DDaiVlanDhcpBindingLogging_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 3, 1, 5),
    _DDaiVlanDhcpBindingLogging_Type()
)
dDaiVlanDhcpBindingLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiVlanDhcpBindingLogging.setStatus("current")
_DDaiVlanCfgRowStatus_Type = RowStatus
_DDaiVlanCfgRowStatus_Object = MibTableColumn
dDaiVlanCfgRowStatus = _DDaiVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 2, 3, 1, 99),
    _DDaiVlanCfgRowStatus_Type()
)
dDaiVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiVlanCfgRowStatus.setStatus("current")
_DDaiInterface_ObjectIdentity = ObjectIdentity
dDaiInterface = _DDaiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 3)
)
_DDaiIfConfigTable_Object = MibTable
dDaiIfConfigTable = _DDaiIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dDaiIfConfigTable.setStatus("current")
_DDaiIfConfigEntry_Object = MibTableRow
dDaiIfConfigEntry = _DDaiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 3, 1, 1)
)
dDaiIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDaiIfConfigEntry.setStatus("current")
_DDaiIfTrustEnabled_Type = TruthValue
_DDaiIfTrustEnabled_Object = MibTableColumn
dDaiIfTrustEnabled = _DDaiIfTrustEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 3, 1, 1, 1),
    _DDaiIfTrustEnabled_Type()
)
dDaiIfTrustEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiIfTrustEnabled.setStatus("current")
_DDaiIfRateLimitTable_Object = MibTable
dDaiIfRateLimitTable = _DDaiIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dDaiIfRateLimitTable.setStatus("current")
_DDaiIfRateLimitEntry_Object = MibTableRow
dDaiIfRateLimitEntry = _DDaiIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 3, 2, 1)
)
dDaiIfRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dDaiIfRateLimitEntry.setStatus("current")
_DDaiIfRateLimit_Type = Unsigned32
_DDaiIfRateLimit_Object = MibTableColumn
dDaiIfRateLimit = _DDaiIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 3, 2, 1, 1),
    _DDaiIfRateLimit_Type()
)
dDaiIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    dDaiIfRateLimit.setUnits("packet per second")
_DDaiIfBurstInterval_Type = Unsigned32
_DDaiIfBurstInterval_Object = MibTableColumn
dDaiIfBurstInterval = _DDaiIfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 3, 2, 1, 2),
    _DDaiIfBurstInterval_Type()
)
dDaiIfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiIfBurstInterval.setStatus("current")
if mibBuilder.loadTexts:
    dDaiIfBurstInterval.setUnits("second")
_DDaiStatistics_ObjectIdentity = ObjectIdentity
dDaiStatistics = _DDaiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4)
)
_DDaiVlanStatsTable_Object = MibTable
dDaiVlanStatsTable = _DDaiVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dDaiVlanStatsTable.setStatus("current")
_DDaiVlanStatsEntry_Object = MibTableRow
dDaiVlanStatsEntry = _DDaiVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1)
)
dDaiVlanStatsEntry.setIndexNames(
    (0, "DLINKSW-DAI-MIB", "dDaiVlanStatsIndex"),
)
if mibBuilder.loadTexts:
    dDaiVlanStatsEntry.setStatus("current")
_DDaiVlanStatsIndex_Type = VlanId
_DDaiVlanStatsIndex_Object = MibTableColumn
dDaiVlanStatsIndex = _DDaiVlanStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 1),
    _DDaiVlanStatsIndex_Type()
)
dDaiVlanStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDaiVlanStatsIndex.setStatus("current")
_DDaiVlanForwarded_Type = Counter64
_DDaiVlanForwarded_Object = MibTableColumn
dDaiVlanForwarded = _DDaiVlanForwarded_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 2),
    _DDaiVlanForwarded_Type()
)
dDaiVlanForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanForwarded.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanForwarded.setUnits("packets")
_DDaiVlanDropped_Type = Counter64
_DDaiVlanDropped_Object = MibTableColumn
dDaiVlanDropped = _DDaiVlanDropped_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 3),
    _DDaiVlanDropped_Type()
)
dDaiVlanDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanDropped.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanDropped.setUnits("packets")
_DDaiVlanAclPermitted_Type = Counter64
_DDaiVlanAclPermitted_Object = MibTableColumn
dDaiVlanAclPermitted = _DDaiVlanAclPermitted_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 4),
    _DDaiVlanAclPermitted_Type()
)
dDaiVlanAclPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanAclPermitted.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanAclPermitted.setUnits("packets")
_DDaiVlanDhcpBindingsPermitted_Type = Counter64
_DDaiVlanDhcpBindingsPermitted_Object = MibTableColumn
dDaiVlanDhcpBindingsPermitted = _DDaiVlanDhcpBindingsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 5),
    _DDaiVlanDhcpBindingsPermitted_Type()
)
dDaiVlanDhcpBindingsPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanDhcpBindingsPermitted.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanDhcpBindingsPermitted.setUnits("packets")
_DDaiVlanAclDenied_Type = Counter64
_DDaiVlanAclDenied_Object = MibTableColumn
dDaiVlanAclDenied = _DDaiVlanAclDenied_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 6),
    _DDaiVlanAclDenied_Type()
)
dDaiVlanAclDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanAclDenied.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanAclDenied.setUnits("packets")
_DDaiVlanDhcpBindingDenied_Type = Counter64
_DDaiVlanDhcpBindingDenied_Object = MibTableColumn
dDaiVlanDhcpBindingDenied = _DDaiVlanDhcpBindingDenied_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 7),
    _DDaiVlanDhcpBindingDenied_Type()
)
dDaiVlanDhcpBindingDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanDhcpBindingDenied.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanDhcpBindingDenied.setUnits("packets")
_DDaiVlanSrcMacValidationFailures_Type = Counter64
_DDaiVlanSrcMacValidationFailures_Object = MibTableColumn
dDaiVlanSrcMacValidationFailures = _DDaiVlanSrcMacValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 8),
    _DDaiVlanSrcMacValidationFailures_Type()
)
dDaiVlanSrcMacValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanSrcMacValidationFailures.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanSrcMacValidationFailures.setUnits("packets")
_DDaiVlanDstMacValidationFailures_Type = Counter64
_DDaiVlanDstMacValidationFailures_Object = MibTableColumn
dDaiVlanDstMacValidationFailures = _DDaiVlanDstMacValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 9),
    _DDaiVlanDstMacValidationFailures_Type()
)
dDaiVlanDstMacValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanDstMacValidationFailures.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanDstMacValidationFailures.setUnits("packets")
_DDaiVlanIpValidationFailures_Type = Counter64
_DDaiVlanIpValidationFailures_Object = MibTableColumn
dDaiVlanIpValidationFailures = _DDaiVlanIpValidationFailures_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 10),
    _DDaiVlanIpValidationFailures_Type()
)
dDaiVlanIpValidationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiVlanIpValidationFailures.setStatus("current")
if mibBuilder.loadTexts:
    dDaiVlanIpValidationFailures.setUnits("packets")


class _DDaiVlanStatsClear_Type(Integer32):
    """Custom type dDaiVlanStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DDaiVlanStatsClear_Type.__name__ = "Integer32"
_DDaiVlanStatsClear_Object = MibTableColumn
dDaiVlanStatsClear = _DDaiVlanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 1, 1, 99),
    _DDaiVlanStatsClear_Type()
)
dDaiVlanStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiVlanStatsClear.setStatus("current")


class _DDaiVlanStatsClearAll_Type(Integer32):
    """Custom type dDaiVlanStatsClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DDaiVlanStatsClearAll_Type.__name__ = "Integer32"
_DDaiVlanStatsClearAll_Object = MibScalar
dDaiVlanStatsClearAll = _DDaiVlanStatsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 4, 2),
    _DDaiVlanStatsClearAll_Type()
)
dDaiVlanStatsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDaiVlanStatsClearAll.setStatus("current")
_DDaiAclCfg_ObjectIdentity = ObjectIdentity
dDaiAclCfg = _DDaiAclCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5)
)
_DDaiArpAccessListNumber_Type = Unsigned32
_DDaiArpAccessListNumber_Object = MibScalar
dDaiArpAccessListNumber = _DDaiArpAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 1),
    _DDaiArpAccessListNumber_Type()
)
dDaiArpAccessListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDaiArpAccessListNumber.setStatus("current")
_DDaiArpAccessListTable_Object = MibTable
dDaiArpAccessListTable = _DDaiArpAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dDaiArpAccessListTable.setStatus("current")
_DDaiArpAccessListEntry_Object = MibTableRow
dDaiArpAccessListEntry = _DDaiArpAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 2, 1)
)
dDaiArpAccessListEntry.setIndexNames(
    (0, "DLINKSW-DAI-MIB", "dDaiArpAccessListName"),
)
if mibBuilder.loadTexts:
    dDaiArpAccessListEntry.setStatus("current")


class _DDaiArpAccessListName_Type(DisplayString):
    """Custom type dDaiArpAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDaiArpAccessListName_Type.__name__ = "DisplayString"
_DDaiArpAccessListName_Object = MibTableColumn
dDaiArpAccessListName = _DDaiArpAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 2, 1, 1),
    _DDaiArpAccessListName_Type()
)
dDaiArpAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDaiArpAccessListName.setStatus("current")
_DDaiArpAccessListRowStatus_Type = RowStatus
_DDaiArpAccessListRowStatus_Object = MibTableColumn
dDaiArpAccessListRowStatus = _DDaiArpAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 2, 1, 99),
    _DDaiArpAccessListRowStatus_Type()
)
dDaiArpAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiArpAccessListRowStatus.setStatus("current")
_DDaiArpAccessRuleTable_Object = MibTable
dDaiArpAccessRuleTable = _DDaiArpAccessRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3)
)
if mibBuilder.loadTexts:
    dDaiArpAccessRuleTable.setStatus("current")
_DDaiArpAccessRuleEntry_Object = MibTableRow
dDaiArpAccessRuleEntry = _DDaiArpAccessRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3, 1)
)
dDaiArpAccessRuleEntry.setIndexNames(
    (0, "DLINKSW-DAI-MIB", "dDaiArpAccessListName"),
    (0, "DLINKSW-DAI-MIB", "dDaiArpAccessRuleSn"),
)
if mibBuilder.loadTexts:
    dDaiArpAccessRuleEntry.setStatus("current")


class _DDaiArpAccessRuleSn_Type(Integer32):
    """Custom type dDaiArpAccessRuleSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DDaiArpAccessRuleSn_Type.__name__ = "Integer32"
_DDaiArpAccessRuleSn_Object = MibTableColumn
dDaiArpAccessRuleSn = _DDaiArpAccessRuleSn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3, 1, 1),
    _DDaiArpAccessRuleSn_Type()
)
dDaiArpAccessRuleSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDaiArpAccessRuleSn.setStatus("current")
_DDaiArpAccessRuleRowStatus_Type = RowStatus
_DDaiArpAccessRuleRowStatus_Object = MibTableColumn
dDaiArpAccessRuleRowStatus = _DDaiArpAccessRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3, 1, 2),
    _DDaiArpAccessRuleRowStatus_Type()
)
dDaiArpAccessRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiArpAccessRuleRowStatus.setStatus("current")
_DDaiArpAccessRuleAction_Type = DaiRuleType
_DDaiArpAccessRuleAction_Object = MibTableColumn
dDaiArpAccessRuleAction = _DDaiArpAccessRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3, 1, 3),
    _DDaiArpAccessRuleAction_Type()
)
dDaiArpAccessRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiArpAccessRuleAction.setStatus("current")
_DDaiArpAccessRuleSenderMacAddr_Type = MacAddress
_DDaiArpAccessRuleSenderMacAddr_Object = MibTableColumn
dDaiArpAccessRuleSenderMacAddr = _DDaiArpAccessRuleSenderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3, 1, 4),
    _DDaiArpAccessRuleSenderMacAddr_Type()
)
dDaiArpAccessRuleSenderMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiArpAccessRuleSenderMacAddr.setStatus("current")
_DDaiArpAccessRuleSenderMacMask_Type = MacAddress
_DDaiArpAccessRuleSenderMacMask_Object = MibTableColumn
dDaiArpAccessRuleSenderMacMask = _DDaiArpAccessRuleSenderMacMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3, 1, 5),
    _DDaiArpAccessRuleSenderMacMask_Type()
)
dDaiArpAccessRuleSenderMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiArpAccessRuleSenderMacMask.setStatus("current")
_DDaiArpAccessRuleSenderAddr_Type = IpAddress
_DDaiArpAccessRuleSenderAddr_Object = MibTableColumn
dDaiArpAccessRuleSenderAddr = _DDaiArpAccessRuleSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3, 1, 6),
    _DDaiArpAccessRuleSenderAddr_Type()
)
dDaiArpAccessRuleSenderAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiArpAccessRuleSenderAddr.setStatus("current")
_DDaiArpAccessRuleSenderAddrMask_Type = IpAddress
_DDaiArpAccessRuleSenderAddrMask_Object = MibTableColumn
dDaiArpAccessRuleSenderAddrMask = _DDaiArpAccessRuleSenderAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 1, 5, 3, 1, 7),
    _DDaiArpAccessRuleSenderAddrMask_Type()
)
dDaiArpAccessRuleSenderAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDaiArpAccessRuleSenderAddrMask.setStatus("current")
_DDaiConformance_ObjectIdentity = ObjectIdentity
dDaiConformance = _DDaiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2)
)
_DDaiMIBCompliances_ObjectIdentity = ObjectIdentity
dDaiMIBCompliances = _DDaiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 1)
)
_DDaiMIBGroups_ObjectIdentity = ObjectIdentity
dDaiMIBGroups = _DDaiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2)
)

# Managed Objects groups

dDaiVlanCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 1)
)
dDaiVlanCtrlGroup.setObjects(
      *(("DLINKSW-DAI-MIB", "dDaiVlanCrlFirst2K"),
        ("DLINKSW-DAI-MIB", "dDaiVlanCrlSecond2K"))
)
if mibBuilder.loadTexts:
    dDaiVlanCtrlGroup.setStatus("current")

dDaiIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 2)
)
dDaiIfConfigGroup.setObjects(
    ("DLINKSW-DAI-MIB", "dDaiIfTrustEnabled")
)
if mibBuilder.loadTexts:
    dDaiIfConfigGroup.setStatus("current")

dDaiIfRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 3)
)
dDaiIfRateLimitGroup.setObjects(
      *(("DLINKSW-DAI-MIB", "dDaiIfRateLimit"),
        ("DLINKSW-DAI-MIB", "dDaiIfBurstInterval"))
)
if mibBuilder.loadTexts:
    dDaiIfRateLimitGroup.setStatus("current")

dDaiLoggingConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 4)
)
dDaiLoggingConfigGroup.setObjects(
    ("DLINKSW-DAI-MIB", "dDaiLogBufferSize")
)
if mibBuilder.loadTexts:
    dDaiLoggingConfigGroup.setStatus("current")

dDaiAddressValidationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 5)
)
dDaiAddressValidationGroup.setObjects(
    ("DLINKSW-DAI-MIB", "dDaiAddressValidate")
)
if mibBuilder.loadTexts:
    dDaiAddressValidationGroup.setStatus("current")

dDaiVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 6)
)
dDaiVlanCfgGroup.setObjects(
      *(("DLINKSW-DAI-MIB", "dDaiVlanFilterArpAclName"),
        ("DLINKSW-DAI-MIB", "dDaiVlanFilterArpAclStatic"),
        ("DLINKSW-DAI-MIB", "dDaiVlanAclLogging"),
        ("DLINKSW-DAI-MIB", "dDaiVlanDhcpBindingLogging"),
        ("DLINKSW-DAI-MIB", "dDaiVlanCfgRowStatus"))
)
if mibBuilder.loadTexts:
    dDaiVlanCfgGroup.setStatus("current")

dDaiVlanStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 7)
)
dDaiVlanStatisticsGroup.setObjects(
      *(("DLINKSW-DAI-MIB", "dDaiVlanForwarded"),
        ("DLINKSW-DAI-MIB", "dDaiVlanDropped"),
        ("DLINKSW-DAI-MIB", "dDaiVlanAclPermitted"),
        ("DLINKSW-DAI-MIB", "dDaiVlanDhcpBindingsPermitted"),
        ("DLINKSW-DAI-MIB", "dDaiVlanAclDenied"),
        ("DLINKSW-DAI-MIB", "dDaiVlanDhcpBindingDenied"),
        ("DLINKSW-DAI-MIB", "dDaiVlanSrcMacValidationFailures"),
        ("DLINKSW-DAI-MIB", "dDaiVlanDstMacValidationFailures"),
        ("DLINKSW-DAI-MIB", "dDaiVlanIpValidationFailures"))
)
if mibBuilder.loadTexts:
    dDaiVlanStatisticsGroup.setStatus("current")

dDaiLogBufferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 8)
)
dDaiLogBufferGroup.setObjects(
      *(("DLINKSW-DAI-MIB", "dDaiClearLogBuffer"),
        ("DLINKSW-DAI-MIB", "dDaiLogBufferInterface"),
        ("DLINKSW-DAI-MIB", "dDaiLogBufferVlan"),
        ("DLINKSW-DAI-MIB", "dDaiLogBufferSenderMacAddress"),
        ("DLINKSW-DAI-MIB", "dDaiLogBufferSenderIpAddress"),
        ("DLINKSW-DAI-MIB", "dDaiLogBufferLastUpdate"),
        ("DLINKSW-DAI-MIB", "dDaiLogBufferPacketsCount"))
)
if mibBuilder.loadTexts:
    dDaiLogBufferGroup.setStatus("current")

dDaiAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 9)
)
dDaiAclGroup.setObjects(
      *(("DLINKSW-DAI-MIB", "dDaiArpAccessListNumber"),
        ("DLINKSW-DAI-MIB", "dDaiArpAccessListRowStatus"),
        ("DLINKSW-DAI-MIB", "dDaiArpAccessRuleRowStatus"),
        ("DLINKSW-DAI-MIB", "dDaiArpAccessRuleAction"),
        ("DLINKSW-DAI-MIB", "dDaiArpAccessRuleSenderMacAddr"),
        ("DLINKSW-DAI-MIB", "dDaiArpAccessRuleSenderMacMask"),
        ("DLINKSW-DAI-MIB", "dDaiArpAccessRuleSenderAddr"),
        ("DLINKSW-DAI-MIB", "dDaiArpAccessRuleSenderAddrMask"))
)
if mibBuilder.loadTexts:
    dDaiAclGroup.setStatus("current")

dDaiClearStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 2, 10)
)
dDaiClearStatsGroup.setObjects(
      *(("DLINKSW-DAI-MIB", "dDaiVlanStatsClear"),
        ("DLINKSW-DAI-MIB", "dDaiVlanStatsClearAll"))
)
if mibBuilder.loadTexts:
    dDaiClearStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDaiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 130, 2, 1, 1)
)
dDaiMIBCompliance.setObjects(
      *(("DLINKSW-DAI-MIB", "dDaiIfConfigGroup"),
        ("DLINKSW-DAI-MIB", "dDaiVlanCtrlGroup"),
        ("DLINKSW-DAI-MIB", "dDaiVlanCfgGroup"),
        ("DLINKSW-DAI-MIB", "dDaiLoggingConfigGroup"),
        ("DLINKSW-DAI-MIB", "dDaiIfRateLimitGroup"),
        ("DLINKSW-DAI-MIB", "dDaiAddressValidationGroup"),
        ("DLINKSW-DAI-MIB", "dDaiLogBufferGroup"),
        ("DLINKSW-DAI-MIB", "dDaiVlanStatisticsGroup"),
        ("DLINKSW-DAI-MIB", "dDaiAclGroup"),
        ("DLINKSW-DAI-MIB", "dDaiClearStatsGroup"))
)
if mibBuilder.loadTexts:
    dDaiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DAI-MIB",
    **{"DaiRuleType": DaiRuleType,
       "dlinkSwDynamicArpInspectionMIB": dlinkSwDynamicArpInspectionMIB,
       "dDaiNotifications": dDaiNotifications,
       "dDaiObjects": dDaiObjects,
       "dDaiGlobal": dDaiGlobal,
       "dDaiAddressValidate": dDaiAddressValidate,
       "dDaiLogBufferSize": dDaiLogBufferSize,
       "dDaiClearLogBuffer": dDaiClearLogBuffer,
       "dDaiLogBufferTable": dDaiLogBufferTable,
       "dDaiLogBufferEntry": dDaiLogBufferEntry,
       "dDaiLogBufferIndex": dDaiLogBufferIndex,
       "dDaiLogBufferInterface": dDaiLogBufferInterface,
       "dDaiLogBufferVlan": dDaiLogBufferVlan,
       "dDaiLogBufferSenderMacAddress": dDaiLogBufferSenderMacAddress,
       "dDaiLogBufferSenderIpAddress": dDaiLogBufferSenderIpAddress,
       "dDaiLogBufferLastUpdate": dDaiLogBufferLastUpdate,
       "dDaiLogBufferPacketsCount": dDaiLogBufferPacketsCount,
       "dDaiVlan": dDaiVlan,
       "dDaiVlanCrlFirst2K": dDaiVlanCrlFirst2K,
       "dDaiVlanCrlSecond2K": dDaiVlanCrlSecond2K,
       "dDaiVlanCfgTable": dDaiVlanCfgTable,
       "dDaiVlanCfgEntry": dDaiVlanCfgEntry,
       "dDaiVlanCfgId": dDaiVlanCfgId,
       "dDaiVlanFilterArpAclName": dDaiVlanFilterArpAclName,
       "dDaiVlanFilterArpAclStatic": dDaiVlanFilterArpAclStatic,
       "dDaiVlanAclLogging": dDaiVlanAclLogging,
       "dDaiVlanDhcpBindingLogging": dDaiVlanDhcpBindingLogging,
       "dDaiVlanCfgRowStatus": dDaiVlanCfgRowStatus,
       "dDaiInterface": dDaiInterface,
       "dDaiIfConfigTable": dDaiIfConfigTable,
       "dDaiIfConfigEntry": dDaiIfConfigEntry,
       "dDaiIfTrustEnabled": dDaiIfTrustEnabled,
       "dDaiIfRateLimitTable": dDaiIfRateLimitTable,
       "dDaiIfRateLimitEntry": dDaiIfRateLimitEntry,
       "dDaiIfRateLimit": dDaiIfRateLimit,
       "dDaiIfBurstInterval": dDaiIfBurstInterval,
       "dDaiStatistics": dDaiStatistics,
       "dDaiVlanStatsTable": dDaiVlanStatsTable,
       "dDaiVlanStatsEntry": dDaiVlanStatsEntry,
       "dDaiVlanStatsIndex": dDaiVlanStatsIndex,
       "dDaiVlanForwarded": dDaiVlanForwarded,
       "dDaiVlanDropped": dDaiVlanDropped,
       "dDaiVlanAclPermitted": dDaiVlanAclPermitted,
       "dDaiVlanDhcpBindingsPermitted": dDaiVlanDhcpBindingsPermitted,
       "dDaiVlanAclDenied": dDaiVlanAclDenied,
       "dDaiVlanDhcpBindingDenied": dDaiVlanDhcpBindingDenied,
       "dDaiVlanSrcMacValidationFailures": dDaiVlanSrcMacValidationFailures,
       "dDaiVlanDstMacValidationFailures": dDaiVlanDstMacValidationFailures,
       "dDaiVlanIpValidationFailures": dDaiVlanIpValidationFailures,
       "dDaiVlanStatsClear": dDaiVlanStatsClear,
       "dDaiVlanStatsClearAll": dDaiVlanStatsClearAll,
       "dDaiAclCfg": dDaiAclCfg,
       "dDaiArpAccessListNumber": dDaiArpAccessListNumber,
       "dDaiArpAccessListTable": dDaiArpAccessListTable,
       "dDaiArpAccessListEntry": dDaiArpAccessListEntry,
       "dDaiArpAccessListName": dDaiArpAccessListName,
       "dDaiArpAccessListRowStatus": dDaiArpAccessListRowStatus,
       "dDaiArpAccessRuleTable": dDaiArpAccessRuleTable,
       "dDaiArpAccessRuleEntry": dDaiArpAccessRuleEntry,
       "dDaiArpAccessRuleSn": dDaiArpAccessRuleSn,
       "dDaiArpAccessRuleRowStatus": dDaiArpAccessRuleRowStatus,
       "dDaiArpAccessRuleAction": dDaiArpAccessRuleAction,
       "dDaiArpAccessRuleSenderMacAddr": dDaiArpAccessRuleSenderMacAddr,
       "dDaiArpAccessRuleSenderMacMask": dDaiArpAccessRuleSenderMacMask,
       "dDaiArpAccessRuleSenderAddr": dDaiArpAccessRuleSenderAddr,
       "dDaiArpAccessRuleSenderAddrMask": dDaiArpAccessRuleSenderAddrMask,
       "dDaiConformance": dDaiConformance,
       "dDaiMIBCompliances": dDaiMIBCompliances,
       "dDaiMIBCompliance": dDaiMIBCompliance,
       "dDaiMIBGroups": dDaiMIBGroups,
       "dDaiVlanCtrlGroup": dDaiVlanCtrlGroup,
       "dDaiIfConfigGroup": dDaiIfConfigGroup,
       "dDaiIfRateLimitGroup": dDaiIfRateLimitGroup,
       "dDaiLoggingConfigGroup": dDaiLoggingConfigGroup,
       "dDaiAddressValidationGroup": dDaiAddressValidationGroup,
       "dDaiVlanCfgGroup": dDaiVlanCfgGroup,
       "dDaiVlanStatisticsGroup": dDaiVlanStatisticsGroup,
       "dDaiLogBufferGroup": dDaiLogBufferGroup,
       "dDaiAclGroup": dDaiAclGroup,
       "dDaiClearStatsGroup": dDaiClearStatsGroup}
)
