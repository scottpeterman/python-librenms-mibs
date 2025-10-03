# SNMP MIB module (F3-EOTDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-EOTDM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:04 2025
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
 SecondaryState) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "OperationalState",
    "SecondaryState")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3EOTDMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17)
)
if mibBuilder.loadTexts:
    f3EOTDMMIB.setRevisions(
        ("2012-05-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VcgType(TextualConvention, Integer32):
    status = "current"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("t1", 1),
          ("e1", 2),
          ("t3", 3),
          ("e3", 4),
          ("vc12", 5),
          ("vc3", 6),
          ("vc4", 7),
          ("vt15", 8),
          ("sts1", 9),
          ("sts3c", 10))
    )



class WtrTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )



class HoldOffTime(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class CtrlState(TextualConvention, Integer32):
    status = "current"
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
        *(("ctrlNotAppl", 0),
          ("ctrlFixed", 1),
          ("ctrlAdd", 2),
          ("ctrlNorm", 3),
          ("ctrlEos", 4),
          ("ctrlIdle", 5),
          ("ctrlDnu", 6))
    )



class LcasSoState(TextualConvention, Integer32):
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
        *(("srcNotAppl", 0),
          ("srcIdle", 1),
          ("srcAdd", 2),
          ("srcNorm", 3),
          ("srcDnu", 4),
          ("srcRemove", 5))
    )



class MstState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mstNotAppl", 0),
          ("mstOk", 1),
          ("mstFail", 2))
    )



class LcasSkState(TextualConvention, Integer32):
    status = "current"
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
        *(("sinkNotAppl", 0),
          ("sinkIdle", 1),
          ("sinkOk", 2),
          ("sinkFail", 3))
    )



# MIB Managed Objects in the order of their OIDs

_F3EotdmObjects_ObjectIdentity = ObjectIdentity
f3EotdmObjects = _F3EotdmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1)
)
_VcgTable_Object = MibTable
vcgTable = _VcgTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1)
)
if mibBuilder.loadTexts:
    vcgTable.setStatus("current")
_VcgEntry_Object = MibTableRow
vcgEntry = _VcgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1)
)
vcgEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-EOTDM-MIB", "vcgIndex"),
)
if mibBuilder.loadTexts:
    vcgEntry.setStatus("current")


class _VcgIndex_Type(Integer32):
    """Custom type vcgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VcgIndex_Type.__name__ = "Integer32"
_VcgIndex_Object = MibTableColumn
vcgIndex = _VcgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 1),
    _VcgIndex_Type()
)
vcgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgIndex.setStatus("current")
_VcgIfIndex_Type = InterfaceIndex
_VcgIfIndex_Object = MibTableColumn
vcgIfIndex = _VcgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 2),
    _VcgIfIndex_Type()
)
vcgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgIfIndex.setStatus("current")
_VcgAssociatedEthernetPort_Type = VariablePointer
_VcgAssociatedEthernetPort_Object = MibTableColumn
vcgAssociatedEthernetPort = _VcgAssociatedEthernetPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 3),
    _VcgAssociatedEthernetPort_Type()
)
vcgAssociatedEthernetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgAssociatedEthernetPort.setStatus("current")
_VcgAdminState_Type = AdminState
_VcgAdminState_Object = MibTableColumn
vcgAdminState = _VcgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 4),
    _VcgAdminState_Type()
)
vcgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcgAdminState.setStatus("current")
_VcgOperationalState_Type = OperationalState
_VcgOperationalState_Object = MibTableColumn
vcgOperationalState = _VcgOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 5),
    _VcgOperationalState_Type()
)
vcgOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgOperationalState.setStatus("current")
_VcgSecondaryState_Type = SecondaryState
_VcgSecondaryState_Object = MibTableColumn
vcgSecondaryState = _VcgSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 6),
    _VcgSecondaryState_Type()
)
vcgSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgSecondaryState.setStatus("current")
_VcgType_Type = VcgType
_VcgType_Object = MibTableColumn
vcgType = _VcgType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 7),
    _VcgType_Type()
)
vcgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgType.setStatus("current")
_VcgLcasEnabled_Type = TruthValue
_VcgLcasEnabled_Object = MibTableColumn
vcgLcasEnabled = _VcgLcasEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 8),
    _VcgLcasEnabled_Type()
)
vcgLcasEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcgLcasEnabled.setStatus("current")
_VcgWtrTimer_Type = WtrTime
_VcgWtrTimer_Object = MibTableColumn
vcgWtrTimer = _VcgWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 9),
    _VcgWtrTimer_Type()
)
vcgWtrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcgWtrTimer.setStatus("current")
_VcgHoldOffTimer_Type = HoldOffTime
_VcgHoldOffTimer_Object = MibTableColumn
vcgHoldOffTimer = _VcgHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 10),
    _VcgHoldOffTimer_Type()
)
vcgHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vcgHoldOffTimer.setStatus("current")


class _VcgClearWtrTimer_Type(Integer32):
    """Custom type vcgClearWtrTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VcgClearWtrTimer_Type.__name__ = "Integer32"
_VcgClearWtrTimer_Object = MibTableColumn
vcgClearWtrTimer = _VcgClearWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 11),
    _VcgClearWtrTimer_Type()
)
vcgClearWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgClearWtrTimer.setStatus("current")
_VcgRowStatus_Type = RowStatus
_VcgRowStatus_Object = MibTableColumn
vcgRowStatus = _VcgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 1, 1, 12),
    _VcgRowStatus_Type()
)
vcgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgRowStatus.setStatus("current")
_VcgMemberTable_Object = MibTable
vcgMemberTable = _VcgMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2)
)
if mibBuilder.loadTexts:
    vcgMemberTable.setStatus("current")
_VcgMemberEntry_Object = MibTableRow
vcgMemberEntry = _VcgMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1)
)
vcgMemberEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-EOTDM-MIB", "vcgIndex"),
    (0, "F3-EOTDM-MIB", "vcgMemberIndex"),
)
if mibBuilder.loadTexts:
    vcgMemberEntry.setStatus("current")
_VcgMemberIndex_Type = Integer32
_VcgMemberIndex_Object = MibTableColumn
vcgMemberIndex = _VcgMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 1),
    _VcgMemberIndex_Type()
)
vcgMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberIndex.setStatus("current")
_VcgMemberIfIndex_Type = InterfaceIndex
_VcgMemberIfIndex_Object = MibTableColumn
vcgMemberIfIndex = _VcgMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 2),
    _VcgMemberIfIndex_Type()
)
vcgMemberIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgMemberIfIndex.setStatus("current")
_VcgMemberRowStatus_Type = RowStatus
_VcgMemberRowStatus_Object = MibTableColumn
vcgMemberRowStatus = _VcgMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 3),
    _VcgMemberRowStatus_Type()
)
vcgMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vcgMemberRowStatus.setStatus("current")


class _VcgMemberSoSendSeq_Type(Integer32):
    """Custom type vcgMemberSoSendSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_VcgMemberSoSendSeq_Type.__name__ = "Integer32"
_VcgMemberSoSendSeq_Object = MibTableColumn
vcgMemberSoSendSeq = _VcgMemberSoSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 4),
    _VcgMemberSoSendSeq_Type()
)
vcgMemberSoSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSoSendSeq.setStatus("current")
_VcgMemberSoLcasSendCtrl_Type = CtrlState
_VcgMemberSoLcasSendCtrl_Object = MibTableColumn
vcgMemberSoLcasSendCtrl = _VcgMemberSoLcasSendCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 5),
    _VcgMemberSoLcasSendCtrl_Type()
)
vcgMemberSoLcasSendCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSoLcasSendCtrl.setStatus("current")
_VcgMemberSoLcasRecvMst_Type = MstState
_VcgMemberSoLcasRecvMst_Object = MibTableColumn
vcgMemberSoLcasRecvMst = _VcgMemberSoLcasRecvMst_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 6),
    _VcgMemberSoLcasRecvMst_Type()
)
vcgMemberSoLcasRecvMst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSoLcasRecvMst.setStatus("current")
_VcgMemberSoLcasState_Type = LcasSoState
_VcgMemberSoLcasState_Object = MibTableColumn
vcgMemberSoLcasState = _VcgMemberSoLcasState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 7),
    _VcgMemberSoLcasState_Type()
)
vcgMemberSoLcasState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSoLcasState.setStatus("current")


class _VcgMemberSkRecvSeq_Type(Integer32):
    """Custom type vcgMemberSkRecvSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_VcgMemberSkRecvSeq_Type.__name__ = "Integer32"
_VcgMemberSkRecvSeq_Object = MibTableColumn
vcgMemberSkRecvSeq = _VcgMemberSkRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 8),
    _VcgMemberSkRecvSeq_Type()
)
vcgMemberSkRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSkRecvSeq.setStatus("current")


class _VcgMemberSkRecvExpectSeq_Type(Integer32):
    """Custom type vcgMemberSkRecvExpectSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_VcgMemberSkRecvExpectSeq_Type.__name__ = "Integer32"
_VcgMemberSkRecvExpectSeq_Object = MibTableColumn
vcgMemberSkRecvExpectSeq = _VcgMemberSkRecvExpectSeq_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 9),
    _VcgMemberSkRecvExpectSeq_Type()
)
vcgMemberSkRecvExpectSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSkRecvExpectSeq.setStatus("current")
_VcgMemberSkLcasRecvCtrl_Type = CtrlState
_VcgMemberSkLcasRecvCtrl_Object = MibTableColumn
vcgMemberSkLcasRecvCtrl = _VcgMemberSkLcasRecvCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 10),
    _VcgMemberSkLcasRecvCtrl_Type()
)
vcgMemberSkLcasRecvCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSkLcasRecvCtrl.setStatus("current")
_VcgMemberSkLcasSendMst_Type = MstState
_VcgMemberSkLcasSendMst_Object = MibTableColumn
vcgMemberSkLcasSendMst = _VcgMemberSkLcasSendMst_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 11),
    _VcgMemberSkLcasSendMst_Type()
)
vcgMemberSkLcasSendMst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSkLcasSendMst.setStatus("current")
_VcgMemberSkLcasState_Type = LcasSkState
_VcgMemberSkLcasState_Object = MibTableColumn
vcgMemberSkLcasState = _VcgMemberSkLcasState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 1, 2, 1, 12),
    _VcgMemberSkLcasState_Type()
)
vcgMemberSkLcasState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcgMemberSkLcasState.setStatus("current")
_F3EotdmConformance_ObjectIdentity = ObjectIdentity
f3EotdmConformance = _F3EotdmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2)
)
_F3EotdmCompliances_ObjectIdentity = ObjectIdentity
f3EotdmCompliances = _F3EotdmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 1)
)
_F3EotdmGroups_ObjectIdentity = ObjectIdentity
f3EotdmGroups = _F3EotdmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 2)
)

# Managed Objects groups

f3EotdmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 2, 1)
)
f3EotdmObjectGroup.setObjects(
      *(("F3-EOTDM-MIB", "vcgIndex"),
        ("F3-EOTDM-MIB", "vcgIfIndex"),
        ("F3-EOTDM-MIB", "vcgAssociatedEthernetPort"),
        ("F3-EOTDM-MIB", "vcgAdminState"),
        ("F3-EOTDM-MIB", "vcgOperationalState"),
        ("F3-EOTDM-MIB", "vcgSecondaryState"),
        ("F3-EOTDM-MIB", "vcgType"),
        ("F3-EOTDM-MIB", "vcgLcasEnabled"),
        ("F3-EOTDM-MIB", "vcgWtrTimer"),
        ("F3-EOTDM-MIB", "vcgHoldOffTimer"),
        ("F3-EOTDM-MIB", "vcgClearWtrTimer"),
        ("F3-EOTDM-MIB", "vcgRowStatus"),
        ("F3-EOTDM-MIB", "vcgMemberIndex"),
        ("F3-EOTDM-MIB", "vcgMemberIfIndex"),
        ("F3-EOTDM-MIB", "vcgMemberRowStatus"),
        ("F3-EOTDM-MIB", "vcgMemberSoSendSeq"),
        ("F3-EOTDM-MIB", "vcgMemberSoLcasSendCtrl"),
        ("F3-EOTDM-MIB", "vcgMemberSoLcasRecvMst"),
        ("F3-EOTDM-MIB", "vcgMemberSoLcasState"),
        ("F3-EOTDM-MIB", "vcgMemberSkRecvSeq"),
        ("F3-EOTDM-MIB", "vcgMemberSkRecvExpectSeq"),
        ("F3-EOTDM-MIB", "vcgMemberSkLcasRecvCtrl"),
        ("F3-EOTDM-MIB", "vcgMemberSkLcasSendMst"),
        ("F3-EOTDM-MIB", "vcgMemberSkLcasState"))
)
if mibBuilder.loadTexts:
    f3EotdmObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3EotdmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 17, 2, 1, 1)
)
f3EotdmCompliance.setObjects(
    ("F3-EOTDM-MIB", "f3EotdmObjectGroup")
)
if mibBuilder.loadTexts:
    f3EotdmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-EOTDM-MIB",
    **{"VcgType": VcgType,
       "WtrTime": WtrTime,
       "HoldOffTime": HoldOffTime,
       "CtrlState": CtrlState,
       "LcasSoState": LcasSoState,
       "MstState": MstState,
       "LcasSkState": LcasSkState,
       "f3EOTDMMIB": f3EOTDMMIB,
       "f3EotdmObjects": f3EotdmObjects,
       "vcgTable": vcgTable,
       "vcgEntry": vcgEntry,
       "vcgIndex": vcgIndex,
       "vcgIfIndex": vcgIfIndex,
       "vcgAssociatedEthernetPort": vcgAssociatedEthernetPort,
       "vcgAdminState": vcgAdminState,
       "vcgOperationalState": vcgOperationalState,
       "vcgSecondaryState": vcgSecondaryState,
       "vcgType": vcgType,
       "vcgLcasEnabled": vcgLcasEnabled,
       "vcgWtrTimer": vcgWtrTimer,
       "vcgHoldOffTimer": vcgHoldOffTimer,
       "vcgClearWtrTimer": vcgClearWtrTimer,
       "vcgRowStatus": vcgRowStatus,
       "vcgMemberTable": vcgMemberTable,
       "vcgMemberEntry": vcgMemberEntry,
       "vcgMemberIndex": vcgMemberIndex,
       "vcgMemberIfIndex": vcgMemberIfIndex,
       "vcgMemberRowStatus": vcgMemberRowStatus,
       "vcgMemberSoSendSeq": vcgMemberSoSendSeq,
       "vcgMemberSoLcasSendCtrl": vcgMemberSoLcasSendCtrl,
       "vcgMemberSoLcasRecvMst": vcgMemberSoLcasRecvMst,
       "vcgMemberSoLcasState": vcgMemberSoLcasState,
       "vcgMemberSkRecvSeq": vcgMemberSkRecvSeq,
       "vcgMemberSkRecvExpectSeq": vcgMemberSkRecvExpectSeq,
       "vcgMemberSkLcasRecvCtrl": vcgMemberSkLcasRecvCtrl,
       "vcgMemberSkLcasSendMst": vcgMemberSkLcasSendMst,
       "vcgMemberSkLcasState": vcgMemberSkLcasState,
       "f3EotdmConformance": f3EotdmConformance,
       "f3EotdmCompliances": f3EotdmCompliances,
       "f3EotdmCompliance": f3EotdmCompliance,
       "f3EotdmGroups": f3EotdmGroups,
       "f3EotdmObjectGroup": f3EotdmObjectGroup}
)
