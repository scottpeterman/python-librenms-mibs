# SNMP MIB module (TN-ETHSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-ETHSOAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:27 2025
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

(dot1agCfmLtrEntry,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmLtrEntry",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnEthSoamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105)
)
if mibBuilder.loadTexts:
    tnEthSoamMIB.setRevisions(
        ("2012-04-20 00:00",
         "2014-05-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot1agCfmMepId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )



class Dot1agCfmMpDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



class Dot1agCfmMaintDomainName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )



class Dot1agCfmMaintAssocName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class Dot1agCfmMDLevel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TnEthSoamType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("esp", 2),
          ("evc", 3),
          ("vlan", 4),
          ("mplslink", 5),
          ("mplstunnel", 6),
          ("mplspw", 7),
          ("mplslsp", 8))
    )



class TnEthSoamTestPatternType(TextualConvention, Integer32):
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
        *(("allzero", 1),
          ("allone", 2),
          ("onezero", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TnEthSoamMIBNotifications_ObjectIdentity = ObjectIdentity
tnEthSoamMIBNotifications = _TnEthSoamMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 0)
)
_TnEthSoamMIBObjects_ObjectIdentity = ObjectIdentity
tnEthSoamMIBObjects = _TnEthSoamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1)
)
_TnEthSoamMPMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamMPMgmt = _TnEthSoamMPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1)
)
_TnEthSoamMPTable_Object = MibTable
tnEthSoamMPTable = _TnEthSoamMPTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamMPTable.setStatus("current")
_TnEthSoamMPEntry_Object = MibTableRow
tnEthSoamMPEntry = _TnEthSoamMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1)
)
tnEthSoamMPEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamMPEntry.setStatus("current")


class _TnEthSoaminstance_Type(Unsigned32):
    """Custom type tnEthSoaminstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnEthSoaminstance_Type.__name__ = "Unsigned32"
_TnEthSoaminstance_Object = MibTableColumn
tnEthSoaminstance = _TnEthSoaminstance_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 1),
    _TnEthSoaminstance_Type()
)
tnEthSoaminstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoaminstance.setStatus("current")
_TnEthSoamDomaintype_Type = TnEthSoamType
_TnEthSoamDomaintype_Object = MibTableColumn
tnEthSoamDomaintype = _TnEthSoamDomaintype_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 2),
    _TnEthSoamDomaintype_Type()
)
tnEthSoamDomaintype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDomaintype.setStatus("current")


class _TnEthSoamMode_Type(Integer32):
    """Custom type tnEthSoamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mep", 1),
          ("mip", 2))
    )


_TnEthSoamMode_Type.__name__ = "Integer32"
_TnEthSoamMode_Object = MibTableColumn
tnEthSoamMode = _TnEthSoamMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 3),
    _TnEthSoamMode_Type()
)
tnEthSoamMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamMode.setStatus("current")
_TnEthSoamdirection_Type = Dot1agCfmMpDirection
_TnEthSoamdirection_Object = MibTableColumn
tnEthSoamdirection = _TnEthSoamdirection_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 4),
    _TnEthSoamdirection_Type()
)
tnEthSoamdirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamdirection.setStatus("current")
_TnEthSoamresidencePort_Type = InterfaceIndex
_TnEthSoamresidencePort_Object = MibTableColumn
tnEthSoamresidencePort = _TnEthSoamresidencePort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 5),
    _TnEthSoamresidencePort_Type()
)
tnEthSoamresidencePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamresidencePort.setStatus("current")
_TnEthSoamlevel_Type = Dot1agCfmMDLevel
_TnEthSoamlevel_Object = MibTableColumn
tnEthSoamlevel = _TnEthSoamlevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 6),
    _TnEthSoamlevel_Type()
)
tnEthSoamlevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamlevel.setStatus("current")
_TnEthSoamFlowInstance_Type = Integer32
_TnEthSoamFlowInstance_Object = MibTableColumn
tnEthSoamFlowInstance = _TnEthSoamFlowInstance_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 7),
    _TnEthSoamFlowInstance_Type()
)
tnEthSoamFlowInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamFlowInstance.setStatus("current")
_TnEthSoamTaggedVID_Type = VlanIdOrNone
_TnEthSoamTaggedVID_Object = MibTableColumn
tnEthSoamTaggedVID = _TnEthSoamTaggedVID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 8),
    _TnEthSoamTaggedVID_Type()
)
tnEthSoamTaggedVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamTaggedVID.setStatus("current")
_TnEthSoamAlarm_Type = TruthValue
_TnEthSoamAlarm_Object = MibTableColumn
tnEthSoamAlarm = _TnEthSoamAlarm_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 9),
    _TnEthSoamAlarm_Type()
)
tnEthSoamAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamAlarm.setStatus("current")
_TnEthSoamStatus_Type = RowStatus
_TnEthSoamStatus_Object = MibTableColumn
tnEthSoamStatus = _TnEthSoamStatus_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 1, 1, 1, 11),
    _TnEthSoamStatus_Type()
)
tnEthSoamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamStatus.setStatus("current")
_TnEthSoamPeerCfgMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamPeerCfgMgmt = _TnEthSoamPeerCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 2)
)
_TnEthSoamPeerCfgTable_Object = MibTable
tnEthSoamPeerCfgTable = _TnEthSoamPeerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamPeerCfgTable.setStatus("current")
_TnEthSoamPeerCfgEntry_Object = MibTableRow
tnEthSoamPeerCfgEntry = _TnEthSoamPeerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 2, 1, 1)
)
tnEthSoamPeerCfgEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
    (0, "TN-ETHSOAM-MIB", "tnEthSoamPeerCfgMepId"),
)
if mibBuilder.loadTexts:
    tnEthSoamPeerCfgEntry.setStatus("current")
_TnEthSoamPeerCfgMepId_Type = Dot1agCfmMepId
_TnEthSoamPeerCfgMepId_Object = MibTableColumn
tnEthSoamPeerCfgMepId = _TnEthSoamPeerCfgMepId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 2, 1, 1, 1),
    _TnEthSoamPeerCfgMepId_Type()
)
tnEthSoamPeerCfgMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoamPeerCfgMepId.setStatus("current")
_TnEthSoamPeerCfgUnicastMac_Type = MacAddress
_TnEthSoamPeerCfgUnicastMac_Object = MibTableColumn
tnEthSoamPeerCfgUnicastMac = _TnEthSoamPeerCfgUnicastMac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 2, 1, 1, 2),
    _TnEthSoamPeerCfgUnicastMac_Type()
)
tnEthSoamPeerCfgUnicastMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamPeerCfgUnicastMac.setStatus("current")
_TnEthSoamPeerCfgRowState_Type = RowStatus
_TnEthSoamPeerCfgRowState_Object = MibTableColumn
tnEthSoamPeerCfgRowState = _TnEthSoamPeerCfgRowState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 2, 1, 1, 3),
    _TnEthSoamPeerCfgRowState_Type()
)
tnEthSoamPeerCfgRowState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamPeerCfgRowState.setStatus("current")
_TnEthSoamPeerStatusMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamPeerStatusMgmt = _TnEthSoamPeerStatusMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 3)
)
_TnEthSoamPeerStatusTable_Object = MibTable
tnEthSoamPeerStatusTable = _TnEthSoamPeerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamPeerStatusTable.setStatus("current")
_TnEthSoamPeerStatusEntry_Object = MibTableRow
tnEthSoamPeerStatusEntry = _TnEthSoamPeerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 3, 1, 1)
)
tnEthSoamPeerStatusEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
    (0, "TN-ETHSOAM-MIB", "tnEthSoamPeerStatusMepId"),
)
if mibBuilder.loadTexts:
    tnEthSoamPeerStatusEntry.setStatus("current")
_TnEthSoamPeerStatusMepId_Type = Dot1agCfmMepId
_TnEthSoamPeerStatusMepId_Object = MibTableColumn
tnEthSoamPeerStatusMepId = _TnEthSoamPeerStatusMepId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 3, 1, 1, 1),
    _TnEthSoamPeerStatusMepId_Type()
)
tnEthSoamPeerStatusMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSoamPeerStatusMepId.setStatus("current")
_TnEthSoamPeerStatuscLOC_Type = TruthValue
_TnEthSoamPeerStatuscLOC_Object = MibTableColumn
tnEthSoamPeerStatuscLOC = _TnEthSoamPeerStatuscLOC_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 3, 1, 1, 2),
    _TnEthSoamPeerStatuscLOC_Type()
)
tnEthSoamPeerStatuscLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPeerStatuscLOC.setStatus("current")
_TnEthSoamPeerStatuscRDI_Type = TruthValue
_TnEthSoamPeerStatuscRDI_Object = MibTableColumn
tnEthSoamPeerStatuscRDI = _TnEthSoamPeerStatuscRDI_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 3, 1, 1, 3),
    _TnEthSoamPeerStatuscRDI_Type()
)
tnEthSoamPeerStatuscRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPeerStatuscRDI.setStatus("current")
_TnEthSoamPeerStatuscPeriod_Type = TruthValue
_TnEthSoamPeerStatuscPeriod_Object = MibTableColumn
tnEthSoamPeerStatuscPeriod = _TnEthSoamPeerStatuscPeriod_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 3, 1, 1, 4),
    _TnEthSoamPeerStatuscPeriod_Type()
)
tnEthSoamPeerStatuscPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPeerStatuscPeriod.setStatus("current")
_TnEthSoamPeerStatuscPriority_Type = TruthValue
_TnEthSoamPeerStatuscPriority_Object = MibTableColumn
tnEthSoamPeerStatuscPriority = _TnEthSoamPeerStatuscPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 3, 1, 1, 5),
    _TnEthSoamPeerStatuscPriority_Type()
)
tnEthSoamPeerStatuscPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamPeerStatuscPriority.setStatus("current")
_TnEthSoamAPSCfgMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamAPSCfgMgmt = _TnEthSoamAPSCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 4)
)
_TnEthSoamAPSCfgTable_Object = MibTable
tnEthSoamAPSCfgTable = _TnEthSoamAPSCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamAPSCfgTable.setStatus("current")
_TnEthSoamAPSCfgEntry_Object = MibTableRow
tnEthSoamAPSCfgEntry = _TnEthSoamAPSCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 4, 1, 1)
)
tnEthSoamAPSCfgEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamAPSCfgEntry.setStatus("current")
_TnEthSoamAPSCfgEnable_Type = TruthValue
_TnEthSoamAPSCfgEnable_Object = MibTableColumn
tnEthSoamAPSCfgEnable = _TnEthSoamAPSCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 4, 1, 1, 1),
    _TnEthSoamAPSCfgEnable_Type()
)
tnEthSoamAPSCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamAPSCfgEnable.setStatus("current")
_TnEthSoamAPSCfgPriority_Type = IEEE8021PriorityValue
_TnEthSoamAPSCfgPriority_Object = MibTableColumn
tnEthSoamAPSCfgPriority = _TnEthSoamAPSCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 4, 1, 1, 2),
    _TnEthSoamAPSCfgPriority_Type()
)
tnEthSoamAPSCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamAPSCfgPriority.setStatus("current")


class _TnEthSoamAPSCfgCast_Type(Integer32):
    """Custom type tnEthSoamAPSCfgCast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 0),
          ("multicast", 1))
    )


_TnEthSoamAPSCfgCast_Type.__name__ = "Integer32"
_TnEthSoamAPSCfgCast_Object = MibTableColumn
tnEthSoamAPSCfgCast = _TnEthSoamAPSCfgCast_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 4, 1, 1, 3),
    _TnEthSoamAPSCfgCast_Type()
)
tnEthSoamAPSCfgCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamAPSCfgCast.setStatus("current")


class _TnEthSoamAPSCfgType_Type(Integer32):
    """Custom type tnEthSoamAPSCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("raps", 0),
          ("laps", 1))
    )


_TnEthSoamAPSCfgType_Type.__name__ = "Integer32"
_TnEthSoamAPSCfgType_Object = MibTableColumn
tnEthSoamAPSCfgType = _TnEthSoamAPSCfgType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 4, 1, 1, 4),
    _TnEthSoamAPSCfgType_Type()
)
tnEthSoamAPSCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamAPSCfgType.setStatus("current")


class _TnEthSoamAPSCfgLastOctet_Type(Unsigned32):
    """Custom type tnEthSoamAPSCfgLastOctet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TnEthSoamAPSCfgLastOctet_Type.__name__ = "Unsigned32"
_TnEthSoamAPSCfgLastOctet_Object = MibTableColumn
tnEthSoamAPSCfgLastOctet = _TnEthSoamAPSCfgLastOctet_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 4, 1, 1, 5),
    _TnEthSoamAPSCfgLastOctet_Type()
)
tnEthSoamAPSCfgLastOctet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamAPSCfgLastOctet.setStatus("current")
_TnEthSoamClientCfgMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamClientCfgMgmt = _TnEthSoamClientCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5)
)
_TnEthSoamClientCfgTable_Object = MibTable
tnEthSoamClientCfgTable = _TnEthSoamClientCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamClientCfgTable.setStatus("current")
_TnEthSoamClientCfgEntry_Object = MibTableRow
tnEthSoamClientCfgEntry = _TnEthSoamClientCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1)
)
tnEthSoamClientCfgEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamClientCfgEntry.setStatus("current")
_TnEthSoamClientCfgDomain_Type = TnEthSoamType
_TnEthSoamClientCfgDomain_Object = MibTableColumn
tnEthSoamClientCfgDomain = _TnEthSoamClientCfgDomain_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 1),
    _TnEthSoamClientCfgDomain_Type()
)
tnEthSoamClientCfgDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgDomain.setStatus("current")
_TnEthSoamClientCfgLevel_Type = Dot1agCfmMDLevel
_TnEthSoamClientCfgLevel_Object = MibTableColumn
tnEthSoamClientCfgLevel = _TnEthSoamClientCfgLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 2),
    _TnEthSoamClientCfgLevel_Type()
)
tnEthSoamClientCfgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgLevel.setStatus("current")
_TnEthSoamClientCfgFlow1_Type = Unsigned32
_TnEthSoamClientCfgFlow1_Object = MibTableColumn
tnEthSoamClientCfgFlow1 = _TnEthSoamClientCfgFlow1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 3),
    _TnEthSoamClientCfgFlow1_Type()
)
tnEthSoamClientCfgFlow1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow1.setStatus("current")
_TnEthSoamClientCfgFlow2_Type = Unsigned32
_TnEthSoamClientCfgFlow2_Object = MibTableColumn
tnEthSoamClientCfgFlow2 = _TnEthSoamClientCfgFlow2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 4),
    _TnEthSoamClientCfgFlow2_Type()
)
tnEthSoamClientCfgFlow2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow2.setStatus("current")
_TnEthSoamClientCfgFlow3_Type = Unsigned32
_TnEthSoamClientCfgFlow3_Object = MibTableColumn
tnEthSoamClientCfgFlow3 = _TnEthSoamClientCfgFlow3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 5),
    _TnEthSoamClientCfgFlow3_Type()
)
tnEthSoamClientCfgFlow3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow3.setStatus("current")
_TnEthSoamClientCfgFlow4_Type = Unsigned32
_TnEthSoamClientCfgFlow4_Object = MibTableColumn
tnEthSoamClientCfgFlow4 = _TnEthSoamClientCfgFlow4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 6),
    _TnEthSoamClientCfgFlow4_Type()
)
tnEthSoamClientCfgFlow4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow4.setStatus("current")
_TnEthSoamClientCfgFlow5_Type = Unsigned32
_TnEthSoamClientCfgFlow5_Object = MibTableColumn
tnEthSoamClientCfgFlow5 = _TnEthSoamClientCfgFlow5_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 7),
    _TnEthSoamClientCfgFlow5_Type()
)
tnEthSoamClientCfgFlow5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow5.setStatus("current")
_TnEthSoamClientCfgFlow6_Type = Unsigned32
_TnEthSoamClientCfgFlow6_Object = MibTableColumn
tnEthSoamClientCfgFlow6 = _TnEthSoamClientCfgFlow6_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 8),
    _TnEthSoamClientCfgFlow6_Type()
)
tnEthSoamClientCfgFlow6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow6.setStatus("current")
_TnEthSoamClientCfgFlow7_Type = Unsigned32
_TnEthSoamClientCfgFlow7_Object = MibTableColumn
tnEthSoamClientCfgFlow7 = _TnEthSoamClientCfgFlow7_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 9),
    _TnEthSoamClientCfgFlow7_Type()
)
tnEthSoamClientCfgFlow7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow7.setStatus("current")
_TnEthSoamClientCfgFlow8_Type = Unsigned32
_TnEthSoamClientCfgFlow8_Object = MibTableColumn
tnEthSoamClientCfgFlow8 = _TnEthSoamClientCfgFlow8_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 10),
    _TnEthSoamClientCfgFlow8_Type()
)
tnEthSoamClientCfgFlow8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow8.setStatus("current")
_TnEthSoamClientCfgFlow9_Type = Unsigned32
_TnEthSoamClientCfgFlow9_Object = MibTableColumn
tnEthSoamClientCfgFlow9 = _TnEthSoamClientCfgFlow9_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 11),
    _TnEthSoamClientCfgFlow9_Type()
)
tnEthSoamClientCfgFlow9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow9.setStatus("current")
_TnEthSoamClientCfgFlow10_Type = Unsigned32
_TnEthSoamClientCfgFlow10_Object = MibTableColumn
tnEthSoamClientCfgFlow10 = _TnEthSoamClientCfgFlow10_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 5, 1, 1, 12),
    _TnEthSoamClientCfgFlow10_Type()
)
tnEthSoamClientCfgFlow10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamClientCfgFlow10.setStatus("current")
_TnEthSoamLocalCfgMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamLocalCfgMgmt = _TnEthSoamLocalCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6)
)
_TnEthSoamLocalCfgTable_Object = MibTable
tnEthSoamLocalCfgTable = _TnEthSoamLocalCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamLocalCfgTable.setStatus("current")
_TnEthSoamLocalCfgEntry_Object = MibTableRow
tnEthSoamLocalCfgEntry = _TnEthSoamLocalCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1)
)
tnEthSoamLocalCfgEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamLocalCfgEntry.setStatus("current")


class _TnEthSoamFormat_Type(Integer32):
    """Custom type tnEthSoamFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("itu", 1),
          ("ieee", 2))
    )


_TnEthSoamFormat_Type.__name__ = "Integer32"
_TnEthSoamFormat_Object = MibTableColumn
tnEthSoamFormat = _TnEthSoamFormat_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1, 1),
    _TnEthSoamFormat_Type()
)
tnEthSoamFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamFormat.setStatus("current")
_TnEthSoamDomainName_Type = OctetString
_TnEthSoamDomainName_Object = MibTableColumn
tnEthSoamDomainName = _TnEthSoamDomainName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1, 2),
    _TnEthSoamDomainName_Type()
)
tnEthSoamDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamDomainName.setStatus("current")
_TnEthSoamMegOrMaName_Type = OctetString
_TnEthSoamMegOrMaName_Object = MibTableColumn
tnEthSoamMegOrMaName = _TnEthSoamMegOrMaName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1, 3),
    _TnEthSoamMegOrMaName_Type()
)
tnEthSoamMegOrMaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamMegOrMaName.setStatus("current")
_TnEthSoamMepID_Type = Dot1agCfmMepId
_TnEthSoamMepID_Object = MibTableColumn
tnEthSoamMepID = _TnEthSoamMepID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1, 4),
    _TnEthSoamMepID_Type()
)
tnEthSoamMepID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamMepID.setStatus("current")


class _TnEthSoamCcmInterval_Type(Integer32):
    """Custom type tnEthSoamCcmInterval based on Integer32"""
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
        *(("interval300s", 1),
          ("interval100s", 2),
          ("interval10s", 3),
          ("interval1s", 4),
          ("interval6M", 5),
          ("interval1M", 6),
          ("interval6H", 7))
    )


_TnEthSoamCcmInterval_Type.__name__ = "Integer32"
_TnEthSoamCcmInterval_Object = MibTableColumn
tnEthSoamCcmInterval = _TnEthSoamCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1, 5),
    _TnEthSoamCcmInterval_Type()
)
tnEthSoamCcmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamCcmInterval.setStatus("current")


class _TnEthSoamEVCQos_Type(Integer32):
    """Custom type tnEthSoamEVCQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TnEthSoamEVCQos_Type.__name__ = "Integer32"
_TnEthSoamEVCQos_Object = MibTableColumn
tnEthSoamEVCQos = _TnEthSoamEVCQos_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1, 6),
    _TnEthSoamEVCQos_Type()
)
tnEthSoamEVCQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamEVCQos.setStatus("current")


class _TnEthSoamEVCPolicyID_Type(Integer32):
    """Custom type tnEthSoamEVCPolicyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TnEthSoamEVCPolicyID_Type.__name__ = "Integer32"
_TnEthSoamEVCPolicyID_Object = MibTableColumn
tnEthSoamEVCPolicyID = _TnEthSoamEVCPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1, 7),
    _TnEthSoamEVCPolicyID_Type()
)
tnEthSoamEVCPolicyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamEVCPolicyID.setStatus("current")
_TnEthSoamVOE_Type = TruthValue
_TnEthSoamVOE_Object = MibTableColumn
tnEthSoamVOE = _TnEthSoamVOE_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 6, 1, 1, 8),
    _TnEthSoamVOE_Type()
)
tnEthSoamVOE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamVOE.setStatus("current")
_TnEthSoamStatusMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamStatusMgmt = _TnEthSoamStatusMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7)
)
_TnEthSoamStatusTable_Object = MibTable
tnEthSoamStatusTable = _TnEthSoamStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamStatusTable.setStatus("current")
_TnEthSoamStatusEntry_Object = MibTableRow
tnEthSoamStatusEntry = _TnEthSoamStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1)
)
tnEthSoamStatusEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamStatusEntry.setStatus("current")
_TnEthSoamStatusCCMLevel_Type = TruthValue
_TnEthSoamStatusCCMLevel_Object = MibTableColumn
tnEthSoamStatusCCMLevel = _TnEthSoamStatusCCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1, 1),
    _TnEthSoamStatusCCMLevel_Type()
)
tnEthSoamStatusCCMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamStatusCCMLevel.setStatus("current")
_TnEthSoamStatusCCMMeg_Type = TruthValue
_TnEthSoamStatusCCMMeg_Object = MibTableColumn
tnEthSoamStatusCCMMeg = _TnEthSoamStatusCCMMeg_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1, 2),
    _TnEthSoamStatusCCMMeg_Type()
)
tnEthSoamStatusCCMMeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamStatusCCMMeg.setStatus("current")
_TnEthSoamStatusCCMMep_Type = TruthValue
_TnEthSoamStatusCCMMep_Object = MibTableColumn
tnEthSoamStatusCCMMep = _TnEthSoamStatusCCMMep_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1, 3),
    _TnEthSoamStatusCCMMep_Type()
)
tnEthSoamStatusCCMMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamStatusCCMMep.setStatus("current")
_TnEthSoamStatusAIS_Type = TruthValue
_TnEthSoamStatusAIS_Object = MibTableColumn
tnEthSoamStatusAIS = _TnEthSoamStatusAIS_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1, 4),
    _TnEthSoamStatusAIS_Type()
)
tnEthSoamStatusAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamStatusAIS.setStatus("current")
_TnEthSoamStatusCLK_Type = TruthValue
_TnEthSoamStatusCLK_Object = MibTableColumn
tnEthSoamStatusCLK = _TnEthSoamStatusCLK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1, 5),
    _TnEthSoamStatusCLK_Type()
)
tnEthSoamStatusCLK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamStatusCLK.setStatus("current")
_TnEthSoamStatusSSF_Type = TruthValue
_TnEthSoamStatusSSF_Object = MibTableColumn
tnEthSoamStatusSSF = _TnEthSoamStatusSSF_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1, 6),
    _TnEthSoamStatusSSF_Type()
)
tnEthSoamStatusSSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamStatusSSF.setStatus("current")
_TnEthSoamStatusBLK_Type = TruthValue
_TnEthSoamStatusBLK_Object = MibTableColumn
tnEthSoamStatusBLK = _TnEthSoamStatusBLK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1, 7),
    _TnEthSoamStatusBLK_Type()
)
tnEthSoamStatusBLK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamStatusBLK.setStatus("current")
_TnEthSoamStatusTSF_Type = TruthValue
_TnEthSoamStatusTSF_Object = MibTableColumn
tnEthSoamStatusTSF = _TnEthSoamStatusTSF_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 7, 1, 1, 8),
    _TnEthSoamStatusTSF_Type()
)
tnEthSoamStatusTSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamStatusTSF.setStatus("current")
_TnEthSoamLossStateMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamLossStateMgmt = _TnEthSoamLossStateMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8)
)
_TnEthSoamLossStateTable_Object = MibTable
tnEthSoamLossStateTable = _TnEthSoamLossStateTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamLossStateTable.setStatus("current")
_TnEthSoamLossStateEntry_Object = MibTableRow
tnEthSoamLossStateEntry = _TnEthSoamLossStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1, 1)
)
tnEthSoamLossStateEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamLossStateEntry.setStatus("current")
_TnEthSoamLossStateTxCount_Type = Gauge32
_TnEthSoamLossStateTxCount_Object = MibTableColumn
tnEthSoamLossStateTxCount = _TnEthSoamLossStateTxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1, 1, 1),
    _TnEthSoamLossStateTxCount_Type()
)
tnEthSoamLossStateTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamLossStateTxCount.setStatus("current")
_TnEthSoamLossStateRxCount_Type = Gauge32
_TnEthSoamLossStateRxCount_Object = MibTableColumn
tnEthSoamLossStateRxCount = _TnEthSoamLossStateRxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1, 1, 2),
    _TnEthSoamLossStateRxCount_Type()
)
tnEthSoamLossStateRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamLossStateRxCount.setStatus("current")
_TnEthSoamLossStateNELossCount_Type = Gauge32
_TnEthSoamLossStateNELossCount_Object = MibTableColumn
tnEthSoamLossStateNELossCount = _TnEthSoamLossStateNELossCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1, 1, 3),
    _TnEthSoamLossStateNELossCount_Type()
)
tnEthSoamLossStateNELossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamLossStateNELossCount.setStatus("current")
_TnEthSoamLossStateFELossCount_Type = Gauge32
_TnEthSoamLossStateFELossCount_Object = MibTableColumn
tnEthSoamLossStateFELossCount = _TnEthSoamLossStateFELossCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1, 1, 4),
    _TnEthSoamLossStateFELossCount_Type()
)
tnEthSoamLossStateFELossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamLossStateFELossCount.setStatus("current")
_TnEthSoamLossStateNELossRatio_Type = Gauge32
_TnEthSoamLossStateNELossRatio_Object = MibTableColumn
tnEthSoamLossStateNELossRatio = _TnEthSoamLossStateNELossRatio_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1, 1, 5),
    _TnEthSoamLossStateNELossRatio_Type()
)
tnEthSoamLossStateNELossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamLossStateNELossRatio.setStatus("current")
_TnEthSoamLossStateFELossRatio_Type = Gauge32
_TnEthSoamLossStateFELossRatio_Object = MibTableColumn
tnEthSoamLossStateFELossRatio = _TnEthSoamLossStateFELossRatio_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1, 1, 6),
    _TnEthSoamLossStateFELossRatio_Type()
)
tnEthSoamLossStateFELossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamLossStateFELossRatio.setStatus("current")
_TnEthSoamLossStateAction_Type = TruthValue
_TnEthSoamLossStateAction_Object = MibTableColumn
tnEthSoamLossStateAction = _TnEthSoamLossStateAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 8, 1, 1, 7),
    _TnEthSoamLossStateAction_Type()
)
tnEthSoamLossStateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamLossStateAction.setStatus("current")
_TnEthSoamTSExtMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamTSExtMgmt = _TnEthSoamTSExtMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 9)
)
_TnEthSoamTSExtTable_Object = MibTable
tnEthSoamTSExtTable = _TnEthSoamTSExtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamTSExtTable.setStatus("current")
_TnEthSoamTSExtEntry_Object = MibTableRow
tnEthSoamTSExtEntry = _TnEthSoamTSExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 9, 1, 1)
)
tnEthSoamTSExtEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamTSExtEntry.setStatus("current")
_TnEthSoamTSSeqNum_Type = TruthValue
_TnEthSoamTSSeqNum_Object = MibTableColumn
tnEthSoamTSSeqNum = _TnEthSoamTSSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 9, 1, 1, 1),
    _TnEthSoamTSSeqNum_Type()
)
tnEthSoamTSSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamTSSeqNum.setStatus("current")
_TnEthSoamTSStateRxRate_Type = Integer32
_TnEthSoamTSStateRxRate_Object = MibTableColumn
tnEthSoamTSStateRxRate = _TnEthSoamTSStateRxRate_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 9, 1, 1, 2),
    _TnEthSoamTSStateRxRate_Type()
)
tnEthSoamTSStateRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamTSStateRxRate.setStatus("current")
_TnEthSoamTSStateAction_Type = TruthValue
_TnEthSoamTSStateAction_Object = MibTableColumn
tnEthSoamTSStateAction = _TnEthSoamTSStateAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 9, 1, 1, 3),
    _TnEthSoamTSStateAction_Type()
)
tnEthSoamTSStateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamTSStateAction.setStatus("current")


class _TnEthSoamTestCfgPattern_Type(TnEthSoamTestPatternType):
    """Custom type tnEthSoamTestCfgPattern based on TnEthSoamTestPatternType"""
    defaultValue = 1


_TnEthSoamTestCfgPattern_Type.__name__ = "TnEthSoamTestPatternType"
_TnEthSoamTestCfgPattern_Object = MibTableColumn
tnEthSoamTestCfgPattern = _TnEthSoamTestCfgPattern_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 9, 1, 1, 4),
    _TnEthSoamTestCfgPattern_Type()
)
tnEthSoamTestCfgPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamTestCfgPattern.setStatus("current")
_TnEthSoamLtmMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamLtmMgmt = _TnEthSoamLtmMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 10)
)
_TnEthSoamLtmTable_Object = MibTable
tnEthSoamLtmTable = _TnEthSoamLtmTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamLtmTable.setStatus("current")
_TnEthSoamLtmEntry_Object = MibTableRow
tnEthSoamLtmEntry = _TnEthSoamLtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 10, 1, 1)
)
tnEthSoamLtmEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamLtmEntry.setStatus("current")
_TnEthSoamltmPriority_Type = IEEE8021PriorityValue
_TnEthSoamltmPriority_Object = MibTableColumn
tnEthSoamltmPriority = _TnEthSoamltmPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 10, 1, 1, 1),
    _TnEthSoamltmPriority_Type()
)
tnEthSoamltmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamltmPriority.setStatus("current")
_TnEthSoamLtrMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamLtrMgmt = _TnEthSoamLtrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 11)
)
_TnEthSoamLtrTable_Object = MibTable
tnEthSoamLtrTable = _TnEthSoamLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamLtrTable.setStatus("current")
_TnEthSoamLtrEntry_Object = MibTableRow
tnEthSoamLtrEntry = _TnEthSoamLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamLtrEntry.setStatus("current")


class _TnEthSoamLtrDirection_Type(Integer32):
    """Custom type tnEthSoamLtrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_TnEthSoamLtrDirection_Type.__name__ = "Integer32"
_TnEthSoamLtrDirection_Object = MibTableColumn
tnEthSoamLtrDirection = _TnEthSoamLtrDirection_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 11, 1, 1, 1),
    _TnEthSoamLtrDirection_Type()
)
tnEthSoamLtrDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamLtrDirection.setStatus("current")
_TnEthSoamAisCfgMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamAisCfgMgmt = _TnEthSoamAisCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 12)
)
_TnEthSoamAisCfgTable_Object = MibTable
tnEthSoamAisCfgTable = _TnEthSoamAisCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 12, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamAisCfgTable.setStatus("current")
_TnEthSoamAisCfgEntry_Object = MibTableRow
tnEthSoamAisCfgEntry = _TnEthSoamAisCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamAisCfgEntry.setStatus("current")
_TnEthSoamAisCfgProtection_Type = TruthValue
_TnEthSoamAisCfgProtection_Object = MibTableColumn
tnEthSoamAisCfgProtection = _TnEthSoamAisCfgProtection_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 12, 1, 1, 1),
    _TnEthSoamAisCfgProtection_Type()
)
tnEthSoamAisCfgProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamAisCfgProtection.setStatus("current")
_TnEthSoamDmCfgMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamDmCfgMgmt = _TnEthSoamDmCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13)
)
_TnEthSoamDmCfgTable_Object = MibTable
tnEthSoamDmCfgTable = _TnEthSoamDmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamDmCfgTable.setStatus("current")
_TnEthSoamDmCfgEntry_Object = MibTableRow
tnEthSoamDmCfgEntry = _TnEthSoamDmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1)
)
tnEthSoamDmCfgEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamDmCfgEntry.setStatus("current")
_TnEthSoamDmCfgEnable_Type = TruthValue
_TnEthSoamDmCfgEnable_Object = MibTableColumn
tnEthSoamDmCfgEnable = _TnEthSoamDmCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 1),
    _TnEthSoamDmCfgEnable_Type()
)
tnEthSoamDmCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgEnable.setStatus("current")
_TnEthSoamDmCfgPriority_Type = IEEE8021PriorityValue
_TnEthSoamDmCfgPriority_Object = MibTableColumn
tnEthSoamDmCfgPriority = _TnEthSoamDmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 2),
    _TnEthSoamDmCfgPriority_Type()
)
tnEthSoamDmCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgPriority.setStatus("current")


class _TnEthSoamDmCfgCast_Type(Integer32):
    """Custom type tnEthSoamDmCfgCast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 0),
          ("multicast", 1))
    )


_TnEthSoamDmCfgCast_Type.__name__ = "Integer32"
_TnEthSoamDmCfgCast_Object = MibTableColumn
tnEthSoamDmCfgCast = _TnEthSoamDmCfgCast_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 3),
    _TnEthSoamDmCfgCast_Type()
)
tnEthSoamDmCfgCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgCast.setStatus("current")
_TnEthSoamDmCfgPeerId_Type = Dot1agCfmMepId
_TnEthSoamDmCfgPeerId_Object = MibTableColumn
tnEthSoamDmCfgPeerId = _TnEthSoamDmCfgPeerId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 4),
    _TnEthSoamDmCfgPeerId_Type()
)
tnEthSoamDmCfgPeerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgPeerId.setStatus("current")


class _TnEthSoamDmCfgWayType_Type(Integer32):
    """Custom type tnEthSoamDmCfgWayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_TnEthSoamDmCfgWayType_Type.__name__ = "Integer32"
_TnEthSoamDmCfgWayType_Object = MibTableColumn
tnEthSoamDmCfgWayType = _TnEthSoamDmCfgWayType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 5),
    _TnEthSoamDmCfgWayType_Type()
)
tnEthSoamDmCfgWayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgWayType.setStatus("current")


class _TnEthSoamDmCfgTxMode_Type(Integer32):
    """Custom type tnEthSoamDmCfgTxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standardize", 1),
          ("proprietary", 2))
    )


_TnEthSoamDmCfgTxMode_Type.__name__ = "Integer32"
_TnEthSoamDmCfgTxMode_Object = MibTableColumn
tnEthSoamDmCfgTxMode = _TnEthSoamDmCfgTxMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 6),
    _TnEthSoamDmCfgTxMode_Type()
)
tnEthSoamDmCfgTxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgTxMode.setStatus("current")


class _TnEthSoamDmCfgCalc_Type(Integer32):
    """Custom type tnEthSoamDmCfgCalc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundtrip", 1),
          ("flow", 2))
    )


_TnEthSoamDmCfgCalc_Type.__name__ = "Integer32"
_TnEthSoamDmCfgCalc_Object = MibTableColumn
tnEthSoamDmCfgCalc = _TnEthSoamDmCfgCalc_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 7),
    _TnEthSoamDmCfgCalc_Type()
)
tnEthSoamDmCfgCalc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgCalc.setStatus("current")


class _TnEthSoamDmCfgGap_Type(Unsigned32):
    """Custom type tnEthSoamDmCfgGap based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_TnEthSoamDmCfgGap_Type.__name__ = "Unsigned32"
_TnEthSoamDmCfgGap_Object = MibTableColumn
tnEthSoamDmCfgGap = _TnEthSoamDmCfgGap_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 8),
    _TnEthSoamDmCfgGap_Type()
)
tnEthSoamDmCfgGap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgGap.setStatus("current")


class _TnEthSoamDmCfgCount_Type(Integer32):
    """Custom type tnEthSoamDmCfgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_TnEthSoamDmCfgCount_Type.__name__ = "Integer32"
_TnEthSoamDmCfgCount_Object = MibTableColumn
tnEthSoamDmCfgCount = _TnEthSoamDmCfgCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 9),
    _TnEthSoamDmCfgCount_Type()
)
tnEthSoamDmCfgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgCount.setStatus("current")


class _TnEthSoamDmCfgUnit_Type(Integer32):
    """Custom type tnEthSoamDmCfgUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 1),
          ("us", 2))
    )


_TnEthSoamDmCfgUnit_Type.__name__ = "Integer32"
_TnEthSoamDmCfgUnit_Object = MibTableColumn
tnEthSoamDmCfgUnit = _TnEthSoamDmCfgUnit_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 10),
    _TnEthSoamDmCfgUnit_Type()
)
tnEthSoamDmCfgUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgUnit.setStatus("current")
_TnEthSoamDmCfgD2forD1_Type = TruthValue
_TnEthSoamDmCfgD2forD1_Object = MibTableColumn
tnEthSoamDmCfgD2forD1 = _TnEthSoamDmCfgD2forD1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 11),
    _TnEthSoamDmCfgD2forD1_Type()
)
tnEthSoamDmCfgD2forD1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgD2forD1.setStatus("current")


class _TnEthSoamDmCfgCOAction_Type(Integer32):
    """Custom type tnEthSoamDmCfgCOAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("reset", 2))
    )


_TnEthSoamDmCfgCOAction_Type.__name__ = "Integer32"
_TnEthSoamDmCfgCOAction_Object = MibTableColumn
tnEthSoamDmCfgCOAction = _TnEthSoamDmCfgCOAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 13, 1, 1, 12),
    _TnEthSoamDmCfgCOAction_Type()
)
tnEthSoamDmCfgCOAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnEthSoamDmCfgCOAction.setStatus("current")
_TnEthSoamDmStateMgmt_ObjectIdentity = ObjectIdentity
tnEthSoamDmStateMgmt = _TnEthSoamDmStateMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14)
)
_TnEthSoamDmStateTable_Object = MibTable
tnEthSoamDmStateTable = _TnEthSoamDmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1)
)
if mibBuilder.loadTexts:
    tnEthSoamDmStateTable.setStatus("current")
_TnEthSoamDmStateEntry_Object = MibTableRow
tnEthSoamDmStateEntry = _TnEthSoamDmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1)
)
tnEthSoamDmStateEntry.setIndexNames(
    (0, "TN-ETHSOAM-MIB", "tnEthSoaminstance"),
)
if mibBuilder.loadTexts:
    tnEthSoamDmStateEntry.setStatus("current")
_TnEthSoamDmStateFNTxCount_Type = Gauge32
_TnEthSoamDmStateFNTxCount_Object = MibTableColumn
tnEthSoamDmStateFNTxCount = _TnEthSoamDmStateFNTxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 1),
    _TnEthSoamDmStateFNTxCount_Type()
)
tnEthSoamDmStateFNTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNTxCount.setStatus("current")
_TnEthSoamDmStateFNRxTimeout_Type = Gauge32
_TnEthSoamDmStateFNRxTimeout_Object = MibTableColumn
tnEthSoamDmStateFNRxTimeout = _TnEthSoamDmStateFNRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 2),
    _TnEthSoamDmStateFNRxTimeout_Type()
)
tnEthSoamDmStateFNRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNRxTimeout.setStatus("current")
_TnEthSoamDmStateFNRxCount_Type = Gauge32
_TnEthSoamDmStateFNRxCount_Object = MibTableColumn
tnEthSoamDmStateFNRxCount = _TnEthSoamDmStateFNRxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 3),
    _TnEthSoamDmStateFNRxCount_Type()
)
tnEthSoamDmStateFNRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNRxCount.setStatus("current")
_TnEthSoamDmStateFNRxError_Type = Gauge32
_TnEthSoamDmStateFNRxError_Object = MibTableColumn
tnEthSoamDmStateFNRxError = _TnEthSoamDmStateFNRxError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 4),
    _TnEthSoamDmStateFNRxError_Type()
)
tnEthSoamDmStateFNRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNRxError.setStatus("current")
_TnEthSoamDmStateFNAvgTotal_Type = Gauge32
_TnEthSoamDmStateFNAvgTotal_Object = MibTableColumn
tnEthSoamDmStateFNAvgTotal = _TnEthSoamDmStateFNAvgTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 5),
    _TnEthSoamDmStateFNAvgTotal_Type()
)
tnEthSoamDmStateFNAvgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNAvgTotal.setStatus("current")
_TnEthSoamDmStateFNAvgLastN_Type = Gauge32
_TnEthSoamDmStateFNAvgLastN_Object = MibTableColumn
tnEthSoamDmStateFNAvgLastN = _TnEthSoamDmStateFNAvgLastN_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 6),
    _TnEthSoamDmStateFNAvgLastN_Type()
)
tnEthSoamDmStateFNAvgLastN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNAvgLastN.setStatus("current")
_TnEthSoamDmStateFNAvgVarTotal_Type = Gauge32
_TnEthSoamDmStateFNAvgVarTotal_Object = MibTableColumn
tnEthSoamDmStateFNAvgVarTotal = _TnEthSoamDmStateFNAvgVarTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 7),
    _TnEthSoamDmStateFNAvgVarTotal_Type()
)
tnEthSoamDmStateFNAvgVarTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNAvgVarTotal.setStatus("current")
_TnEthSoamDmStateFNAvgVarLastN_Type = Gauge32
_TnEthSoamDmStateFNAvgVarLastN_Object = MibTableColumn
tnEthSoamDmStateFNAvgVarLastN = _TnEthSoamDmStateFNAvgVarLastN_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 8),
    _TnEthSoamDmStateFNAvgVarLastN_Type()
)
tnEthSoamDmStateFNAvgVarLastN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNAvgVarLastN.setStatus("current")
_TnEthSoamDmStateFNMinValue_Type = Gauge32
_TnEthSoamDmStateFNMinValue_Object = MibTableColumn
tnEthSoamDmStateFNMinValue = _TnEthSoamDmStateFNMinValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 9),
    _TnEthSoamDmStateFNMinValue_Type()
)
tnEthSoamDmStateFNMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNMinValue.setStatus("current")
_TnEthSoamDmStateFNMaxValue_Type = Gauge32
_TnEthSoamDmStateFNMaxValue_Object = MibTableColumn
tnEthSoamDmStateFNMaxValue = _TnEthSoamDmStateFNMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 10),
    _TnEthSoamDmStateFNMaxValue_Type()
)
tnEthSoamDmStateFNMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNMaxValue.setStatus("current")
_TnEthSoamDmStateFNOverFlow_Type = Gauge32
_TnEthSoamDmStateFNOverFlow_Object = MibTableColumn
tnEthSoamDmStateFNOverFlow = _TnEthSoamDmStateFNOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 11),
    _TnEthSoamDmStateFNOverFlow_Type()
)
tnEthSoamDmStateFNOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateFNOverFlow.setStatus("current")
_TnEthSoamDmStateNFTxCount_Type = Gauge32
_TnEthSoamDmStateNFTxCount_Object = MibTableColumn
tnEthSoamDmStateNFTxCount = _TnEthSoamDmStateNFTxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 12),
    _TnEthSoamDmStateNFTxCount_Type()
)
tnEthSoamDmStateNFTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFTxCount.setStatus("current")
_TnEthSoamDmStateNFRxTimeout_Type = Gauge32
_TnEthSoamDmStateNFRxTimeout_Object = MibTableColumn
tnEthSoamDmStateNFRxTimeout = _TnEthSoamDmStateNFRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 13),
    _TnEthSoamDmStateNFRxTimeout_Type()
)
tnEthSoamDmStateNFRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFRxTimeout.setStatus("current")
_TnEthSoamDmStateNFRxCount_Type = Gauge32
_TnEthSoamDmStateNFRxCount_Object = MibTableColumn
tnEthSoamDmStateNFRxCount = _TnEthSoamDmStateNFRxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 14),
    _TnEthSoamDmStateNFRxCount_Type()
)
tnEthSoamDmStateNFRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFRxCount.setStatus("current")
_TnEthSoamDmStateNFRxError_Type = Gauge32
_TnEthSoamDmStateNFRxError_Object = MibTableColumn
tnEthSoamDmStateNFRxError = _TnEthSoamDmStateNFRxError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 15),
    _TnEthSoamDmStateNFRxError_Type()
)
tnEthSoamDmStateNFRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFRxError.setStatus("current")
_TnEthSoamDmStateNFAvgTotal_Type = Gauge32
_TnEthSoamDmStateNFAvgTotal_Object = MibTableColumn
tnEthSoamDmStateNFAvgTotal = _TnEthSoamDmStateNFAvgTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 16),
    _TnEthSoamDmStateNFAvgTotal_Type()
)
tnEthSoamDmStateNFAvgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFAvgTotal.setStatus("current")
_TnEthSoamDmStateNFAvgLastN_Type = Gauge32
_TnEthSoamDmStateNFAvgLastN_Object = MibTableColumn
tnEthSoamDmStateNFAvgLastN = _TnEthSoamDmStateNFAvgLastN_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 17),
    _TnEthSoamDmStateNFAvgLastN_Type()
)
tnEthSoamDmStateNFAvgLastN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFAvgLastN.setStatus("current")
_TnEthSoamDmStateNFAvgVarTotal_Type = Gauge32
_TnEthSoamDmStateNFAvgVarTotal_Object = MibTableColumn
tnEthSoamDmStateNFAvgVarTotal = _TnEthSoamDmStateNFAvgVarTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 18),
    _TnEthSoamDmStateNFAvgVarTotal_Type()
)
tnEthSoamDmStateNFAvgVarTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFAvgVarTotal.setStatus("current")
_TnEthSoamDmStateNFAvgVarLastN_Type = Gauge32
_TnEthSoamDmStateNFAvgVarLastN_Object = MibTableColumn
tnEthSoamDmStateNFAvgVarLastN = _TnEthSoamDmStateNFAvgVarLastN_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 19),
    _TnEthSoamDmStateNFAvgVarLastN_Type()
)
tnEthSoamDmStateNFAvgVarLastN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFAvgVarLastN.setStatus("current")
_TnEthSoamDmStateNFMinValue_Type = Gauge32
_TnEthSoamDmStateNFMinValue_Object = MibTableColumn
tnEthSoamDmStateNFMinValue = _TnEthSoamDmStateNFMinValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 20),
    _TnEthSoamDmStateNFMinValue_Type()
)
tnEthSoamDmStateNFMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFMinValue.setStatus("current")
_TnEthSoamDmStateNFMaxValue_Type = Gauge32
_TnEthSoamDmStateNFMaxValue_Object = MibTableColumn
tnEthSoamDmStateNFMaxValue = _TnEthSoamDmStateNFMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 21),
    _TnEthSoamDmStateNFMaxValue_Type()
)
tnEthSoamDmStateNFMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFMaxValue.setStatus("current")
_TnEthSoamDmStateNFOverFlow_Type = Gauge32
_TnEthSoamDmStateNFOverFlow_Object = MibTableColumn
tnEthSoamDmStateNFOverFlow = _TnEthSoamDmStateNFOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 22),
    _TnEthSoamDmStateNFOverFlow_Type()
)
tnEthSoamDmStateNFOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateNFOverFlow.setStatus("current")
_TnEthSoamDmStateTwoWayTxCount_Type = Gauge32
_TnEthSoamDmStateTwoWayTxCount_Object = MibTableColumn
tnEthSoamDmStateTwoWayTxCount = _TnEthSoamDmStateTwoWayTxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 23),
    _TnEthSoamDmStateTwoWayTxCount_Type()
)
tnEthSoamDmStateTwoWayTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayTxCount.setStatus("current")
_TnEthSoamDmStateTwoWayRxTimeout_Type = Gauge32
_TnEthSoamDmStateTwoWayRxTimeout_Object = MibTableColumn
tnEthSoamDmStateTwoWayRxTimeout = _TnEthSoamDmStateTwoWayRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 24),
    _TnEthSoamDmStateTwoWayRxTimeout_Type()
)
tnEthSoamDmStateTwoWayRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayRxTimeout.setStatus("current")
_TnEthSoamDmStateTwoWayRxCount_Type = Gauge32
_TnEthSoamDmStateTwoWayRxCount_Object = MibTableColumn
tnEthSoamDmStateTwoWayRxCount = _TnEthSoamDmStateTwoWayRxCount_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 25),
    _TnEthSoamDmStateTwoWayRxCount_Type()
)
tnEthSoamDmStateTwoWayRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayRxCount.setStatus("current")
_TnEthSoamDmStateTwoWayRxError_Type = Gauge32
_TnEthSoamDmStateTwoWayRxError_Object = MibTableColumn
tnEthSoamDmStateTwoWayRxError = _TnEthSoamDmStateTwoWayRxError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 26),
    _TnEthSoamDmStateTwoWayRxError_Type()
)
tnEthSoamDmStateTwoWayRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayRxError.setStatus("current")
_TnEthSoamDmStateTwoWayAvgTotal_Type = Gauge32
_TnEthSoamDmStateTwoWayAvgTotal_Object = MibTableColumn
tnEthSoamDmStateTwoWayAvgTotal = _TnEthSoamDmStateTwoWayAvgTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 27),
    _TnEthSoamDmStateTwoWayAvgTotal_Type()
)
tnEthSoamDmStateTwoWayAvgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayAvgTotal.setStatus("current")
_TnEthSoamDmStateTwoWayAvgLastN_Type = Gauge32
_TnEthSoamDmStateTwoWayAvgLastN_Object = MibTableColumn
tnEthSoamDmStateTwoWayAvgLastN = _TnEthSoamDmStateTwoWayAvgLastN_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 28),
    _TnEthSoamDmStateTwoWayAvgLastN_Type()
)
tnEthSoamDmStateTwoWayAvgLastN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayAvgLastN.setStatus("current")
_TnEthSoamDmStateTwoWayAvgVarTotal_Type = Gauge32
_TnEthSoamDmStateTwoWayAvgVarTotal_Object = MibTableColumn
tnEthSoamDmStateTwoWayAvgVarTotal = _TnEthSoamDmStateTwoWayAvgVarTotal_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 29),
    _TnEthSoamDmStateTwoWayAvgVarTotal_Type()
)
tnEthSoamDmStateTwoWayAvgVarTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayAvgVarTotal.setStatus("current")
_TnEthSoamDmStateTwoWayAvgVarLastN_Type = Gauge32
_TnEthSoamDmStateTwoWayAvgVarLastN_Object = MibTableColumn
tnEthSoamDmStateTwoWayAvgVarLastN = _TnEthSoamDmStateTwoWayAvgVarLastN_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 30),
    _TnEthSoamDmStateTwoWayAvgVarLastN_Type()
)
tnEthSoamDmStateTwoWayAvgVarLastN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayAvgVarLastN.setStatus("current")
_TnEthSoamDmStateTwoWayMinValue_Type = Gauge32
_TnEthSoamDmStateTwoWayMinValue_Object = MibTableColumn
tnEthSoamDmStateTwoWayMinValue = _TnEthSoamDmStateTwoWayMinValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 31),
    _TnEthSoamDmStateTwoWayMinValue_Type()
)
tnEthSoamDmStateTwoWayMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayMinValue.setStatus("current")
_TnEthSoamDmStateTwoWayMaxValue_Type = Gauge32
_TnEthSoamDmStateTwoWayMaxValue_Object = MibTableColumn
tnEthSoamDmStateTwoWayMaxValue = _TnEthSoamDmStateTwoWayMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 32),
    _TnEthSoamDmStateTwoWayMaxValue_Type()
)
tnEthSoamDmStateTwoWayMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayMaxValue.setStatus("current")
_TnEthSoamDmStateTwoWayOverFlow_Type = Gauge32
_TnEthSoamDmStateTwoWayOverFlow_Object = MibTableColumn
tnEthSoamDmStateTwoWayOverFlow = _TnEthSoamDmStateTwoWayOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 33),
    _TnEthSoamDmStateTwoWayOverFlow_Type()
)
tnEthSoamDmStateTwoWayOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSoamDmStateTwoWayOverFlow.setStatus("current")
_TnEthSoamDmStateAction_Type = TruthValue
_TnEthSoamDmStateAction_Object = MibTableColumn
tnEthSoamDmStateAction = _TnEthSoamDmStateAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 1, 14, 1, 1, 34),
    _TnEthSoamDmStateAction_Type()
)
tnEthSoamDmStateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSoamDmStateAction.setStatus("current")
_TnEthSoamMIBConformance_ObjectIdentity = ObjectIdentity
tnEthSoamMIBConformance = _TnEthSoamMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 2)
)
dot1agCfmLtrEntry.registerAugmentions(
    ("TN-ETHSOAM-MIB",
     "tnEthSoamLtrEntry")
)
tnEthSoamLtrEntry.setIndexNames(*dot1agCfmLtrEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TN-ETHSOAM-MIB",
     "tnEthSoamAisCfgEntry")
)
tnEthSoamAisCfgEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups


# Notification objects

tnEthSoamFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 0, 1)
)
tnEthSoamFaultAlarm.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
        ("TN-ETHSOAM-MIB", "tnEthSoamStatusCCMLevel"),
        ("TN-ETHSOAM-MIB", "tnEthSoamStatusCCMMeg"),
        ("TN-ETHSOAM-MIB", "tnEthSoamStatusCCMMep"),
        ("TN-ETHSOAM-MIB", "tnEthSoamStatusAIS"),
        ("TN-ETHSOAM-MIB", "tnEthSoamStatusCLK"),
        ("TN-ETHSOAM-MIB", "tnEthSoamStatusSSF"))
)
if mibBuilder.loadTexts:
    tnEthSoamFaultAlarm.setStatus(
        "current"
    )

tnEthSoamPeerFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 105, 0, 2)
)
tnEthSoamPeerFaultAlarm.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
        ("TN-ETHSOAM-MIB", "tnEthSoamPeerStatuscLOC"),
        ("TN-ETHSOAM-MIB", "tnEthSoamPeerStatuscRDI"),
        ("TN-ETHSOAM-MIB", "tnEthSoamPeerStatuscPeriod"),
        ("TN-ETHSOAM-MIB", "tnEthSoamPeerStatuscPriority"))
)
if mibBuilder.loadTexts:
    tnEthSoamPeerFaultAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-ETHSOAM-MIB",
    **{"Dot1agCfmMepId": Dot1agCfmMepId,
       "Dot1agCfmMpDirection": Dot1agCfmMpDirection,
       "Dot1agCfmMaintDomainName": Dot1agCfmMaintDomainName,
       "Dot1agCfmMaintAssocName": Dot1agCfmMaintAssocName,
       "Dot1agCfmMDLevel": Dot1agCfmMDLevel,
       "TnEthSoamType": TnEthSoamType,
       "TnEthSoamTestPatternType": TnEthSoamTestPatternType,
       "tnEthSoamMIB": tnEthSoamMIB,
       "tnEthSoamMIBNotifications": tnEthSoamMIBNotifications,
       "tnEthSoamFaultAlarm": tnEthSoamFaultAlarm,
       "tnEthSoamPeerFaultAlarm": tnEthSoamPeerFaultAlarm,
       "tnEthSoamMIBObjects": tnEthSoamMIBObjects,
       "tnEthSoamMPMgmt": tnEthSoamMPMgmt,
       "tnEthSoamMPTable": tnEthSoamMPTable,
       "tnEthSoamMPEntry": tnEthSoamMPEntry,
       "tnEthSoaminstance": tnEthSoaminstance,
       "tnEthSoamDomaintype": tnEthSoamDomaintype,
       "tnEthSoamMode": tnEthSoamMode,
       "tnEthSoamdirection": tnEthSoamdirection,
       "tnEthSoamresidencePort": tnEthSoamresidencePort,
       "tnEthSoamlevel": tnEthSoamlevel,
       "tnEthSoamFlowInstance": tnEthSoamFlowInstance,
       "tnEthSoamTaggedVID": tnEthSoamTaggedVID,
       "tnEthSoamAlarm": tnEthSoamAlarm,
       "tnEthSoamStatus": tnEthSoamStatus,
       "tnEthSoamPeerCfgMgmt": tnEthSoamPeerCfgMgmt,
       "tnEthSoamPeerCfgTable": tnEthSoamPeerCfgTable,
       "tnEthSoamPeerCfgEntry": tnEthSoamPeerCfgEntry,
       "tnEthSoamPeerCfgMepId": tnEthSoamPeerCfgMepId,
       "tnEthSoamPeerCfgUnicastMac": tnEthSoamPeerCfgUnicastMac,
       "tnEthSoamPeerCfgRowState": tnEthSoamPeerCfgRowState,
       "tnEthSoamPeerStatusMgmt": tnEthSoamPeerStatusMgmt,
       "tnEthSoamPeerStatusTable": tnEthSoamPeerStatusTable,
       "tnEthSoamPeerStatusEntry": tnEthSoamPeerStatusEntry,
       "tnEthSoamPeerStatusMepId": tnEthSoamPeerStatusMepId,
       "tnEthSoamPeerStatuscLOC": tnEthSoamPeerStatuscLOC,
       "tnEthSoamPeerStatuscRDI": tnEthSoamPeerStatuscRDI,
       "tnEthSoamPeerStatuscPeriod": tnEthSoamPeerStatuscPeriod,
       "tnEthSoamPeerStatuscPriority": tnEthSoamPeerStatuscPriority,
       "tnEthSoamAPSCfgMgmt": tnEthSoamAPSCfgMgmt,
       "tnEthSoamAPSCfgTable": tnEthSoamAPSCfgTable,
       "tnEthSoamAPSCfgEntry": tnEthSoamAPSCfgEntry,
       "tnEthSoamAPSCfgEnable": tnEthSoamAPSCfgEnable,
       "tnEthSoamAPSCfgPriority": tnEthSoamAPSCfgPriority,
       "tnEthSoamAPSCfgCast": tnEthSoamAPSCfgCast,
       "tnEthSoamAPSCfgType": tnEthSoamAPSCfgType,
       "tnEthSoamAPSCfgLastOctet": tnEthSoamAPSCfgLastOctet,
       "tnEthSoamClientCfgMgmt": tnEthSoamClientCfgMgmt,
       "tnEthSoamClientCfgTable": tnEthSoamClientCfgTable,
       "tnEthSoamClientCfgEntry": tnEthSoamClientCfgEntry,
       "tnEthSoamClientCfgDomain": tnEthSoamClientCfgDomain,
       "tnEthSoamClientCfgLevel": tnEthSoamClientCfgLevel,
       "tnEthSoamClientCfgFlow1": tnEthSoamClientCfgFlow1,
       "tnEthSoamClientCfgFlow2": tnEthSoamClientCfgFlow2,
       "tnEthSoamClientCfgFlow3": tnEthSoamClientCfgFlow3,
       "tnEthSoamClientCfgFlow4": tnEthSoamClientCfgFlow4,
       "tnEthSoamClientCfgFlow5": tnEthSoamClientCfgFlow5,
       "tnEthSoamClientCfgFlow6": tnEthSoamClientCfgFlow6,
       "tnEthSoamClientCfgFlow7": tnEthSoamClientCfgFlow7,
       "tnEthSoamClientCfgFlow8": tnEthSoamClientCfgFlow8,
       "tnEthSoamClientCfgFlow9": tnEthSoamClientCfgFlow9,
       "tnEthSoamClientCfgFlow10": tnEthSoamClientCfgFlow10,
       "tnEthSoamLocalCfgMgmt": tnEthSoamLocalCfgMgmt,
       "tnEthSoamLocalCfgTable": tnEthSoamLocalCfgTable,
       "tnEthSoamLocalCfgEntry": tnEthSoamLocalCfgEntry,
       "tnEthSoamFormat": tnEthSoamFormat,
       "tnEthSoamDomainName": tnEthSoamDomainName,
       "tnEthSoamMegOrMaName": tnEthSoamMegOrMaName,
       "tnEthSoamMepID": tnEthSoamMepID,
       "tnEthSoamCcmInterval": tnEthSoamCcmInterval,
       "tnEthSoamEVCQos": tnEthSoamEVCQos,
       "tnEthSoamEVCPolicyID": tnEthSoamEVCPolicyID,
       "tnEthSoamVOE": tnEthSoamVOE,
       "tnEthSoamStatusMgmt": tnEthSoamStatusMgmt,
       "tnEthSoamStatusTable": tnEthSoamStatusTable,
       "tnEthSoamStatusEntry": tnEthSoamStatusEntry,
       "tnEthSoamStatusCCMLevel": tnEthSoamStatusCCMLevel,
       "tnEthSoamStatusCCMMeg": tnEthSoamStatusCCMMeg,
       "tnEthSoamStatusCCMMep": tnEthSoamStatusCCMMep,
       "tnEthSoamStatusAIS": tnEthSoamStatusAIS,
       "tnEthSoamStatusCLK": tnEthSoamStatusCLK,
       "tnEthSoamStatusSSF": tnEthSoamStatusSSF,
       "tnEthSoamStatusBLK": tnEthSoamStatusBLK,
       "tnEthSoamStatusTSF": tnEthSoamStatusTSF,
       "tnEthSoamLossStateMgmt": tnEthSoamLossStateMgmt,
       "tnEthSoamLossStateTable": tnEthSoamLossStateTable,
       "tnEthSoamLossStateEntry": tnEthSoamLossStateEntry,
       "tnEthSoamLossStateTxCount": tnEthSoamLossStateTxCount,
       "tnEthSoamLossStateRxCount": tnEthSoamLossStateRxCount,
       "tnEthSoamLossStateNELossCount": tnEthSoamLossStateNELossCount,
       "tnEthSoamLossStateFELossCount": tnEthSoamLossStateFELossCount,
       "tnEthSoamLossStateNELossRatio": tnEthSoamLossStateNELossRatio,
       "tnEthSoamLossStateFELossRatio": tnEthSoamLossStateFELossRatio,
       "tnEthSoamLossStateAction": tnEthSoamLossStateAction,
       "tnEthSoamTSExtMgmt": tnEthSoamTSExtMgmt,
       "tnEthSoamTSExtTable": tnEthSoamTSExtTable,
       "tnEthSoamTSExtEntry": tnEthSoamTSExtEntry,
       "tnEthSoamTSSeqNum": tnEthSoamTSSeqNum,
       "tnEthSoamTSStateRxRate": tnEthSoamTSStateRxRate,
       "tnEthSoamTSStateAction": tnEthSoamTSStateAction,
       "tnEthSoamTestCfgPattern": tnEthSoamTestCfgPattern,
       "tnEthSoamLtmMgmt": tnEthSoamLtmMgmt,
       "tnEthSoamLtmTable": tnEthSoamLtmTable,
       "tnEthSoamLtmEntry": tnEthSoamLtmEntry,
       "tnEthSoamltmPriority": tnEthSoamltmPriority,
       "tnEthSoamLtrMgmt": tnEthSoamLtrMgmt,
       "tnEthSoamLtrTable": tnEthSoamLtrTable,
       "tnEthSoamLtrEntry": tnEthSoamLtrEntry,
       "tnEthSoamLtrDirection": tnEthSoamLtrDirection,
       "tnEthSoamAisCfgMgmt": tnEthSoamAisCfgMgmt,
       "tnEthSoamAisCfgTable": tnEthSoamAisCfgTable,
       "tnEthSoamAisCfgEntry": tnEthSoamAisCfgEntry,
       "tnEthSoamAisCfgProtection": tnEthSoamAisCfgProtection,
       "tnEthSoamDmCfgMgmt": tnEthSoamDmCfgMgmt,
       "tnEthSoamDmCfgTable": tnEthSoamDmCfgTable,
       "tnEthSoamDmCfgEntry": tnEthSoamDmCfgEntry,
       "tnEthSoamDmCfgEnable": tnEthSoamDmCfgEnable,
       "tnEthSoamDmCfgPriority": tnEthSoamDmCfgPriority,
       "tnEthSoamDmCfgCast": tnEthSoamDmCfgCast,
       "tnEthSoamDmCfgPeerId": tnEthSoamDmCfgPeerId,
       "tnEthSoamDmCfgWayType": tnEthSoamDmCfgWayType,
       "tnEthSoamDmCfgTxMode": tnEthSoamDmCfgTxMode,
       "tnEthSoamDmCfgCalc": tnEthSoamDmCfgCalc,
       "tnEthSoamDmCfgGap": tnEthSoamDmCfgGap,
       "tnEthSoamDmCfgCount": tnEthSoamDmCfgCount,
       "tnEthSoamDmCfgUnit": tnEthSoamDmCfgUnit,
       "tnEthSoamDmCfgD2forD1": tnEthSoamDmCfgD2forD1,
       "tnEthSoamDmCfgCOAction": tnEthSoamDmCfgCOAction,
       "tnEthSoamDmStateMgmt": tnEthSoamDmStateMgmt,
       "tnEthSoamDmStateTable": tnEthSoamDmStateTable,
       "tnEthSoamDmStateEntry": tnEthSoamDmStateEntry,
       "tnEthSoamDmStateFNTxCount": tnEthSoamDmStateFNTxCount,
       "tnEthSoamDmStateFNRxTimeout": tnEthSoamDmStateFNRxTimeout,
       "tnEthSoamDmStateFNRxCount": tnEthSoamDmStateFNRxCount,
       "tnEthSoamDmStateFNRxError": tnEthSoamDmStateFNRxError,
       "tnEthSoamDmStateFNAvgTotal": tnEthSoamDmStateFNAvgTotal,
       "tnEthSoamDmStateFNAvgLastN": tnEthSoamDmStateFNAvgLastN,
       "tnEthSoamDmStateFNAvgVarTotal": tnEthSoamDmStateFNAvgVarTotal,
       "tnEthSoamDmStateFNAvgVarLastN": tnEthSoamDmStateFNAvgVarLastN,
       "tnEthSoamDmStateFNMinValue": tnEthSoamDmStateFNMinValue,
       "tnEthSoamDmStateFNMaxValue": tnEthSoamDmStateFNMaxValue,
       "tnEthSoamDmStateFNOverFlow": tnEthSoamDmStateFNOverFlow,
       "tnEthSoamDmStateNFTxCount": tnEthSoamDmStateNFTxCount,
       "tnEthSoamDmStateNFRxTimeout": tnEthSoamDmStateNFRxTimeout,
       "tnEthSoamDmStateNFRxCount": tnEthSoamDmStateNFRxCount,
       "tnEthSoamDmStateNFRxError": tnEthSoamDmStateNFRxError,
       "tnEthSoamDmStateNFAvgTotal": tnEthSoamDmStateNFAvgTotal,
       "tnEthSoamDmStateNFAvgLastN": tnEthSoamDmStateNFAvgLastN,
       "tnEthSoamDmStateNFAvgVarTotal": tnEthSoamDmStateNFAvgVarTotal,
       "tnEthSoamDmStateNFAvgVarLastN": tnEthSoamDmStateNFAvgVarLastN,
       "tnEthSoamDmStateNFMinValue": tnEthSoamDmStateNFMinValue,
       "tnEthSoamDmStateNFMaxValue": tnEthSoamDmStateNFMaxValue,
       "tnEthSoamDmStateNFOverFlow": tnEthSoamDmStateNFOverFlow,
       "tnEthSoamDmStateTwoWayTxCount": tnEthSoamDmStateTwoWayTxCount,
       "tnEthSoamDmStateTwoWayRxTimeout": tnEthSoamDmStateTwoWayRxTimeout,
       "tnEthSoamDmStateTwoWayRxCount": tnEthSoamDmStateTwoWayRxCount,
       "tnEthSoamDmStateTwoWayRxError": tnEthSoamDmStateTwoWayRxError,
       "tnEthSoamDmStateTwoWayAvgTotal": tnEthSoamDmStateTwoWayAvgTotal,
       "tnEthSoamDmStateTwoWayAvgLastN": tnEthSoamDmStateTwoWayAvgLastN,
       "tnEthSoamDmStateTwoWayAvgVarTotal": tnEthSoamDmStateTwoWayAvgVarTotal,
       "tnEthSoamDmStateTwoWayAvgVarLastN": tnEthSoamDmStateTwoWayAvgVarLastN,
       "tnEthSoamDmStateTwoWayMinValue": tnEthSoamDmStateTwoWayMinValue,
       "tnEthSoamDmStateTwoWayMaxValue": tnEthSoamDmStateTwoWayMaxValue,
       "tnEthSoamDmStateTwoWayOverFlow": tnEthSoamDmStateTwoWayOverFlow,
       "tnEthSoamDmStateAction": tnEthSoamDmStateAction,
       "tnEthSoamMIBConformance": tnEthSoamMIBConformance}
)
