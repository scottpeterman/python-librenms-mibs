# SNMP MIB module (F3-EOMPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-EOMPLS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:01 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(AdminState,
 CmPmBinAction,
 CmPmIntervalType,
 OperationalState,
 PerfCounter64,
 SecondaryState,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "CmPmIntervalType",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState",
    "VlanId",
    "VlanPriority")

(neIndex,) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex")

(cmEthernetNetPortEntry,
 cmFlowEntry,
 cmPrioMapV2PrioMappingCOSEntry) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetNetPortEntry",
    "cmFlowEntry",
    "cmPrioMapV2PrioMappingCOSEntry")

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
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3EoMplsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39)
)
if mibBuilder.loadTexts:
    f3EoMplsMIB.setRevisions(
        ("2015-08-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EoMplsMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raw", 1),
          ("tagged", 2))
    )



class EoMplsDiscoveryType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3EoMplsConfigObjects_ObjectIdentity = ObjectIdentity
f3EoMplsConfigObjects = _F3EoMplsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1)
)
_F3EoMplsPwTable_Object = MibTable
f3EoMplsPwTable = _F3EoMplsPwTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1)
)
if mibBuilder.loadTexts:
    f3EoMplsPwTable.setStatus("current")
_F3EoMplsPwEntry_Object = MibTableRow
f3EoMplsPwEntry = _F3EoMplsPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1)
)
f3EoMplsPwEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwIndex"),
)
if mibBuilder.loadTexts:
    f3EoMplsPwEntry.setStatus("current")
_F3EoMplsPwIndex_Type = Integer32
_F3EoMplsPwIndex_Object = MibTableColumn
f3EoMplsPwIndex = _F3EoMplsPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 1),
    _F3EoMplsPwIndex_Type()
)
f3EoMplsPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3EoMplsPwIndex.setStatus("current")
_F3EoMplsPwMode_Type = EoMplsMode
_F3EoMplsPwMode_Object = MibTableColumn
f3EoMplsPwMode = _F3EoMplsPwMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 2),
    _F3EoMplsPwMode_Type()
)
f3EoMplsPwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwMode.setStatus("current")


class _F3EoMplsPwTxTunnelLabel_Type(Unsigned32):
    """Custom type f3EoMplsPwTxTunnelLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_F3EoMplsPwTxTunnelLabel_Type.__name__ = "Unsigned32"
_F3EoMplsPwTxTunnelLabel_Object = MibTableColumn
f3EoMplsPwTxTunnelLabel = _F3EoMplsPwTxTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 3),
    _F3EoMplsPwTxTunnelLabel_Type()
)
f3EoMplsPwTxTunnelLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwTxTunnelLabel.setStatus("current")


class _F3EoMplsPwTxTunnelExp_Type(Unsigned32):
    """Custom type f3EoMplsPwTxTunnelExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3EoMplsPwTxTunnelExp_Type.__name__ = "Unsigned32"
_F3EoMplsPwTxTunnelExp_Object = MibTableColumn
f3EoMplsPwTxTunnelExp = _F3EoMplsPwTxTunnelExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 4),
    _F3EoMplsPwTxTunnelExp_Type()
)
f3EoMplsPwTxTunnelExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwTxTunnelExp.setStatus("current")


class _F3EoMplsPwTxTunnelTtl_Type(Unsigned32):
    """Custom type f3EoMplsPwTxTunnelTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3EoMplsPwTxTunnelTtl_Type.__name__ = "Unsigned32"
_F3EoMplsPwTxTunnelTtl_Object = MibTableColumn
f3EoMplsPwTxTunnelTtl = _F3EoMplsPwTxTunnelTtl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 5),
    _F3EoMplsPwTxTunnelTtl_Type()
)
f3EoMplsPwTxTunnelTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwTxTunnelTtl.setStatus("current")
_F3EoMplsPwTxVcLabelControl_Type = TruthValue
_F3EoMplsPwTxVcLabelControl_Object = MibTableColumn
f3EoMplsPwTxVcLabelControl = _F3EoMplsPwTxVcLabelControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 6),
    _F3EoMplsPwTxVcLabelControl_Type()
)
f3EoMplsPwTxVcLabelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwTxVcLabelControl.setStatus("current")


class _F3EoMplsPwTxVcLabel_Type(Unsigned32):
    """Custom type f3EoMplsPwTxVcLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_F3EoMplsPwTxVcLabel_Type.__name__ = "Unsigned32"
_F3EoMplsPwTxVcLabel_Object = MibTableColumn
f3EoMplsPwTxVcLabel = _F3EoMplsPwTxVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 7),
    _F3EoMplsPwTxVcLabel_Type()
)
f3EoMplsPwTxVcLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwTxVcLabel.setStatus("current")


class _F3EoMplsPwTxVcExp_Type(Unsigned32):
    """Custom type f3EoMplsPwTxVcExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3EoMplsPwTxVcExp_Type.__name__ = "Unsigned32"
_F3EoMplsPwTxVcExp_Object = MibTableColumn
f3EoMplsPwTxVcExp = _F3EoMplsPwTxVcExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 8),
    _F3EoMplsPwTxVcExp_Type()
)
f3EoMplsPwTxVcExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwTxVcExp.setStatus("current")


class _F3EoMplsPwTxVcTtl_Type(Unsigned32):
    """Custom type f3EoMplsPwTxVcTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3EoMplsPwTxVcTtl_Type.__name__ = "Unsigned32"
_F3EoMplsPwTxVcTtl_Object = MibTableColumn
f3EoMplsPwTxVcTtl = _F3EoMplsPwTxVcTtl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 9),
    _F3EoMplsPwTxVcTtl_Type()
)
f3EoMplsPwTxVcTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwTxVcTtl.setStatus("current")


class _F3EoMplsPwRxTunnelLabel_Type(Unsigned32):
    """Custom type f3EoMplsPwRxTunnelLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_F3EoMplsPwRxTunnelLabel_Type.__name__ = "Unsigned32"
_F3EoMplsPwRxTunnelLabel_Object = MibTableColumn
f3EoMplsPwRxTunnelLabel = _F3EoMplsPwRxTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 10),
    _F3EoMplsPwRxTunnelLabel_Type()
)
f3EoMplsPwRxTunnelLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwRxTunnelLabel.setStatus("current")


class _F3EoMplsPwRxTunnelExp_Type(Unsigned32):
    """Custom type f3EoMplsPwRxTunnelExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3EoMplsPwRxTunnelExp_Type.__name__ = "Unsigned32"
_F3EoMplsPwRxTunnelExp_Object = MibTableColumn
f3EoMplsPwRxTunnelExp = _F3EoMplsPwRxTunnelExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 11),
    _F3EoMplsPwRxTunnelExp_Type()
)
f3EoMplsPwRxTunnelExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwRxTunnelExp.setStatus("current")


class _F3EoMplsPwRxTunnelTtl_Type(Unsigned32):
    """Custom type f3EoMplsPwRxTunnelTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3EoMplsPwRxTunnelTtl_Type.__name__ = "Unsigned32"
_F3EoMplsPwRxTunnelTtl_Object = MibTableColumn
f3EoMplsPwRxTunnelTtl = _F3EoMplsPwRxTunnelTtl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 12),
    _F3EoMplsPwRxTunnelTtl_Type()
)
f3EoMplsPwRxTunnelTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwRxTunnelTtl.setStatus("current")
_F3EoMplsPwRxVcLabelControl_Type = TruthValue
_F3EoMplsPwRxVcLabelControl_Object = MibTableColumn
f3EoMplsPwRxVcLabelControl = _F3EoMplsPwRxVcLabelControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 13),
    _F3EoMplsPwRxVcLabelControl_Type()
)
f3EoMplsPwRxVcLabelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwRxVcLabelControl.setStatus("current")


class _F3EoMplsPwRxVcLabel_Type(Unsigned32):
    """Custom type f3EoMplsPwRxVcLabel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1048575),
    )


_F3EoMplsPwRxVcLabel_Type.__name__ = "Unsigned32"
_F3EoMplsPwRxVcLabel_Object = MibTableColumn
f3EoMplsPwRxVcLabel = _F3EoMplsPwRxVcLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 14),
    _F3EoMplsPwRxVcLabel_Type()
)
f3EoMplsPwRxVcLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwRxVcLabel.setStatus("current")


class _F3EoMplsPwRxVcExp_Type(Unsigned32):
    """Custom type f3EoMplsPwRxVcExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3EoMplsPwRxVcExp_Type.__name__ = "Unsigned32"
_F3EoMplsPwRxVcExp_Object = MibTableColumn
f3EoMplsPwRxVcExp = _F3EoMplsPwRxVcExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 15),
    _F3EoMplsPwRxVcExp_Type()
)
f3EoMplsPwRxVcExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwRxVcExp.setStatus("current")


class _F3EoMplsPwRxVcTtl_Type(Unsigned32):
    """Custom type f3EoMplsPwRxVcTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3EoMplsPwRxVcTtl_Type.__name__ = "Unsigned32"
_F3EoMplsPwRxVcTtl_Object = MibTableColumn
f3EoMplsPwRxVcTtl = _F3EoMplsPwRxVcTtl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 16),
    _F3EoMplsPwRxVcTtl_Type()
)
f3EoMplsPwRxVcTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwRxVcTtl.setStatus("current")
_F3EoMplsPwOuterStagControl_Type = TruthValue
_F3EoMplsPwOuterStagControl_Object = MibTableColumn
f3EoMplsPwOuterStagControl = _F3EoMplsPwOuterStagControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 17),
    _F3EoMplsPwOuterStagControl_Type()
)
f3EoMplsPwOuterStagControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwOuterStagControl.setStatus("current")
_F3EoMplsPwOuterStagVlanId_Type = VlanId
_F3EoMplsPwOuterStagVlanId_Object = MibTableColumn
f3EoMplsPwOuterStagVlanId = _F3EoMplsPwOuterStagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 18),
    _F3EoMplsPwOuterStagVlanId_Type()
)
f3EoMplsPwOuterStagVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwOuterStagVlanId.setStatus("current")
_F3EoMplsPwOuterStagVlanPri_Type = VlanPriority
_F3EoMplsPwOuterStagVlanPri_Object = MibTableColumn
f3EoMplsPwOuterStagVlanPri = _F3EoMplsPwOuterStagVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 19),
    _F3EoMplsPwOuterStagVlanPri_Type()
)
f3EoMplsPwOuterStagVlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwOuterStagVlanPri.setStatus("current")
_F3EoMplsPwDiscoverType_Type = EoMplsDiscoveryType
_F3EoMplsPwDiscoverType_Object = MibTableColumn
f3EoMplsPwDiscoverType = _F3EoMplsPwDiscoverType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 20),
    _F3EoMplsPwDiscoverType_Type()
)
f3EoMplsPwDiscoverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwDiscoverType.setStatus("current")
_F3EoMplsPwDestIp_Type = IpAddress
_F3EoMplsPwDestIp_Object = MibTableColumn
f3EoMplsPwDestIp = _F3EoMplsPwDestIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 21),
    _F3EoMplsPwDestIp_Type()
)
f3EoMplsPwDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwDestIp.setStatus("current")
_F3EoMplsPwDestMac_Type = MacAddress
_F3EoMplsPwDestMac_Object = MibTableColumn
f3EoMplsPwDestMac = _F3EoMplsPwDestMac_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 22),
    _F3EoMplsPwDestMac_Type()
)
f3EoMplsPwDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwDestMac.setStatus("current")
_F3EoMplsPwAdminState_Type = AdminState
_F3EoMplsPwAdminState_Object = MibTableColumn
f3EoMplsPwAdminState = _F3EoMplsPwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 23),
    _F3EoMplsPwAdminState_Type()
)
f3EoMplsPwAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwAdminState.setStatus("current")
_F3EoMplsPwOperationalState_Type = OperationalState
_F3EoMplsPwOperationalState_Object = MibTableColumn
f3EoMplsPwOperationalState = _F3EoMplsPwOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 24),
    _F3EoMplsPwOperationalState_Type()
)
f3EoMplsPwOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwOperationalState.setStatus("current")
_F3EoMplsPwSecondaryState_Type = SecondaryState
_F3EoMplsPwSecondaryState_Object = MibTableColumn
f3EoMplsPwSecondaryState = _F3EoMplsPwSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 25),
    _F3EoMplsPwSecondaryState_Type()
)
f3EoMplsPwSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwSecondaryState.setStatus("current")
_F3EoMplsPwStorageType_Type = StorageType
_F3EoMplsPwStorageType_Object = MibTableColumn
f3EoMplsPwStorageType = _F3EoMplsPwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 26),
    _F3EoMplsPwStorageType_Type()
)
f3EoMplsPwStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3EoMplsPwStorageType.setStatus("current")
_F3EoMplsPwRowStatus_Type = RowStatus
_F3EoMplsPwRowStatus_Object = MibTableColumn
f3EoMplsPwRowStatus = _F3EoMplsPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 27),
    _F3EoMplsPwRowStatus_Type()
)
f3EoMplsPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3EoMplsPwRowStatus.setStatus("current")
_F3EoMplsPwInnerExpMappingControl_Type = TruthValue
_F3EoMplsPwInnerExpMappingControl_Object = MibTableColumn
f3EoMplsPwInnerExpMappingControl = _F3EoMplsPwInnerExpMappingControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 28),
    _F3EoMplsPwInnerExpMappingControl_Type()
)
f3EoMplsPwInnerExpMappingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwInnerExpMappingControl.setStatus("current")
_F3EoMplsPwOuterExpMappingControl_Type = TruthValue
_F3EoMplsPwOuterExpMappingControl_Object = MibTableColumn
f3EoMplsPwOuterExpMappingControl = _F3EoMplsPwOuterExpMappingControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 29),
    _F3EoMplsPwOuterExpMappingControl_Type()
)
f3EoMplsPwOuterExpMappingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwOuterExpMappingControl.setStatus("current")
_F3EoMplsPwOuterTagPriMappingControl_Type = TruthValue
_F3EoMplsPwOuterTagPriMappingControl_Object = MibTableColumn
f3EoMplsPwOuterTagPriMappingControl = _F3EoMplsPwOuterTagPriMappingControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 30),
    _F3EoMplsPwOuterTagPriMappingControl_Type()
)
f3EoMplsPwOuterTagPriMappingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwOuterTagPriMappingControl.setStatus("current")
_F3EoMplsPwEgressInterface_Type = VariablePointer
_F3EoMplsPwEgressInterface_Object = MibTableColumn
f3EoMplsPwEgressInterface = _F3EoMplsPwEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 1, 1, 31),
    _F3EoMplsPwEgressInterface_Type()
)
f3EoMplsPwEgressInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwEgressInterface.setStatus("current")
_F3NetPortExtEoMplsTable_Object = MibTable
f3NetPortExtEoMplsTable = _F3NetPortExtEoMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 2)
)
if mibBuilder.loadTexts:
    f3NetPortExtEoMplsTable.setStatus("current")
_F3NetPortExtEoMplsEntry_Object = MibTableRow
f3NetPortExtEoMplsEntry = _F3NetPortExtEoMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f3NetPortExtEoMplsEntry.setStatus("current")
_F3NetPortExtEoMplsSrcIp_Type = IpAddress
_F3NetPortExtEoMplsSrcIp_Object = MibTableColumn
f3NetPortExtEoMplsSrcIp = _F3NetPortExtEoMplsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 2, 1, 1),
    _F3NetPortExtEoMplsSrcIp_Type()
)
f3NetPortExtEoMplsSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortExtEoMplsSrcIp.setStatus("current")
_F3PrioMapV2PrioMappingCosExtEoMplsTable_Object = MibTable
f3PrioMapV2PrioMappingCosExtEoMplsTable = _F3PrioMapV2PrioMappingCosExtEoMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 3)
)
if mibBuilder.loadTexts:
    f3PrioMapV2PrioMappingCosExtEoMplsTable.setStatus("current")
_F3PrioMapV2PrioMappingCosExtEoMplsEntry_Object = MibTableRow
f3PrioMapV2PrioMappingCosExtEoMplsEntry = _F3PrioMapV2PrioMappingCosExtEoMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 3, 1)
)
if mibBuilder.loadTexts:
    f3PrioMapV2PrioMappingCosExtEoMplsEntry.setStatus("current")
_F3PrioMapV2PrioMappingCosOuterMplsExp_Type = Integer32
_F3PrioMapV2PrioMappingCosOuterMplsExp_Object = MibTableColumn
f3PrioMapV2PrioMappingCosOuterMplsExp = _F3PrioMapV2PrioMappingCosOuterMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 3, 1, 1),
    _F3PrioMapV2PrioMappingCosOuterMplsExp_Type()
)
f3PrioMapV2PrioMappingCosOuterMplsExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PrioMapV2PrioMappingCosOuterMplsExp.setStatus("current")
_F3PrioMapV2PrioMappingCosInnerMplsExp_Type = Integer32
_F3PrioMapV2PrioMappingCosInnerMplsExp_Object = MibTableColumn
f3PrioMapV2PrioMappingCosInnerMplsExp = _F3PrioMapV2PrioMappingCosInnerMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 1, 3, 1, 2),
    _F3PrioMapV2PrioMappingCosInnerMplsExp_Type()
)
f3PrioMapV2PrioMappingCosInnerMplsExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PrioMapV2PrioMappingCosInnerMplsExp.setStatus("current")
_F3EoMplsPerformance_ObjectIdentity = ObjectIdentity
f3EoMplsPerformance = _F3EoMplsPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2)
)
_F3EoMplsPwStatsTable_Object = MibTable
f3EoMplsPwStatsTable = _F3EoMplsPwStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1)
)
if mibBuilder.loadTexts:
    f3EoMplsPwStatsTable.setStatus("current")
_F3EoMplsPwStatsEntry_Object = MibTableRow
f3EoMplsPwStatsEntry = _F3EoMplsPwStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1)
)
f3EoMplsPwStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwStatsIndex"),
)
if mibBuilder.loadTexts:
    f3EoMplsPwStatsEntry.setStatus("current")


class _F3EoMplsPwStatsIndex_Type(Integer32):
    """Custom type f3EoMplsPwStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3EoMplsPwStatsIndex_Type.__name__ = "Integer32"
_F3EoMplsPwStatsIndex_Object = MibTableColumn
f3EoMplsPwStatsIndex = _F3EoMplsPwStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 1),
    _F3EoMplsPwStatsIndex_Type()
)
f3EoMplsPwStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwStatsIndex.setStatus("current")
_F3EoMplsPwStatsIntervalType_Type = CmPmIntervalType
_F3EoMplsPwStatsIntervalType_Object = MibTableColumn
f3EoMplsPwStatsIntervalType = _F3EoMplsPwStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 2),
    _F3EoMplsPwStatsIntervalType_Type()
)
f3EoMplsPwStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwStatsIntervalType.setStatus("current")
_F3EoMplsPwStatsValid_Type = TruthValue
_F3EoMplsPwStatsValid_Object = MibTableColumn
f3EoMplsPwStatsValid = _F3EoMplsPwStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 3),
    _F3EoMplsPwStatsValid_Type()
)
f3EoMplsPwStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwStatsValid.setStatus("current")
_F3EoMplsPwStatsAction_Type = CmPmBinAction
_F3EoMplsPwStatsAction_Object = MibTableColumn
f3EoMplsPwStatsAction = _F3EoMplsPwStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 4),
    _F3EoMplsPwStatsAction_Type()
)
f3EoMplsPwStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwStatsAction.setStatus("current")
_F3EoMplsPwStatsTtlEqual0Drop_Type = PerfCounter64
_F3EoMplsPwStatsTtlEqual0Drop_Object = MibTableColumn
f3EoMplsPwStatsTtlEqual0Drop = _F3EoMplsPwStatsTtlEqual0Drop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 1, 1, 5),
    _F3EoMplsPwStatsTtlEqual0Drop_Type()
)
f3EoMplsPwStatsTtlEqual0Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwStatsTtlEqual0Drop.setStatus("current")
_F3EoMplsPwHistoryTable_Object = MibTable
f3EoMplsPwHistoryTable = _F3EoMplsPwHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2)
)
if mibBuilder.loadTexts:
    f3EoMplsPwHistoryTable.setStatus("current")
_F3EoMplsPwHistoryEntry_Object = MibTableRow
f3EoMplsPwHistoryEntry = _F3EoMplsPwHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1)
)
f3EoMplsPwHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwStatsIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3EoMplsPwHistoryEntry.setStatus("current")


class _F3EoMplsPwHistoryIndex_Type(Integer32):
    """Custom type f3EoMplsPwHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3EoMplsPwHistoryIndex_Type.__name__ = "Integer32"
_F3EoMplsPwHistoryIndex_Object = MibTableColumn
f3EoMplsPwHistoryIndex = _F3EoMplsPwHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 1),
    _F3EoMplsPwHistoryIndex_Type()
)
f3EoMplsPwHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwHistoryIndex.setStatus("current")
_F3EoMplsPwHistoryTime_Type = DateAndTime
_F3EoMplsPwHistoryTime_Object = MibTableColumn
f3EoMplsPwHistoryTime = _F3EoMplsPwHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 2),
    _F3EoMplsPwHistoryTime_Type()
)
f3EoMplsPwHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwHistoryTime.setStatus("current")
_F3EoMplsPwHistoryValid_Type = TruthValue
_F3EoMplsPwHistoryValid_Object = MibTableColumn
f3EoMplsPwHistoryValid = _F3EoMplsPwHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 3),
    _F3EoMplsPwHistoryValid_Type()
)
f3EoMplsPwHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwHistoryValid.setStatus("current")
_F3EoMplsPwHistoryAction_Type = CmPmBinAction
_F3EoMplsPwHistoryAction_Object = MibTableColumn
f3EoMplsPwHistoryAction = _F3EoMplsPwHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 4),
    _F3EoMplsPwHistoryAction_Type()
)
f3EoMplsPwHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwHistoryAction.setStatus("current")
_F3EoMplsPwHistoryTtlEqual0Drop_Type = PerfCounter64
_F3EoMplsPwHistoryTtlEqual0Drop_Object = MibTableColumn
f3EoMplsPwHistoryTtlEqual0Drop = _F3EoMplsPwHistoryTtlEqual0Drop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 2, 1, 5),
    _F3EoMplsPwHistoryTtlEqual0Drop_Type()
)
f3EoMplsPwHistoryTtlEqual0Drop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwHistoryTtlEqual0Drop.setStatus("current")
_F3EoMplsPwThresholdTable_Object = MibTable
f3EoMplsPwThresholdTable = _F3EoMplsPwThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3)
)
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdTable.setStatus("current")
_F3EoMplsPwThresholdEntry_Object = MibTableRow
f3EoMplsPwThresholdEntry = _F3EoMplsPwThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1)
)
f3EoMplsPwThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwStatsIndex"),
    (0, "F3-EOMPLS-MIB", "f3EoMplsPwThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdEntry.setStatus("current")


class _F3EoMplsPwThresholdIndex_Type(Integer32):
    """Custom type f3EoMplsPwThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3EoMplsPwThresholdIndex_Type.__name__ = "Integer32"
_F3EoMplsPwThresholdIndex_Object = MibTableColumn
f3EoMplsPwThresholdIndex = _F3EoMplsPwThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 1),
    _F3EoMplsPwThresholdIndex_Type()
)
f3EoMplsPwThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdIndex.setStatus("current")
_F3EoMplsPwThresholdInterval_Type = CmPmIntervalType
_F3EoMplsPwThresholdInterval_Object = MibTableColumn
f3EoMplsPwThresholdInterval = _F3EoMplsPwThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 2),
    _F3EoMplsPwThresholdInterval_Type()
)
f3EoMplsPwThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdInterval.setStatus("current")
_F3EoMplsPwThresholdVariable_Type = VariablePointer
_F3EoMplsPwThresholdVariable_Object = MibTableColumn
f3EoMplsPwThresholdVariable = _F3EoMplsPwThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 3),
    _F3EoMplsPwThresholdVariable_Type()
)
f3EoMplsPwThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdVariable.setStatus("current")
_F3EoMplsPwThresholdValueLo_Type = Unsigned32
_F3EoMplsPwThresholdValueLo_Object = MibTableColumn
f3EoMplsPwThresholdValueLo = _F3EoMplsPwThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 4),
    _F3EoMplsPwThresholdValueLo_Type()
)
f3EoMplsPwThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdValueLo.setStatus("current")
_F3EoMplsPwThresholdValueHi_Type = Unsigned32
_F3EoMplsPwThresholdValueHi_Object = MibTableColumn
f3EoMplsPwThresholdValueHi = _F3EoMplsPwThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 5),
    _F3EoMplsPwThresholdValueHi_Type()
)
f3EoMplsPwThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdValueHi.setStatus("current")
_F3EoMplsPwThresholdMonValue_Type = Counter64
_F3EoMplsPwThresholdMonValue_Object = MibTableColumn
f3EoMplsPwThresholdMonValue = _F3EoMplsPwThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 2, 3, 1, 6),
    _F3EoMplsPwThresholdMonValue_Type()
)
f3EoMplsPwThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdMonValue.setStatus("current")
_F3EoMplsNotifications_ObjectIdentity = ObjectIdentity
f3EoMplsNotifications = _F3EoMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 3)
)
_F3EoMplsConformance_ObjectIdentity = ObjectIdentity
f3EoMplsConformance = _F3EoMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4)
)
_F3EoMplsCompliances_ObjectIdentity = ObjectIdentity
f3EoMplsCompliances = _F3EoMplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4, 1)
)
_F3EoMplsGroups_ObjectIdentity = ObjectIdentity
f3EoMplsGroups = _F3EoMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4, 2)
)
cmEthernetNetPortEntry.registerAugmentions(
    ("F3-EOMPLS-MIB",
     "f3NetPortExtEoMplsEntry")
)
f3NetPortExtEoMplsEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
cmPrioMapV2PrioMappingCOSEntry.registerAugmentions(
    ("F3-EOMPLS-MIB",
     "f3PrioMapV2PrioMappingCosExtEoMplsEntry")
)
f3PrioMapV2PrioMappingCosExtEoMplsEntry.setIndexNames(*cmPrioMapV2PrioMappingCOSEntry.getIndexNames())

# Managed Objects groups

f3EoMplsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4, 2, 1)
)
f3EoMplsConfigGroup.setObjects(
      *(("F3-EOMPLS-MIB", "f3EoMplsPwIndex"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwMode"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwTxTunnelLabel"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwTxTunnelExp"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwTxTunnelTtl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwTxVcLabelControl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwTxVcLabel"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwTxVcExp"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwTxVcTtl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwRxTunnelLabel"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwRxTunnelExp"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwRxTunnelTtl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwRxVcLabelControl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwRxVcLabel"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwRxVcExp"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwRxVcTtl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwOuterStagControl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwOuterStagVlanId"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwOuterStagVlanPri"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwDiscoverType"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwDestIp"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwDestMac"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwAdminState"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwOperationalState"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwSecondaryState"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwStorageType"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwRowStatus"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwInnerExpMappingControl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwOuterExpMappingControl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwOuterTagPriMappingControl"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwEgressInterface"),
        ("F3-EOMPLS-MIB", "f3NetPortExtEoMplsSrcIp"),
        ("F3-EOMPLS-MIB", "f3PrioMapV2PrioMappingCosOuterMplsExp"),
        ("F3-EOMPLS-MIB", "f3PrioMapV2PrioMappingCosInnerMplsExp"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwStatsIndex"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwStatsIntervalType"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwStatsValid"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwStatsAction"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwStatsTtlEqual0Drop"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryIndex"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryTime"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryValid"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryAction"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwHistoryTtlEqual0Drop"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdIndex"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdInterval"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdVariable"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdValueLo"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdValueHi"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3EoMplsConfigGroup.setStatus("current")


# Notification objects

f3EoMplsPwThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 3, 1)
)
f3EoMplsPwThresholdCrossingAlert.setObjects(
      *(("F3-EOMPLS-MIB", "f3EoMplsPwThresholdIndex"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdInterval"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdVariable"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdValueLo"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdValueHi"),
        ("F3-EOMPLS-MIB", "f3EoMplsPwThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3EoMplsPwThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

f3EoMplsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 39, 4, 1, 1)
)
f3EoMplsCompliance.setObjects(
    ("F3-EOMPLS-MIB", "f3EoMplsConfigGroup")
)
if mibBuilder.loadTexts:
    f3EoMplsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-EOMPLS-MIB",
    **{"EoMplsMode": EoMplsMode,
       "EoMplsDiscoveryType": EoMplsDiscoveryType,
       "f3EoMplsMIB": f3EoMplsMIB,
       "f3EoMplsConfigObjects": f3EoMplsConfigObjects,
       "f3EoMplsPwTable": f3EoMplsPwTable,
       "f3EoMplsPwEntry": f3EoMplsPwEntry,
       "f3EoMplsPwIndex": f3EoMplsPwIndex,
       "f3EoMplsPwMode": f3EoMplsPwMode,
       "f3EoMplsPwTxTunnelLabel": f3EoMplsPwTxTunnelLabel,
       "f3EoMplsPwTxTunnelExp": f3EoMplsPwTxTunnelExp,
       "f3EoMplsPwTxTunnelTtl": f3EoMplsPwTxTunnelTtl,
       "f3EoMplsPwTxVcLabelControl": f3EoMplsPwTxVcLabelControl,
       "f3EoMplsPwTxVcLabel": f3EoMplsPwTxVcLabel,
       "f3EoMplsPwTxVcExp": f3EoMplsPwTxVcExp,
       "f3EoMplsPwTxVcTtl": f3EoMplsPwTxVcTtl,
       "f3EoMplsPwRxTunnelLabel": f3EoMplsPwRxTunnelLabel,
       "f3EoMplsPwRxTunnelExp": f3EoMplsPwRxTunnelExp,
       "f3EoMplsPwRxTunnelTtl": f3EoMplsPwRxTunnelTtl,
       "f3EoMplsPwRxVcLabelControl": f3EoMplsPwRxVcLabelControl,
       "f3EoMplsPwRxVcLabel": f3EoMplsPwRxVcLabel,
       "f3EoMplsPwRxVcExp": f3EoMplsPwRxVcExp,
       "f3EoMplsPwRxVcTtl": f3EoMplsPwRxVcTtl,
       "f3EoMplsPwOuterStagControl": f3EoMplsPwOuterStagControl,
       "f3EoMplsPwOuterStagVlanId": f3EoMplsPwOuterStagVlanId,
       "f3EoMplsPwOuterStagVlanPri": f3EoMplsPwOuterStagVlanPri,
       "f3EoMplsPwDiscoverType": f3EoMplsPwDiscoverType,
       "f3EoMplsPwDestIp": f3EoMplsPwDestIp,
       "f3EoMplsPwDestMac": f3EoMplsPwDestMac,
       "f3EoMplsPwAdminState": f3EoMplsPwAdminState,
       "f3EoMplsPwOperationalState": f3EoMplsPwOperationalState,
       "f3EoMplsPwSecondaryState": f3EoMplsPwSecondaryState,
       "f3EoMplsPwStorageType": f3EoMplsPwStorageType,
       "f3EoMplsPwRowStatus": f3EoMplsPwRowStatus,
       "f3EoMplsPwInnerExpMappingControl": f3EoMplsPwInnerExpMappingControl,
       "f3EoMplsPwOuterExpMappingControl": f3EoMplsPwOuterExpMappingControl,
       "f3EoMplsPwOuterTagPriMappingControl": f3EoMplsPwOuterTagPriMappingControl,
       "f3EoMplsPwEgressInterface": f3EoMplsPwEgressInterface,
       "f3NetPortExtEoMplsTable": f3NetPortExtEoMplsTable,
       "f3NetPortExtEoMplsEntry": f3NetPortExtEoMplsEntry,
       "f3NetPortExtEoMplsSrcIp": f3NetPortExtEoMplsSrcIp,
       "f3PrioMapV2PrioMappingCosExtEoMplsTable": f3PrioMapV2PrioMappingCosExtEoMplsTable,
       "f3PrioMapV2PrioMappingCosExtEoMplsEntry": f3PrioMapV2PrioMappingCosExtEoMplsEntry,
       "f3PrioMapV2PrioMappingCosOuterMplsExp": f3PrioMapV2PrioMappingCosOuterMplsExp,
       "f3PrioMapV2PrioMappingCosInnerMplsExp": f3PrioMapV2PrioMappingCosInnerMplsExp,
       "f3EoMplsPerformance": f3EoMplsPerformance,
       "f3EoMplsPwStatsTable": f3EoMplsPwStatsTable,
       "f3EoMplsPwStatsEntry": f3EoMplsPwStatsEntry,
       "f3EoMplsPwStatsIndex": f3EoMplsPwStatsIndex,
       "f3EoMplsPwStatsIntervalType": f3EoMplsPwStatsIntervalType,
       "f3EoMplsPwStatsValid": f3EoMplsPwStatsValid,
       "f3EoMplsPwStatsAction": f3EoMplsPwStatsAction,
       "f3EoMplsPwStatsTtlEqual0Drop": f3EoMplsPwStatsTtlEqual0Drop,
       "f3EoMplsPwHistoryTable": f3EoMplsPwHistoryTable,
       "f3EoMplsPwHistoryEntry": f3EoMplsPwHistoryEntry,
       "f3EoMplsPwHistoryIndex": f3EoMplsPwHistoryIndex,
       "f3EoMplsPwHistoryTime": f3EoMplsPwHistoryTime,
       "f3EoMplsPwHistoryValid": f3EoMplsPwHistoryValid,
       "f3EoMplsPwHistoryAction": f3EoMplsPwHistoryAction,
       "f3EoMplsPwHistoryTtlEqual0Drop": f3EoMplsPwHistoryTtlEqual0Drop,
       "f3EoMplsPwThresholdTable": f3EoMplsPwThresholdTable,
       "f3EoMplsPwThresholdEntry": f3EoMplsPwThresholdEntry,
       "f3EoMplsPwThresholdIndex": f3EoMplsPwThresholdIndex,
       "f3EoMplsPwThresholdInterval": f3EoMplsPwThresholdInterval,
       "f3EoMplsPwThresholdVariable": f3EoMplsPwThresholdVariable,
       "f3EoMplsPwThresholdValueLo": f3EoMplsPwThresholdValueLo,
       "f3EoMplsPwThresholdValueHi": f3EoMplsPwThresholdValueHi,
       "f3EoMplsPwThresholdMonValue": f3EoMplsPwThresholdMonValue,
       "f3EoMplsNotifications": f3EoMplsNotifications,
       "f3EoMplsPwThresholdCrossingAlert": f3EoMplsPwThresholdCrossingAlert,
       "f3EoMplsConformance": f3EoMplsConformance,
       "f3EoMplsCompliances": f3EoMplsCompliances,
       "f3EoMplsCompliance": f3EoMplsCompliance,
       "f3EoMplsGroups": f3EoMplsGroups,
       "f3EoMplsConfigGroup": f3EoMplsConfigGroup}
)
