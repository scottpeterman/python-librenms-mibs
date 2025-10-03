# SNMP MIB module (F3-ERP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-ERP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:07 2025
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
 OperationalState,
 SecondaryState,
 VlanEthertype,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "OperationalState",
    "SecondaryState",
    "VlanEthertype",
    "VlanId",
    "VlanPriority")

(neIndex,) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex")

(CmProtUnitState,
 CmProtUnitType) = mibBuilder.importSymbols(
    "CM-PROTECTION-MIB",
    "CmProtUnitState",
    "CmProtUnitType")

(Dot1agCfmMDLevel,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMDLevel")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3ErpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25)
)
if mibBuilder.loadTexts:
    f3ErpMIB.setRevisions(
        ("2012-09-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class G8032Version(TextualConvention, Integer32):
    status = "current"
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



class RPLRole(TextualConvention, Integer32):
    status = "current"
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
          ("neighbor", 2),
          ("owner", 3))
    )



class RingPortStatus(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("unblocked", 1),
          ("unblockedSF", 2),
          ("unblockedSD", 3),
          ("blockedRPL", 4),
          ("blockedSF", 5),
          ("blockedSD", 6),
          ("blockedMS", 7),
          ("blockedFS", 8),
          ("blockedPending", 9),
          ("subringInterConnect", 10),
          ("subringInterConnectSF", 11))
    )



class RingNodeState(TextualConvention, Integer32):
    status = "current"
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
        *(("idle", 1),
          ("protection", 2),
          ("manual", 3),
          ("forced", 4),
          ("pending", 5))
    )



class RAPSRequest(TextualConvention, Integer32):
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
        *(("noRequest", 1),
          ("manual", 2),
          ("forced", 3),
          ("signailFail", 4),
          ("signailDegrade", 5),
          ("notApplicable", 6))
    )



class ERPGroupAction(TextualConvention, Integer32):
    status = "current"
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
        *(("noAction", 1),
          ("forcedSwitch", 2),
          ("manualSwitch", 3),
          ("clearSwitch", 4),
          ("resetStats", 5))
    )



class RapsInterconnectionNode(TextualConvention, Integer32):
    status = "current"
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
          ("primary", 2),
          ("secondary", 3))
    )



class RapsMultipleFailure(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("primary", 2),
          ("secondary", 3))
    )



# MIB Managed Objects in the order of their OIDs

_F3ErpConfigObjects_ObjectIdentity = ObjectIdentity
f3ErpConfigObjects = _F3ErpConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1)
)
_F3ErpGroupTable_Object = MibTable
f3ErpGroupTable = _F3ErpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1)
)
if mibBuilder.loadTexts:
    f3ErpGroupTable.setStatus("current")
_F3ErpGroupEntry_Object = MibTableRow
f3ErpGroupEntry = _F3ErpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1)
)
f3ErpGroupEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-ERP-MIB", "f3ErpGroupIndex"),
)
if mibBuilder.loadTexts:
    f3ErpGroupEntry.setStatus("current")


class _F3ErpGroupIndex_Type(Integer32):
    """Custom type f3ErpGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3ErpGroupIndex_Type.__name__ = "Integer32"
_F3ErpGroupIndex_Object = MibTableColumn
f3ErpGroupIndex = _F3ErpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 1),
    _F3ErpGroupIndex_Type()
)
f3ErpGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ErpGroupIndex.setStatus("current")
_F3ErpGroupAdminState_Type = AdminState
_F3ErpGroupAdminState_Object = MibTableColumn
f3ErpGroupAdminState = _F3ErpGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 2),
    _F3ErpGroupAdminState_Type()
)
f3ErpGroupAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupAdminState.setStatus("current")
_F3ErpGroupOperationalState_Type = OperationalState
_F3ErpGroupOperationalState_Object = MibTableColumn
f3ErpGroupOperationalState = _F3ErpGroupOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 3),
    _F3ErpGroupOperationalState_Type()
)
f3ErpGroupOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupOperationalState.setStatus("current")
_F3ErpGroupSecondaryState_Type = SecondaryState
_F3ErpGroupSecondaryState_Object = MibTableColumn
f3ErpGroupSecondaryState = _F3ErpGroupSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 4),
    _F3ErpGroupSecondaryState_Type()
)
f3ErpGroupSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupSecondaryState.setStatus("current")


class _F3ErpGroupRapsRingId_Type(Integer32):
    """Custom type f3ErpGroupRapsRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3ErpGroupRapsRingId_Type.__name__ = "Integer32"
_F3ErpGroupRapsRingId_Object = MibTableColumn
f3ErpGroupRapsRingId = _F3ErpGroupRapsRingId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 5),
    _F3ErpGroupRapsRingId_Type()
)
f3ErpGroupRapsRingId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRapsRingId.setStatus("current")
_F3ErpGroupRapsNodeId_Type = MacAddress
_F3ErpGroupRapsNodeId_Object = MibTableColumn
f3ErpGroupRapsNodeId = _F3ErpGroupRapsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 6),
    _F3ErpGroupRapsNodeId_Type()
)
f3ErpGroupRapsNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRapsNodeId.setStatus("current")
_F3ErpGroupRapsVlanId_Type = VlanId
_F3ErpGroupRapsVlanId_Object = MibTableColumn
f3ErpGroupRapsVlanId = _F3ErpGroupRapsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 7),
    _F3ErpGroupRapsVlanId_Type()
)
f3ErpGroupRapsVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRapsVlanId.setStatus("current")
_F3ErpGroupRapsVlanPrio_Type = VlanPriority
_F3ErpGroupRapsVlanPrio_Object = MibTableColumn
f3ErpGroupRapsVlanPrio = _F3ErpGroupRapsVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 8),
    _F3ErpGroupRapsVlanPrio_Type()
)
f3ErpGroupRapsVlanPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRapsVlanPrio.setStatus("current")
_F3ErpGroupRapsVlanEtherType_Type = Unsigned32
_F3ErpGroupRapsVlanEtherType_Object = MibTableColumn
f3ErpGroupRapsVlanEtherType = _F3ErpGroupRapsVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 9),
    _F3ErpGroupRapsVlanEtherType_Type()
)
f3ErpGroupRapsVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRapsVlanEtherType.setStatus("current")
_F3ErpGroupRapsMdLevel_Type = Dot1agCfmMDLevel
_F3ErpGroupRapsMdLevel_Object = MibTableColumn
f3ErpGroupRapsMdLevel = _F3ErpGroupRapsMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 10),
    _F3ErpGroupRapsMdLevel_Type()
)
f3ErpGroupRapsMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRapsMdLevel.setStatus("current")
_F3ErpGroupCompatibleVersion_Type = G8032Version
_F3ErpGroupCompatibleVersion_Object = MibTableColumn
f3ErpGroupCompatibleVersion = _F3ErpGroupCompatibleVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 11),
    _F3ErpGroupCompatibleVersion_Type()
)
f3ErpGroupCompatibleVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ErpGroupCompatibleVersion.setStatus("current")
_F3ErpGroupRevertive_Type = TruthValue
_F3ErpGroupRevertive_Object = MibTableColumn
f3ErpGroupRevertive = _F3ErpGroupRevertive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 12),
    _F3ErpGroupRevertive_Type()
)
f3ErpGroupRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRevertive.setStatus("current")
_F3ErpGroupSubRingWithoutVirtChan_Type = TruthValue
_F3ErpGroupSubRingWithoutVirtChan_Object = MibTableColumn
f3ErpGroupSubRingWithoutVirtChan = _F3ErpGroupSubRingWithoutVirtChan_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 13),
    _F3ErpGroupSubRingWithoutVirtChan_Type()
)
f3ErpGroupSubRingWithoutVirtChan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupSubRingWithoutVirtChan.setStatus("current")


class _F3ErpGroupGuardTime_Type(Integer32):
    """Custom type f3ErpGroupGuardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_F3ErpGroupGuardTime_Type.__name__ = "Integer32"
_F3ErpGroupGuardTime_Object = MibTableColumn
f3ErpGroupGuardTime = _F3ErpGroupGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 14),
    _F3ErpGroupGuardTime_Type()
)
f3ErpGroupGuardTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupGuardTime.setStatus("current")


class _F3ErpGroupWaitToRestore_Type(Integer32):
    """Custom type f3ErpGroupWaitToRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_F3ErpGroupWaitToRestore_Type.__name__ = "Integer32"
_F3ErpGroupWaitToRestore_Object = MibTableColumn
f3ErpGroupWaitToRestore = _F3ErpGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 15),
    _F3ErpGroupWaitToRestore_Type()
)
f3ErpGroupWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupWaitToRestore.setStatus("current")


class _F3ErpGroupHoldOffTime_Type(Integer32):
    """Custom type f3ErpGroupHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_F3ErpGroupHoldOffTime_Type.__name__ = "Integer32"
_F3ErpGroupHoldOffTime_Object = MibTableColumn
f3ErpGroupHoldOffTime = _F3ErpGroupHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 16),
    _F3ErpGroupHoldOffTime_Type()
)
f3ErpGroupHoldOffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupHoldOffTime.setStatus("current")
_F3ErpGroupRingPort0_Type = VariablePointer
_F3ErpGroupRingPort0_Object = MibTableColumn
f3ErpGroupRingPort0 = _F3ErpGroupRingPort0_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 17),
    _F3ErpGroupRingPort0_Type()
)
f3ErpGroupRingPort0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRingPort0.setStatus("current")
_F3ErpGroupRingPort0MEP_Type = VariablePointer
_F3ErpGroupRingPort0MEP_Object = MibTableColumn
f3ErpGroupRingPort0MEP = _F3ErpGroupRingPort0MEP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 18),
    _F3ErpGroupRingPort0MEP_Type()
)
f3ErpGroupRingPort0MEP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRingPort0MEP.setStatus("current")
_F3ErpGroupRingPort0Role_Type = RPLRole
_F3ErpGroupRingPort0Role_Object = MibTableColumn
f3ErpGroupRingPort0Role = _F3ErpGroupRingPort0Role_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 19),
    _F3ErpGroupRingPort0Role_Type()
)
f3ErpGroupRingPort0Role.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRingPort0Role.setStatus("current")
_F3ErpGroupRingPort1_Type = VariablePointer
_F3ErpGroupRingPort1_Object = MibTableColumn
f3ErpGroupRingPort1 = _F3ErpGroupRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 20),
    _F3ErpGroupRingPort1_Type()
)
f3ErpGroupRingPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRingPort1.setStatus("current")
_F3ErpGroupRingPort1MEP_Type = VariablePointer
_F3ErpGroupRingPort1MEP_Object = MibTableColumn
f3ErpGroupRingPort1MEP = _F3ErpGroupRingPort1MEP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 21),
    _F3ErpGroupRingPort1MEP_Type()
)
f3ErpGroupRingPort1MEP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRingPort1MEP.setStatus("current")
_F3ErpGroupRingPort1Role_Type = RPLRole
_F3ErpGroupRingPort1Role_Object = MibTableColumn
f3ErpGroupRingPort1Role = _F3ErpGroupRingPort1Role_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 22),
    _F3ErpGroupRingPort1Role_Type()
)
f3ErpGroupRingPort1Role.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRingPort1Role.setStatus("current")
_F3ErpGroupProtectMgmtTunnel_Type = TruthValue
_F3ErpGroupProtectMgmtTunnel_Object = MibTableColumn
f3ErpGroupProtectMgmtTunnel = _F3ErpGroupProtectMgmtTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 23),
    _F3ErpGroupProtectMgmtTunnel_Type()
)
f3ErpGroupProtectMgmtTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupProtectMgmtTunnel.setStatus("current")
_F3ErpGroupNodeState_Type = RingNodeState
_F3ErpGroupNodeState_Object = MibTableColumn
f3ErpGroupNodeState = _F3ErpGroupNodeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 24),
    _F3ErpGroupNodeState_Type()
)
f3ErpGroupNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupNodeState.setStatus("current")
_F3ErpGroupWTRRemainingTime_Type = Integer32
_F3ErpGroupWTRRemainingTime_Object = MibTableColumn
f3ErpGroupWTRRemainingTime = _F3ErpGroupWTRRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 25),
    _F3ErpGroupWTRRemainingTime_Type()
)
f3ErpGroupWTRRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupWTRRemainingTime.setStatus("current")
_F3ErpGroupTxRapsRequest_Type = RAPSRequest
_F3ErpGroupTxRapsRequest_Object = MibTableColumn
f3ErpGroupTxRapsRequest = _F3ErpGroupTxRapsRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 26),
    _F3ErpGroupTxRapsRequest_Type()
)
f3ErpGroupTxRapsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupTxRapsRequest.setStatus("current")
_F3ErpGroupTxRapsRplBlocked_Type = TruthValue
_F3ErpGroupTxRapsRplBlocked_Object = MibTableColumn
f3ErpGroupTxRapsRplBlocked = _F3ErpGroupTxRapsRplBlocked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 27),
    _F3ErpGroupTxRapsRplBlocked_Type()
)
f3ErpGroupTxRapsRplBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupTxRapsRplBlocked.setStatus("current")
_F3ErpGroupTxRapsDNF_Type = TruthValue
_F3ErpGroupTxRapsDNF_Object = MibTableColumn
f3ErpGroupTxRapsDNF = _F3ErpGroupTxRapsDNF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 28),
    _F3ErpGroupTxRapsDNF_Type()
)
f3ErpGroupTxRapsDNF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupTxRapsDNF.setStatus("current")


class _F3ErpGroupTxRapsBPR_Type(Integer32):
    """Custom type f3ErpGroupTxRapsBPR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_F3ErpGroupTxRapsBPR_Type.__name__ = "Integer32"
_F3ErpGroupTxRapsBPR_Object = MibTableColumn
f3ErpGroupTxRapsBPR = _F3ErpGroupTxRapsBPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 29),
    _F3ErpGroupTxRapsBPR_Type()
)
f3ErpGroupTxRapsBPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupTxRapsBPR.setStatus("current")
_F3ErpGroupAction_Type = ERPGroupAction
_F3ErpGroupAction_Object = MibTableColumn
f3ErpGroupAction = _F3ErpGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 30),
    _F3ErpGroupAction_Type()
)
f3ErpGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ErpGroupAction.setStatus("current")
_F3ErpGroupActionObject_Type = VariablePointer
_F3ErpGroupActionObject_Object = MibTableColumn
f3ErpGroupActionObject = _F3ErpGroupActionObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 31),
    _F3ErpGroupActionObject_Type()
)
f3ErpGroupActionObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ErpGroupActionObject.setStatus("current")


class _F3ErpGroupUserLabel_Type(DisplayString):
    """Custom type f3ErpGroupUserLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3ErpGroupUserLabel_Type.__name__ = "DisplayString"
_F3ErpGroupUserLabel_Object = MibTableColumn
f3ErpGroupUserLabel = _F3ErpGroupUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 32),
    _F3ErpGroupUserLabel_Type()
)
f3ErpGroupUserLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupUserLabel.setStatus("current")
_F3ErpGroupStorageType_Type = StorageType
_F3ErpGroupStorageType_Object = MibTableColumn
f3ErpGroupStorageType = _F3ErpGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 33),
    _F3ErpGroupStorageType_Type()
)
f3ErpGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupStorageType.setStatus("current")
_F3ErpGroupRowStatus_Type = RowStatus
_F3ErpGroupRowStatus_Object = MibTableColumn
f3ErpGroupRowStatus = _F3ErpGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 34),
    _F3ErpGroupRowStatus_Type()
)
f3ErpGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRowStatus.setStatus("current")
_F3ErpGroupInterconnectionErp_Type = VariablePointer
_F3ErpGroupInterconnectionErp_Object = MibTableColumn
f3ErpGroupInterconnectionErp = _F3ErpGroupInterconnectionErp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 35),
    _F3ErpGroupInterconnectionErp_Type()
)
f3ErpGroupInterconnectionErp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ErpGroupInterconnectionErp.setStatus("current")
_F3ErpGroupInterconnectPropagateTc_Type = TruthValue
_F3ErpGroupInterconnectPropagateTc_Object = MibTableColumn
f3ErpGroupInterconnectPropagateTc = _F3ErpGroupInterconnectPropagateTc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 36),
    _F3ErpGroupInterconnectPropagateTc_Type()
)
f3ErpGroupInterconnectPropagateTc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ErpGroupInterconnectPropagateTc.setStatus("current")
_F3ErpGroupRapsVirtualChannelMep_Type = VariablePointer
_F3ErpGroupRapsVirtualChannelMep_Object = MibTableColumn
f3ErpGroupRapsVirtualChannelMep = _F3ErpGroupRapsVirtualChannelMep_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 37),
    _F3ErpGroupRapsVirtualChannelMep_Type()
)
f3ErpGroupRapsVirtualChannelMep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ErpGroupRapsVirtualChannelMep.setStatus("current")
_F3ErpGroupMaxFpNum_Type = Integer32
_F3ErpGroupMaxFpNum_Object = MibTableColumn
f3ErpGroupMaxFpNum = _F3ErpGroupMaxFpNum_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 38),
    _F3ErpGroupMaxFpNum_Type()
)
f3ErpGroupMaxFpNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3ErpGroupMaxFpNum.setStatus("current")
_F3ErpGroupRapsInterconnectionNode_Type = RapsInterconnectionNode
_F3ErpGroupRapsInterconnectionNode_Object = MibTableColumn
f3ErpGroupRapsInterconnectionNode = _F3ErpGroupRapsInterconnectionNode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 39),
    _F3ErpGroupRapsInterconnectionNode_Type()
)
f3ErpGroupRapsInterconnectionNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRapsInterconnectionNode.setStatus("current")
_F3ErpGroupRapsMultipleFailure_Type = RapsMultipleFailure
_F3ErpGroupRapsMultipleFailure_Object = MibTableColumn
f3ErpGroupRapsMultipleFailure = _F3ErpGroupRapsMultipleFailure_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 1, 1, 40),
    _F3ErpGroupRapsMultipleFailure_Type()
)
f3ErpGroupRapsMultipleFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3ErpGroupRapsMultipleFailure.setStatus("current")
_F3ErpGroupProtectedFlowTable_Object = MibTable
f3ErpGroupProtectedFlowTable = _F3ErpGroupProtectedFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 2)
)
if mibBuilder.loadTexts:
    f3ErpGroupProtectedFlowTable.setStatus("current")
_F3ErpGroupProtectedFlowEntry_Object = MibTableRow
f3ErpGroupProtectedFlowEntry = _F3ErpGroupProtectedFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 2, 1)
)
f3ErpGroupProtectedFlowEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-ERP-MIB", "f3ErpGroupIndex"),
    (0, "F3-ERP-MIB", "f3ErpGroupProtectedFlow"),
)
if mibBuilder.loadTexts:
    f3ErpGroupProtectedFlowEntry.setStatus("current")
_F3ErpGroupProtectedFlow_Type = VariablePointer
_F3ErpGroupProtectedFlow_Object = MibTableColumn
f3ErpGroupProtectedFlow = _F3ErpGroupProtectedFlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 2, 1, 1),
    _F3ErpGroupProtectedFlow_Type()
)
f3ErpGroupProtectedFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpGroupProtectedFlow.setStatus("current")
_F3ErpUnitTable_Object = MibTable
f3ErpUnitTable = _F3ErpUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3)
)
if mibBuilder.loadTexts:
    f3ErpUnitTable.setStatus("current")
_F3ErpUnitEntry_Object = MibTableRow
f3ErpUnitEntry = _F3ErpUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1)
)
f3ErpUnitEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-ERP-MIB", "f3ErpGroupIndex"),
    (0, "F3-ERP-MIB", "f3ErpUnitIndex"),
)
if mibBuilder.loadTexts:
    f3ErpUnitEntry.setStatus("current")


class _F3ErpUnitIndex_Type(Integer32):
    """Custom type f3ErpUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_F3ErpUnitIndex_Type.__name__ = "Integer32"
_F3ErpUnitIndex_Object = MibTableColumn
f3ErpUnitIndex = _F3ErpUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 1),
    _F3ErpUnitIndex_Type()
)
f3ErpUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3ErpUnitIndex.setStatus("current")
_F3ErpUnitPort_Type = VariablePointer
_F3ErpUnitPort_Object = MibTableColumn
f3ErpUnitPort = _F3ErpUnitPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 2),
    _F3ErpUnitPort_Type()
)
f3ErpUnitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPort.setStatus("current")
_F3ErpUnitPortMEP_Type = VariablePointer
_F3ErpUnitPortMEP_Object = MibTableColumn
f3ErpUnitPortMEP = _F3ErpUnitPortMEP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 3),
    _F3ErpUnitPortMEP_Type()
)
f3ErpUnitPortMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortMEP.setStatus("current")
_F3ErpUnitPortRole_Type = RPLRole
_F3ErpUnitPortRole_Object = MibTableColumn
f3ErpUnitPortRole = _F3ErpUnitPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 4),
    _F3ErpUnitPortRole_Type()
)
f3ErpUnitPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortRole.setStatus("current")
_F3ErpUnitPortStatus_Type = RingPortStatus
_F3ErpUnitPortStatus_Object = MibTableColumn
f3ErpUnitPortStatus = _F3ErpUnitPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 5),
    _F3ErpUnitPortStatus_Type()
)
f3ErpUnitPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortStatus.setStatus("current")
_F3ErpUnitPortRxRapsRequest_Type = RAPSRequest
_F3ErpUnitPortRxRapsRequest_Object = MibTableColumn
f3ErpUnitPortRxRapsRequest = _F3ErpUnitPortRxRapsRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 6),
    _F3ErpUnitPortRxRapsRequest_Type()
)
f3ErpUnitPortRxRapsRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortRxRapsRequest.setStatus("current")
_F3ErpUnitPortRxRapsRplBlocked_Type = TruthValue
_F3ErpUnitPortRxRapsRplBlocked_Object = MibTableColumn
f3ErpUnitPortRxRapsRplBlocked = _F3ErpUnitPortRxRapsRplBlocked_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 7),
    _F3ErpUnitPortRxRapsRplBlocked_Type()
)
f3ErpUnitPortRxRapsRplBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortRxRapsRplBlocked.setStatus("current")
_F3ErpUnitPortRxRapsDNF_Type = TruthValue
_F3ErpUnitPortRxRapsDNF_Object = MibTableColumn
f3ErpUnitPortRxRapsDNF = _F3ErpUnitPortRxRapsDNF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 8),
    _F3ErpUnitPortRxRapsDNF_Type()
)
f3ErpUnitPortRxRapsDNF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortRxRapsDNF.setStatus("current")


class _F3ErpUnitPortRxRapsBPR_Type(Integer32):
    """Custom type f3ErpUnitPortRxRapsBPR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_F3ErpUnitPortRxRapsBPR_Type.__name__ = "Integer32"
_F3ErpUnitPortRxRapsBPR_Object = MibTableColumn
f3ErpUnitPortRxRapsBPR = _F3ErpUnitPortRxRapsBPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 9),
    _F3ErpUnitPortRxRapsBPR_Type()
)
f3ErpUnitPortRxRapsBPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortRxRapsBPR.setStatus("current")
_F3ErpUnitPortRxRapsNodeId_Type = MacAddress
_F3ErpUnitPortRxRapsNodeId_Object = MibTableColumn
f3ErpUnitPortRxRapsNodeId = _F3ErpUnitPortRxRapsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 10),
    _F3ErpUnitPortRxRapsNodeId_Type()
)
f3ErpUnitPortRxRapsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortRxRapsNodeId.setStatus("current")
_F3ErpUnitPortRapsFp_Type = VariablePointer
_F3ErpUnitPortRapsFp_Object = MibTableColumn
f3ErpUnitPortRapsFp = _F3ErpUnitPortRapsFp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 1, 3, 1, 11),
    _F3ErpUnitPortRapsFp_Type()
)
f3ErpUnitPortRapsFp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitPortRapsFp.setStatus("current")
_F3ErpStatsObjects_ObjectIdentity = ObjectIdentity
f3ErpStatsObjects = _F3ErpStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2)
)
_F3ErpUnitStatsTable_Object = MibTable
f3ErpUnitStatsTable = _F3ErpUnitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1)
)
if mibBuilder.loadTexts:
    f3ErpUnitStatsTable.setStatus("current")
_F3ErpUnitStatsEntry_Object = MibTableRow
f3ErpUnitStatsEntry = _F3ErpUnitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1)
)
f3ErpUnitStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-ERP-MIB", "f3ErpGroupIndex"),
    (0, "F3-ERP-MIB", "f3ErpUnitIndex"),
)
if mibBuilder.loadTexts:
    f3ErpUnitStatsEntry.setStatus("current")
_F3ErpUnitNumBlockedStateTrans_Type = Unsigned32
_F3ErpUnitNumBlockedStateTrans_Object = MibTableColumn
f3ErpUnitNumBlockedStateTrans = _F3ErpUnitNumBlockedStateTrans_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 1),
    _F3ErpUnitNumBlockedStateTrans_Type()
)
f3ErpUnitNumBlockedStateTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitNumBlockedStateTrans.setStatus("current")
_F3ErpUnitRapsPDUsTx_Type = Unsigned32
_F3ErpUnitRapsPDUsTx_Object = MibTableColumn
f3ErpUnitRapsPDUsTx = _F3ErpUnitRapsPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 2),
    _F3ErpUnitRapsPDUsTx_Type()
)
f3ErpUnitRapsPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsPDUsTx.setStatus("current")
_F3ErpUnitRapsPDUsRx_Type = Unsigned32
_F3ErpUnitRapsPDUsRx_Object = MibTableColumn
f3ErpUnitRapsPDUsRx = _F3ErpUnitRapsPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 3),
    _F3ErpUnitRapsPDUsRx_Type()
)
f3ErpUnitRapsPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsPDUsRx.setStatus("current")
_F3ErpUnitRapsPDUsDiscarded_Type = Unsigned32
_F3ErpUnitRapsPDUsDiscarded_Object = MibTableColumn
f3ErpUnitRapsPDUsDiscarded = _F3ErpUnitRapsPDUsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 4),
    _F3ErpUnitRapsPDUsDiscarded_Type()
)
f3ErpUnitRapsPDUsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsPDUsDiscarded.setStatus("current")
_F3ErpUnitRapsNoReqPDUsTx_Type = Unsigned32
_F3ErpUnitRapsNoReqPDUsTx_Object = MibTableColumn
f3ErpUnitRapsNoReqPDUsTx = _F3ErpUnitRapsNoReqPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 5),
    _F3ErpUnitRapsNoReqPDUsTx_Type()
)
f3ErpUnitRapsNoReqPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsNoReqPDUsTx.setStatus("current")
_F3ErpUnitRapsNoReqRBPDUsTx_Type = Unsigned32
_F3ErpUnitRapsNoReqRBPDUsTx_Object = MibTableColumn
f3ErpUnitRapsNoReqRBPDUsTx = _F3ErpUnitRapsNoReqRBPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 6),
    _F3ErpUnitRapsNoReqRBPDUsTx_Type()
)
f3ErpUnitRapsNoReqRBPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsNoReqRBPDUsTx.setStatus("current")
_F3ErpUnitRapsSignalFailPDUsTx_Type = Unsigned32
_F3ErpUnitRapsSignalFailPDUsTx_Object = MibTableColumn
f3ErpUnitRapsSignalFailPDUsTx = _F3ErpUnitRapsSignalFailPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 7),
    _F3ErpUnitRapsSignalFailPDUsTx_Type()
)
f3ErpUnitRapsSignalFailPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsSignalFailPDUsTx.setStatus("current")
_F3ErpUnitRapsManualSwitchPDUsTx_Type = Unsigned32
_F3ErpUnitRapsManualSwitchPDUsTx_Object = MibTableColumn
f3ErpUnitRapsManualSwitchPDUsTx = _F3ErpUnitRapsManualSwitchPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 8),
    _F3ErpUnitRapsManualSwitchPDUsTx_Type()
)
f3ErpUnitRapsManualSwitchPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsManualSwitchPDUsTx.setStatus("current")
_F3ErpUnitRapsForcedSwitchPDUsTx_Type = Unsigned32
_F3ErpUnitRapsForcedSwitchPDUsTx_Object = MibTableColumn
f3ErpUnitRapsForcedSwitchPDUsTx = _F3ErpUnitRapsForcedSwitchPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 9),
    _F3ErpUnitRapsForcedSwitchPDUsTx_Type()
)
f3ErpUnitRapsForcedSwitchPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsForcedSwitchPDUsTx.setStatus("current")
_F3ErpUnitRapsEventPDUsTx_Type = Unsigned32
_F3ErpUnitRapsEventPDUsTx_Object = MibTableColumn
f3ErpUnitRapsEventPDUsTx = _F3ErpUnitRapsEventPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 10),
    _F3ErpUnitRapsEventPDUsTx_Type()
)
f3ErpUnitRapsEventPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsEventPDUsTx.setStatus("current")
_F3ErpUnitRapsNoReqPDUsRx_Type = Unsigned32
_F3ErpUnitRapsNoReqPDUsRx_Object = MibTableColumn
f3ErpUnitRapsNoReqPDUsRx = _F3ErpUnitRapsNoReqPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 11),
    _F3ErpUnitRapsNoReqPDUsRx_Type()
)
f3ErpUnitRapsNoReqPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsNoReqPDUsRx.setStatus("current")
_F3ErpUnitRapsNoReqRBPDUsRx_Type = Unsigned32
_F3ErpUnitRapsNoReqRBPDUsRx_Object = MibTableColumn
f3ErpUnitRapsNoReqRBPDUsRx = _F3ErpUnitRapsNoReqRBPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 12),
    _F3ErpUnitRapsNoReqRBPDUsRx_Type()
)
f3ErpUnitRapsNoReqRBPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsNoReqRBPDUsRx.setStatus("current")
_F3ErpUnitRapsSignalFailPDUsRx_Type = Unsigned32
_F3ErpUnitRapsSignalFailPDUsRx_Object = MibTableColumn
f3ErpUnitRapsSignalFailPDUsRx = _F3ErpUnitRapsSignalFailPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 13),
    _F3ErpUnitRapsSignalFailPDUsRx_Type()
)
f3ErpUnitRapsSignalFailPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsSignalFailPDUsRx.setStatus("current")
_F3ErpUnitRapsManualSwitchPDUsRx_Type = Unsigned32
_F3ErpUnitRapsManualSwitchPDUsRx_Object = MibTableColumn
f3ErpUnitRapsManualSwitchPDUsRx = _F3ErpUnitRapsManualSwitchPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 14),
    _F3ErpUnitRapsManualSwitchPDUsRx_Type()
)
f3ErpUnitRapsManualSwitchPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsManualSwitchPDUsRx.setStatus("current")
_F3ErpUnitRapsForcedSwitchPDUsRx_Type = Unsigned32
_F3ErpUnitRapsForcedSwitchPDUsRx_Object = MibTableColumn
f3ErpUnitRapsForcedSwitchPDUsRx = _F3ErpUnitRapsForcedSwitchPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 15),
    _F3ErpUnitRapsForcedSwitchPDUsRx_Type()
)
f3ErpUnitRapsForcedSwitchPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsForcedSwitchPDUsRx.setStatus("current")
_F3ErpUnitRapsEventPDUsRx_Type = Unsigned32
_F3ErpUnitRapsEventPDUsRx_Object = MibTableColumn
f3ErpUnitRapsEventPDUsRx = _F3ErpUnitRapsEventPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 16),
    _F3ErpUnitRapsEventPDUsRx_Type()
)
f3ErpUnitRapsEventPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsEventPDUsRx.setStatus("current")
_F3ErpUnitRapsInvalidOamVersionPDUsRx_Type = Unsigned32
_F3ErpUnitRapsInvalidOamVersionPDUsRx_Object = MibTableColumn
f3ErpUnitRapsInvalidOamVersionPDUsRx = _F3ErpUnitRapsInvalidOamVersionPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 17),
    _F3ErpUnitRapsInvalidOamVersionPDUsRx_Type()
)
f3ErpUnitRapsInvalidOamVersionPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsInvalidOamVersionPDUsRx.setStatus("current")
_F3ErpUnitRapsRsvdRequestPDUsRx_Type = Unsigned32
_F3ErpUnitRapsRsvdRequestPDUsRx_Object = MibTableColumn
f3ErpUnitRapsRsvdRequestPDUsRx = _F3ErpUnitRapsRsvdRequestPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 18),
    _F3ErpUnitRapsRsvdRequestPDUsRx_Type()
)
f3ErpUnitRapsRsvdRequestPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsRsvdRequestPDUsRx.setStatus("current")
_F3ErpUnitRapsRsvdEventSubcode_Type = Unsigned32
_F3ErpUnitRapsRsvdEventSubcode_Object = MibTableColumn
f3ErpUnitRapsRsvdEventSubcode = _F3ErpUnitRapsRsvdEventSubcode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 2, 1, 1, 19),
    _F3ErpUnitRapsRsvdEventSubcode_Type()
)
f3ErpUnitRapsRsvdEventSubcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ErpUnitRapsRsvdEventSubcode.setStatus("current")
_F3ErpConformance_ObjectIdentity = ObjectIdentity
f3ErpConformance = _F3ErpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3)
)
_F3ErpCompliances_ObjectIdentity = ObjectIdentity
f3ErpCompliances = _F3ErpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 1)
)
_F3ErpGroups_ObjectIdentity = ObjectIdentity
f3ErpGroups = _F3ErpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 2)
)

# Managed Objects groups

f3ErpGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 2, 1)
)
f3ErpGroupGroup.setObjects(
      *(("F3-ERP-MIB", "f3ErpGroupAdminState"),
        ("F3-ERP-MIB", "f3ErpGroupOperationalState"),
        ("F3-ERP-MIB", "f3ErpGroupSecondaryState"),
        ("F3-ERP-MIB", "f3ErpGroupRapsRingId"),
        ("F3-ERP-MIB", "f3ErpGroupRapsNodeId"),
        ("F3-ERP-MIB", "f3ErpGroupRapsVlanId"),
        ("F3-ERP-MIB", "f3ErpGroupRapsVlanPrio"),
        ("F3-ERP-MIB", "f3ErpGroupRapsVlanEtherType"),
        ("F3-ERP-MIB", "f3ErpGroupRapsMdLevel"),
        ("F3-ERP-MIB", "f3ErpGroupCompatibleVersion"),
        ("F3-ERP-MIB", "f3ErpGroupRevertive"),
        ("F3-ERP-MIB", "f3ErpGroupSubRingWithoutVirtChan"),
        ("F3-ERP-MIB", "f3ErpGroupGuardTime"),
        ("F3-ERP-MIB", "f3ErpGroupWaitToRestore"),
        ("F3-ERP-MIB", "f3ErpGroupHoldOffTime"),
        ("F3-ERP-MIB", "f3ErpGroupRingPort0"),
        ("F3-ERP-MIB", "f3ErpGroupRingPort0MEP"),
        ("F3-ERP-MIB", "f3ErpGroupRingPort0Role"),
        ("F3-ERP-MIB", "f3ErpGroupRingPort1"),
        ("F3-ERP-MIB", "f3ErpGroupRingPort1MEP"),
        ("F3-ERP-MIB", "f3ErpGroupRingPort1Role"),
        ("F3-ERP-MIB", "f3ErpGroupProtectMgmtTunnel"),
        ("F3-ERP-MIB", "f3ErpGroupNodeState"),
        ("F3-ERP-MIB", "f3ErpGroupWTRRemainingTime"),
        ("F3-ERP-MIB", "f3ErpGroupTxRapsRequest"),
        ("F3-ERP-MIB", "f3ErpGroupTxRapsRplBlocked"),
        ("F3-ERP-MIB", "f3ErpGroupTxRapsDNF"),
        ("F3-ERP-MIB", "f3ErpGroupTxRapsBPR"),
        ("F3-ERP-MIB", "f3ErpGroupAction"),
        ("F3-ERP-MIB", "f3ErpGroupActionObject"),
        ("F3-ERP-MIB", "f3ErpGroupUserLabel"),
        ("F3-ERP-MIB", "f3ErpGroupStorageType"),
        ("F3-ERP-MIB", "f3ErpGroupRowStatus"),
        ("F3-ERP-MIB", "f3ErpGroupProtectedFlow"),
        ("F3-ERP-MIB", "f3ErpGroupInterconnectionErp"),
        ("F3-ERP-MIB", "f3ErpGroupInterconnectPropagateTc"),
        ("F3-ERP-MIB", "f3ErpGroupRapsVirtualChannelMep"),
        ("F3-ERP-MIB", "f3ErpGroupMaxFpNum"),
        ("F3-ERP-MIB", "f3ErpGroupRapsInterconnectionNode"),
        ("F3-ERP-MIB", "f3ErpGroupRapsMultipleFailure"))
)
if mibBuilder.loadTexts:
    f3ErpGroupGroup.setStatus("current")

f3ErpUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 2, 2)
)
f3ErpUnitGroup.setObjects(
      *(("F3-ERP-MIB", "f3ErpUnitPort"),
        ("F3-ERP-MIB", "f3ErpUnitPortMEP"),
        ("F3-ERP-MIB", "f3ErpUnitPortRole"),
        ("F3-ERP-MIB", "f3ErpUnitPortStatus"),
        ("F3-ERP-MIB", "f3ErpUnitPortRxRapsRequest"),
        ("F3-ERP-MIB", "f3ErpUnitPortRxRapsRplBlocked"),
        ("F3-ERP-MIB", "f3ErpUnitPortRxRapsDNF"),
        ("F3-ERP-MIB", "f3ErpUnitPortRxRapsBPR"),
        ("F3-ERP-MIB", "f3ErpUnitPortRxRapsNodeId"),
        ("F3-ERP-MIB", "f3ErpUnitPortRapsFp"))
)
if mibBuilder.loadTexts:
    f3ErpUnitGroup.setStatus("current")

f3ErpUnitStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 2, 3)
)
f3ErpUnitStatsGroup.setObjects(
      *(("F3-ERP-MIB", "f3ErpUnitNumBlockedStateTrans"),
        ("F3-ERP-MIB", "f3ErpUnitRapsPDUsTx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsPDUsDiscarded"),
        ("F3-ERP-MIB", "f3ErpUnitRapsNoReqPDUsTx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsNoReqRBPDUsTx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsSignalFailPDUsTx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsManualSwitchPDUsTx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsForcedSwitchPDUsTx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsEventPDUsTx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsNoReqPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsNoReqRBPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsSignalFailPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsManualSwitchPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsForcedSwitchPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsEventPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsInvalidOamVersionPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsRsvdRequestPDUsRx"),
        ("F3-ERP-MIB", "f3ErpUnitRapsRsvdEventSubcode"))
)
if mibBuilder.loadTexts:
    f3ErpUnitStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3ErpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 25, 3, 1, 1)
)
f3ErpCompliance.setObjects(
      *(("F3-ERP-MIB", "f3ErpGroupGroup"),
        ("F3-ERP-MIB", "f3ErpUnitGroup"),
        ("F3-ERP-MIB", "f3ErpUnitStatsGroup"))
)
if mibBuilder.loadTexts:
    f3ErpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-ERP-MIB",
    **{"G8032Version": G8032Version,
       "RPLRole": RPLRole,
       "RingPortStatus": RingPortStatus,
       "RingNodeState": RingNodeState,
       "RAPSRequest": RAPSRequest,
       "ERPGroupAction": ERPGroupAction,
       "RapsInterconnectionNode": RapsInterconnectionNode,
       "RapsMultipleFailure": RapsMultipleFailure,
       "f3ErpMIB": f3ErpMIB,
       "f3ErpConfigObjects": f3ErpConfigObjects,
       "f3ErpGroupTable": f3ErpGroupTable,
       "f3ErpGroupEntry": f3ErpGroupEntry,
       "f3ErpGroupIndex": f3ErpGroupIndex,
       "f3ErpGroupAdminState": f3ErpGroupAdminState,
       "f3ErpGroupOperationalState": f3ErpGroupOperationalState,
       "f3ErpGroupSecondaryState": f3ErpGroupSecondaryState,
       "f3ErpGroupRapsRingId": f3ErpGroupRapsRingId,
       "f3ErpGroupRapsNodeId": f3ErpGroupRapsNodeId,
       "f3ErpGroupRapsVlanId": f3ErpGroupRapsVlanId,
       "f3ErpGroupRapsVlanPrio": f3ErpGroupRapsVlanPrio,
       "f3ErpGroupRapsVlanEtherType": f3ErpGroupRapsVlanEtherType,
       "f3ErpGroupRapsMdLevel": f3ErpGroupRapsMdLevel,
       "f3ErpGroupCompatibleVersion": f3ErpGroupCompatibleVersion,
       "f3ErpGroupRevertive": f3ErpGroupRevertive,
       "f3ErpGroupSubRingWithoutVirtChan": f3ErpGroupSubRingWithoutVirtChan,
       "f3ErpGroupGuardTime": f3ErpGroupGuardTime,
       "f3ErpGroupWaitToRestore": f3ErpGroupWaitToRestore,
       "f3ErpGroupHoldOffTime": f3ErpGroupHoldOffTime,
       "f3ErpGroupRingPort0": f3ErpGroupRingPort0,
       "f3ErpGroupRingPort0MEP": f3ErpGroupRingPort0MEP,
       "f3ErpGroupRingPort0Role": f3ErpGroupRingPort0Role,
       "f3ErpGroupRingPort1": f3ErpGroupRingPort1,
       "f3ErpGroupRingPort1MEP": f3ErpGroupRingPort1MEP,
       "f3ErpGroupRingPort1Role": f3ErpGroupRingPort1Role,
       "f3ErpGroupProtectMgmtTunnel": f3ErpGroupProtectMgmtTunnel,
       "f3ErpGroupNodeState": f3ErpGroupNodeState,
       "f3ErpGroupWTRRemainingTime": f3ErpGroupWTRRemainingTime,
       "f3ErpGroupTxRapsRequest": f3ErpGroupTxRapsRequest,
       "f3ErpGroupTxRapsRplBlocked": f3ErpGroupTxRapsRplBlocked,
       "f3ErpGroupTxRapsDNF": f3ErpGroupTxRapsDNF,
       "f3ErpGroupTxRapsBPR": f3ErpGroupTxRapsBPR,
       "f3ErpGroupAction": f3ErpGroupAction,
       "f3ErpGroupActionObject": f3ErpGroupActionObject,
       "f3ErpGroupUserLabel": f3ErpGroupUserLabel,
       "f3ErpGroupStorageType": f3ErpGroupStorageType,
       "f3ErpGroupRowStatus": f3ErpGroupRowStatus,
       "f3ErpGroupInterconnectionErp": f3ErpGroupInterconnectionErp,
       "f3ErpGroupInterconnectPropagateTc": f3ErpGroupInterconnectPropagateTc,
       "f3ErpGroupRapsVirtualChannelMep": f3ErpGroupRapsVirtualChannelMep,
       "f3ErpGroupMaxFpNum": f3ErpGroupMaxFpNum,
       "f3ErpGroupRapsInterconnectionNode": f3ErpGroupRapsInterconnectionNode,
       "f3ErpGroupRapsMultipleFailure": f3ErpGroupRapsMultipleFailure,
       "f3ErpGroupProtectedFlowTable": f3ErpGroupProtectedFlowTable,
       "f3ErpGroupProtectedFlowEntry": f3ErpGroupProtectedFlowEntry,
       "f3ErpGroupProtectedFlow": f3ErpGroupProtectedFlow,
       "f3ErpUnitTable": f3ErpUnitTable,
       "f3ErpUnitEntry": f3ErpUnitEntry,
       "f3ErpUnitIndex": f3ErpUnitIndex,
       "f3ErpUnitPort": f3ErpUnitPort,
       "f3ErpUnitPortMEP": f3ErpUnitPortMEP,
       "f3ErpUnitPortRole": f3ErpUnitPortRole,
       "f3ErpUnitPortStatus": f3ErpUnitPortStatus,
       "f3ErpUnitPortRxRapsRequest": f3ErpUnitPortRxRapsRequest,
       "f3ErpUnitPortRxRapsRplBlocked": f3ErpUnitPortRxRapsRplBlocked,
       "f3ErpUnitPortRxRapsDNF": f3ErpUnitPortRxRapsDNF,
       "f3ErpUnitPortRxRapsBPR": f3ErpUnitPortRxRapsBPR,
       "f3ErpUnitPortRxRapsNodeId": f3ErpUnitPortRxRapsNodeId,
       "f3ErpUnitPortRapsFp": f3ErpUnitPortRapsFp,
       "f3ErpStatsObjects": f3ErpStatsObjects,
       "f3ErpUnitStatsTable": f3ErpUnitStatsTable,
       "f3ErpUnitStatsEntry": f3ErpUnitStatsEntry,
       "f3ErpUnitNumBlockedStateTrans": f3ErpUnitNumBlockedStateTrans,
       "f3ErpUnitRapsPDUsTx": f3ErpUnitRapsPDUsTx,
       "f3ErpUnitRapsPDUsRx": f3ErpUnitRapsPDUsRx,
       "f3ErpUnitRapsPDUsDiscarded": f3ErpUnitRapsPDUsDiscarded,
       "f3ErpUnitRapsNoReqPDUsTx": f3ErpUnitRapsNoReqPDUsTx,
       "f3ErpUnitRapsNoReqRBPDUsTx": f3ErpUnitRapsNoReqRBPDUsTx,
       "f3ErpUnitRapsSignalFailPDUsTx": f3ErpUnitRapsSignalFailPDUsTx,
       "f3ErpUnitRapsManualSwitchPDUsTx": f3ErpUnitRapsManualSwitchPDUsTx,
       "f3ErpUnitRapsForcedSwitchPDUsTx": f3ErpUnitRapsForcedSwitchPDUsTx,
       "f3ErpUnitRapsEventPDUsTx": f3ErpUnitRapsEventPDUsTx,
       "f3ErpUnitRapsNoReqPDUsRx": f3ErpUnitRapsNoReqPDUsRx,
       "f3ErpUnitRapsNoReqRBPDUsRx": f3ErpUnitRapsNoReqRBPDUsRx,
       "f3ErpUnitRapsSignalFailPDUsRx": f3ErpUnitRapsSignalFailPDUsRx,
       "f3ErpUnitRapsManualSwitchPDUsRx": f3ErpUnitRapsManualSwitchPDUsRx,
       "f3ErpUnitRapsForcedSwitchPDUsRx": f3ErpUnitRapsForcedSwitchPDUsRx,
       "f3ErpUnitRapsEventPDUsRx": f3ErpUnitRapsEventPDUsRx,
       "f3ErpUnitRapsInvalidOamVersionPDUsRx": f3ErpUnitRapsInvalidOamVersionPDUsRx,
       "f3ErpUnitRapsRsvdRequestPDUsRx": f3ErpUnitRapsRsvdRequestPDUsRx,
       "f3ErpUnitRapsRsvdEventSubcode": f3ErpUnitRapsRsvdEventSubcode,
       "f3ErpConformance": f3ErpConformance,
       "f3ErpCompliances": f3ErpCompliances,
       "f3ErpCompliance": f3ErpCompliance,
       "f3ErpGroups": f3ErpGroups,
       "f3ErpGroupGroup": f3ErpGroupGroup,
       "f3ErpUnitGroup": f3ErpUnitGroup,
       "f3ErpUnitStatsGroup": f3ErpUnitStatsGroup}
)
