# SNMP MIB module (F3-AMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-AMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:38 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "VlanId")

(IpManagementTunnelEncapsulationType,
 IpManagementTunnelType,
 IpSourceAddrType) = mibBuilder.importSymbols(
    "CM-IP-MIB",
    "IpManagementTunnelEncapsulationType",
    "IpManagementTunnelType",
    "IpSourceAddrType")

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
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3AMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24)
)
if mibBuilder.loadTexts:
    f3AMPMIB.setRevisions(
        ("2012-09-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AMPRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )



class AMPStatus(TextualConvention, Integer32):
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
        *(("notAvailable", 1),
          ("disabled", 2),
          ("associatingActive", 3),
          ("associatingPassive", 4),
          ("associated", 5),
          ("noPeer", 6))
    )



class AMPConfigStatus(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("provision", 2),
          ("noPeer", 3),
          ("request", 4),
          ("configSuccess", 5),
          ("configFail", 6),
          ("timeout", 7))
    )



class AMPProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("efmOam", 1)
    )



class AMPConfigAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("clearStats", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3AmpConfigObjects_ObjectIdentity = ObjectIdentity
f3AmpConfigObjects = _F3AmpConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1)
)
_F3AmpConfigTable_Object = MibTable
f3AmpConfigTable = _F3AmpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1)
)
if mibBuilder.loadTexts:
    f3AmpConfigTable.setStatus("current")
_F3AmpConfigEntry_Object = MibTableRow
f3AmpConfigEntry = _F3AmpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1)
)
f3AmpConfigEntry.setIndexNames(
    (0, "F3-AMP-MIB", "f3AmpConfigIndex"),
)
if mibBuilder.loadTexts:
    f3AmpConfigEntry.setStatus("current")


class _F3AmpConfigIndex_Type(Integer32):
    """Custom type f3AmpConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_F3AmpConfigIndex_Type.__name__ = "Integer32"
_F3AmpConfigIndex_Object = MibTableColumn
f3AmpConfigIndex = _F3AmpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 1),
    _F3AmpConfigIndex_Type()
)
f3AmpConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AmpConfigIndex.setStatus("current")
_F3AmpConfigRole_Type = AMPRole
_F3AmpConfigRole_Object = MibTableColumn
f3AmpConfigRole = _F3AmpConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 2),
    _F3AmpConfigRole_Type()
)
f3AmpConfigRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRole.setStatus("current")
_F3AmpConfigProtocol_Type = AMPProtocol
_F3AmpConfigProtocol_Object = MibTableColumn
f3AmpConfigProtocol = _F3AmpConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 3),
    _F3AmpConfigProtocol_Type()
)
f3AmpConfigProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigProtocol.setStatus("current")
_F3AmpConfigEnabled_Type = TruthValue
_F3AmpConfigEnabled_Object = MibTableColumn
f3AmpConfigEnabled = _F3AmpConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 4),
    _F3AmpConfigEnabled_Type()
)
f3AmpConfigEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigEnabled.setStatus("current")
_F3AmpConfigPort_Type = VariablePointer
_F3AmpConfigPort_Object = MibTableColumn
f3AmpConfigPort = _F3AmpConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 5),
    _F3AmpConfigPort_Type()
)
f3AmpConfigPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigPort.setStatus("current")
_F3AmpConfigStatus_Type = AMPStatus
_F3AmpConfigStatus_Object = MibTableColumn
f3AmpConfigStatus = _F3AmpConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 6),
    _F3AmpConfigStatus_Type()
)
f3AmpConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpConfigStatus.setStatus("current")
_F3AmpConfigRemSysName_Type = DisplayString
_F3AmpConfigRemSysName_Object = MibTableColumn
f3AmpConfigRemSysName = _F3AmpConfigRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 7),
    _F3AmpConfigRemSysName_Type()
)
f3AmpConfigRemSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemSysName.setStatus("current")
_F3AmpConfigRemSysIpAddr_Type = IpAddress
_F3AmpConfigRemSysIpAddr_Object = MibTableColumn
f3AmpConfigRemSysIpAddr = _F3AmpConfigRemSysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 8),
    _F3AmpConfigRemSysIpAddr_Type()
)
f3AmpConfigRemSysIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemSysIpAddr.setStatus("current")
_F3AmpConfigRemSysIpMask_Type = IpAddress
_F3AmpConfigRemSysIpMask_Object = MibTableColumn
f3AmpConfigRemSysIpMask = _F3AmpConfigRemSysIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 9),
    _F3AmpConfigRemSysIpMask_Type()
)
f3AmpConfigRemSysIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemSysIpMask.setStatus("current")
_F3AmpConfigRemSysDefGateway_Type = IpAddress
_F3AmpConfigRemSysDefGateway_Object = MibTableColumn
f3AmpConfigRemSysDefGateway = _F3AmpConfigRemSysDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 10),
    _F3AmpConfigRemSysDefGateway_Type()
)
f3AmpConfigRemSysDefGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemSysDefGateway.setStatus("current")
_F3AmpConfigRemSysSNMPV1IfName_Type = DisplayString
_F3AmpConfigRemSysSNMPV1IfName_Object = MibTableColumn
f3AmpConfigRemSysSNMPV1IfName = _F3AmpConfigRemSysSNMPV1IfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 11),
    _F3AmpConfigRemSysSNMPV1IfName_Type()
)
f3AmpConfigRemSysSNMPV1IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpConfigRemSysSNMPV1IfName.setStatus("current")
_F3AmpConfigRemSysSrcIpAddrType_Type = IpSourceAddrType
_F3AmpConfigRemSysSrcIpAddrType_Object = MibTableColumn
f3AmpConfigRemSysSrcIpAddrType = _F3AmpConfigRemSysSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 12),
    _F3AmpConfigRemSysSrcIpAddrType_Type()
)
f3AmpConfigRemSysSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpConfigRemSysSrcIpAddrType.setStatus("current")
_F3AmpConfigRemSysSrcIpAddrIfName_Type = DisplayString
_F3AmpConfigRemSysSrcIpAddrIfName_Object = MibTableColumn
f3AmpConfigRemSysSrcIpAddrIfName = _F3AmpConfigRemSysSrcIpAddrIfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 13),
    _F3AmpConfigRemSysSrcIpAddrIfName_Type()
)
f3AmpConfigRemSysSrcIpAddrIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpConfigRemSysSrcIpAddrIfName.setStatus("current")


class _F3AmpConfigRemTunnelIndex_Type(Integer32):
    """Custom type f3AmpConfigRemTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_F3AmpConfigRemTunnelIndex_Type.__name__ = "Integer32"
_F3AmpConfigRemTunnelIndex_Object = MibTableColumn
f3AmpConfigRemTunnelIndex = _F3AmpConfigRemTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 14),
    _F3AmpConfigRemTunnelIndex_Type()
)
f3AmpConfigRemTunnelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelIndex.setStatus("current")
_F3AmpConfigRemTunnelName_Type = DisplayString
_F3AmpConfigRemTunnelName_Object = MibTableColumn
f3AmpConfigRemTunnelName = _F3AmpConfigRemTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 15),
    _F3AmpConfigRemTunnelName_Type()
)
f3AmpConfigRemTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelName.setStatus("current")
_F3AmpConfigRemTunnelType_Type = IpManagementTunnelType
_F3AmpConfigRemTunnelType_Object = MibTableColumn
f3AmpConfigRemTunnelType = _F3AmpConfigRemTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 16),
    _F3AmpConfigRemTunnelType_Type()
)
f3AmpConfigRemTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelType.setStatus("current")
_F3AmpConfigRemTunnelIpAddr_Type = IpAddress
_F3AmpConfigRemTunnelIpAddr_Object = MibTableColumn
f3AmpConfigRemTunnelIpAddr = _F3AmpConfigRemTunnelIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 17),
    _F3AmpConfigRemTunnelIpAddr_Type()
)
f3AmpConfigRemTunnelIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelIpAddr.setStatus("current")
_F3AmpConfigRemTunnelIpMask_Type = IpAddress
_F3AmpConfigRemTunnelIpMask_Object = MibTableColumn
f3AmpConfigRemTunnelIpMask = _F3AmpConfigRemTunnelIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 18),
    _F3AmpConfigRemTunnelIpMask_Type()
)
f3AmpConfigRemTunnelIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelIpMask.setStatus("current")
_F3AmpConfigRemTunnelVlanId_Type = VlanId
_F3AmpConfigRemTunnelVlanId_Object = MibTableColumn
f3AmpConfigRemTunnelVlanId = _F3AmpConfigRemTunnelVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 19),
    _F3AmpConfigRemTunnelVlanId_Type()
)
f3AmpConfigRemTunnelVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelVlanId.setStatus("current")
_F3AmpConfigRemTunnelSVlanId_Type = VlanId
_F3AmpConfigRemTunnelSVlanId_Object = MibTableColumn
f3AmpConfigRemTunnelSVlanId = _F3AmpConfigRemTunnelSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 20),
    _F3AmpConfigRemTunnelSVlanId_Type()
)
f3AmpConfigRemTunnelSVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelSVlanId.setStatus("current")
_F3AmpConfigRemTunnelSVlanIdEnabled_Type = TruthValue
_F3AmpConfigRemTunnelSVlanIdEnabled_Object = MibTableColumn
f3AmpConfigRemTunnelSVlanIdEnabled = _F3AmpConfigRemTunnelSVlanIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 21),
    _F3AmpConfigRemTunnelSVlanIdEnabled_Type()
)
f3AmpConfigRemTunnelSVlanIdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelSVlanIdEnabled.setStatus("current")
_F3AmpConfigRemTunnelRip2PktsEnabled_Type = TruthValue
_F3AmpConfigRemTunnelRip2PktsEnabled_Object = MibTableColumn
f3AmpConfigRemTunnelRip2PktsEnabled = _F3AmpConfigRemTunnelRip2PktsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 22),
    _F3AmpConfigRemTunnelRip2PktsEnabled_Type()
)
f3AmpConfigRemTunnelRip2PktsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelRip2PktsEnabled.setStatus("current")


class _F3AmpConfigRemTunnelCOS_Type(Integer32):
    """Custom type f3AmpConfigRemTunnelCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_F3AmpConfigRemTunnelCOS_Type.__name__ = "Integer32"
_F3AmpConfigRemTunnelCOS_Object = MibTableColumn
f3AmpConfigRemTunnelCOS = _F3AmpConfigRemTunnelCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 23),
    _F3AmpConfigRemTunnelCOS_Type()
)
f3AmpConfigRemTunnelCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelCOS.setStatus("current")
_F3AmpConfigRemTunnelCIR_Type = Unsigned32
_F3AmpConfigRemTunnelCIR_Object = MibTableColumn
f3AmpConfigRemTunnelCIR = _F3AmpConfigRemTunnelCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 24),
    _F3AmpConfigRemTunnelCIR_Type()
)
f3AmpConfigRemTunnelCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelCIR.setStatus("current")
_F3AmpConfigRemTunnelEIR_Type = Unsigned32
_F3AmpConfigRemTunnelEIR_Object = MibTableColumn
f3AmpConfigRemTunnelEIR = _F3AmpConfigRemTunnelEIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 25),
    _F3AmpConfigRemTunnelEIR_Type()
)
f3AmpConfigRemTunnelEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelEIR.setStatus("current")
_F3AmpConfigRemTunnelBufferSize_Type = Unsigned32
_F3AmpConfigRemTunnelBufferSize_Object = MibTableColumn
f3AmpConfigRemTunnelBufferSize = _F3AmpConfigRemTunnelBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 26),
    _F3AmpConfigRemTunnelBufferSize_Type()
)
f3AmpConfigRemTunnelBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelBufferSize.setStatus("current")
_F3AmpConfigRemTunnelEncapType_Type = IpManagementTunnelEncapsulationType
_F3AmpConfigRemTunnelEncapType_Object = MibTableColumn
f3AmpConfigRemTunnelEncapType = _F3AmpConfigRemTunnelEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 27),
    _F3AmpConfigRemTunnelEncapType_Type()
)
f3AmpConfigRemTunnelEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelEncapType.setStatus("current")
_F3AmpConfigRemTunnelMtu_Type = Integer32
_F3AmpConfigRemTunnelMtu_Object = MibTableColumn
f3AmpConfigRemTunnelMtu = _F3AmpConfigRemTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 28),
    _F3AmpConfigRemTunnelMtu_Type()
)
f3AmpConfigRemTunnelMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRemTunnelMtu.setStatus("current")
_F3AmpConfigAction_Type = AMPConfigAction
_F3AmpConfigAction_Object = MibTableColumn
f3AmpConfigAction = _F3AmpConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 29),
    _F3AmpConfigAction_Type()
)
f3AmpConfigAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigAction.setStatus("current")
_F3AmpConfigStorageType_Type = StorageType
_F3AmpConfigStorageType_Object = MibTableColumn
f3AmpConfigStorageType = _F3AmpConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 30),
    _F3AmpConfigStorageType_Type()
)
f3AmpConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigStorageType.setStatus("current")
_F3AmpConfigRowStatus_Type = RowStatus
_F3AmpConfigRowStatus_Object = MibTableColumn
f3AmpConfigRowStatus = _F3AmpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 1, 1, 1, 31),
    _F3AmpConfigRowStatus_Type()
)
f3AmpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3AmpConfigRowStatus.setStatus("current")
_F3AmpStatsObjects_ObjectIdentity = ObjectIdentity
f3AmpStatsObjects = _F3AmpStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2)
)
_F3AmpStatsTable_Object = MibTable
f3AmpStatsTable = _F3AmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1)
)
if mibBuilder.loadTexts:
    f3AmpStatsTable.setStatus("current")
_F3AmpStatsEntry_Object = MibTableRow
f3AmpStatsEntry = _F3AmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1)
)
f3AmpStatsEntry.setIndexNames(
    (0, "F3-AMP-MIB", "f3AmpConfigIndex"),
)
if mibBuilder.loadTexts:
    f3AmpStatsEntry.setStatus("current")
_F3AmpStatsProvDataTx_Type = Unsigned32
_F3AmpStatsProvDataTx_Object = MibTableColumn
f3AmpStatsProvDataTx = _F3AmpStatsProvDataTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 1),
    _F3AmpStatsProvDataTx_Type()
)
f3AmpStatsProvDataTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsProvDataTx.setStatus("current")
_F3AmpStatsProvDataRx_Type = Unsigned32
_F3AmpStatsProvDataRx_Object = MibTableColumn
f3AmpStatsProvDataRx = _F3AmpStatsProvDataRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 2),
    _F3AmpStatsProvDataRx_Type()
)
f3AmpStatsProvDataRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsProvDataRx.setStatus("current")
_F3AmpStatsProvRequestTx_Type = Unsigned32
_F3AmpStatsProvRequestTx_Object = MibTableColumn
f3AmpStatsProvRequestTx = _F3AmpStatsProvRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 3),
    _F3AmpStatsProvRequestTx_Type()
)
f3AmpStatsProvRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsProvRequestTx.setStatus("current")
_F3AmpStatsProvRequestRx_Type = Unsigned32
_F3AmpStatsProvRequestRx_Object = MibTableColumn
f3AmpStatsProvRequestRx = _F3AmpStatsProvRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 4),
    _F3AmpStatsProvRequestRx_Type()
)
f3AmpStatsProvRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsProvRequestRx.setStatus("current")
_F3AmpStatsConfigSuccessTx_Type = Unsigned32
_F3AmpStatsConfigSuccessTx_Object = MibTableColumn
f3AmpStatsConfigSuccessTx = _F3AmpStatsConfigSuccessTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 5),
    _F3AmpStatsConfigSuccessTx_Type()
)
f3AmpStatsConfigSuccessTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsConfigSuccessTx.setStatus("current")
_F3AmpStatsConfigSuccessRx_Type = Unsigned32
_F3AmpStatsConfigSuccessRx_Object = MibTableColumn
f3AmpStatsConfigSuccessRx = _F3AmpStatsConfigSuccessRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 6),
    _F3AmpStatsConfigSuccessRx_Type()
)
f3AmpStatsConfigSuccessRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsConfigSuccessRx.setStatus("current")
_F3AmpStatsConfigFailTx_Type = Unsigned32
_F3AmpStatsConfigFailTx_Object = MibTableColumn
f3AmpStatsConfigFailTx = _F3AmpStatsConfigFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 7),
    _F3AmpStatsConfigFailTx_Type()
)
f3AmpStatsConfigFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsConfigFailTx.setStatus("current")
_F3AmpStatsConfigFailRx_Type = Unsigned32
_F3AmpStatsConfigFailRx_Object = MibTableColumn
f3AmpStatsConfigFailRx = _F3AmpStatsConfigFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 8),
    _F3AmpStatsConfigFailRx_Type()
)
f3AmpStatsConfigFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsConfigFailRx.setStatus("current")
_F3AmpStatsSpuriousMessageRx_Type = Unsigned32
_F3AmpStatsSpuriousMessageRx_Object = MibTableColumn
f3AmpStatsSpuriousMessageRx = _F3AmpStatsSpuriousMessageRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 9),
    _F3AmpStatsSpuriousMessageRx_Type()
)
f3AmpStatsSpuriousMessageRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsSpuriousMessageRx.setStatus("current")
_F3AmpStatsTimeoutRx_Type = Unsigned32
_F3AmpStatsTimeoutRx_Object = MibTableColumn
f3AmpStatsTimeoutRx = _F3AmpStatsTimeoutRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 10),
    _F3AmpStatsTimeoutRx_Type()
)
f3AmpStatsTimeoutRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsTimeoutRx.setStatus("current")
_F3AmpStatsLastRxStatus_Type = AMPConfigStatus
_F3AmpStatsLastRxStatus_Object = MibTableColumn
f3AmpStatsLastRxStatus = _F3AmpStatsLastRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 11),
    _F3AmpStatsLastRxStatus_Type()
)
f3AmpStatsLastRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsLastRxStatus.setStatus("current")
_F3AmpStatsRxTimeStamp_Type = DateAndTime
_F3AmpStatsRxTimeStamp_Object = MibTableColumn
f3AmpStatsRxTimeStamp = _F3AmpStatsRxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 12),
    _F3AmpStatsRxTimeStamp_Type()
)
f3AmpStatsRxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsRxTimeStamp.setStatus("current")
_F3AmpStatsLastTxStatus_Type = AMPConfigStatus
_F3AmpStatsLastTxStatus_Object = MibTableColumn
f3AmpStatsLastTxStatus = _F3AmpStatsLastTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 13),
    _F3AmpStatsLastTxStatus_Type()
)
f3AmpStatsLastTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsLastTxStatus.setStatus("current")
_F3AmpStatsTxTimeStamp_Type = DateAndTime
_F3AmpStatsTxTimeStamp_Object = MibTableColumn
f3AmpStatsTxTimeStamp = _F3AmpStatsTxTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 2, 1, 1, 14),
    _F3AmpStatsTxTimeStamp_Type()
)
f3AmpStatsTxTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AmpStatsTxTimeStamp.setStatus("current")
_F3AmpConformance_ObjectIdentity = ObjectIdentity
f3AmpConformance = _F3AmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3)
)
_F3AmpCompliances_ObjectIdentity = ObjectIdentity
f3AmpCompliances = _F3AmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 1)
)
_F3AmpGroups_ObjectIdentity = ObjectIdentity
f3AmpGroups = _F3AmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2)
)

# Managed Objects groups

f3AmpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2, 1)
)
f3AmpConfigGroup.setObjects(
      *(("F3-AMP-MIB", "f3AmpConfigRole"),
        ("F3-AMP-MIB", "f3AmpConfigProtocol"),
        ("F3-AMP-MIB", "f3AmpConfigEnabled"),
        ("F3-AMP-MIB", "f3AmpConfigPort"),
        ("F3-AMP-MIB", "f3AmpConfigStatus"),
        ("F3-AMP-MIB", "f3AmpConfigRemSysName"),
        ("F3-AMP-MIB", "f3AmpConfigRemSysIpAddr"),
        ("F3-AMP-MIB", "f3AmpConfigRemSysIpMask"),
        ("F3-AMP-MIB", "f3AmpConfigRemSysDefGateway"),
        ("F3-AMP-MIB", "f3AmpConfigRemSysSNMPV1IfName"),
        ("F3-AMP-MIB", "f3AmpConfigRemSysSrcIpAddrType"),
        ("F3-AMP-MIB", "f3AmpConfigRemSysSrcIpAddrIfName"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelIndex"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelName"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelType"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelIpAddr"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelIpMask"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelVlanId"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelSVlanId"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelSVlanIdEnabled"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelRip2PktsEnabled"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelCOS"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelCIR"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelEIR"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelBufferSize"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelEncapType"),
        ("F3-AMP-MIB", "f3AmpConfigRemTunnelMtu"),
        ("F3-AMP-MIB", "f3AmpConfigAction"),
        ("F3-AMP-MIB", "f3AmpConfigStorageType"),
        ("F3-AMP-MIB", "f3AmpConfigRowStatus"))
)
if mibBuilder.loadTexts:
    f3AmpConfigGroup.setStatus("current")

f3AmpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 2, 2)
)
f3AmpStatsGroup.setObjects(
      *(("F3-AMP-MIB", "f3AmpStatsProvDataTx"),
        ("F3-AMP-MIB", "f3AmpStatsProvDataRx"),
        ("F3-AMP-MIB", "f3AmpStatsProvRequestTx"),
        ("F3-AMP-MIB", "f3AmpStatsProvRequestRx"),
        ("F3-AMP-MIB", "f3AmpStatsConfigSuccessTx"),
        ("F3-AMP-MIB", "f3AmpStatsConfigSuccessRx"),
        ("F3-AMP-MIB", "f3AmpStatsConfigFailTx"),
        ("F3-AMP-MIB", "f3AmpStatsConfigFailRx"),
        ("F3-AMP-MIB", "f3AmpStatsSpuriousMessageRx"),
        ("F3-AMP-MIB", "f3AmpStatsTimeoutRx"),
        ("F3-AMP-MIB", "f3AmpStatsLastRxStatus"),
        ("F3-AMP-MIB", "f3AmpStatsRxTimeStamp"),
        ("F3-AMP-MIB", "f3AmpStatsLastTxStatus"),
        ("F3-AMP-MIB", "f3AmpStatsTxTimeStamp"))
)
if mibBuilder.loadTexts:
    f3AmpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3AmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 24, 3, 1, 1)
)
f3AmpCompliance.setObjects(
      *(("F3-AMP-MIB", "f3AmpConfigGroup"),
        ("F3-AMP-MIB", "f3AmpStatsGroup"))
)
if mibBuilder.loadTexts:
    f3AmpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-AMP-MIB",
    **{"AMPRole": AMPRole,
       "AMPStatus": AMPStatus,
       "AMPConfigStatus": AMPConfigStatus,
       "AMPProtocol": AMPProtocol,
       "AMPConfigAction": AMPConfigAction,
       "f3AMPMIB": f3AMPMIB,
       "f3AmpConfigObjects": f3AmpConfigObjects,
       "f3AmpConfigTable": f3AmpConfigTable,
       "f3AmpConfigEntry": f3AmpConfigEntry,
       "f3AmpConfigIndex": f3AmpConfigIndex,
       "f3AmpConfigRole": f3AmpConfigRole,
       "f3AmpConfigProtocol": f3AmpConfigProtocol,
       "f3AmpConfigEnabled": f3AmpConfigEnabled,
       "f3AmpConfigPort": f3AmpConfigPort,
       "f3AmpConfigStatus": f3AmpConfigStatus,
       "f3AmpConfigRemSysName": f3AmpConfigRemSysName,
       "f3AmpConfigRemSysIpAddr": f3AmpConfigRemSysIpAddr,
       "f3AmpConfigRemSysIpMask": f3AmpConfigRemSysIpMask,
       "f3AmpConfigRemSysDefGateway": f3AmpConfigRemSysDefGateway,
       "f3AmpConfigRemSysSNMPV1IfName": f3AmpConfigRemSysSNMPV1IfName,
       "f3AmpConfigRemSysSrcIpAddrType": f3AmpConfigRemSysSrcIpAddrType,
       "f3AmpConfigRemSysSrcIpAddrIfName": f3AmpConfigRemSysSrcIpAddrIfName,
       "f3AmpConfigRemTunnelIndex": f3AmpConfigRemTunnelIndex,
       "f3AmpConfigRemTunnelName": f3AmpConfigRemTunnelName,
       "f3AmpConfigRemTunnelType": f3AmpConfigRemTunnelType,
       "f3AmpConfigRemTunnelIpAddr": f3AmpConfigRemTunnelIpAddr,
       "f3AmpConfigRemTunnelIpMask": f3AmpConfigRemTunnelIpMask,
       "f3AmpConfigRemTunnelVlanId": f3AmpConfigRemTunnelVlanId,
       "f3AmpConfigRemTunnelSVlanId": f3AmpConfigRemTunnelSVlanId,
       "f3AmpConfigRemTunnelSVlanIdEnabled": f3AmpConfigRemTunnelSVlanIdEnabled,
       "f3AmpConfigRemTunnelRip2PktsEnabled": f3AmpConfigRemTunnelRip2PktsEnabled,
       "f3AmpConfigRemTunnelCOS": f3AmpConfigRemTunnelCOS,
       "f3AmpConfigRemTunnelCIR": f3AmpConfigRemTunnelCIR,
       "f3AmpConfigRemTunnelEIR": f3AmpConfigRemTunnelEIR,
       "f3AmpConfigRemTunnelBufferSize": f3AmpConfigRemTunnelBufferSize,
       "f3AmpConfigRemTunnelEncapType": f3AmpConfigRemTunnelEncapType,
       "f3AmpConfigRemTunnelMtu": f3AmpConfigRemTunnelMtu,
       "f3AmpConfigAction": f3AmpConfigAction,
       "f3AmpConfigStorageType": f3AmpConfigStorageType,
       "f3AmpConfigRowStatus": f3AmpConfigRowStatus,
       "f3AmpStatsObjects": f3AmpStatsObjects,
       "f3AmpStatsTable": f3AmpStatsTable,
       "f3AmpStatsEntry": f3AmpStatsEntry,
       "f3AmpStatsProvDataTx": f3AmpStatsProvDataTx,
       "f3AmpStatsProvDataRx": f3AmpStatsProvDataRx,
       "f3AmpStatsProvRequestTx": f3AmpStatsProvRequestTx,
       "f3AmpStatsProvRequestRx": f3AmpStatsProvRequestRx,
       "f3AmpStatsConfigSuccessTx": f3AmpStatsConfigSuccessTx,
       "f3AmpStatsConfigSuccessRx": f3AmpStatsConfigSuccessRx,
       "f3AmpStatsConfigFailTx": f3AmpStatsConfigFailTx,
       "f3AmpStatsConfigFailRx": f3AmpStatsConfigFailRx,
       "f3AmpStatsSpuriousMessageRx": f3AmpStatsSpuriousMessageRx,
       "f3AmpStatsTimeoutRx": f3AmpStatsTimeoutRx,
       "f3AmpStatsLastRxStatus": f3AmpStatsLastRxStatus,
       "f3AmpStatsRxTimeStamp": f3AmpStatsRxTimeStamp,
       "f3AmpStatsLastTxStatus": f3AmpStatsLastTxStatus,
       "f3AmpStatsTxTimeStamp": f3AmpStatsTxTimeStamp,
       "f3AmpConformance": f3AmpConformance,
       "f3AmpCompliances": f3AmpCompliances,
       "f3AmpCompliance": f3AmpCompliance,
       "f3AmpGroups": f3AmpGroups,
       "f3AmpConfigGroup": f3AmpConfigGroup,
       "f3AmpStatsGroup": f3AmpStatsGroup}
)
