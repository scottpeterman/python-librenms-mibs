# SNMP MIB module (VENTURI-SERVER-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\venturi\VENTURI-SERVER-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:48 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vServerMgmt,) = mibBuilder.importSymbols(
    "VENTURI-SERVER-MIB",
    "vServerMgmt")

(VenturiBooleanType,
 VenturiLogLevels,
 VenturiLogModuleType,
 VenturiSyslogFacilityType,
 VenturiThresholdLevels,
 VenturiTrapSeverity,
 VenturiTrapType) = mibBuilder.importSymbols(
    "VENTURI-TC",
    "VenturiBooleanType",
    "VenturiLogLevels",
    "VenturiLogModuleType",
    "VenturiSyslogFacilityType",
    "VenturiThresholdLevels",
    "VenturiTrapSeverity",
    "VenturiTrapType")


# MODULE-IDENTITY

vServerConf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4)
)
if mibBuilder.loadTexts:
    vServerConf.setRevisions(
        ("2011-01-03 00:00",
         "2010-12-13 00:00",
         "2010-03-01 00:00",
         "2010-01-12 00:00",
         "2010-01-06 00:00",
         "2009-03-24 00:00",
         "2008-05-06 00:00",
         "2008-03-18 00:00",
         "2008-03-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VServerConfIPSvcs_ObjectIdentity = ObjectIdentity
vServerConfIPSvcs = _VServerConfIPSvcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1)
)
_VServerConfIPSvcsPhysicalIf_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsPhysicalIf = _VServerConfIPSvcsPhysicalIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1)
)
_VServerConfIPSvcsPhysicalScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsPhysicalScalars = _VServerConfIPSvcsPhysicalScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 1)
)
_VServerConfIPSvcsPhysicalTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsPhysicalTbls = _VServerConfIPSvcsPhysicalTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2)
)
_VServerEthConfTbl_Object = MibTable
vServerEthConfTbl = _VServerEthConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vServerEthConfTbl.setStatus("current")
_VServerEthConfTblEntry_Object = MibTableRow
vServerEthConfTblEntry = _VServerEthConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2, 1, 1)
)
vServerEthConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerEthConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerEthConfTblEntry.setStatus("current")
_VServerEthConfTblIndex_Type = Unsigned32
_VServerEthConfTblIndex_Object = MibTableColumn
vServerEthConfTblIndex = _VServerEthConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2, 1, 1, 1),
    _VServerEthConfTblIndex_Type()
)
vServerEthConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerEthConfTblIndex.setStatus("current")


class _VServerEthConfTblIfName_Type(OctetString):
    """Custom type vServerEthConfTblIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerEthConfTblIfName_Type.__name__ = "OctetString"
_VServerEthConfTblIfName_Object = MibTableColumn
vServerEthConfTblIfName = _VServerEthConfTblIfName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2, 1, 1, 2),
    _VServerEthConfTblIfName_Type()
)
vServerEthConfTblIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerEthConfTblIfName.setStatus("current")


class _VServerEthConfTblMACAddress_Type(OctetString):
    """Custom type vServerEthConfTblMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerEthConfTblMACAddress_Type.__name__ = "OctetString"
_VServerEthConfTblMACAddress_Object = MibTableColumn
vServerEthConfTblMACAddress = _VServerEthConfTblMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2, 1, 1, 3),
    _VServerEthConfTblMACAddress_Type()
)
vServerEthConfTblMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerEthConfTblMACAddress.setStatus("current")
_VServerEthConfTblMTU_Type = Unsigned32
_VServerEthConfTblMTU_Object = MibTableColumn
vServerEthConfTblMTU = _VServerEthConfTblMTU_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2, 1, 1, 4),
    _VServerEthConfTblMTU_Type()
)
vServerEthConfTblMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerEthConfTblMTU.setStatus("current")


class _VServerEthConfTblCurConf_Type(OctetString):
    """Custom type vServerEthConfTblCurConf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerEthConfTblCurConf_Type.__name__ = "OctetString"
_VServerEthConfTblCurConf_Object = MibTableColumn
vServerEthConfTblCurConf = _VServerEthConfTblCurConf_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2, 1, 1, 6),
    _VServerEthConfTblCurConf_Type()
)
vServerEthConfTblCurConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerEthConfTblCurConf.setStatus("current")


class _VServerEthConfTblNewConf_Type(OctetString):
    """Custom type vServerEthConfTblNewConf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerEthConfTblNewConf_Type.__name__ = "OctetString"
_VServerEthConfTblNewConf_Object = MibTableColumn
vServerEthConfTblNewConf = _VServerEthConfTblNewConf_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 1, 2, 1, 1, 7),
    _VServerEthConfTblNewConf_Type()
)
vServerEthConfTblNewConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerEthConfTblNewConf.setStatus("deprecated")
_VServerConfIPSvcsLogicalIf_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsLogicalIf = _VServerConfIPSvcsLogicalIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2)
)
_VServerConfIPSvcsLogicalScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsLogicalScalars = _VServerConfIPSvcsLogicalScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2, 1)
)
_VServerConfIPSvcsLogicalTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsLogicalTbls = _VServerConfIPSvcsLogicalTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2, 2)
)
_VServerLogicalIfTbl_Object = MibTable
vServerLogicalIfTbl = _VServerLogicalIfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vServerLogicalIfTbl.setStatus("current")
_VServerLogicalIfTblEntry_Object = MibTableRow
vServerLogicalIfTblEntry = _VServerLogicalIfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2, 2, 1, 1)
)
vServerLogicalIfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerLogicalIfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerLogicalIfTblEntry.setStatus("current")
_VServerLogicalIfTblIndex_Type = Unsigned32
_VServerLogicalIfTblIndex_Object = MibTableColumn
vServerLogicalIfTblIndex = _VServerLogicalIfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2, 2, 1, 1, 1),
    _VServerLogicalIfTblIndex_Type()
)
vServerLogicalIfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerLogicalIfTblIndex.setStatus("current")


class _VServerLogicalIfTblName_Type(OctetString):
    """Custom type vServerLogicalIfTblName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerLogicalIfTblName_Type.__name__ = "OctetString"
_VServerLogicalIfTblName_Object = MibTableColumn
vServerLogicalIfTblName = _VServerLogicalIfTblName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2, 2, 1, 1, 2),
    _VServerLogicalIfTblName_Type()
)
vServerLogicalIfTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerLogicalIfTblName.setStatus("current")


class _VServerLogicalIfTblMode_Type(OctetString):
    """Custom type vServerLogicalIfTblMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerLogicalIfTblMode_Type.__name__ = "OctetString"
_VServerLogicalIfTblMode_Object = MibTableColumn
vServerLogicalIfTblMode = _VServerLogicalIfTblMode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2, 2, 1, 1, 3),
    _VServerLogicalIfTblMode_Type()
)
vServerLogicalIfTblMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerLogicalIfTblMode.setStatus("current")


class _VServerLogicalIfTblParams_Type(OctetString):
    """Custom type vServerLogicalIfTblParams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerLogicalIfTblParams_Type.__name__ = "OctetString"
_VServerLogicalIfTblParams_Object = MibTableColumn
vServerLogicalIfTblParams = _VServerLogicalIfTblParams_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 2, 2, 1, 1, 4),
    _VServerLogicalIfTblParams_Type()
)
vServerLogicalIfTblParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerLogicalIfTblParams.setStatus("current")
_VServerConfIPSvcsMgmtIf_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsMgmtIf = _VServerConfIPSvcsMgmtIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3)
)
_VServerConfIPSvcsMgmtScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsMgmtScalars = _VServerConfIPSvcsMgmtScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 1)
)
_VServerConfIPSvcsMgmtTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsMgmtTbls = _VServerConfIPSvcsMgmtTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2)
)
_VServerMgmtIfTbl_Object = MibTable
vServerMgmtIfTbl = _VServerMgmtIfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vServerMgmtIfTbl.setStatus("current")
_VServerMgmtIfTblEntry_Object = MibTableRow
vServerMgmtIfTblEntry = _VServerMgmtIfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1)
)
vServerMgmtIfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerMgmtIfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerMgmtIfTblEntry.setStatus("current")
_VServerMgmtIfTblIndex_Type = Unsigned32
_VServerMgmtIfTblIndex_Object = MibTableColumn
vServerMgmtIfTblIndex = _VServerMgmtIfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 1),
    _VServerMgmtIfTblIndex_Type()
)
vServerMgmtIfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerMgmtIfTblIndex.setStatus("current")
_VServerMgmtIfTblIp_Type = IpAddress
_VServerMgmtIfTblIp_Object = MibTableColumn
vServerMgmtIfTblIp = _VServerMgmtIfTblIp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 2),
    _VServerMgmtIfTblIp_Type()
)
vServerMgmtIfTblIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblIp.setStatus("current")
_VServerMgmtIfTblNetmask_Type = IpAddress
_VServerMgmtIfTblNetmask_Object = MibTableColumn
vServerMgmtIfTblNetmask = _VServerMgmtIfTblNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 3),
    _VServerMgmtIfTblNetmask_Type()
)
vServerMgmtIfTblNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblNetmask.setStatus("current")
_VServerMgmtIfTblDefaultGw_Type = IpAddress
_VServerMgmtIfTblDefaultGw_Object = MibTableColumn
vServerMgmtIfTblDefaultGw = _VServerMgmtIfTblDefaultGw_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 4),
    _VServerMgmtIfTblDefaultGw_Type()
)
vServerMgmtIfTblDefaultGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblDefaultGw.setStatus("current")
_VServerMgmtIfTblBroadcast_Type = IpAddress
_VServerMgmtIfTblBroadcast_Object = MibTableColumn
vServerMgmtIfTblBroadcast = _VServerMgmtIfTblBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 5),
    _VServerMgmtIfTblBroadcast_Type()
)
vServerMgmtIfTblBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblBroadcast.setStatus("current")
_VServerMgmtIfTblDns1_Type = IpAddress
_VServerMgmtIfTblDns1_Object = MibTableColumn
vServerMgmtIfTblDns1 = _VServerMgmtIfTblDns1_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 6),
    _VServerMgmtIfTblDns1_Type()
)
vServerMgmtIfTblDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblDns1.setStatus("current")
_VServerMgmtIfTblDns2_Type = IpAddress
_VServerMgmtIfTblDns2_Object = MibTableColumn
vServerMgmtIfTblDns2 = _VServerMgmtIfTblDns2_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 7),
    _VServerMgmtIfTblDns2_Type()
)
vServerMgmtIfTblDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblDns2.setStatus("current")
_VServerMgmtIfTblDns3_Type = IpAddress
_VServerMgmtIfTblDns3_Object = MibTableColumn
vServerMgmtIfTblDns3 = _VServerMgmtIfTblDns3_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 8),
    _VServerMgmtIfTblDns3_Type()
)
vServerMgmtIfTblDns3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblDns3.setStatus("current")


class _VServerMgmtIfTblDnsdomain_Type(OctetString):
    """Custom type vServerMgmtIfTblDnsdomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerMgmtIfTblDnsdomain_Type.__name__ = "OctetString"
_VServerMgmtIfTblDnsdomain_Object = MibTableColumn
vServerMgmtIfTblDnsdomain = _VServerMgmtIfTblDnsdomain_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 9),
    _VServerMgmtIfTblDnsdomain_Type()
)
vServerMgmtIfTblDnsdomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblDnsdomain.setStatus("current")
_VServerMgmtIfTblLogicalNicID_Type = Integer32
_VServerMgmtIfTblLogicalNicID_Object = MibTableColumn
vServerMgmtIfTblLogicalNicID = _VServerMgmtIfTblLogicalNicID_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 10),
    _VServerMgmtIfTblLogicalNicID_Type()
)
vServerMgmtIfTblLogicalNicID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblLogicalNicID.setStatus("current")
_VServerMgmtIfTblNetifId_Type = Integer32
_VServerMgmtIfTblNetifId_Object = MibTableColumn
vServerMgmtIfTblNetifId = _VServerMgmtIfTblNetifId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 3, 2, 1, 1, 11),
    _VServerMgmtIfTblNetifId_Type()
)
vServerMgmtIfTblNetifId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMgmtIfTblNetifId.setStatus("deprecated")
_VServerConfIPSvcsDataIf_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsDataIf = _VServerConfIPSvcsDataIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4)
)
_VServerConfIPSvcsDataScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsDataScalars = _VServerConfIPSvcsDataScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 1)
)
_VServerConfIPSvcsDataTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsDataTbls = _VServerConfIPSvcsDataTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2)
)
_VServerTransLstnPorts_Object = MibTable
vServerTransLstnPorts = _VServerTransLstnPorts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vServerTransLstnPorts.setStatus("current")
_VServerTransLstnPortsEntry_Object = MibTableRow
vServerTransLstnPortsEntry = _VServerTransLstnPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1)
)
vServerTransLstnPortsEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerTransLstnPortsIndex"),
)
if mibBuilder.loadTexts:
    vServerTransLstnPortsEntry.setStatus("current")
_VServerTransLstnPortsIndex_Type = Unsigned32
_VServerTransLstnPortsIndex_Object = MibTableColumn
vServerTransLstnPortsIndex = _VServerTransLstnPortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 1),
    _VServerTransLstnPortsIndex_Type()
)
vServerTransLstnPortsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransLstnPortsIndex.setStatus("current")
_VServerTransLstnPortsIp_Type = IpAddress
_VServerTransLstnPortsIp_Object = MibTableColumn
vServerTransLstnPortsIp = _VServerTransLstnPortsIp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 2),
    _VServerTransLstnPortsIp_Type()
)
vServerTransLstnPortsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsIp.setStatus("current")
_VServerTransLstnPortsNetmask_Type = IpAddress
_VServerTransLstnPortsNetmask_Object = MibTableColumn
vServerTransLstnPortsNetmask = _VServerTransLstnPortsNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 3),
    _VServerTransLstnPortsNetmask_Type()
)
vServerTransLstnPortsNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsNetmask.setStatus("current")
_VServerTransLstnPortsDefaultGw_Type = IpAddress
_VServerTransLstnPortsDefaultGw_Object = MibTableColumn
vServerTransLstnPortsDefaultGw = _VServerTransLstnPortsDefaultGw_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 4),
    _VServerTransLstnPortsDefaultGw_Type()
)
vServerTransLstnPortsDefaultGw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsDefaultGw.setStatus("current")
_VServerTransLstnPortsBroadcast_Type = IpAddress
_VServerTransLstnPortsBroadcast_Object = MibTableColumn
vServerTransLstnPortsBroadcast = _VServerTransLstnPortsBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 5),
    _VServerTransLstnPortsBroadcast_Type()
)
vServerTransLstnPortsBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsBroadcast.setStatus("current")
_VServerTransLstnPortsDns1_Type = IpAddress
_VServerTransLstnPortsDns1_Object = MibTableColumn
vServerTransLstnPortsDns1 = _VServerTransLstnPortsDns1_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 6),
    _VServerTransLstnPortsDns1_Type()
)
vServerTransLstnPortsDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsDns1.setStatus("current")
_VServerTransLstnPortsDns2_Type = IpAddress
_VServerTransLstnPortsDns2_Object = MibTableColumn
vServerTransLstnPortsDns2 = _VServerTransLstnPortsDns2_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 7),
    _VServerTransLstnPortsDns2_Type()
)
vServerTransLstnPortsDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsDns2.setStatus("current")
_VServerTransLstnPortsDns3_Type = IpAddress
_VServerTransLstnPortsDns3_Object = MibTableColumn
vServerTransLstnPortsDns3 = _VServerTransLstnPortsDns3_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 8),
    _VServerTransLstnPortsDns3_Type()
)
vServerTransLstnPortsDns3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsDns3.setStatus("current")


class _VServerTransLstnPortsDnsdomain_Type(OctetString):
    """Custom type vServerTransLstnPortsDnsdomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerTransLstnPortsDnsdomain_Type.__name__ = "OctetString"
_VServerTransLstnPortsDnsdomain_Object = MibTableColumn
vServerTransLstnPortsDnsdomain = _VServerTransLstnPortsDnsdomain_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 9),
    _VServerTransLstnPortsDnsdomain_Type()
)
vServerTransLstnPortsDnsdomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsDnsdomain.setStatus("current")
_VServerTransLstnPortsUdpPort_Type = Integer32
_VServerTransLstnPortsUdpPort_Object = MibTableColumn
vServerTransLstnPortsUdpPort = _VServerTransLstnPortsUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 10),
    _VServerTransLstnPortsUdpPort_Type()
)
vServerTransLstnPortsUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsUdpPort.setStatus("current")
_VServerTransLstnPortsTcpPort_Type = Integer32
_VServerTransLstnPortsTcpPort_Object = MibTableColumn
vServerTransLstnPortsTcpPort = _VServerTransLstnPortsTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 11),
    _VServerTransLstnPortsTcpPort_Type()
)
vServerTransLstnPortsTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsTcpPort.setStatus("current")
_VServerTransLstnPortsNetifId_Type = Integer32
_VServerTransLstnPortsNetifId_Object = MibTableColumn
vServerTransLstnPortsNetifId = _VServerTransLstnPortsNetifId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 12),
    _VServerTransLstnPortsNetifId_Type()
)
vServerTransLstnPortsNetifId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsNetifId.setStatus("current")


class _VServerTransLstnPortsFlag_Type(OctetString):
    """Custom type vServerTransLstnPortsFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerTransLstnPortsFlag_Type.__name__ = "OctetString"
_VServerTransLstnPortsFlag_Object = MibTableColumn
vServerTransLstnPortsFlag = _VServerTransLstnPortsFlag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 13),
    _VServerTransLstnPortsFlag_Type()
)
vServerTransLstnPortsFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsFlag.setStatus("current")
_VServerTransLstnPortsLogicalNicID_Type = Integer32
_VServerTransLstnPortsLogicalNicID_Object = MibTableColumn
vServerTransLstnPortsLogicalNicID = _VServerTransLstnPortsLogicalNicID_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 4, 2, 1, 1, 14),
    _VServerTransLstnPortsLogicalNicID_Type()
)
vServerTransLstnPortsLogicalNicID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransLstnPortsLogicalNicID.setStatus("current")
_VServerConfIPSvcsAdvanced_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsAdvanced = _VServerConfIPSvcsAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5)
)
_VServerConfIPSvcsAdvancedScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsAdvancedScalars = _VServerConfIPSvcsAdvancedScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 1)
)
_VServerConfIPSvcsAdvancedTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsAdvancedTbls = _VServerConfIPSvcsAdvancedTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2)
)
_VServerVirtSvr_Object = MibTable
vServerVirtSvr = _VServerVirtSvr_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vServerVirtSvr.setStatus("current")
_VServerVirtSvrEntry_Object = MibTableRow
vServerVirtSvrEntry = _VServerVirtSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 1, 1)
)
vServerVirtSvrEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerVirtSvrIndex"),
)
if mibBuilder.loadTexts:
    vServerVirtSvrEntry.setStatus("current")
_VServerVirtSvrIndex_Type = Unsigned32
_VServerVirtSvrIndex_Object = MibTableColumn
vServerVirtSvrIndex = _VServerVirtSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 1, 1, 1),
    _VServerVirtSvrIndex_Type()
)
vServerVirtSvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerVirtSvrIndex.setStatus("current")


class _VServerVirtSvrHostname_Type(OctetString):
    """Custom type vServerVirtSvrHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerVirtSvrHostname_Type.__name__ = "OctetString"
_VServerVirtSvrHostname_Object = MibTableColumn
vServerVirtSvrHostname = _VServerVirtSvrHostname_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 1, 1, 2),
    _VServerVirtSvrHostname_Type()
)
vServerVirtSvrHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVirtSvrHostname.setStatus("current")


class _VServerVirtSvrIpaddr_Type(OctetString):
    """Custom type vServerVirtSvrIpaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerVirtSvrIpaddr_Type.__name__ = "OctetString"
_VServerVirtSvrIpaddr_Object = MibTableColumn
vServerVirtSvrIpaddr = _VServerVirtSvrIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 1, 1, 3),
    _VServerVirtSvrIpaddr_Type()
)
vServerVirtSvrIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVirtSvrIpaddr.setStatus("current")


class _VServerVirtSvrPortRange_Type(OctetString):
    """Custom type vServerVirtSvrPortRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerVirtSvrPortRange_Type.__name__ = "OctetString"
_VServerVirtSvrPortRange_Object = MibTableColumn
vServerVirtSvrPortRange = _VServerVirtSvrPortRange_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 1, 1, 4),
    _VServerVirtSvrPortRange_Type()
)
vServerVirtSvrPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVirtSvrPortRange.setStatus("current")


class _VServerVirtSvrDestinations_Type(OctetString):
    """Custom type vServerVirtSvrDestinations based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerVirtSvrDestinations_Type.__name__ = "OctetString"
_VServerVirtSvrDestinations_Object = MibTableColumn
vServerVirtSvrDestinations = _VServerVirtSvrDestinations_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 1, 1, 5),
    _VServerVirtSvrDestinations_Type()
)
vServerVirtSvrDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVirtSvrDestinations.setStatus("current")
_VServerDefaultDestTbl_Object = MibTable
vServerDefaultDestTbl = _VServerDefaultDestTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    vServerDefaultDestTbl.setStatus("current")
_VServerDefaultDestTblEntry_Object = MibTableRow
vServerDefaultDestTblEntry = _VServerDefaultDestTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 2, 1)
)
vServerDefaultDestTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerDefaultDestTblIndex"),
)
if mibBuilder.loadTexts:
    vServerDefaultDestTblEntry.setStatus("current")
_VServerDefaultDestTblIndex_Type = Unsigned32
_VServerDefaultDestTblIndex_Object = MibTableColumn
vServerDefaultDestTblIndex = _VServerDefaultDestTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 2, 1, 1),
    _VServerDefaultDestTblIndex_Type()
)
vServerDefaultDestTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDefaultDestTblIndex.setStatus("current")


class _VServerDefaultDestTblDestinations_Type(OctetString):
    """Custom type vServerDefaultDestTblDestinations based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerDefaultDestTblDestinations_Type.__name__ = "OctetString"
_VServerDefaultDestTblDestinations_Object = MibTableColumn
vServerDefaultDestTblDestinations = _VServerDefaultDestTblDestinations_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 5, 2, 2, 1, 2),
    _VServerDefaultDestTblDestinations_Type()
)
vServerDefaultDestTblDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerDefaultDestTblDestinations.setStatus("current")
_VServerConfIPSvcsPxy_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsPxy = _VServerConfIPSvcsPxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6)
)
_VServerConfIPSvcsPxyScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsPxyScalars = _VServerConfIPSvcsPxyScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 1)
)
_VServerConfIPSvcsPxyTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsPxyTbls = _VServerConfIPSvcsPxyTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2)
)
_VServerVSPxyTbl_Object = MibTable
vServerVSPxyTbl = _VServerVSPxyTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vServerVSPxyTbl.setStatus("current")
_VServerVSPxyTblEntry_Object = MibTableRow
vServerVSPxyTblEntry = _VServerVSPxyTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2, 1, 1)
)
vServerVSPxyTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerVSPxyTblIndex"),
)
if mibBuilder.loadTexts:
    vServerVSPxyTblEntry.setStatus("current")
_VServerVSPxyTblIndex_Type = Unsigned32
_VServerVSPxyTblIndex_Object = MibTableColumn
vServerVSPxyTblIndex = _VServerVSPxyTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2, 1, 1, 1),
    _VServerVSPxyTblIndex_Type()
)
vServerVSPxyTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerVSPxyTblIndex.setStatus("current")


class _VServerVSPxyTblHnameIp_Type(OctetString):
    """Custom type vServerVSPxyTblHnameIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerVSPxyTblHnameIp_Type.__name__ = "OctetString"
_VServerVSPxyTblHnameIp_Object = MibTableColumn
vServerVSPxyTblHnameIp = _VServerVSPxyTblHnameIp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2, 1, 1, 2),
    _VServerVSPxyTblHnameIp_Type()
)
vServerVSPxyTblHnameIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVSPxyTblHnameIp.setStatus("current")
_VServerVSPxyTblPort_Type = Integer32
_VServerVSPxyTblPort_Object = MibTableColumn
vServerVSPxyTblPort = _VServerVSPxyTblPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2, 1, 1, 3),
    _VServerVSPxyTblPort_Type()
)
vServerVSPxyTblPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVSPxyTblPort.setStatus("current")
_VServerVSPxyTblTpType_Type = Integer32
_VServerVSPxyTblTpType_Object = MibTableColumn
vServerVSPxyTblTpType = _VServerVSPxyTblTpType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2, 1, 1, 4),
    _VServerVSPxyTblTpType_Type()
)
vServerVSPxyTblTpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVSPxyTblTpType.setStatus("current")
_VServerVSPxyTblBalance_Type = Unsigned32
_VServerVSPxyTblBalance_Object = MibTableColumn
vServerVSPxyTblBalance = _VServerVSPxyTblBalance_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2, 1, 1, 5),
    _VServerVSPxyTblBalance_Type()
)
vServerVSPxyTblBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVSPxyTblBalance.setStatus("current")
_VServerVSPxyTblHealthCheck_Type = VenturiBooleanType
_VServerVSPxyTblHealthCheck_Object = MibTableColumn
vServerVSPxyTblHealthCheck = _VServerVSPxyTblHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 6, 2, 1, 1, 6),
    _VServerVSPxyTblHealthCheck_Type()
)
vServerVSPxyTblHealthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerVSPxyTblHealthCheck.setStatus("current")
_VServerConfIPSvcsStatic_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsStatic = _VServerConfIPSvcsStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7)
)
_VServerConfIPSvcsStaticScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsStaticScalars = _VServerConfIPSvcsStaticScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 1)
)
_VServerConfIPSvcsStaticTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsStaticTbls = _VServerConfIPSvcsStaticTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 2)
)
_VServerStaticRouteTbl_Object = MibTable
vServerStaticRouteTbl = _VServerStaticRouteTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vServerStaticRouteTbl.setStatus("current")
_VServerStaticRouteTblEntry_Object = MibTableRow
vServerStaticRouteTblEntry = _VServerStaticRouteTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 2, 1, 1)
)
vServerStaticRouteTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerStaticRouteTblIndex"),
)
if mibBuilder.loadTexts:
    vServerStaticRouteTblEntry.setStatus("current")
_VServerStaticRouteTblIndex_Type = Unsigned32
_VServerStaticRouteTblIndex_Object = MibTableColumn
vServerStaticRouteTblIndex = _VServerStaticRouteTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 2, 1, 1, 1),
    _VServerStaticRouteTblIndex_Type()
)
vServerStaticRouteTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStaticRouteTblIndex.setStatus("current")


class _VServerStaticRouteTblAllowRelay_Type(OctetString):
    """Custom type vServerStaticRouteTblAllowRelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerStaticRouteTblAllowRelay_Type.__name__ = "OctetString"
_VServerStaticRouteTblAllowRelay_Object = MibTableColumn
vServerStaticRouteTblAllowRelay = _VServerStaticRouteTblAllowRelay_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 2, 1, 1, 2),
    _VServerStaticRouteTblAllowRelay_Type()
)
vServerStaticRouteTblAllowRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerStaticRouteTblAllowRelay.setStatus("current")


class _VServerStaticRouteTblMaskSize_Type(OctetString):
    """Custom type vServerStaticRouteTblMaskSize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerStaticRouteTblMaskSize_Type.__name__ = "OctetString"
_VServerStaticRouteTblMaskSize_Object = MibTableColumn
vServerStaticRouteTblMaskSize = _VServerStaticRouteTblMaskSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 2, 1, 1, 3),
    _VServerStaticRouteTblMaskSize_Type()
)
vServerStaticRouteTblMaskSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerStaticRouteTblMaskSize.setStatus("current")
_VServerStaticRouteTblAddress_Type = IpAddress
_VServerStaticRouteTblAddress_Object = MibTableColumn
vServerStaticRouteTblAddress = _VServerStaticRouteTblAddress_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 2, 1, 1, 4),
    _VServerStaticRouteTblAddress_Type()
)
vServerStaticRouteTblAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerStaticRouteTblAddress.setStatus("current")
_VServerStaticRouteTblGatewayAddr_Type = IpAddress
_VServerStaticRouteTblGatewayAddr_Object = MibTableColumn
vServerStaticRouteTblGatewayAddr = _VServerStaticRouteTblGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 7, 2, 1, 1, 5),
    _VServerStaticRouteTblGatewayAddr_Type()
)
vServerStaticRouteTblGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerStaticRouteTblGatewayAddr.setStatus("current")
_VServerConfIPSvcsDscp_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsDscp = _VServerConfIPSvcsDscp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8)
)
_VServerConfIPSvcsDscpScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsDscpScalars = _VServerConfIPSvcsDscpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1)
)
_VServerCLPreserveDscp_Type = VenturiBooleanType
_VServerCLPreserveDscp_Object = MibScalar
vServerCLPreserveDscp = _VServerCLPreserveDscp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 1),
    _VServerCLPreserveDscp_Type()
)
vServerCLPreserveDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCLPreserveDscp.setStatus("current")
_VServerCLDscpForObjectsServedFromCache_Type = Integer32
_VServerCLDscpForObjectsServedFromCache_Object = MibScalar
vServerCLDscpForObjectsServedFromCache = _VServerCLDscpForObjectsServedFromCache_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 2),
    _VServerCLDscpForObjectsServedFromCache_Type()
)
vServerCLDscpForObjectsServedFromCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCLDscpForObjectsServedFromCache.setStatus("current")
_VServerCSPreserveDscp_Type = VenturiBooleanType
_VServerCSPreserveDscp_Object = MibScalar
vServerCSPreserveDscp = _VServerCSPreserveDscp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 3),
    _VServerCSPreserveDscp_Type()
)
vServerCSPreserveDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCSPreserveDscp.setStatus("current")
_VServerCSDscpForObjectsServedFromCache_Type = Integer32
_VServerCSDscpForObjectsServedFromCache_Object = MibScalar
vServerCSDscpForObjectsServedFromCache = _VServerCSDscpForObjectsServedFromCache_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 4),
    _VServerCSDscpForObjectsServedFromCache_Type()
)
vServerCSDscpForObjectsServedFromCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCSDscpForObjectsServedFromCache.setStatus("deprecated")
_VServerCSDscpForTrafficMarkedDscp0_Type = Integer32
_VServerCSDscpForTrafficMarkedDscp0_Object = MibScalar
vServerCSDscpForTrafficMarkedDscp0 = _VServerCSDscpForTrafficMarkedDscp0_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 5),
    _VServerCSDscpForTrafficMarkedDscp0_Type()
)
vServerCSDscpForTrafficMarkedDscp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCSDscpForTrafficMarkedDscp0.setStatus("current")
_VServerCSDscpForVTPControlTraffic_Type = Integer32
_VServerCSDscpForVTPControlTraffic_Object = MibScalar
vServerCSDscpForVTPControlTraffic = _VServerCSDscpForVTPControlTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 6),
    _VServerCSDscpForVTPControlTraffic_Type()
)
vServerCSDscpForVTPControlTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCSDscpForVTPControlTraffic.setStatus("current")
_VServerConfGwCStatsIntermediateUpdate_Type = Unsigned32
_VServerConfGwCStatsIntermediateUpdate_Object = MibScalar
vServerConfGwCStatsIntermediateUpdate = _VServerConfGwCStatsIntermediateUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 7),
    _VServerConfGwCStatsIntermediateUpdate_Type()
)
vServerConfGwCStatsIntermediateUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfGwCStatsIntermediateUpdate.setStatus("current")
_VServerCLDscpForTrafficMarkedDscp0_Type = Integer32
_VServerCLDscpForTrafficMarkedDscp0_Object = MibScalar
vServerCLDscpForTrafficMarkedDscp0 = _VServerCLDscpForTrafficMarkedDscp0_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 8),
    _VServerCLDscpForTrafficMarkedDscp0_Type()
)
vServerCLDscpForTrafficMarkedDscp0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCLDscpForTrafficMarkedDscp0.setStatus("current")
_VServerConfIntermediateUpdateEnable_Type = VenturiBooleanType
_VServerConfIntermediateUpdateEnable_Object = MibScalar
vServerConfIntermediateUpdateEnable = _VServerConfIntermediateUpdateEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 1, 9),
    _VServerConfIntermediateUpdateEnable_Type()
)
vServerConfIntermediateUpdateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfIntermediateUpdateEnable.setStatus("current")
_VServerConfIPSvcsDscpTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsDscpTbls = _VServerConfIPSvcsDscpTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2)
)
_VServerConfDscpFilterTbl_Object = MibTable
vServerConfDscpFilterTbl = _VServerConfDscpFilterTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vServerConfDscpFilterTbl.setStatus("current")
_VServerConfDscpFilterEntry_Object = MibTableRow
vServerConfDscpFilterEntry = _VServerConfDscpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 1, 1)
)
vServerConfDscpFilterEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerConfDscpFilterIndex"),
)
if mibBuilder.loadTexts:
    vServerConfDscpFilterEntry.setStatus("current")
_VServerConfDscpFilterIndex_Type = Unsigned32
_VServerConfDscpFilterIndex_Object = MibTableColumn
vServerConfDscpFilterIndex = _VServerConfDscpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 1, 1, 1),
    _VServerConfDscpFilterIndex_Type()
)
vServerConfDscpFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConfDscpFilterIndex.setStatus("current")
_VServerConfDscpFilterValue_Type = Integer32
_VServerConfDscpFilterValue_Object = MibTableColumn
vServerConfDscpFilterValue = _VServerConfDscpFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 1, 1, 2),
    _VServerConfDscpFilterValue_Type()
)
vServerConfDscpFilterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfDscpFilterValue.setStatus("current")
_VServerConfDscpFilterUseForBwEst_Type = VenturiBooleanType
_VServerConfDscpFilterUseForBwEst_Object = MibTableColumn
vServerConfDscpFilterUseForBwEst = _VServerConfDscpFilterUseForBwEst_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 1, 1, 3),
    _VServerConfDscpFilterUseForBwEst_Type()
)
vServerConfDscpFilterUseForBwEst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfDscpFilterUseForBwEst.setStatus("current")
_VServerConfGwIpMaskFilterTbl_Object = MibTable
vServerConfGwIpMaskFilterTbl = _VServerConfGwIpMaskFilterTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    vServerConfGwIpMaskFilterTbl.setStatus("current")
_VServerConfGwIpMaskFilterEntry_Object = MibTableRow
vServerConfGwIpMaskFilterEntry = _VServerConfGwIpMaskFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 2, 1)
)
vServerConfGwIpMaskFilterEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerConfGwIpMaskFilterIndex"),
)
if mibBuilder.loadTexts:
    vServerConfGwIpMaskFilterEntry.setStatus("current")
_VServerConfGwIpMaskFilterIndex_Type = Unsigned32
_VServerConfGwIpMaskFilterIndex_Object = MibTableColumn
vServerConfGwIpMaskFilterIndex = _VServerConfGwIpMaskFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 2, 1, 1),
    _VServerConfGwIpMaskFilterIndex_Type()
)
vServerConfGwIpMaskFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConfGwIpMaskFilterIndex.setStatus("current")
_VServerConfGwNetworkIp_Type = IpAddress
_VServerConfGwNetworkIp_Object = MibTableColumn
vServerConfGwNetworkIp = _VServerConfGwNetworkIp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 2, 1, 2),
    _VServerConfGwNetworkIp_Type()
)
vServerConfGwNetworkIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfGwNetworkIp.setStatus("current")
_VServerConfGwNetmask_Type = IpAddress
_VServerConfGwNetmask_Object = MibTableColumn
vServerConfGwNetmask = _VServerConfGwNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 2, 1, 3),
    _VServerConfGwNetmask_Type()
)
vServerConfGwNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfGwNetmask.setStatus("current")
_VServerConfTransBucketMappingTbl_Object = MibTable
vServerConfTransBucketMappingTbl = _VServerConfTransBucketMappingTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 3)
)
if mibBuilder.loadTexts:
    vServerConfTransBucketMappingTbl.setStatus("current")
_VServerConfTransBucketEntry_Object = MibTableRow
vServerConfTransBucketEntry = _VServerConfTransBucketEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 3, 1)
)
vServerConfTransBucketEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerConfTransMappingIndex"),
)
if mibBuilder.loadTexts:
    vServerConfTransBucketEntry.setStatus("current")
_VServerConfTransMappingIndex_Type = Unsigned32
_VServerConfTransMappingIndex_Object = MibTableColumn
vServerConfTransMappingIndex = _VServerConfTransMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 3, 1, 1),
    _VServerConfTransMappingIndex_Type()
)
vServerConfTransMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConfTransMappingIndex.setStatus("current")
_VServerConfTransMappingDscp_Type = Unsigned32
_VServerConfTransMappingDscp_Object = MibTableColumn
vServerConfTransMappingDscp = _VServerConfTransMappingDscp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 3, 1, 2),
    _VServerConfTransMappingDscp_Type()
)
vServerConfTransMappingDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConfTransMappingDscp.setStatus("current")
_VServerConfTransMappingBucket_Type = Integer32
_VServerConfTransMappingBucket_Object = MibTableColumn
vServerConfTransMappingBucket = _VServerConfTransMappingBucket_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 8, 2, 3, 1, 3),
    _VServerConfTransMappingBucket_Type()
)
vServerConfTransMappingBucket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfTransMappingBucket.setStatus("current")
_VServerConfIPSvcsQos_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsQos = _VServerConfIPSvcsQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9)
)
_VServerConfIPSvcsQosScalars_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsQosScalars = _VServerConfIPSvcsQosScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 1)
)
_VServerConfDscpReclassificationEnable_Type = VenturiBooleanType
_VServerConfDscpReclassificationEnable_Object = MibScalar
vServerConfDscpReclassificationEnable = _VServerConfDscpReclassificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 1, 1),
    _VServerConfDscpReclassificationEnable_Type()
)
vServerConfDscpReclassificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfDscpReclassificationEnable.setStatus("current")
_VServerConfShapingMinBandwidth_Type = Unsigned32
_VServerConfShapingMinBandwidth_Object = MibScalar
vServerConfShapingMinBandwidth = _VServerConfShapingMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 1, 2),
    _VServerConfShapingMinBandwidth_Type()
)
vServerConfShapingMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfShapingMinBandwidth.setStatus("current")


class _VServerConfShapingMinFscValue_Type(OctetString):
    """Custom type vServerConfShapingMinFscValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_VServerConfShapingMinFscValue_Type.__name__ = "OctetString"
_VServerConfShapingMinFscValue_Object = MibScalar
vServerConfShapingMinFscValue = _VServerConfShapingMinFscValue_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 1, 3),
    _VServerConfShapingMinFscValue_Type()
)
vServerConfShapingMinFscValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfShapingMinFscValue.setStatus("current")


class _VServerConfShapingFscNumerator_Type(OctetString):
    """Custom type vServerConfShapingFscNumerator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_VServerConfShapingFscNumerator_Type.__name__ = "OctetString"
_VServerConfShapingFscNumerator_Object = MibScalar
vServerConfShapingFscNumerator = _VServerConfShapingFscNumerator_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 1, 4),
    _VServerConfShapingFscNumerator_Type()
)
vServerConfShapingFscNumerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfShapingFscNumerator.setStatus("current")
_VServerConfDSCPToTransportShapingEnable_Type = VenturiBooleanType
_VServerConfDSCPToTransportShapingEnable_Object = MibScalar
vServerConfDSCPToTransportShapingEnable = _VServerConfDSCPToTransportShapingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 1, 5),
    _VServerConfDSCPToTransportShapingEnable_Type()
)
vServerConfDSCPToTransportShapingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfDSCPToTransportShapingEnable.setStatus("current")
_VServerConfShapingMaxSubscriberCount_Type = Unsigned32
_VServerConfShapingMaxSubscriberCount_Object = MibScalar
vServerConfShapingMaxSubscriberCount = _VServerConfShapingMaxSubscriberCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 1, 6),
    _VServerConfShapingMaxSubscriberCount_Type()
)
vServerConfShapingMaxSubscriberCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfShapingMaxSubscriberCount.setStatus("current")
_VServerConfIPSvcsQosTbls_ObjectIdentity = ObjectIdentity
vServerConfIPSvcsQosTbls = _VServerConfIPSvcsQosTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2)
)
_VServerConfClientedReclassifyTbl_Object = MibTable
vServerConfClientedReclassifyTbl = _VServerConfClientedReclassifyTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyTbl.setStatus("current")
_VServerConfClientedReclassifyEntry_Object = MibTableRow
vServerConfClientedReclassifyEntry = _VServerConfClientedReclassifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1)
)
vServerConfClientedReclassifyEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerConfClientedReclassifyIndex"),
)
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyEntry.setStatus("current")
_VServerConfClientedReclassifyIndex_Type = Unsigned32
_VServerConfClientedReclassifyIndex_Object = MibTableColumn
vServerConfClientedReclassifyIndex = _VServerConfClientedReclassifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1, 1),
    _VServerConfClientedReclassifyIndex_Type()
)
vServerConfClientedReclassifyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyIndex.setStatus("current")


class _VServerConfClientedReclassifyPorts_Type(OctetString):
    """Custom type vServerConfClientedReclassifyPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerConfClientedReclassifyPorts_Type.__name__ = "OctetString"
_VServerConfClientedReclassifyPorts_Object = MibTableColumn
vServerConfClientedReclassifyPorts = _VServerConfClientedReclassifyPorts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1, 2),
    _VServerConfClientedReclassifyPorts_Type()
)
vServerConfClientedReclassifyPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyPorts.setStatus("current")


class _VServerConfClientedReclassifyIngressDscp_Type(OctetString):
    """Custom type vServerConfClientedReclassifyIngressDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerConfClientedReclassifyIngressDscp_Type.__name__ = "OctetString"
_VServerConfClientedReclassifyIngressDscp_Object = MibTableColumn
vServerConfClientedReclassifyIngressDscp = _VServerConfClientedReclassifyIngressDscp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1, 3),
    _VServerConfClientedReclassifyIngressDscp_Type()
)
vServerConfClientedReclassifyIngressDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyIngressDscp.setStatus("current")


class _VServerConfClientedReclassifyContentType_Type(OctetString):
    """Custom type vServerConfClientedReclassifyContentType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerConfClientedReclassifyContentType_Type.__name__ = "OctetString"
_VServerConfClientedReclassifyContentType_Object = MibTableColumn
vServerConfClientedReclassifyContentType = _VServerConfClientedReclassifyContentType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1, 4),
    _VServerConfClientedReclassifyContentType_Type()
)
vServerConfClientedReclassifyContentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyContentType.setStatus("current")
_VServerConfClientedReclassifySizeThreshold_Type = Unsigned32
_VServerConfClientedReclassifySizeThreshold_Object = MibTableColumn
vServerConfClientedReclassifySizeThreshold = _VServerConfClientedReclassifySizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1, 5),
    _VServerConfClientedReclassifySizeThreshold_Type()
)
vServerConfClientedReclassifySizeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfClientedReclassifySizeThreshold.setStatus("current")
_VServerConfClientedReclassifyPeriodicClear_Type = VenturiBooleanType
_VServerConfClientedReclassifyPeriodicClear_Object = MibTableColumn
vServerConfClientedReclassifyPeriodicClear = _VServerConfClientedReclassifyPeriodicClear_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1, 6),
    _VServerConfClientedReclassifyPeriodicClear_Type()
)
vServerConfClientedReclassifyPeriodicClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyPeriodicClear.setStatus("current")
_VServerConfClientedReclassifyPeriodicClearSecs_Type = Integer32
_VServerConfClientedReclassifyPeriodicClearSecs_Object = MibTableColumn
vServerConfClientedReclassifyPeriodicClearSecs = _VServerConfClientedReclassifyPeriodicClearSecs_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1, 7),
    _VServerConfClientedReclassifyPeriodicClearSecs_Type()
)
vServerConfClientedReclassifyPeriodicClearSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyPeriodicClearSecs.setStatus("current")
_VServerConfClientedReclassifyEgressDscp_Type = Integer32
_VServerConfClientedReclassifyEgressDscp_Object = MibTableColumn
vServerConfClientedReclassifyEgressDscp = _VServerConfClientedReclassifyEgressDscp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 1, 1, 8),
    _VServerConfClientedReclassifyEgressDscp_Type()
)
vServerConfClientedReclassifyEgressDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfClientedReclassifyEgressDscp.setStatus("current")
_VServerConfVtpShapingClassTbl_Object = MibTable
vServerConfVtpShapingClassTbl = _VServerConfVtpShapingClassTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassTbl.setStatus("current")
_VServerConfVtpShapingClassEntry_Object = MibTableRow
vServerConfVtpShapingClassEntry = _VServerConfVtpShapingClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1)
)
vServerConfVtpShapingClassEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerConfVtpShapingClassIndex"),
)
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassEntry.setStatus("current")
_VServerConfVtpShapingClassIndex_Type = Unsigned32
_VServerConfVtpShapingClassIndex_Object = MibTableColumn
vServerConfVtpShapingClassIndex = _VServerConfVtpShapingClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1, 1),
    _VServerConfVtpShapingClassIndex_Type()
)
vServerConfVtpShapingClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassIndex.setStatus("current")


class _VServerConfVtpShaping_Type(OctetString):
    """Custom type vServerConfVtpShaping based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VServerConfVtpShaping_Type.__name__ = "OctetString"
_VServerConfVtpShaping_Object = MibTableColumn
vServerConfVtpShaping = _VServerConfVtpShaping_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1, 2),
    _VServerConfVtpShaping_Type()
)
vServerConfVtpShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConfVtpShaping.setStatus("current")
_VServerConfVtpShapingClassThreshold_Type = Unsigned32
_VServerConfVtpShapingClassThreshold_Object = MibTableColumn
vServerConfVtpShapingClassThreshold = _VServerConfVtpShapingClassThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1, 3),
    _VServerConfVtpShapingClassThreshold_Type()
)
vServerConfVtpShapingClassThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassThreshold.setStatus("current")
_VServerConfVtpShapingClassFscEnable_Type = VenturiBooleanType
_VServerConfVtpShapingClassFscEnable_Object = MibTableColumn
vServerConfVtpShapingClassFscEnable = _VServerConfVtpShapingClassFscEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1, 4),
    _VServerConfVtpShapingClassFscEnable_Type()
)
vServerConfVtpShapingClassFscEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassFscEnable.setStatus("current")


class _VServerConfVtpShapingClassScale0_Type(OctetString):
    """Custom type vServerConfVtpShapingClassScale0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_VServerConfVtpShapingClassScale0_Type.__name__ = "OctetString"
_VServerConfVtpShapingClassScale0_Object = MibTableColumn
vServerConfVtpShapingClassScale0 = _VServerConfVtpShapingClassScale0_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1, 5),
    _VServerConfVtpShapingClassScale0_Type()
)
vServerConfVtpShapingClassScale0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassScale0.setStatus("current")


class _VServerConfVtpShapingClassScale1_Type(OctetString):
    """Custom type vServerConfVtpShapingClassScale1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_VServerConfVtpShapingClassScale1_Type.__name__ = "OctetString"
_VServerConfVtpShapingClassScale1_Object = MibTableColumn
vServerConfVtpShapingClassScale1 = _VServerConfVtpShapingClassScale1_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1, 6),
    _VServerConfVtpShapingClassScale1_Type()
)
vServerConfVtpShapingClassScale1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassScale1.setStatus("current")


class _VServerConfVtpShapingClassScale2_Type(OctetString):
    """Custom type vServerConfVtpShapingClassScale2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_VServerConfVtpShapingClassScale2_Type.__name__ = "OctetString"
_VServerConfVtpShapingClassScale2_Object = MibTableColumn
vServerConfVtpShapingClassScale2 = _VServerConfVtpShapingClassScale2_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1, 7),
    _VServerConfVtpShapingClassScale2_Type()
)
vServerConfVtpShapingClassScale2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassScale2.setStatus("current")


class _VServerConfVtpShapingClassScale3_Type(OctetString):
    """Custom type vServerConfVtpShapingClassScale3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_VServerConfVtpShapingClassScale3_Type.__name__ = "OctetString"
_VServerConfVtpShapingClassScale3_Object = MibTableColumn
vServerConfVtpShapingClassScale3 = _VServerConfVtpShapingClassScale3_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 1, 9, 2, 2, 1, 8),
    _VServerConfVtpShapingClassScale3_Type()
)
vServerConfVtpShapingClassScale3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfVtpShapingClassScale3.setStatus("current")
_VServerConfAppSvcs_ObjectIdentity = ObjectIdentity
vServerConfAppSvcs = _VServerConfAppSvcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2)
)
_VServerConfAppSvcsTransport_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsTransport = _VServerConfAppSvcsTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1)
)
_VServerConfAppSvcsTransportScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsTransportScalars = _VServerConfAppSvcsTransportScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1)
)
_VServerUDPXportConfigMtu_Type = Unsigned32
_VServerUDPXportConfigMtu_Object = MibScalar
vServerUDPXportConfigMtu = _VServerUDPXportConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 1),
    _VServerUDPXportConfigMtu_Type()
)
vServerUDPXportConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUDPXportConfigMtu.setStatus("current")
_VServerTransportConfigDoMtuDisc_Type = VenturiBooleanType
_VServerTransportConfigDoMtuDisc_Object = MibScalar
vServerTransportConfigDoMtuDisc = _VServerTransportConfigDoMtuDisc_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 2),
    _VServerTransportConfigDoMtuDisc_Type()
)
vServerTransportConfigDoMtuDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransportConfigDoMtuDisc.setStatus("current")
_VServerUDPXportConfigMaxBwExt_Type = Unsigned32
_VServerUDPXportConfigMaxBwExt_Object = MibScalar
vServerUDPXportConfigMaxBwExt = _VServerUDPXportConfigMaxBwExt_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 3),
    _VServerUDPXportConfigMaxBwExt_Type()
)
vServerUDPXportConfigMaxBwExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUDPXportConfigMaxBwExt.setStatus("current")
_VServerUDPXportConfigMaxBw2client_Type = Unsigned32
_VServerUDPXportConfigMaxBw2client_Object = MibScalar
vServerUDPXportConfigMaxBw2client = _VServerUDPXportConfigMaxBw2client_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 4),
    _VServerUDPXportConfigMaxBw2client_Type()
)
vServerUDPXportConfigMaxBw2client.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUDPXportConfigMaxBw2client.setStatus("current")
_VServerTransConfigAutoTuneEnable_Type = VenturiBooleanType
_VServerTransConfigAutoTuneEnable_Object = MibScalar
vServerTransConfigAutoTuneEnable = _VServerTransConfigAutoTuneEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 5),
    _VServerTransConfigAutoTuneEnable_Type()
)
vServerTransConfigAutoTuneEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfigAutoTuneEnable.setStatus("current")
_VServerTransConfigTcpCongControlType_Type = Unsigned32
_VServerTransConfigTcpCongControlType_Object = MibScalar
vServerTransConfigTcpCongControlType = _VServerTransConfigTcpCongControlType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 6),
    _VServerTransConfigTcpCongControlType_Type()
)
vServerTransConfigTcpCongControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfigTcpCongControlType.setStatus("current")
_VServerTransConfigTcpInitialWindowSize_Type = Unsigned32
_VServerTransConfigTcpInitialWindowSize_Object = MibScalar
vServerTransConfigTcpInitialWindowSize = _VServerTransConfigTcpInitialWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 7),
    _VServerTransConfigTcpInitialWindowSize_Type()
)
vServerTransConfigTcpInitialWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfigTcpInitialWindowSize.setStatus("current")
_VServerTransConfigFastHttpRendering_Type = VenturiBooleanType
_VServerTransConfigFastHttpRendering_Object = MibScalar
vServerTransConfigFastHttpRendering = _VServerTransConfigFastHttpRendering_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 8),
    _VServerTransConfigFastHttpRendering_Type()
)
vServerTransConfigFastHttpRendering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfigFastHttpRendering.setStatus("current")
_VServerTransConfigTimeWaitTimeout_Type = Unsigned32
_VServerTransConfigTimeWaitTimeout_Object = MibScalar
vServerTransConfigTimeWaitTimeout = _VServerTransConfigTimeWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 9),
    _VServerTransConfigTimeWaitTimeout_Type()
)
vServerTransConfigTimeWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfigTimeWaitTimeout.setStatus("current")
_VServerTransConfigIdleTimeout_Type = Unsigned32
_VServerTransConfigIdleTimeout_Object = MibScalar
vServerTransConfigIdleTimeout = _VServerTransConfigIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 10),
    _VServerTransConfigIdleTimeout_Type()
)
vServerTransConfigIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfigIdleTimeout.setStatus("current")
_VServerTransConfigHttpReqOptimization_Type = VenturiBooleanType
_VServerTransConfigHttpReqOptimization_Object = MibScalar
vServerTransConfigHttpReqOptimization = _VServerTransConfigHttpReqOptimization_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 1, 11),
    _VServerTransConfigHttpReqOptimization_Type()
)
vServerTransConfigHttpReqOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfigHttpReqOptimization.setStatus("current")
_VServerConfAppSvcsTransportTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsTransportTbls = _VServerConfAppSvcsTransportTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2)
)
_VServerMasterPxyTbl_Object = MibTable
vServerMasterPxyTbl = _VServerMasterPxyTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vServerMasterPxyTbl.setStatus("current")
_VServerMasterPxyTblEntry_Object = MibTableRow
vServerMasterPxyTblEntry = _VServerMasterPxyTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1)
)
vServerMasterPxyTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerMasterPxyTblIndex"),
)
if mibBuilder.loadTexts:
    vServerMasterPxyTblEntry.setStatus("current")
_VServerMasterPxyTblIndex_Type = Unsigned32
_VServerMasterPxyTblIndex_Object = MibTableColumn
vServerMasterPxyTblIndex = _VServerMasterPxyTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 1),
    _VServerMasterPxyTblIndex_Type()
)
vServerMasterPxyTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerMasterPxyTblIndex.setStatus("current")


class _VServerMasterPxyTblPxyMethName_Type(OctetString):
    """Custom type vServerMasterPxyTblPxyMethName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerMasterPxyTblPxyMethName_Type.__name__ = "OctetString"
_VServerMasterPxyTblPxyMethName_Object = MibTableColumn
vServerMasterPxyTblPxyMethName = _VServerMasterPxyTblPxyMethName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 2),
    _VServerMasterPxyTblPxyMethName_Type()
)
vServerMasterPxyTblPxyMethName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblPxyMethName.setStatus("current")


class _VServerMasterPxyTblStatsName_Type(OctetString):
    """Custom type vServerMasterPxyTblStatsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerMasterPxyTblStatsName_Type.__name__ = "OctetString"
_VServerMasterPxyTblStatsName_Object = MibTableColumn
vServerMasterPxyTblStatsName = _VServerMasterPxyTblStatsName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 3),
    _VServerMasterPxyTblStatsName_Type()
)
vServerMasterPxyTblStatsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblStatsName.setStatus("current")
_VServerMasterPxyTblFlags_Type = VenturiBooleanType
_VServerMasterPxyTblFlags_Object = MibTableColumn
vServerMasterPxyTblFlags = _VServerMasterPxyTblFlags_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 4),
    _VServerMasterPxyTblFlags_Type()
)
vServerMasterPxyTblFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblFlags.setStatus("current")


class _VServerMasterPxyTblPxyHost_Type(OctetString):
    """Custom type vServerMasterPxyTblPxyHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerMasterPxyTblPxyHost_Type.__name__ = "OctetString"
_VServerMasterPxyTblPxyHost_Object = MibTableColumn
vServerMasterPxyTblPxyHost = _VServerMasterPxyTblPxyHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 5),
    _VServerMasterPxyTblPxyHost_Type()
)
vServerMasterPxyTblPxyHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblPxyHost.setStatus("current")
_VServerMasterPxyTblPxyPort_Type = Integer32
_VServerMasterPxyTblPxyPort_Object = MibTableColumn
vServerMasterPxyTblPxyPort = _VServerMasterPxyTblPxyPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 6),
    _VServerMasterPxyTblPxyPort_Type()
)
vServerMasterPxyTblPxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblPxyPort.setStatus("current")


class _VServerMasterPxyTblDestHost_Type(OctetString):
    """Custom type vServerMasterPxyTblDestHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerMasterPxyTblDestHost_Type.__name__ = "OctetString"
_VServerMasterPxyTblDestHost_Object = MibTableColumn
vServerMasterPxyTblDestHost = _VServerMasterPxyTblDestHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 7),
    _VServerMasterPxyTblDestHost_Type()
)
vServerMasterPxyTblDestHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblDestHost.setStatus("current")
_VServerMasterPxyTblDestPort_Type = Integer32
_VServerMasterPxyTblDestPort_Object = MibTableColumn
vServerMasterPxyTblDestPort = _VServerMasterPxyTblDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 8),
    _VServerMasterPxyTblDestPort_Type()
)
vServerMasterPxyTblDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblDestPort.setStatus("current")
_VServerMasterPxyTblTCPKeepAlive_Type = Integer32
_VServerMasterPxyTblTCPKeepAlive_Object = MibTableColumn
vServerMasterPxyTblTCPKeepAlive = _VServerMasterPxyTblTCPKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 9),
    _VServerMasterPxyTblTCPKeepAlive_Type()
)
vServerMasterPxyTblTCPKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblTCPKeepAlive.setStatus("current")
_VServerMasterPxyTblTCPKeepAliveTime_Type = Integer32
_VServerMasterPxyTblTCPKeepAliveTime_Object = MibTableColumn
vServerMasterPxyTblTCPKeepAliveTime = _VServerMasterPxyTblTCPKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 10),
    _VServerMasterPxyTblTCPKeepAliveTime_Type()
)
vServerMasterPxyTblTCPKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblTCPKeepAliveTime.setStatus("current")
_VServerMasterPxyTblTCPKeepAliveProbes_Type = Integer32
_VServerMasterPxyTblTCPKeepAliveProbes_Object = MibTableColumn
vServerMasterPxyTblTCPKeepAliveProbes = _VServerMasterPxyTblTCPKeepAliveProbes_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 11),
    _VServerMasterPxyTblTCPKeepAliveProbes_Type()
)
vServerMasterPxyTblTCPKeepAliveProbes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblTCPKeepAliveProbes.setStatus("current")
_VServerMasterPxyTblTCPKeepAliveIntvl_Type = Integer32
_VServerMasterPxyTblTCPKeepAliveIntvl_Object = MibTableColumn
vServerMasterPxyTblTCPKeepAliveIntvl = _VServerMasterPxyTblTCPKeepAliveIntvl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 1, 1, 12),
    _VServerMasterPxyTblTCPKeepAliveIntvl_Type()
)
vServerMasterPxyTblTCPKeepAliveIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMasterPxyTblTCPKeepAliveIntvl.setStatus("current")
_VServerTransConfTbl_Object = MibTable
vServerTransConfTbl = _VServerTransConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vServerTransConfTbl.setStatus("current")
_VServerTransConfTblEntry_Object = MibTableRow
vServerTransConfTblEntry = _VServerTransConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 2, 1)
)
vServerTransConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerTransConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerTransConfTblEntry.setStatus("current")
_VServerTransConfTblIndex_Type = Unsigned32
_VServerTransConfTblIndex_Object = MibTableColumn
vServerTransConfTblIndex = _VServerTransConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 2, 1, 1),
    _VServerTransConfTblIndex_Type()
)
vServerTransConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransConfTblIndex.setStatus("current")
_VServerTransConfTblMode_Type = Unsigned32
_VServerTransConfTblMode_Object = MibTableColumn
vServerTransConfTblMode = _VServerTransConfTblMode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 2, 1, 2),
    _VServerTransConfTblMode_Type()
)
vServerTransConfTblMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfTblMode.setStatus("current")
_VServerTransConfTblType_Type = Unsigned32
_VServerTransConfTblType_Object = MibTableColumn
vServerTransConfTblType = _VServerTransConfTblType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 2, 1, 3),
    _VServerTransConfTblType_Type()
)
vServerTransConfTblType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfTblType.setStatus("deprecated")
_VServerTransConfTblAutodetect_Type = Unsigned32
_VServerTransConfTblAutodetect_Object = MibTableColumn
vServerTransConfTblAutodetect = _VServerTransConfTblAutodetect_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 2, 1, 4),
    _VServerTransConfTblAutodetect_Type()
)
vServerTransConfTblAutodetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransConfTblAutodetect.setStatus("deprecated")
_VServerTransPxyPmapTbl_Object = MibTable
vServerTransPxyPmapTbl = _VServerTransPxyPmapTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vServerTransPxyPmapTbl.setStatus("current")
_VServerTransPxyPmapTblEntry_Object = MibTableRow
vServerTransPxyPmapTblEntry = _VServerTransPxyPmapTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 3, 1)
)
vServerTransPxyPmapTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerTransPxyPmapTblIndex"),
)
if mibBuilder.loadTexts:
    vServerTransPxyPmapTblEntry.setStatus("current")
_VServerTransPxyPmapTblIndex_Type = Unsigned32
_VServerTransPxyPmapTblIndex_Object = MibTableColumn
vServerTransPxyPmapTblIndex = _VServerTransPxyPmapTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 3, 1, 1),
    _VServerTransPxyPmapTblIndex_Type()
)
vServerTransPxyPmapTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransPxyPmapTblIndex.setStatus("current")


class _VServerTransPxyPmapTblName_Type(OctetString):
    """Custom type vServerTransPxyPmapTblName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerTransPxyPmapTblName_Type.__name__ = "OctetString"
_VServerTransPxyPmapTblName_Object = MibTableColumn
vServerTransPxyPmapTblName = _VServerTransPxyPmapTblName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 3, 1, 2),
    _VServerTransPxyPmapTblName_Type()
)
vServerTransPxyPmapTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransPxyPmapTblName.setStatus("current")


class _VServerTransPxyPmapTblPorts_Type(OctetString):
    """Custom type vServerTransPxyPmapTblPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerTransPxyPmapTblPorts_Type.__name__ = "OctetString"
_VServerTransPxyPmapTblPorts_Object = MibTableColumn
vServerTransPxyPmapTblPorts = _VServerTransPxyPmapTblPorts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 3, 1, 3),
    _VServerTransPxyPmapTblPorts_Type()
)
vServerTransPxyPmapTblPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransPxyPmapTblPorts.setStatus("current")
_VServerTransPxyPmapTblReDirect_Type = Integer32
_VServerTransPxyPmapTblReDirect_Object = MibTableColumn
vServerTransPxyPmapTblReDirect = _VServerTransPxyPmapTblReDirect_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 3, 1, 4),
    _VServerTransPxyPmapTblReDirect_Type()
)
vServerTransPxyPmapTblReDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransPxyPmapTblReDirect.setStatus("current")


class _VServerTransPxyPmapTblAppMethName_Type(OctetString):
    """Custom type vServerTransPxyPmapTblAppMethName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerTransPxyPmapTblAppMethName_Type.__name__ = "OctetString"
_VServerTransPxyPmapTblAppMethName_Object = MibTableColumn
vServerTransPxyPmapTblAppMethName = _VServerTransPxyPmapTblAppMethName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 3, 1, 5),
    _VServerTransPxyPmapTblAppMethName_Type()
)
vServerTransPxyPmapTblAppMethName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransPxyPmapTblAppMethName.setStatus("current")
_VServerTransPxyPmapTblSPort_Type = Integer32
_VServerTransPxyPmapTblSPort_Object = MibTableColumn
vServerTransPxyPmapTblSPort = _VServerTransPxyPmapTblSPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 3, 1, 6),
    _VServerTransPxyPmapTblSPort_Type()
)
vServerTransPxyPmapTblSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransPxyPmapTblSPort.setStatus("current")
_VServerDefTransPxyPmapTbl_Object = MibTable
vServerDefTransPxyPmapTbl = _VServerDefTransPxyPmapTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    vServerDefTransPxyPmapTbl.setStatus("current")
_VServerDefTransPxyPmapTblEntry_Object = MibTableRow
vServerDefTransPxyPmapTblEntry = _VServerDefTransPxyPmapTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 4, 1)
)
vServerDefTransPxyPmapTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerDefTransPxyPmapTblIndex"),
)
if mibBuilder.loadTexts:
    vServerDefTransPxyPmapTblEntry.setStatus("current")
_VServerDefTransPxyPmapTblIndex_Type = Unsigned32
_VServerDefTransPxyPmapTblIndex_Object = MibTableColumn
vServerDefTransPxyPmapTblIndex = _VServerDefTransPxyPmapTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 4, 1, 1),
    _VServerDefTransPxyPmapTblIndex_Type()
)
vServerDefTransPxyPmapTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDefTransPxyPmapTblIndex.setStatus("current")


class _VServerDefTransPxyPmapTblName_Type(OctetString):
    """Custom type vServerDefTransPxyPmapTblName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerDefTransPxyPmapTblName_Type.__name__ = "OctetString"
_VServerDefTransPxyPmapTblName_Object = MibTableColumn
vServerDefTransPxyPmapTblName = _VServerDefTransPxyPmapTblName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 4, 1, 2),
    _VServerDefTransPxyPmapTblName_Type()
)
vServerDefTransPxyPmapTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerDefTransPxyPmapTblName.setStatus("current")


class _VServerDefTransPxyPmapTblPorts_Type(OctetString):
    """Custom type vServerDefTransPxyPmapTblPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerDefTransPxyPmapTblPorts_Type.__name__ = "OctetString"
_VServerDefTransPxyPmapTblPorts_Object = MibTableColumn
vServerDefTransPxyPmapTblPorts = _VServerDefTransPxyPmapTblPorts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 4, 1, 3),
    _VServerDefTransPxyPmapTblPorts_Type()
)
vServerDefTransPxyPmapTblPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerDefTransPxyPmapTblPorts.setStatus("current")
_VServerDefTransPxyPmapTblReDirect_Type = Integer32
_VServerDefTransPxyPmapTblReDirect_Object = MibTableColumn
vServerDefTransPxyPmapTblReDirect = _VServerDefTransPxyPmapTblReDirect_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 4, 1, 4),
    _VServerDefTransPxyPmapTblReDirect_Type()
)
vServerDefTransPxyPmapTblReDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerDefTransPxyPmapTblReDirect.setStatus("current")


class _VServerDefTransPxyPmapTblAppMethName_Type(OctetString):
    """Custom type vServerDefTransPxyPmapTblAppMethName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerDefTransPxyPmapTblAppMethName_Type.__name__ = "OctetString"
_VServerDefTransPxyPmapTblAppMethName_Object = MibTableColumn
vServerDefTransPxyPmapTblAppMethName = _VServerDefTransPxyPmapTblAppMethName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 4, 1, 5),
    _VServerDefTransPxyPmapTblAppMethName_Type()
)
vServerDefTransPxyPmapTblAppMethName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerDefTransPxyPmapTblAppMethName.setStatus("current")
_VServerDefTransPxyPmapTblSPort_Type = Integer32
_VServerDefTransPxyPmapTblSPort_Object = MibTableColumn
vServerDefTransPxyPmapTblSPort = _VServerDefTransPxyPmapTblSPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 1, 2, 4, 1, 6),
    _VServerDefTransPxyPmapTblSPort_Type()
)
vServerDefTransPxyPmapTblSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerDefTransPxyPmapTblSPort.setStatus("current")
_VServerConfAppSvcsCompression_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsCompression = _VServerConfAppSvcsCompression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2)
)
_VServerConfAppSvcsCompressionScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsCompressionScalars = _VServerConfAppSvcsCompressionScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 1)
)
_VServerConfAppSvcsCompressionTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsCompressionTbls = _VServerConfAppSvcsCompressionTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2)
)
_VServerSvrCompCfgTbl_Object = MibTable
vServerSvrCompCfgTbl = _VServerSvrCompCfgTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vServerSvrCompCfgTbl.setStatus("current")
_VServerSvrCompCfgTblEntry_Object = MibTableRow
vServerSvrCompCfgTblEntry = _VServerSvrCompCfgTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1)
)
vServerSvrCompCfgTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerSvrCompCfgTblIndex"),
)
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblEntry.setStatus("current")
_VServerSvrCompCfgTblIndex_Type = Unsigned32
_VServerSvrCompCfgTblIndex_Object = MibTableColumn
vServerSvrCompCfgTblIndex = _VServerSvrCompCfgTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 1),
    _VServerSvrCompCfgTblIndex_Type()
)
vServerSvrCompCfgTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblIndex.setStatus("current")
_VServerSvrCompCfgTblGif2Png_Type = Unsigned32
_VServerSvrCompCfgTblGif2Png_Object = MibTableColumn
vServerSvrCompCfgTblGif2Png = _VServerSvrCompCfgTblGif2Png_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 2),
    _VServerSvrCompCfgTblGif2Png_Type()
)
vServerSvrCompCfgTblGif2Png.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblGif2Png.setStatus("current")
_VServerSvrCompCfgTblPng2Png_Type = Unsigned32
_VServerSvrCompCfgTblPng2Png_Object = MibTableColumn
vServerSvrCompCfgTblPng2Png = _VServerSvrCompCfgTblPng2Png_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 3),
    _VServerSvrCompCfgTblPng2Png_Type()
)
vServerSvrCompCfgTblPng2Png.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblPng2Png.setStatus("current")
_VServerSvrCompCfgTblPPM_Type = Unsigned32
_VServerSvrCompCfgTblPPM_Object = MibTableColumn
vServerSvrCompCfgTblPPM = _VServerSvrCompCfgTblPPM_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 4),
    _VServerSvrCompCfgTblPPM_Type()
)
vServerSvrCompCfgTblPPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblPPM.setStatus("current")
_VServerSvrCompCfgTblJ2k_Type = Unsigned32
_VServerSvrCompCfgTblJ2k_Object = MibTableColumn
vServerSvrCompCfgTblJ2k = _VServerSvrCompCfgTblJ2k_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 5),
    _VServerSvrCompCfgTblJ2k_Type()
)
vServerSvrCompCfgTblJ2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblJ2k.setStatus("current")
_VServerSvrCompCfgTblAZ_Type = Unsigned32
_VServerSvrCompCfgTblAZ_Object = MibTableColumn
vServerSvrCompCfgTblAZ = _VServerSvrCompCfgTblAZ_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 6),
    _VServerSvrCompCfgTblAZ_Type()
)
vServerSvrCompCfgTblAZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblAZ.setStatus("current")
_VServerSvrCompCfgTblPrgJpeg_Type = Unsigned32
_VServerSvrCompCfgTblPrgJpeg_Object = MibTableColumn
vServerSvrCompCfgTblPrgJpeg = _VServerSvrCompCfgTblPrgJpeg_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 7),
    _VServerSvrCompCfgTblPrgJpeg_Type()
)
vServerSvrCompCfgTblPrgJpeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblPrgJpeg.setStatus("current")
_VServerSvrCompCfgTblReqCompContentCS_Type = Unsigned32
_VServerSvrCompCfgTblReqCompContentCS_Object = MibTableColumn
vServerSvrCompCfgTblReqCompContentCS = _VServerSvrCompCfgTblReqCompContentCS_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 8),
    _VServerSvrCompCfgTblReqCompContentCS_Type()
)
vServerSvrCompCfgTblReqCompContentCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblReqCompContentCS.setStatus("current")
_VServerSvrCompCfgTblReqCompContentCless_Type = Unsigned32
_VServerSvrCompCfgTblReqCompContentCless_Object = MibTableColumn
vServerSvrCompCfgTblReqCompContentCless = _VServerSvrCompCfgTblReqCompContentCless_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 9),
    _VServerSvrCompCfgTblReqCompContentCless_Type()
)
vServerSvrCompCfgTblReqCompContentCless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblReqCompContentCless.setStatus("current")
_VServerSvrCompCfgTblJPegArith_Type = Unsigned32
_VServerSvrCompCfgTblJPegArith_Object = MibTableColumn
vServerSvrCompCfgTblJPegArith = _VServerSvrCompCfgTblJPegArith_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 10),
    _VServerSvrCompCfgTblJPegArith_Type()
)
vServerSvrCompCfgTblJPegArith.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblJPegArith.setStatus("current")
_VServerSvrCompCfgTblLossyHtml_Type = Unsigned32
_VServerSvrCompCfgTblLossyHtml_Object = MibTableColumn
vServerSvrCompCfgTblLossyHtml = _VServerSvrCompCfgTblLossyHtml_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 1, 1, 11),
    _VServerSvrCompCfgTblLossyHtml_Type()
)
vServerSvrCompCfgTblLossyHtml.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSvrCompCfgTblLossyHtml.setStatus("current")
_VServerCompSvrTbl_Object = MibTable
vServerCompSvrTbl = _VServerCompSvrTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    vServerCompSvrTbl.setStatus("current")
_VServerCompSvrTblEntry_Object = MibTableRow
vServerCompSvrTblEntry = _VServerCompSvrTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1)
)
vServerCompSvrTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerCompSvrTblIndex"),
)
if mibBuilder.loadTexts:
    vServerCompSvrTblEntry.setStatus("current")
_VServerCompSvrTblIndex_Type = Unsigned32
_VServerCompSvrTblIndex_Object = MibTableColumn
vServerCompSvrTblIndex = _VServerCompSvrTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 1),
    _VServerCompSvrTblIndex_Type()
)
vServerCompSvrTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCompSvrTblIndex.setStatus("current")
_VServerCompSvrTblJPegSize_Type = Unsigned32
_VServerCompSvrTblJPegSize_Object = MibTableColumn
vServerCompSvrTblJPegSize = _VServerCompSvrTblJPegSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 2),
    _VServerCompSvrTblJPegSize_Type()
)
vServerCompSvrTblJPegSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblJPegSize.setStatus("current")
_VServerCompSvrTblJPegMinSize_Type = Unsigned32
_VServerCompSvrTblJPegMinSize_Object = MibTableColumn
vServerCompSvrTblJPegMinSize = _VServerCompSvrTblJPegMinSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 3),
    _VServerCompSvrTblJPegMinSize_Type()
)
vServerCompSvrTblJPegMinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblJPegMinSize.setStatus("current")
_VServerCompSvrTblJPegMethod_Type = Unsigned32
_VServerCompSvrTblJPegMethod_Object = MibTableColumn
vServerCompSvrTblJPegMethod = _VServerCompSvrTblJPegMethod_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 4),
    _VServerCompSvrTblJPegMethod_Type()
)
vServerCompSvrTblJPegMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblJPegMethod.setStatus("current")
_VServerCompSvrTblMaxChunk_Type = Unsigned32
_VServerCompSvrTblMaxChunk_Object = MibTableColumn
vServerCompSvrTblMaxChunk = _VServerCompSvrTblMaxChunk_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 5),
    _VServerCompSvrTblMaxChunk_Type()
)
vServerCompSvrTblMaxChunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblMaxChunk.setStatus("current")
_VServerCompSvrTblGzipSize_Type = Unsigned32
_VServerCompSvrTblGzipSize_Object = MibTableColumn
vServerCompSvrTblGzipSize = _VServerCompSvrTblGzipSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 6),
    _VServerCompSvrTblGzipSize_Type()
)
vServerCompSvrTblGzipSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblGzipSize.setStatus("current")
_VServerCompSvrTblJ2kSize_Type = Unsigned32
_VServerCompSvrTblJ2kSize_Object = MibTableColumn
vServerCompSvrTblJ2kSize = _VServerCompSvrTblJ2kSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 7),
    _VServerCompSvrTblJ2kSize_Type()
)
vServerCompSvrTblJ2kSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblJ2kSize.setStatus("current")
_VServerCompSvrTblJ2kMinSize_Type = Unsigned32
_VServerCompSvrTblJ2kMinSize_Object = MibTableColumn
vServerCompSvrTblJ2kMinSize = _VServerCompSvrTblJ2kMinSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 8),
    _VServerCompSvrTblJ2kMinSize_Type()
)
vServerCompSvrTblJ2kMinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblJ2kMinSize.setStatus("current")
_VServerCompSvrTblJpgMaxPix4J2k_Type = Unsigned32
_VServerCompSvrTblJpgMaxPix4J2k_Object = MibTableColumn
vServerCompSvrTblJpgMaxPix4J2k = _VServerCompSvrTblJpgMaxPix4J2k_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 9),
    _VServerCompSvrTblJpgMaxPix4J2k_Type()
)
vServerCompSvrTblJpgMaxPix4J2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblJpgMaxPix4J2k.setStatus("current")
_VServerCompSvrTblJpgMaxPix4Opt_Type = Unsigned32
_VServerCompSvrTblJpgMaxPix4Opt_Object = MibTableColumn
vServerCompSvrTblJpgMaxPix4Opt = _VServerCompSvrTblJpgMaxPix4Opt_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 10),
    _VServerCompSvrTblJpgMaxPix4Opt_Type()
)
vServerCompSvrTblJpgMaxPix4Opt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblJpgMaxPix4Opt.setStatus("current")
_VServerCompSvrTblAzMaxSize_Type = Unsigned32
_VServerCompSvrTblAzMaxSize_Object = MibTableColumn
vServerCompSvrTblAzMaxSize = _VServerCompSvrTblAzMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 11),
    _VServerCompSvrTblAzMaxSize_Type()
)
vServerCompSvrTblAzMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblAzMaxSize.setStatus("current")
_VServerCompSvrTblJpegMinBpp_Type = Unsigned32
_VServerCompSvrTblJpegMinBpp_Object = MibTableColumn
vServerCompSvrTblJpegMinBpp = _VServerCompSvrTblJpegMinBpp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 3, 1, 12),
    _VServerCompSvrTblJpegMinBpp_Type()
)
vServerCompSvrTblJpegMinBpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCompSvrTblJpegMinBpp.setStatus("current")
_VServerHttpConfTbl_Object = MibTable
vServerHttpConfTbl = _VServerHttpConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    vServerHttpConfTbl.setStatus("current")
_VServerHttpConfTblEntry_Object = MibTableRow
vServerHttpConfTblEntry = _VServerHttpConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1)
)
vServerHttpConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerHttpConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerHttpConfTblEntry.setStatus("current")
_VServerHttpConfTblIndex_Type = Unsigned32
_VServerHttpConfTblIndex_Object = MibTableColumn
vServerHttpConfTblIndex = _VServerHttpConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 1),
    _VServerHttpConfTblIndex_Type()
)
vServerHttpConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerHttpConfTblIndex.setStatus("current")
_VServerHttpConfTblPrefetch_Type = Unsigned32
_VServerHttpConfTblPrefetch_Object = MibTableColumn
vServerHttpConfTblPrefetch = _VServerHttpConfTblPrefetch_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 2),
    _VServerHttpConfTblPrefetch_Type()
)
vServerHttpConfTblPrefetch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblPrefetch.setStatus("current")
_VServerHttpConfTblIdentify_Type = Unsigned32
_VServerHttpConfTblIdentify_Object = MibTableColumn
vServerHttpConfTblIdentify = _VServerHttpConfTblIdentify_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 3),
    _VServerHttpConfTblIdentify_Type()
)
vServerHttpConfTblIdentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblIdentify.setStatus("current")
_VServerHttpConfTblXForwardFor_Type = Unsigned32
_VServerHttpConfTblXForwardFor_Object = MibTableColumn
vServerHttpConfTblXForwardFor = _VServerHttpConfTblXForwardFor_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 4),
    _VServerHttpConfTblXForwardFor_Type()
)
vServerHttpConfTblXForwardFor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblXForwardFor.setStatus("current")
_VServerHttpConfTblCompObjEnabled_Type = VenturiBooleanType
_VServerHttpConfTblCompObjEnabled_Object = MibTableColumn
vServerHttpConfTblCompObjEnabled = _VServerHttpConfTblCompObjEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 5),
    _VServerHttpConfTblCompObjEnabled_Type()
)
vServerHttpConfTblCompObjEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblCompObjEnabled.setStatus("current")
_VServerHttpConfTblSSCLCompFlag_Type = VenturiBooleanType
_VServerHttpConfTblSSCLCompFlag_Object = MibTableColumn
vServerHttpConfTblSSCLCompFlag = _VServerHttpConfTblSSCLCompFlag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 6),
    _VServerHttpConfTblSSCLCompFlag_Type()
)
vServerHttpConfTblSSCLCompFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblSSCLCompFlag.setStatus("current")
_VServerHttpConfTblSSCompFlag_Type = VenturiBooleanType
_VServerHttpConfTblSSCompFlag_Object = MibTableColumn
vServerHttpConfTblSSCompFlag = _VServerHttpConfTblSSCompFlag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 7),
    _VServerHttpConfTblSSCompFlag_Type()
)
vServerHttpConfTblSSCompFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblSSCompFlag.setStatus("current")
_VServerHttpConfTblKeepAlive_Type = VenturiBooleanType
_VServerHttpConfTblKeepAlive_Object = MibTableColumn
vServerHttpConfTblKeepAlive = _VServerHttpConfTblKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 8),
    _VServerHttpConfTblKeepAlive_Type()
)
vServerHttpConfTblKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblKeepAlive.setStatus("current")
_VServerHttpConfTblKATimeOut_Type = Unsigned32
_VServerHttpConfTblKATimeOut_Object = MibTableColumn
vServerHttpConfTblKATimeOut = _VServerHttpConfTblKATimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 9),
    _VServerHttpConfTblKATimeOut_Type()
)
vServerHttpConfTblKATimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblKATimeOut.setStatus("current")
_VServerHttpConfTblProxyOverride_Type = Unsigned32
_VServerHttpConfTblProxyOverride_Object = MibTableColumn
vServerHttpConfTblProxyOverride = _VServerHttpConfTblProxyOverride_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 10),
    _VServerHttpConfTblProxyOverride_Type()
)
vServerHttpConfTblProxyOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblProxyOverride.setStatus("current")
_VServerHttpConfTblSSStdIComp_Type = Unsigned32
_VServerHttpConfTblSSStdIComp_Object = MibTableColumn
vServerHttpConfTblSSStdIComp = _VServerHttpConfTblSSStdIComp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 4, 1, 11),
    _VServerHttpConfTblSSStdIComp_Type()
)
vServerHttpConfTblSSStdIComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpConfTblSSStdIComp.setStatus("current")
_VServerSIEConfTbl_Object = MibTable
vServerSIEConfTbl = _VServerSIEConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    vServerSIEConfTbl.setStatus("current")
_VServerSIEConfTblEntry_Object = MibTableRow
vServerSIEConfTblEntry = _VServerSIEConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 5, 1)
)
vServerSIEConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerSIEConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerSIEConfTblEntry.setStatus("current")
_VServerSIEConfTblIndex_Type = Unsigned32
_VServerSIEConfTblIndex_Object = MibTableColumn
vServerSIEConfTblIndex = _VServerSIEConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 5, 1, 1),
    _VServerSIEConfTblIndex_Type()
)
vServerSIEConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSIEConfTblIndex.setStatus("current")
_VServerSIEConfTblEnabled_Type = VenturiBooleanType
_VServerSIEConfTblEnabled_Object = MibTableColumn
vServerSIEConfTblEnabled = _VServerSIEConfTblEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 5, 1, 2),
    _VServerSIEConfTblEnabled_Type()
)
vServerSIEConfTblEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSIEConfTblEnabled.setStatus("current")
_VServerSIEConfTblHttpEnabled_Type = VenturiBooleanType
_VServerSIEConfTblHttpEnabled_Object = MibTableColumn
vServerSIEConfTblHttpEnabled = _VServerSIEConfTblHttpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 5, 1, 3),
    _VServerSIEConfTblHttpEnabled_Type()
)
vServerSIEConfTblHttpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSIEConfTblHttpEnabled.setStatus("current")
_VServerSIEConfTblFtpEnabled_Type = VenturiBooleanType
_VServerSIEConfTblFtpEnabled_Object = MibTableColumn
vServerSIEConfTblFtpEnabled = _VServerSIEConfTblFtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 5, 1, 4),
    _VServerSIEConfTblFtpEnabled_Type()
)
vServerSIEConfTblFtpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSIEConfTblFtpEnabled.setStatus("current")
_VServerSIEConfTblEmailEnabled_Type = VenturiBooleanType
_VServerSIEConfTblEmailEnabled_Object = MibTableColumn
vServerSIEConfTblEmailEnabled = _VServerSIEConfTblEmailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 5, 1, 5),
    _VServerSIEConfTblEmailEnabled_Type()
)
vServerSIEConfTblEmailEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSIEConfTblEmailEnabled.setStatus("current")
_VServerSIEConfTblStatsEnabled_Type = VenturiBooleanType
_VServerSIEConfTblStatsEnabled_Object = MibTableColumn
vServerSIEConfTblStatsEnabled = _VServerSIEConfTblStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 5, 1, 6),
    _VServerSIEConfTblStatsEnabled_Type()
)
vServerSIEConfTblStatsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSIEConfTblStatsEnabled.setStatus("current")
_VServerImageCompTbl_Object = MibTable
vServerImageCompTbl = _VServerImageCompTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    vServerImageCompTbl.setStatus("current")
_VServerImageCompTblEntry_Object = MibTableRow
vServerImageCompTblEntry = _VServerImageCompTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1)
)
vServerImageCompTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerImageCompTblIndex"),
)
if mibBuilder.loadTexts:
    vServerImageCompTblEntry.setStatus("current")
_VServerImageCompTblIndex_Type = Unsigned32
_VServerImageCompTblIndex_Object = MibTableColumn
vServerImageCompTblIndex = _VServerImageCompTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 1),
    _VServerImageCompTblIndex_Type()
)
vServerImageCompTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerImageCompTblIndex.setStatus("current")


class _VServerImageCompTblName_Type(OctetString):
    """Custom type vServerImageCompTblName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VServerImageCompTblName_Type.__name__ = "OctetString"
_VServerImageCompTblName_Object = MibTableColumn
vServerImageCompTblName = _VServerImageCompTblName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 2),
    _VServerImageCompTblName_Type()
)
vServerImageCompTblName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerImageCompTblName.setStatus("current")
_VServerImageCompTblId_Type = Unsigned32
_VServerImageCompTblId_Object = MibTableColumn
vServerImageCompTblId = _VServerImageCompTblId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 3),
    _VServerImageCompTblId_Type()
)
vServerImageCompTblId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerImageCompTblId.setStatus("current")


class _VServerImageCompTblType0_Type(OctetString):
    """Custom type vServerImageCompTblType0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VServerImageCompTblType0_Type.__name__ = "OctetString"
_VServerImageCompTblType0_Object = MibTableColumn
vServerImageCompTblType0 = _VServerImageCompTblType0_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 4),
    _VServerImageCompTblType0_Type()
)
vServerImageCompTblType0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblType0.setStatus("current")
_VServerImageCompTblLevel0_Type = Unsigned32
_VServerImageCompTblLevel0_Object = MibTableColumn
vServerImageCompTblLevel0 = _VServerImageCompTblLevel0_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 5),
    _VServerImageCompTblLevel0_Type()
)
vServerImageCompTblLevel0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblLevel0.setStatus("current")


class _VServerImageCompTblType1_Type(OctetString):
    """Custom type vServerImageCompTblType1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VServerImageCompTblType1_Type.__name__ = "OctetString"
_VServerImageCompTblType1_Object = MibTableColumn
vServerImageCompTblType1 = _VServerImageCompTblType1_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 6),
    _VServerImageCompTblType1_Type()
)
vServerImageCompTblType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblType1.setStatus("current")
_VServerImageCompTblLevel1_Type = Unsigned32
_VServerImageCompTblLevel1_Object = MibTableColumn
vServerImageCompTblLevel1 = _VServerImageCompTblLevel1_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 7),
    _VServerImageCompTblLevel1_Type()
)
vServerImageCompTblLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblLevel1.setStatus("current")


class _VServerImageCompTblType2_Type(OctetString):
    """Custom type vServerImageCompTblType2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VServerImageCompTblType2_Type.__name__ = "OctetString"
_VServerImageCompTblType2_Object = MibTableColumn
vServerImageCompTblType2 = _VServerImageCompTblType2_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 8),
    _VServerImageCompTblType2_Type()
)
vServerImageCompTblType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblType2.setStatus("current")
_VServerImageCompTblLevel2_Type = Unsigned32
_VServerImageCompTblLevel2_Object = MibTableColumn
vServerImageCompTblLevel2 = _VServerImageCompTblLevel2_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 9),
    _VServerImageCompTblLevel2_Type()
)
vServerImageCompTblLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblLevel2.setStatus("current")


class _VServerImageCompTblType3_Type(OctetString):
    """Custom type vServerImageCompTblType3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VServerImageCompTblType3_Type.__name__ = "OctetString"
_VServerImageCompTblType3_Object = MibTableColumn
vServerImageCompTblType3 = _VServerImageCompTblType3_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 10),
    _VServerImageCompTblType3_Type()
)
vServerImageCompTblType3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblType3.setStatus("current")
_VServerImageCompTblLevel3_Type = Unsigned32
_VServerImageCompTblLevel3_Object = MibTableColumn
vServerImageCompTblLevel3 = _VServerImageCompTblLevel3_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 11),
    _VServerImageCompTblLevel3_Type()
)
vServerImageCompTblLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblLevel3.setStatus("current")


class _VServerImageCompTblType4_Type(OctetString):
    """Custom type vServerImageCompTblType4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VServerImageCompTblType4_Type.__name__ = "OctetString"
_VServerImageCompTblType4_Object = MibTableColumn
vServerImageCompTblType4 = _VServerImageCompTblType4_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 12),
    _VServerImageCompTblType4_Type()
)
vServerImageCompTblType4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblType4.setStatus("current")
_VServerImageCompTblLevel4_Type = Unsigned32
_VServerImageCompTblLevel4_Object = MibTableColumn
vServerImageCompTblLevel4 = _VServerImageCompTblLevel4_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 6, 1, 13),
    _VServerImageCompTblLevel4_Type()
)
vServerImageCompTblLevel4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerImageCompTblLevel4.setStatus("current")
_VServerHttpHdrAccessConfigTbl_Object = MibTable
vServerHttpHdrAccessConfigTbl = _VServerHttpHdrAccessConfigTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 7)
)
if mibBuilder.loadTexts:
    vServerHttpHdrAccessConfigTbl.setStatus("current")
_VServerHttpHdrAccessTblEntry_Object = MibTableRow
vServerHttpHdrAccessTblEntry = _VServerHttpHdrAccessTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 7, 1)
)
vServerHttpHdrAccessTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerHttpHdrAccessTblIndex"),
)
if mibBuilder.loadTexts:
    vServerHttpHdrAccessTblEntry.setStatus("current")
_VServerHttpHdrAccessTblIndex_Type = Unsigned32
_VServerHttpHdrAccessTblIndex_Object = MibTableColumn
vServerHttpHdrAccessTblIndex = _VServerHttpHdrAccessTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 7, 1, 1),
    _VServerHttpHdrAccessTblIndex_Type()
)
vServerHttpHdrAccessTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerHttpHdrAccessTblIndex.setStatus("current")


class _VServerHttpHdrAccessTblHdrFieldName_Type(OctetString):
    """Custom type vServerHttpHdrAccessTblHdrFieldName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VServerHttpHdrAccessTblHdrFieldName_Type.__name__ = "OctetString"
_VServerHttpHdrAccessTblHdrFieldName_Object = MibTableColumn
vServerHttpHdrAccessTblHdrFieldName = _VServerHttpHdrAccessTblHdrFieldName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 7, 1, 2),
    _VServerHttpHdrAccessTblHdrFieldName_Type()
)
vServerHttpHdrAccessTblHdrFieldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerHttpHdrAccessTblHdrFieldName.setStatus("current")


class _VServerHttpHdrAccessTblAllowDeny_Type(OctetString):
    """Custom type vServerHttpHdrAccessTblAllowDeny based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VServerHttpHdrAccessTblAllowDeny_Type.__name__ = "OctetString"
_VServerHttpHdrAccessTblAllowDeny_Object = MibTableColumn
vServerHttpHdrAccessTblAllowDeny = _VServerHttpHdrAccessTblAllowDeny_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 2, 2, 7, 1, 3),
    _VServerHttpHdrAccessTblAllowDeny_Type()
)
vServerHttpHdrAccessTblAllowDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpHdrAccessTblAllowDeny.setStatus("current")
_VServerConfAppSvcsClient_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsClient = _VServerConfAppSvcsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3)
)
_VServerConfAppSvcsClientScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsClientScalars = _VServerConfAppSvcsClientScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 1)
)
_VServerClientlessEnabled_Type = VenturiBooleanType
_VServerClientlessEnabled_Object = MibScalar
vServerClientlessEnabled = _VServerClientlessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 1, 1),
    _VServerClientlessEnabled_Type()
)
vServerClientlessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientlessEnabled.setStatus("current")
_VServerClientlessTransInterceptEnable_Type = VenturiBooleanType
_VServerClientlessTransInterceptEnable_Object = MibScalar
vServerClientlessTransInterceptEnable = _VServerClientlessTransInterceptEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 1, 2),
    _VServerClientlessTransInterceptEnable_Type()
)
vServerClientlessTransInterceptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientlessTransInterceptEnable.setStatus("current")
_VServerConfAppSvcsClientTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsClientTbls = _VServerConfAppSvcsClientTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2)
)
_VServerAppClientUpdateTbl_Object = MibTable
vServerAppClientUpdateTbl = _VServerAppClientUpdateTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vServerAppClientUpdateTbl.setStatus("current")
_VServerAppClientUpdateTblEntry_Object = MibTableRow
vServerAppClientUpdateTblEntry = _VServerAppClientUpdateTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 1, 1)
)
vServerAppClientUpdateTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerAppClientUpdateTblIndex"),
)
if mibBuilder.loadTexts:
    vServerAppClientUpdateTblEntry.setStatus("current")
_VServerAppClientUpdateTblIndex_Type = Unsigned32
_VServerAppClientUpdateTblIndex_Object = MibTableColumn
vServerAppClientUpdateTblIndex = _VServerAppClientUpdateTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 1, 1, 1),
    _VServerAppClientUpdateTblIndex_Type()
)
vServerAppClientUpdateTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAppClientUpdateTblIndex.setStatus("current")


class _VServerAppClientUpdateTblLocalURL_Type(OctetString):
    """Custom type vServerAppClientUpdateTblLocalURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerAppClientUpdateTblLocalURL_Type.__name__ = "OctetString"
_VServerAppClientUpdateTblLocalURL_Object = MibTableColumn
vServerAppClientUpdateTblLocalURL = _VServerAppClientUpdateTblLocalURL_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 1, 1, 2),
    _VServerAppClientUpdateTblLocalURL_Type()
)
vServerAppClientUpdateTblLocalURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAppClientUpdateTblLocalURL.setStatus("current")
_VServerAppClientUpdateTblPort_Type = Integer32
_VServerAppClientUpdateTblPort_Object = MibTableColumn
vServerAppClientUpdateTblPort = _VServerAppClientUpdateTblPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 1, 1, 3),
    _VServerAppClientUpdateTblPort_Type()
)
vServerAppClientUpdateTblPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAppClientUpdateTblPort.setStatus("current")
_VServerAppClientlessConfTbl_Object = MibTable
vServerAppClientlessConfTbl = _VServerAppClientlessConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    vServerAppClientlessConfTbl.setStatus("current")
_VServerAppClientlessConfTblEntry_Object = MibTableRow
vServerAppClientlessConfTblEntry = _VServerAppClientlessConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 2, 1)
)
vServerAppClientlessConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerAppClientlessConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerAppClientlessConfTblEntry.setStatus("current")
_VServerAppClientlessConfTblIndex_Type = Unsigned32
_VServerAppClientlessConfTblIndex_Object = MibTableColumn
vServerAppClientlessConfTblIndex = _VServerAppClientlessConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 2, 1, 1),
    _VServerAppClientlessConfTblIndex_Type()
)
vServerAppClientlessConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAppClientlessConfTblIndex.setStatus("current")
_VServerAppClientlessConfTblEnable_Type = VenturiBooleanType
_VServerAppClientlessConfTblEnable_Object = MibTableColumn
vServerAppClientlessConfTblEnable = _VServerAppClientlessConfTblEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 2, 1, 2),
    _VServerAppClientlessConfTblEnable_Type()
)
vServerAppClientlessConfTblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAppClientlessConfTblEnable.setStatus("current")


class _VServerAppClientlessConfTblURL_Type(OctetString):
    """Custom type vServerAppClientlessConfTblURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerAppClientlessConfTblURL_Type.__name__ = "OctetString"
_VServerAppClientlessConfTblURL_Object = MibTableColumn
vServerAppClientlessConfTblURL = _VServerAppClientlessConfTblURL_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 2, 1, 3),
    _VServerAppClientlessConfTblURL_Type()
)
vServerAppClientlessConfTblURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAppClientlessConfTblURL.setStatus("current")
_VServerAppClientlessConfTblIdle_Type = Unsigned32
_VServerAppClientlessConfTblIdle_Object = MibTableColumn
vServerAppClientlessConfTblIdle = _VServerAppClientlessConfTblIdle_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 2, 1, 4),
    _VServerAppClientlessConfTblIdle_Type()
)
vServerAppClientlessConfTblIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAppClientlessConfTblIdle.setStatus("current")
_VServerClientAutoUpgGblTbl_Object = MibTable
vServerClientAutoUpgGblTbl = _VServerClientAutoUpgGblTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    vServerClientAutoUpgGblTbl.setStatus("current")
_VServerClientAutoUpgGblTblEntry_Object = MibTableRow
vServerClientAutoUpgGblTblEntry = _VServerClientAutoUpgGblTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 3, 1)
)
vServerClientAutoUpgGblTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerClientAutoUpgGblTblIndex"),
)
if mibBuilder.loadTexts:
    vServerClientAutoUpgGblTblEntry.setStatus("current")
_VServerClientAutoUpgGblTblIndex_Type = Unsigned32
_VServerClientAutoUpgGblTblIndex_Object = MibTableColumn
vServerClientAutoUpgGblTblIndex = _VServerClientAutoUpgGblTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 3, 1, 1),
    _VServerClientAutoUpgGblTblIndex_Type()
)
vServerClientAutoUpgGblTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientAutoUpgGblTblIndex.setStatus("current")
_VServerClientAutoUpgGblTblEnable_Type = VenturiBooleanType
_VServerClientAutoUpgGblTblEnable_Object = MibTableColumn
vServerClientAutoUpgGblTblEnable = _VServerClientAutoUpgGblTblEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 3, 1, 2),
    _VServerClientAutoUpgGblTblEnable_Type()
)
vServerClientAutoUpgGblTblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgGblTblEnable.setStatus("current")
_VServerClientAutoUpgGblTblUpgTimeInterval_Type = Unsigned32
_VServerClientAutoUpgGblTblUpgTimeInterval_Object = MibTableColumn
vServerClientAutoUpgGblTblUpgTimeInterval = _VServerClientAutoUpgGblTblUpgTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 3, 1, 3),
    _VServerClientAutoUpgGblTblUpgTimeInterval_Type()
)
vServerClientAutoUpgGblTblUpgTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgGblTblUpgTimeInterval.setStatus("current")
_VServerClientAutoUpgGblTblMaxClientVerStored_Type = Unsigned32
_VServerClientAutoUpgGblTblMaxClientVerStored_Object = MibTableColumn
vServerClientAutoUpgGblTblMaxClientVerStored = _VServerClientAutoUpgGblTblMaxClientVerStored_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 3, 1, 4),
    _VServerClientAutoUpgGblTblMaxClientVerStored_Type()
)
vServerClientAutoUpgGblTblMaxClientVerStored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgGblTblMaxClientVerStored.setStatus("current")
_VServerClientAutoUpgConfTgtTbl_Object = MibTable
vServerClientAutoUpgConfTgtTbl = _VServerClientAutoUpgConfTgtTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4)
)
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTbl.setStatus("current")
_VServerClientAutoUpgConfTgtTblEntry_Object = MibTableRow
vServerClientAutoUpgConfTgtTblEntry = _VServerClientAutoUpgConfTgtTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1)
)
vServerClientAutoUpgConfTgtTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerClientAutoUpgConfTgtTblIndex"),
)
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblEntry.setStatus("current")
_VServerClientAutoUpgConfTgtTblIndex_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblIndex_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblIndex = _VServerClientAutoUpgConfTgtTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 1),
    _VServerClientAutoUpgConfTgtTblIndex_Type()
)
vServerClientAutoUpgConfTgtTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblIndex.setStatus("current")
_VServerClientAutoUpgConfTgtTblHourPerDay_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblHourPerDay_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblHourPerDay = _VServerClientAutoUpgConfTgtTblHourPerDay_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 2),
    _VServerClientAutoUpgConfTgtTblHourPerDay_Type()
)
vServerClientAutoUpgConfTgtTblHourPerDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblHourPerDay.setStatus("current")
_VServerClientAutoUpgConfTgtTblSunday_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblSunday_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblSunday = _VServerClientAutoUpgConfTgtTblSunday_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 3),
    _VServerClientAutoUpgConfTgtTblSunday_Type()
)
vServerClientAutoUpgConfTgtTblSunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblSunday.setStatus("current")
_VServerClientAutoUpgConfTgtTblMonday_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblMonday_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblMonday = _VServerClientAutoUpgConfTgtTblMonday_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 4),
    _VServerClientAutoUpgConfTgtTblMonday_Type()
)
vServerClientAutoUpgConfTgtTblMonday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblMonday.setStatus("current")
_VServerClientAutoUpgConfTgtTblTuesday_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblTuesday_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblTuesday = _VServerClientAutoUpgConfTgtTblTuesday_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 5),
    _VServerClientAutoUpgConfTgtTblTuesday_Type()
)
vServerClientAutoUpgConfTgtTblTuesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblTuesday.setStatus("current")
_VServerClientAutoUpgConfTgtTblWednesday_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblWednesday_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblWednesday = _VServerClientAutoUpgConfTgtTblWednesday_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 6),
    _VServerClientAutoUpgConfTgtTblWednesday_Type()
)
vServerClientAutoUpgConfTgtTblWednesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblWednesday.setStatus("current")
_VServerClientAutoUpgConfTgtTblThursday_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblThursday_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblThursday = _VServerClientAutoUpgConfTgtTblThursday_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 7),
    _VServerClientAutoUpgConfTgtTblThursday_Type()
)
vServerClientAutoUpgConfTgtTblThursday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblThursday.setStatus("current")
_VServerClientAutoUpgConfTgtTblFriday_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblFriday_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblFriday = _VServerClientAutoUpgConfTgtTblFriday_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 8),
    _VServerClientAutoUpgConfTgtTblFriday_Type()
)
vServerClientAutoUpgConfTgtTblFriday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblFriday.setStatus("current")
_VServerClientAutoUpgConfTgtTblSaturday_Type = Unsigned32
_VServerClientAutoUpgConfTgtTblSaturday_Object = MibTableColumn
vServerClientAutoUpgConfTgtTblSaturday = _VServerClientAutoUpgConfTgtTblSaturday_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 4, 1, 9),
    _VServerClientAutoUpgConfTgtTblSaturday_Type()
)
vServerClientAutoUpgConfTgtTblSaturday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgConfTgtTblSaturday.setStatus("current")
_VServerClientAutoUpgVerTgtTbl_Object = MibTable
vServerClientAutoUpgVerTgtTbl = _VServerClientAutoUpgVerTgtTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 5)
)
if mibBuilder.loadTexts:
    vServerClientAutoUpgVerTgtTbl.setStatus("current")
_VServerClientAutoUpgVerTgtTblEntry_Object = MibTableRow
vServerClientAutoUpgVerTgtTblEntry = _VServerClientAutoUpgVerTgtTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 5, 1)
)
vServerClientAutoUpgVerTgtTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerClientAutoUpgVerTgtTblIndex"),
)
if mibBuilder.loadTexts:
    vServerClientAutoUpgVerTgtTblEntry.setStatus("current")
_VServerClientAutoUpgVerTgtTblIndex_Type = Unsigned32
_VServerClientAutoUpgVerTgtTblIndex_Object = MibTableColumn
vServerClientAutoUpgVerTgtTblIndex = _VServerClientAutoUpgVerTgtTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 5, 1, 1),
    _VServerClientAutoUpgVerTgtTblIndex_Type()
)
vServerClientAutoUpgVerTgtTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientAutoUpgVerTgtTblIndex.setStatus("current")
_VServerClientAutoUpgVerTgtTblRow_Type = Unsigned32
_VServerClientAutoUpgVerTgtTblRow_Object = MibTableColumn
vServerClientAutoUpgVerTgtTblRow = _VServerClientAutoUpgVerTgtTblRow_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 5, 1, 2),
    _VServerClientAutoUpgVerTgtTblRow_Type()
)
vServerClientAutoUpgVerTgtTblRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgVerTgtTblRow.setStatus("current")


class _VServerClientAutoUpgVerTgtTblVer_Type(OctetString):
    """Custom type vServerClientAutoUpgVerTgtTblVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerClientAutoUpgVerTgtTblVer_Type.__name__ = "OctetString"
_VServerClientAutoUpgVerTgtTblVer_Object = MibTableColumn
vServerClientAutoUpgVerTgtTblVer = _VServerClientAutoUpgVerTgtTblVer_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 5, 1, 3),
    _VServerClientAutoUpgVerTgtTblVer_Type()
)
vServerClientAutoUpgVerTgtTblVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgVerTgtTblVer.setStatus("current")


class _VServerClientAutoUpgVerTgtTblPlatform_Type(OctetString):
    """Custom type vServerClientAutoUpgVerTgtTblPlatform based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerClientAutoUpgVerTgtTblPlatform_Type.__name__ = "OctetString"
_VServerClientAutoUpgVerTgtTblPlatform_Object = MibTableColumn
vServerClientAutoUpgVerTgtTblPlatform = _VServerClientAutoUpgVerTgtTblPlatform_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 5, 1, 4),
    _VServerClientAutoUpgVerTgtTblPlatform_Type()
)
vServerClientAutoUpgVerTgtTblPlatform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgVerTgtTblPlatform.setStatus("current")


class _VServerClientAutoUpgVerTgtTblClientPayload_Type(OctetString):
    """Custom type vServerClientAutoUpgVerTgtTblClientPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerClientAutoUpgVerTgtTblClientPayload_Type.__name__ = "OctetString"
_VServerClientAutoUpgVerTgtTblClientPayload_Object = MibTableColumn
vServerClientAutoUpgVerTgtTblClientPayload = _VServerClientAutoUpgVerTgtTblClientPayload_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 5, 1, 5),
    _VServerClientAutoUpgVerTgtTblClientPayload_Type()
)
vServerClientAutoUpgVerTgtTblClientPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientAutoUpgVerTgtTblClientPayload.setStatus("current")
_VServerClientUpdateInfo_Object = MibTable
vServerClientUpdateInfo = _VServerClientUpdateInfo_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 6)
)
if mibBuilder.loadTexts:
    vServerClientUpdateInfo.setStatus("current")
_VServerClientUpdateInfoEntry_Object = MibTableRow
vServerClientUpdateInfoEntry = _VServerClientUpdateInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 6, 1)
)
vServerClientUpdateInfoEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerClientUpdateInfoIndex"),
)
if mibBuilder.loadTexts:
    vServerClientUpdateInfoEntry.setStatus("current")
_VServerClientUpdateInfoIndex_Type = Unsigned32
_VServerClientUpdateInfoIndex_Object = MibTableColumn
vServerClientUpdateInfoIndex = _VServerClientUpdateInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 6, 1, 1),
    _VServerClientUpdateInfoIndex_Type()
)
vServerClientUpdateInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientUpdateInfoIndex.setStatus("current")
_VServerClientUpdateInfoSendClntUpdate_Type = VenturiBooleanType
_VServerClientUpdateInfoSendClntUpdate_Object = MibTableColumn
vServerClientUpdateInfoSendClntUpdate = _VServerClientUpdateInfoSendClntUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 6, 1, 2),
    _VServerClientUpdateInfoSendClntUpdate_Type()
)
vServerClientUpdateInfoSendClntUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientUpdateInfoSendClntUpdate.setStatus("current")
_VServerClientUpdateInfoClientVer_Type = OctetString
_VServerClientUpdateInfoClientVer_Object = MibTableColumn
vServerClientUpdateInfoClientVer = _VServerClientUpdateInfoClientVer_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 6, 1, 3),
    _VServerClientUpdateInfoClientVer_Type()
)
vServerClientUpdateInfoClientVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientUpdateInfoClientVer.setStatus("current")
_VServerClientUpdateInfoUrl_Type = OctetString
_VServerClientUpdateInfoUrl_Object = MibTableColumn
vServerClientUpdateInfoUrl = _VServerClientUpdateInfoUrl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 6, 1, 4),
    _VServerClientUpdateInfoUrl_Type()
)
vServerClientUpdateInfoUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientUpdateInfoUrl.setStatus("current")
_VServerClientUpdateInfoExpTime_Type = Unsigned32
_VServerClientUpdateInfoExpTime_Object = MibTableColumn
vServerClientUpdateInfoExpTime = _VServerClientUpdateInfoExpTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 3, 2, 6, 1, 5),
    _VServerClientUpdateInfoExpTime_Type()
)
vServerClientUpdateInfoExpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerClientUpdateInfoExpTime.setStatus("current")
_VServerConfAppSvcsFtp_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsFtp = _VServerConfAppSvcsFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4)
)
_VServerConfAppSvcsFtpScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsFtpScalars = _VServerConfAppSvcsFtpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 1)
)
_VServerConfAppSvcsFtpTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsFtpTbls = _VServerConfAppSvcsFtpTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 2)
)
_VServerFtpConfTbl_Object = MibTable
vServerFtpConfTbl = _VServerFtpConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vServerFtpConfTbl.setStatus("current")
_VServerFtpConfTblEntry_Object = MibTableRow
vServerFtpConfTblEntry = _VServerFtpConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 2, 1, 1)
)
vServerFtpConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerFtpConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerFtpConfTblEntry.setStatus("current")
_VServerFtpConfTblIndex_Type = Unsigned32
_VServerFtpConfTblIndex_Object = MibTableColumn
vServerFtpConfTblIndex = _VServerFtpConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 2, 1, 1, 1),
    _VServerFtpConfTblIndex_Type()
)
vServerFtpConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerFtpConfTblIndex.setStatus("current")


class _VServerFtpConfTblDataMethName_Type(OctetString):
    """Custom type vServerFtpConfTblDataMethName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerFtpConfTblDataMethName_Type.__name__ = "OctetString"
_VServerFtpConfTblDataMethName_Object = MibTableColumn
vServerFtpConfTblDataMethName = _VServerFtpConfTblDataMethName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 2, 1, 1, 2),
    _VServerFtpConfTblDataMethName_Type()
)
vServerFtpConfTblDataMethName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFtpConfTblDataMethName.setStatus("current")


class _VServerFtpConfTblSocksMethName_Type(OctetString):
    """Custom type vServerFtpConfTblSocksMethName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerFtpConfTblSocksMethName_Type.__name__ = "OctetString"
_VServerFtpConfTblSocksMethName_Object = MibTableColumn
vServerFtpConfTblSocksMethName = _VServerFtpConfTblSocksMethName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 2, 1, 1, 3),
    _VServerFtpConfTblSocksMethName_Type()
)
vServerFtpConfTblSocksMethName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFtpConfTblSocksMethName.setStatus("current")
_VServerFtpConfTblTimeout_Type = Unsigned32
_VServerFtpConfTblTimeout_Object = MibTableColumn
vServerFtpConfTblTimeout = _VServerFtpConfTblTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 2, 1, 1, 4),
    _VServerFtpConfTblTimeout_Type()
)
vServerFtpConfTblTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFtpConfTblTimeout.setStatus("current")
_VServerFtpConfTblDelay_Type = Unsigned32
_VServerFtpConfTblDelay_Object = MibTableColumn
vServerFtpConfTblDelay = _VServerFtpConfTblDelay_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 4, 2, 1, 1, 5),
    _VServerFtpConfTblDelay_Type()
)
vServerFtpConfTblDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFtpConfTblDelay.setStatus("current")
_VServerConfAppSvcsQOS_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsQOS = _VServerConfAppSvcsQOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 5)
)
_VServerConfAppSvcsQOSScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsQOSScalars = _VServerConfAppSvcsQOSScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 5, 1)
)
_VServerConfQOSLicensed_Type = Unsigned32
_VServerConfQOSLicensed_Object = MibScalar
vServerConfQOSLicensed = _VServerConfQOSLicensed_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 5, 1, 1),
    _VServerConfQOSLicensed_Type()
)
vServerConfQOSLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConfQOSLicensed.setStatus("current")
_VServerConfQOSEnabled_Type = Unsigned32
_VServerConfQOSEnabled_Object = MibScalar
vServerConfQOSEnabled = _VServerConfQOSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 5, 1, 2),
    _VServerConfQOSEnabled_Type()
)
vServerConfQOSEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfQOSEnabled.setStatus("current")
_VServerConfUpdateQOSProfilesNow_Type = Unsigned32
_VServerConfUpdateQOSProfilesNow_Object = MibScalar
vServerConfUpdateQOSProfilesNow = _VServerConfUpdateQOSProfilesNow_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 5, 1, 3),
    _VServerConfUpdateQOSProfilesNow_Type()
)
vServerConfUpdateQOSProfilesNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfUpdateQOSProfilesNow.setStatus("current")


class _VServerConfUpdQOSProfName_Type(OctetString):
    """Custom type vServerConfUpdQOSProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerConfUpdQOSProfName_Type.__name__ = "OctetString"
_VServerConfUpdQOSProfName_Object = MibScalar
vServerConfUpdQOSProfName = _VServerConfUpdQOSProfName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 5, 1, 4),
    _VServerConfUpdQOSProfName_Type()
)
vServerConfUpdQOSProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfUpdQOSProfName.setStatus("current")


class _VServerConfAssignDefProfName_Type(OctetString):
    """Custom type vServerConfAssignDefProfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerConfAssignDefProfName_Type.__name__ = "OctetString"
_VServerConfAssignDefProfName_Object = MibScalar
vServerConfAssignDefProfName = _VServerConfAssignDefProfName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 5, 1, 5),
    _VServerConfAssignDefProfName_Type()
)
vServerConfAssignDefProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAssignDefProfName.setStatus("current")
_VServerConfAppSvcsQOSTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsQOSTbls = _VServerConfAppSvcsQOSTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 5, 2)
)
_VServerConfAppSvcsUserAgent_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsUserAgent = _VServerConfAppSvcsUserAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6)
)
_VServerConfAppSvcsUserAgentScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsUserAgentScalars = _VServerConfAppSvcsUserAgentScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 1)
)
_VServerConfAppSvcsUserAgentTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsUserAgentTbls = _VServerConfAppSvcsUserAgentTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2)
)
_VServerUACfgTbl_Object = MibTable
vServerUACfgTbl = _VServerUACfgTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vServerUACfgTbl.setStatus("current")
_VServerUACfgTblEntry_Object = MibTableRow
vServerUACfgTblEntry = _VServerUACfgTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1)
)
vServerUACfgTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerUACfgTblIndex"),
)
if mibBuilder.loadTexts:
    vServerUACfgTblEntry.setStatus("current")
_VServerUACfgTblIndex_Type = Unsigned32
_VServerUACfgTblIndex_Object = MibTableColumn
vServerUACfgTblIndex = _VServerUACfgTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 1),
    _VServerUACfgTblIndex_Type()
)
vServerUACfgTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerUACfgTblIndex.setStatus("current")
_VServerUAId_Type = Unsigned32
_VServerUAId_Object = MibTableColumn
vServerUAId = _VServerUAId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 2),
    _VServerUAId_Type()
)
vServerUAId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAId.setStatus("current")


class _VServerUAHeaderSig_Type(OctetString):
    """Custom type vServerUAHeaderSig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerUAHeaderSig_Type.__name__ = "OctetString"
_VServerUAHeaderSig_Object = MibTableColumn
vServerUAHeaderSig = _VServerUAHeaderSig_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 3),
    _VServerUAHeaderSig_Type()
)
vServerUAHeaderSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAHeaderSig.setStatus("current")
_VServerUAMultiPartId_Type = Unsigned32
_VServerUAMultiPartId_Object = MibTableColumn
vServerUAMultiPartId = _VServerUAMultiPartId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 4),
    _VServerUAMultiPartId_Type()
)
vServerUAMultiPartId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMultiPartId.setStatus("current")
_VServerUAGZIPEnabled_Type = Unsigned32
_VServerUAGZIPEnabled_Object = MibTableColumn
vServerUAGZIPEnabled = _VServerUAGZIPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 5),
    _VServerUAGZIPEnabled_Type()
)
vServerUAGZIPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAGZIPEnabled.setStatus("current")
_VServerUACLPerRedEnabled_Type = Unsigned32
_VServerUACLPerRedEnabled_Object = MibTableColumn
vServerUACLPerRedEnabled = _VServerUACLPerRedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 6),
    _VServerUACLPerRedEnabled_Type()
)
vServerUACLPerRedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUACLPerRedEnabled.setStatus("current")
_VServerUAPrgJpegEnabled_Type = VenturiBooleanType
_VServerUAPrgJpegEnabled_Object = MibTableColumn
vServerUAPrgJpegEnabled = _VServerUAPrgJpegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 7),
    _VServerUAPrgJpegEnabled_Type()
)
vServerUAPrgJpegEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAPrgJpegEnabled.setStatus("current")
_VServerUALossyJpegEnabled_Type = VenturiBooleanType
_VServerUALossyJpegEnabled_Object = MibTableColumn
vServerUALossyJpegEnabled = _VServerUALossyJpegEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 8),
    _VServerUALossyJpegEnabled_Type()
)
vServerUALossyJpegEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUALossyJpegEnabled.setStatus("current")
_VServerUALossyGifEnabled_Type = VenturiBooleanType
_VServerUALossyGifEnabled_Object = MibTableColumn
vServerUALossyGifEnabled = _VServerUALossyGifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 9),
    _VServerUALossyGifEnabled_Type()
)
vServerUALossyGifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUALossyGifEnabled.setStatus("current")
_VServerUALossyHtmlEnabled_Type = VenturiBooleanType
_VServerUALossyHtmlEnabled_Object = MibTableColumn
vServerUALossyHtmlEnabled = _VServerUALossyHtmlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 10),
    _VServerUALossyHtmlEnabled_Type()
)
vServerUALossyHtmlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUALossyHtmlEnabled.setStatus("current")
_VServerUALossyPngEnabled_Type = VenturiBooleanType
_VServerUALossyPngEnabled_Object = MibTableColumn
vServerUALossyPngEnabled = _VServerUALossyPngEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 11),
    _VServerUALossyPngEnabled_Type()
)
vServerUALossyPngEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUALossyPngEnabled.setStatus("current")
_VServerUAItractivNoChunk_Type = VenturiBooleanType
_VServerUAItractivNoChunk_Object = MibTableColumn
vServerUAItractivNoChunk = _VServerUAItractivNoChunk_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 1, 1, 12),
    _VServerUAItractivNoChunk_Type()
)
vServerUAItractivNoChunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAItractivNoChunk.setStatus("current")
_VServerUAMultiPartCfgTbl_Object = MibTable
vServerUAMultiPartCfgTbl = _VServerUAMultiPartCfgTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2)
)
if mibBuilder.loadTexts:
    vServerUAMultiPartCfgTbl.setStatus("current")
_VServerUAMultiPartCfgTblEntry_Object = MibTableRow
vServerUAMultiPartCfgTblEntry = _VServerUAMultiPartCfgTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1)
)
vServerUAMultiPartCfgTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerUAMPartCfgTblIndex"),
)
if mibBuilder.loadTexts:
    vServerUAMultiPartCfgTblEntry.setStatus("current")
_VServerUAMPartCfgTblIndex_Type = Unsigned32
_VServerUAMPartCfgTblIndex_Object = MibTableColumn
vServerUAMPartCfgTblIndex = _VServerUAMPartCfgTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 1),
    _VServerUAMPartCfgTblIndex_Type()
)
vServerUAMPartCfgTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerUAMPartCfgTblIndex.setStatus("current")
_VServerUAMPartId_Type = Unsigned32
_VServerUAMPartId_Object = MibTableColumn
vServerUAMPartId = _VServerUAMPartId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 2),
    _VServerUAMPartId_Type()
)
vServerUAMPartId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartId.setStatus("current")
_VServerUAMPartEnable_Type = VenturiBooleanType
_VServerUAMPartEnable_Object = MibTableColumn
vServerUAMPartEnable = _VServerUAMPartEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 3),
    _VServerUAMPartEnable_Type()
)
vServerUAMPartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartEnable.setStatus("current")
_VServerUAMPartMaxPartSize_Type = Unsigned32
_VServerUAMPartMaxPartSize_Object = MibTableColumn
vServerUAMPartMaxPartSize = _VServerUAMPartMaxPartSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 4),
    _VServerUAMPartMaxPartSize_Type()
)
vServerUAMPartMaxPartSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartMaxPartSize.setStatus("current")
_VServerUAMPartMaxPackSize_Type = Unsigned32
_VServerUAMPartMaxPackSize_Object = MibTableColumn
vServerUAMPartMaxPackSize = _VServerUAMPartMaxPackSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 5),
    _VServerUAMPartMaxPackSize_Type()
)
vServerUAMPartMaxPackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartMaxPackSize.setStatus("current")
_VServerUAMPartMaxWaitTime_Type = Unsigned32
_VServerUAMPartMaxWaitTime_Object = MibTableColumn
vServerUAMPartMaxWaitTime = _VServerUAMPartMaxWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 6),
    _VServerUAMPartMaxWaitTime_Type()
)
vServerUAMPartMaxWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartMaxWaitTime.setStatus("current")
_VServerUAMPartUseMixedType_Type = VenturiBooleanType
_VServerUAMPartUseMixedType_Object = MibTableColumn
vServerUAMPartUseMixedType = _VServerUAMPartUseMixedType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 7),
    _VServerUAMPartUseMixedType_Type()
)
vServerUAMPartUseMixedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartUseMixedType.setStatus("current")
_VServerUAMPartEnableMFilter_Type = VenturiBooleanType
_VServerUAMPartEnableMFilter_Object = MibTableColumn
vServerUAMPartEnableMFilter = _VServerUAMPartEnableMFilter_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 8),
    _VServerUAMPartEnableMFilter_Type()
)
vServerUAMPartEnableMFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartEnableMFilter.setStatus("current")
_VServerUAMPartNoOtherDomObj_Type = VenturiBooleanType
_VServerUAMPartNoOtherDomObj_Object = MibTableColumn
vServerUAMPartNoOtherDomObj = _VServerUAMPartNoOtherDomObj_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 11),
    _VServerUAMPartNoOtherDomObj_Type()
)
vServerUAMPartNoOtherDomObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartNoOtherDomObj.setStatus("current")
_VServerUAMPartIncludeTxt_Type = VenturiBooleanType
_VServerUAMPartIncludeTxt_Object = MibTableColumn
vServerUAMPartIncludeTxt = _VServerUAMPartIncludeTxt_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 12),
    _VServerUAMPartIncludeTxt_Type()
)
vServerUAMPartIncludeTxt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartIncludeTxt.setStatus("current")
_VServerUAMPartIncludeImg_Type = VenturiBooleanType
_VServerUAMPartIncludeImg_Object = MibTableColumn
vServerUAMPartIncludeImg = _VServerUAMPartIncludeImg_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 13),
    _VServerUAMPartIncludeImg_Type()
)
vServerUAMPartIncludeImg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartIncludeImg.setStatus("current")
_VServerUAMPartIncludeCss_Type = VenturiBooleanType
_VServerUAMPartIncludeCss_Object = MibTableColumn
vServerUAMPartIncludeCss = _VServerUAMPartIncludeCss_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 14),
    _VServerUAMPartIncludeCss_Type()
)
vServerUAMPartIncludeCss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartIncludeCss.setStatus("current")
_VServerUAMPartIncludeJs_Type = VenturiBooleanType
_VServerUAMPartIncludeJs_Object = MibTableColumn
vServerUAMPartIncludeJs = _VServerUAMPartIncludeJs_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 15),
    _VServerUAMPartIncludeJs_Type()
)
vServerUAMPartIncludeJs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartIncludeJs.setStatus("current")
_VServerUAMPartCacheSubObjects_Type = VenturiBooleanType
_VServerUAMPartCacheSubObjects_Object = MibTableColumn
vServerUAMPartCacheSubObjects = _VServerUAMPartCacheSubObjects_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 6, 2, 2, 1, 16),
    _VServerUAMPartCacheSubObjects_Type()
)
vServerUAMPartCacheSubObjects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUAMPartCacheSubObjects.setStatus("current")
_VServerConfAppSvcsSIC_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsSIC = _VServerConfAppSvcsSIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 7)
)
_VServerConfAppSvcsSICScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsSICScalars = _VServerConfAppSvcsSICScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 7, 1)
)
_VServerConfAppSvcsSICTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsSICTbls = _VServerConfAppSvcsSICTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 7, 2)
)
_VServerConfAppSvcsDBoard_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsDBoard = _VServerConfAppSvcsDBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8)
)
_VServerConfAppSvcsDBoardScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsDBoardScalars = _VServerConfAppSvcsDBoardScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1)
)
_VServerDBoardCUsrCnt_Type = Counter64
_VServerDBoardCUsrCnt_Object = MibScalar
vServerDBoardCUsrCnt = _VServerDBoardCUsrCnt_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 1),
    _VServerDBoardCUsrCnt_Type()
)
vServerDBoardCUsrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardCUsrCnt.setStatus("current")
_VServerDBoardCLUsrCnt_Type = Counter64
_VServerDBoardCLUsrCnt_Object = MibScalar
vServerDBoardCLUsrCnt = _VServerDBoardCLUsrCnt_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 2),
    _VServerDBoardCLUsrCnt_Type()
)
vServerDBoardCLUsrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardCLUsrCnt.setStatus("current")
_VServerDBoardCConn_Type = Counter64
_VServerDBoardCConn_Object = MibScalar
vServerDBoardCConn = _VServerDBoardCConn_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 3),
    _VServerDBoardCConn_Type()
)
vServerDBoardCConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardCConn.setStatus("current")
_VServerDBoardCLConn_Type = Counter64
_VServerDBoardCLConn_Object = MibScalar
vServerDBoardCLConn = _VServerDBoardCLConn_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 4),
    _VServerDBoardCLConn_Type()
)
vServerDBoardCLConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardCLConn.setStatus("current")
_VServerDBoardTotalConn_Type = Counter64
_VServerDBoardTotalConn_Object = MibScalar
vServerDBoardTotalConn = _VServerDBoardTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 5),
    _VServerDBoardTotalConn_Type()
)
vServerDBoardTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardTotalConn.setStatus("current")
_VServerDBoardCTraffic_Type = Counter64
_VServerDBoardCTraffic_Object = MibScalar
vServerDBoardCTraffic = _VServerDBoardCTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 6),
    _VServerDBoardCTraffic_Type()
)
vServerDBoardCTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardCTraffic.setStatus("current")
_VServerDBoardCLTraffic_Type = Counter64
_VServerDBoardCLTraffic_Object = MibScalar
vServerDBoardCLTraffic = _VServerDBoardCLTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 7),
    _VServerDBoardCLTraffic_Type()
)
vServerDBoardCLTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardCLTraffic.setStatus("current")
_VServerDBoardTotalTraffic_Type = Counter64
_VServerDBoardTotalTraffic_Object = MibScalar
vServerDBoardTotalTraffic = _VServerDBoardTotalTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 8),
    _VServerDBoardTotalTraffic_Type()
)
vServerDBoardTotalTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardTotalTraffic.setStatus("current")
_VServerDBoardDownStreamSavings_Type = Counter64
_VServerDBoardDownStreamSavings_Object = MibScalar
vServerDBoardDownStreamSavings = _VServerDBoardDownStreamSavings_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 9),
    _VServerDBoardDownStreamSavings_Type()
)
vServerDBoardDownStreamSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardDownStreamSavings.setStatus("current")
_VServerDBoardUpStreamSavings_Type = Counter64
_VServerDBoardUpStreamSavings_Object = MibScalar
vServerDBoardUpStreamSavings = _VServerDBoardUpStreamSavings_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 10),
    _VServerDBoardUpStreamSavings_Type()
)
vServerDBoardUpStreamSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardUpStreamSavings.setStatus("current")
_VServerDBoardCPULoad_Type = Unsigned32
_VServerDBoardCPULoad_Object = MibScalar
vServerDBoardCPULoad = _VServerDBoardCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 11),
    _VServerDBoardCPULoad_Type()
)
vServerDBoardCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardCPULoad.setStatus("current")
_VServerDBoardMemUsed_Type = Counter64
_VServerDBoardMemUsed_Object = MibScalar
vServerDBoardMemUsed = _VServerDBoardMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 12),
    _VServerDBoardMemUsed_Type()
)
vServerDBoardMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardMemUsed.setStatus("current")
_VServerDBoardMemFree_Type = Counter64
_VServerDBoardMemFree_Object = MibScalar
vServerDBoardMemFree = _VServerDBoardMemFree_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 13),
    _VServerDBoardMemFree_Type()
)
vServerDBoardMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardMemFree.setStatus("current")
_VServerDBoardMemSwap_Type = Counter64
_VServerDBoardMemSwap_Object = MibScalar
vServerDBoardMemSwap = _VServerDBoardMemSwap_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 14),
    _VServerDBoardMemSwap_Type()
)
vServerDBoardMemSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardMemSwap.setStatus("current")
_VServerDBoardDiskSpace_Type = Counter64
_VServerDBoardDiskSpace_Object = MibScalar
vServerDBoardDiskSpace = _VServerDBoardDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 1, 15),
    _VServerDBoardDiskSpace_Type()
)
vServerDBoardDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerDBoardDiskSpace.setStatus("current")
_VServerConfAppSvcsDBoardTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsDBoardTbls = _VServerConfAppSvcsDBoardTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 8, 2)
)
_VServerConfAppSvcsIPE_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsIPE = _VServerConfAppSvcsIPE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9)
)
_VServerConfAppSvcsIPEScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsIPEScalars = _VServerConfAppSvcsIPEScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9, 1)
)
_VServerConfAppSvcsIPETbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsIPETbls = _VServerConfAppSvcsIPETbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9, 2)
)
_VServerIPEFilterTbl_Object = MibTable
vServerIPEFilterTbl = _VServerIPEFilterTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9, 2, 1)
)
if mibBuilder.loadTexts:
    vServerIPEFilterTbl.setStatus("current")
_VServerIPEFilterTblEntry_Object = MibTableRow
vServerIPEFilterTblEntry = _VServerIPEFilterTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9, 2, 1, 1)
)
vServerIPEFilterTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerIPEFilterIndex"),
)
if mibBuilder.loadTexts:
    vServerIPEFilterTblEntry.setStatus("current")
_VServerIPEFilterIndex_Type = Unsigned32
_VServerIPEFilterIndex_Object = MibTableColumn
vServerIPEFilterIndex = _VServerIPEFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9, 2, 1, 1, 1),
    _VServerIPEFilterIndex_Type()
)
vServerIPEFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerIPEFilterIndex.setStatus("current")
_VServerIPEFilterEnabled_Type = VenturiBooleanType
_VServerIPEFilterEnabled_Object = MibTableColumn
vServerIPEFilterEnabled = _VServerIPEFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9, 2, 1, 1, 2),
    _VServerIPEFilterEnabled_Type()
)
vServerIPEFilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerIPEFilterEnabled.setStatus("current")
_VServerIPEFilterAddress_Type = IpAddress
_VServerIPEFilterAddress_Object = MibTableColumn
vServerIPEFilterAddress = _VServerIPEFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9, 2, 1, 1, 3),
    _VServerIPEFilterAddress_Type()
)
vServerIPEFilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerIPEFilterAddress.setStatus("current")
_VServerIPEFilterMaskSize_Type = Unsigned32
_VServerIPEFilterMaskSize_Object = MibTableColumn
vServerIPEFilterMaskSize = _VServerIPEFilterMaskSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 9, 2, 1, 1, 4),
    _VServerIPEFilterMaskSize_Type()
)
vServerIPEFilterMaskSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerIPEFilterMaskSize.setStatus("current")
if mibBuilder.loadTexts:
    vServerIPEFilterMaskSize.setUnits("bits")
_VServerConfAppSvcsHHI_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsHHI = _VServerConfAppSvcsHHI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10)
)
_VSvrConfAppSvcsHHIScalars_ObjectIdentity = ObjectIdentity
vSvrConfAppSvcsHHIScalars = _VSvrConfAppSvcsHHIScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 1)
)
_VSvrConfAppSvcsHHITbls_ObjectIdentity = ObjectIdentity
vSvrConfAppSvcsHHITbls = _VSvrConfAppSvcsHHITbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2)
)
_VSvrConfHHIMain_Object = MibTable
vSvrConfHHIMain = _VSvrConfHHIMain_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 1)
)
if mibBuilder.loadTexts:
    vSvrConfHHIMain.setStatus("current")
_VSvrConfHHIMainEntry_Object = MibTableRow
vSvrConfHHIMainEntry = _VSvrConfHHIMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 1, 1)
)
vSvrConfHHIMainEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vSvrConfHHIMainIndex"),
)
if mibBuilder.loadTexts:
    vSvrConfHHIMainEntry.setStatus("current")
_VSvrConfHHIMainIndex_Type = Unsigned32
_VSvrConfHHIMainIndex_Object = MibTableColumn
vSvrConfHHIMainIndex = _VSvrConfHHIMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 1, 1, 1),
    _VSvrConfHHIMainIndex_Type()
)
vSvrConfHHIMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSvrConfHHIMainIndex.setStatus("current")


class _VSvrConfHHIMainURL_Type(OctetString):
    """Custom type vSvrConfHHIMainURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_VSvrConfHHIMainURL_Type.__name__ = "OctetString"
_VSvrConfHHIMainURL_Object = MibTableColumn
vSvrConfHHIMainURL = _VSvrConfHHIMainURL_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 1, 1, 2),
    _VSvrConfHHIMainURL_Type()
)
vSvrConfHHIMainURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIMainURL.setStatus("current")
_VSvrConfHHIMainTmplID_Type = Integer32
_VSvrConfHHIMainTmplID_Object = MibTableColumn
vSvrConfHHIMainTmplID = _VSvrConfHHIMainTmplID_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 1, 1, 3),
    _VSvrConfHHIMainTmplID_Type()
)
vSvrConfHHIMainTmplID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIMainTmplID.setStatus("current")
_VSvrConfHHITmpl_Object = MibTable
vSvrConfHHITmpl = _VSvrConfHHITmpl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 2)
)
if mibBuilder.loadTexts:
    vSvrConfHHITmpl.setStatus("current")
_VSvrConfHHITmplEntry_Object = MibTableRow
vSvrConfHHITmplEntry = _VSvrConfHHITmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 2, 1)
)
vSvrConfHHITmplEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vSvrConfHHITmplIndex"),
)
if mibBuilder.loadTexts:
    vSvrConfHHITmplEntry.setStatus("current")
_VSvrConfHHITmplIndex_Type = Unsigned32
_VSvrConfHHITmplIndex_Object = MibTableColumn
vSvrConfHHITmplIndex = _VSvrConfHHITmplIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 2, 1, 1),
    _VSvrConfHHITmplIndex_Type()
)
vSvrConfHHITmplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSvrConfHHITmplIndex.setStatus("current")


class _VSvrConfHHITmplTmplName_Type(OctetString):
    """Custom type vSvrConfHHITmplTmplName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VSvrConfHHITmplTmplName_Type.__name__ = "OctetString"
_VSvrConfHHITmplTmplName_Object = MibTableColumn
vSvrConfHHITmplTmplName = _VSvrConfHHITmplTmplName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 2, 1, 2),
    _VSvrConfHHITmplTmplName_Type()
)
vSvrConfHHITmplTmplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHITmplTmplName.setStatus("current")


class _VSvrConfHHITmplFlds_Type(OctetString):
    """Custom type vSvrConfHHITmplFlds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VSvrConfHHITmplFlds_Type.__name__ = "OctetString"
_VSvrConfHHITmplFlds_Object = MibTableColumn
vSvrConfHHITmplFlds = _VSvrConfHHITmplFlds_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 2, 1, 3),
    _VSvrConfHHITmplFlds_Type()
)
vSvrConfHHITmplFlds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHITmplFlds.setStatus("current")
_VSvrConfHHIHdr_Object = MibTable
vSvrConfHHIHdr = _VSvrConfHHIHdr_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 3)
)
if mibBuilder.loadTexts:
    vSvrConfHHIHdr.setStatus("current")
_VSvrConfHHIHdrEntry_Object = MibTableRow
vSvrConfHHIHdrEntry = _VSvrConfHHIHdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 3, 1)
)
vSvrConfHHIHdrEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vSvrConfHHIHdrIndex"),
)
if mibBuilder.loadTexts:
    vSvrConfHHIHdrEntry.setStatus("current")
_VSvrConfHHIHdrIndex_Type = Unsigned32
_VSvrConfHHIHdrIndex_Object = MibTableColumn
vSvrConfHHIHdrIndex = _VSvrConfHHIHdrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 3, 1, 1),
    _VSvrConfHHIHdrIndex_Type()
)
vSvrConfHHIHdrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSvrConfHHIHdrIndex.setStatus("current")


class _VSvrConfHHIHdrHdrName_Type(OctetString):
    """Custom type vSvrConfHHIHdrHdrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VSvrConfHHIHdrHdrName_Type.__name__ = "OctetString"
_VSvrConfHHIHdrHdrName_Object = MibTableColumn
vSvrConfHHIHdrHdrName = _VSvrConfHHIHdrHdrName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 3, 1, 2),
    _VSvrConfHHIHdrHdrName_Type()
)
vSvrConfHHIHdrHdrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIHdrHdrName.setStatus("current")
_VSvrConfHHIHdrHdrRadType_Type = Integer32
_VSvrConfHHIHdrHdrRadType_Object = MibTableColumn
vSvrConfHHIHdrHdrRadType = _VSvrConfHHIHdrHdrRadType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 3, 1, 3),
    _VSvrConfHHIHdrHdrRadType_Type()
)
vSvrConfHHIHdrHdrRadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIHdrHdrRadType.setStatus("current")
_VSvrConfHHIHdrHdrRadVndId_Type = Integer32
_VSvrConfHHIHdrHdrRadVndId_Object = MibTableColumn
vSvrConfHHIHdrHdrRadVndId = _VSvrConfHHIHdrHdrRadVndId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 3, 1, 4),
    _VSvrConfHHIHdrHdrRadVndId_Type()
)
vSvrConfHHIHdrHdrRadVndId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIHdrHdrRadVndId.setStatus("current")
_VSvrConfHHIHdrHdrRadVndType_Type = Integer32
_VSvrConfHHIHdrHdrRadVndType_Object = MibTableColumn
vSvrConfHHIHdrHdrRadVndType = _VSvrConfHHIHdrHdrRadVndType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 3, 1, 5),
    _VSvrConfHHIHdrHdrRadVndType_Type()
)
vSvrConfHHIHdrHdrRadVndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIHdrHdrRadVndType.setStatus("current")
_VSvrConfHHIHdrHdrHint_Type = Integer32
_VSvrConfHHIHdrHdrHint_Object = MibTableColumn
vSvrConfHHIHdrHdrHint = _VSvrConfHHIHdrHdrHint_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 3, 1, 6),
    _VSvrConfHHIHdrHdrHint_Type()
)
vSvrConfHHIHdrHdrHint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIHdrHdrHint.setStatus("current")
_VSvrConfHHIFtp_Object = MibTable
vSvrConfHHIFtp = _VSvrConfHHIFtp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4)
)
if mibBuilder.loadTexts:
    vSvrConfHHIFtp.setStatus("current")
_VSvrConfHHIFtpEntry_Object = MibTableRow
vSvrConfHHIFtpEntry = _VSvrConfHHIFtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1)
)
vSvrConfHHIFtpEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vSvrConfHHIFtpIndex"),
)
if mibBuilder.loadTexts:
    vSvrConfHHIFtpEntry.setStatus("current")
_VSvrConfHHIFtpIndex_Type = Unsigned32
_VSvrConfHHIFtpIndex_Object = MibTableColumn
vSvrConfHHIFtpIndex = _VSvrConfHHIFtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 1),
    _VSvrConfHHIFtpIndex_Type()
)
vSvrConfHHIFtpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpIndex.setStatus("current")


class _VSvrConfHHIFtpHost_Type(OctetString):
    """Custom type vSvrConfHHIFtpHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VSvrConfHHIFtpHost_Type.__name__ = "OctetString"
_VSvrConfHHIFtpHost_Object = MibTableColumn
vSvrConfHHIFtpHost = _VSvrConfHHIFtpHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 2),
    _VSvrConfHHIFtpHost_Type()
)
vSvrConfHHIFtpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpHost.setStatus("current")


class _VSvrConfHHIFtpDir_Type(OctetString):
    """Custom type vSvrConfHHIFtpDir based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VSvrConfHHIFtpDir_Type.__name__ = "OctetString"
_VSvrConfHHIFtpDir_Object = MibTableColumn
vSvrConfHHIFtpDir = _VSvrConfHHIFtpDir_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 3),
    _VSvrConfHHIFtpDir_Type()
)
vSvrConfHHIFtpDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpDir.setStatus("current")


class _VSvrConfHHIFtpFile_Type(OctetString):
    """Custom type vSvrConfHHIFtpFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VSvrConfHHIFtpFile_Type.__name__ = "OctetString"
_VSvrConfHHIFtpFile_Object = MibTableColumn
vSvrConfHHIFtpFile = _VSvrConfHHIFtpFile_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 4),
    _VSvrConfHHIFtpFile_Type()
)
vSvrConfHHIFtpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpFile.setStatus("current")


class _VSvrConfHHIFtpUser_Type(OctetString):
    """Custom type vSvrConfHHIFtpUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VSvrConfHHIFtpUser_Type.__name__ = "OctetString"
_VSvrConfHHIFtpUser_Object = MibTableColumn
vSvrConfHHIFtpUser = _VSvrConfHHIFtpUser_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 5),
    _VSvrConfHHIFtpUser_Type()
)
vSvrConfHHIFtpUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpUser.setStatus("current")


class _VSvrConfHHIFtpPasswd_Type(OctetString):
    """Custom type vSvrConfHHIFtpPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VSvrConfHHIFtpPasswd_Type.__name__ = "OctetString"
_VSvrConfHHIFtpPasswd_Object = MibTableColumn
vSvrConfHHIFtpPasswd = _VSvrConfHHIFtpPasswd_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 6),
    _VSvrConfHHIFtpPasswd_Type()
)
vSvrConfHHIFtpPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpPasswd.setStatus("current")
_VSvrConfHHIFtpAction_Type = Integer32
_VSvrConfHHIFtpAction_Object = MibTableColumn
vSvrConfHHIFtpAction = _VSvrConfHHIFtpAction_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 7),
    _VSvrConfHHIFtpAction_Type()
)
vSvrConfHHIFtpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpAction.setStatus("current")
_VSvrConfHHIFtpNow_Type = Integer32
_VSvrConfHHIFtpNow_Object = MibTableColumn
vSvrConfHHIFtpNow = _VSvrConfHHIFtpNow_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 8),
    _VSvrConfHHIFtpNow_Type()
)
vSvrConfHHIFtpNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpNow.setStatus("current")
_VSvrConfHHIFtpResult_Type = Integer32
_VSvrConfHHIFtpResult_Object = MibTableColumn
vSvrConfHHIFtpResult = _VSvrConfHHIFtpResult_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 10, 2, 4, 1, 9),
    _VSvrConfHHIFtpResult_Type()
)
vSvrConfHHIFtpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSvrConfHHIFtpResult.setStatus("current")
_VServerConfAppSvcsWebNotifier_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsWebNotifier = _VServerConfAppSvcsWebNotifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11)
)
_VServerConfAppSvcsWebNotifierScalars_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsWebNotifierScalars = _VServerConfAppSvcsWebNotifierScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 1)
)
_VServerConfAppSvcsWebNotifierTbls_ObjectIdentity = ObjectIdentity
vServerConfAppSvcsWebNotifierTbls = _VServerConfAppSvcsWebNotifierTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2)
)
_VServerWebNotifierTbl_Object = MibTable
vServerWebNotifierTbl = _VServerWebNotifierTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    vServerWebNotifierTbl.setStatus("current")
_VServerWebNotifierTblEntry_Object = MibTableRow
vServerWebNotifierTblEntry = _VServerWebNotifierTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 1, 1)
)
vServerWebNotifierTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerWebNotifierTblIndex"),
)
if mibBuilder.loadTexts:
    vServerWebNotifierTblEntry.setStatus("current")
_VServerWebNotifierTblIndex_Type = Unsigned32
_VServerWebNotifierTblIndex_Object = MibTableColumn
vServerWebNotifierTblIndex = _VServerWebNotifierTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 1, 1, 1),
    _VServerWebNotifierTblIndex_Type()
)
vServerWebNotifierTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerWebNotifierTblIndex.setStatus("current")
_VServerWebNotifierTblEnable_Type = VenturiBooleanType
_VServerWebNotifierTblEnable_Object = MibTableColumn
vServerWebNotifierTblEnable = _VServerWebNotifierTblEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 1, 1, 2),
    _VServerWebNotifierTblEnable_Type()
)
vServerWebNotifierTblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerWebNotifierTblEnable.setStatus("current")
_VServerWebNotifierTblLocation_Type = Unsigned32
_VServerWebNotifierTblLocation_Object = MibTableColumn
vServerWebNotifierTblLocation = _VServerWebNotifierTblLocation_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 1, 1, 3),
    _VServerWebNotifierTblLocation_Type()
)
vServerWebNotifierTblLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerWebNotifierTblLocation.setStatus("current")


class _VServerWebNotifierTblAddString_Type(OctetString):
    """Custom type vServerWebNotifierTblAddString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_VServerWebNotifierTblAddString_Type.__name__ = "OctetString"
_VServerWebNotifierTblAddString_Object = MibTableColumn
vServerWebNotifierTblAddString = _VServerWebNotifierTblAddString_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 1, 1, 4),
    _VServerWebNotifierTblAddString_Type()
)
vServerWebNotifierTblAddString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerWebNotifierTblAddString.setStatus("current")
_VServerWebNotifierHostTbl_Object = MibTable
vServerWebNotifierHostTbl = _VServerWebNotifierHostTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 2)
)
if mibBuilder.loadTexts:
    vServerWebNotifierHostTbl.setStatus("current")
_VServerWebNotifierHostTblEntry_Object = MibTableRow
vServerWebNotifierHostTblEntry = _VServerWebNotifierHostTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 2, 1)
)
vServerWebNotifierHostTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerWebNotifierHostTblIndex"),
)
if mibBuilder.loadTexts:
    vServerWebNotifierHostTblEntry.setStatus("current")
_VServerWebNotifierHostTblIndex_Type = Unsigned32
_VServerWebNotifierHostTblIndex_Object = MibTableColumn
vServerWebNotifierHostTblIndex = _VServerWebNotifierHostTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 2, 1, 1),
    _VServerWebNotifierHostTblIndex_Type()
)
vServerWebNotifierHostTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerWebNotifierHostTblIndex.setStatus("current")


class _VServerWebNotifierHostTblHost_Type(OctetString):
    """Custom type vServerWebNotifierHostTblHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_VServerWebNotifierHostTblHost_Type.__name__ = "OctetString"
_VServerWebNotifierHostTblHost_Object = MibTableColumn
vServerWebNotifierHostTblHost = _VServerWebNotifierHostTblHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 2, 11, 2, 2, 1, 2),
    _VServerWebNotifierHostTblHost_Type()
)
vServerWebNotifierHostTblHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerWebNotifierHostTblHost.setStatus("current")
_VServerConfMgmtSvcs_ObjectIdentity = ObjectIdentity
vServerConfMgmtSvcs = _VServerConfMgmtSvcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3)
)
_VServerConfDeviceGlobals_ObjectIdentity = ObjectIdentity
vServerConfDeviceGlobals = _VServerConfDeviceGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1)
)
_VServerConfDeviceGlobalsScalars_ObjectIdentity = ObjectIdentity
vServerConfDeviceGlobalsScalars = _VServerConfDeviceGlobalsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1)
)


class _VServerDateAndTime_Type(OctetString):
    """Custom type vServerDateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerDateAndTime_Type.__name__ = "OctetString"
_VServerDateAndTime_Object = MibScalar
vServerDateAndTime = _VServerDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 1),
    _VServerDateAndTime_Type()
)
vServerDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerDateAndTime.setStatus("current")


class _VServerTZRegion_Type(OctetString):
    """Custom type vServerTZRegion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerTZRegion_Type.__name__ = "OctetString"
_VServerTZRegion_Object = MibScalar
vServerTZRegion = _VServerTZRegion_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 2),
    _VServerTZRegion_Type()
)
vServerTZRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTZRegion.setStatus("current")


class _VServerTimeZone_Type(OctetString):
    """Custom type vServerTimeZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerTimeZone_Type.__name__ = "OctetString"
_VServerTimeZone_Object = MibScalar
vServerTimeZone = _VServerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 3),
    _VServerTimeZone_Type()
)
vServerTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTimeZone.setStatus("current")


class _VServerTimeServerURL_Type(OctetString):
    """Custom type vServerTimeServerURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerTimeServerURL_Type.__name__ = "OctetString"
_VServerTimeServerURL_Object = MibScalar
vServerTimeServerURL = _VServerTimeServerURL_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 4),
    _VServerTimeServerURL_Type()
)
vServerTimeServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTimeServerURL.setStatus("current")


class _VServerTimeServerProtocol_Type(Integer32):
    """Custom type vServerTimeServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ntp", 1))
    )


_VServerTimeServerProtocol_Type.__name__ = "Integer32"
_VServerTimeServerProtocol_Object = MibScalar
vServerTimeServerProtocol = _VServerTimeServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 5),
    _VServerTimeServerProtocol_Type()
)
vServerTimeServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTimeServerProtocol.setStatus("current")
_VServerTimeServerInterval_Type = Unsigned32
_VServerTimeServerInterval_Object = MibScalar
vServerTimeServerInterval = _VServerTimeServerInterval_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 6),
    _VServerTimeServerInterval_Type()
)
vServerTimeServerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTimeServerInterval.setStatus("current")
_VServerFormatOnBoot_Type = VenturiBooleanType
_VServerFormatOnBoot_Object = MibScalar
vServerFormatOnBoot = _VServerFormatOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 7),
    _VServerFormatOnBoot_Type()
)
vServerFormatOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFormatOnBoot.setStatus("current")
_VServerSSHEnabled_Type = VenturiBooleanType
_VServerSSHEnabled_Object = MibScalar
vServerSSHEnabled = _VServerSSHEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 8),
    _VServerSSHEnabled_Type()
)
vServerSSHEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSSHEnabled.setStatus("current")


class _VServerHostname_Type(OctetString):
    """Custom type vServerHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerHostname_Type.__name__ = "OctetString"
_VServerHostname_Object = MibScalar
vServerHostname = _VServerHostname_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 9),
    _VServerHostname_Type()
)
vServerHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHostname.setStatus("current")
_VServerServerIdForClient_Type = Unsigned32
_VServerServerIdForClient_Object = MibScalar
vServerServerIdForClient = _VServerServerIdForClient_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 1, 10),
    _VServerServerIdForClient_Type()
)
vServerServerIdForClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerServerIdForClient.setStatus("current")
_VServerConfDeviceGlobalsTbls_ObjectIdentity = ObjectIdentity
vServerConfDeviceGlobalsTbls = _VServerConfDeviceGlobalsTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2)
)
_VServerUiWebInfoTbl_Object = MibTable
vServerUiWebInfoTbl = _VServerUiWebInfoTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vServerUiWebInfoTbl.setStatus("current")
_VServerUiWebInfoTblEntry_Object = MibTableRow
vServerUiWebInfoTblEntry = _VServerUiWebInfoTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 1, 1)
)
vServerUiWebInfoTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerUiWebInfoTblIndex"),
)
if mibBuilder.loadTexts:
    vServerUiWebInfoTblEntry.setStatus("current")
_VServerUiWebInfoTblIndex_Type = Unsigned32
_VServerUiWebInfoTblIndex_Object = MibTableColumn
vServerUiWebInfoTblIndex = _VServerUiWebInfoTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 1, 1, 1),
    _VServerUiWebInfoTblIndex_Type()
)
vServerUiWebInfoTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerUiWebInfoTblIndex.setStatus("current")
_VServerUiWebInfoTblActive_Type = Unsigned32
_VServerUiWebInfoTblActive_Object = MibTableColumn
vServerUiWebInfoTblActive = _VServerUiWebInfoTblActive_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 1, 1, 2),
    _VServerUiWebInfoTblActive_Type()
)
vServerUiWebInfoTblActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUiWebInfoTblActive.setStatus("current")
_VServerUiWebInfoTblHTTPPort_Type = Unsigned32
_VServerUiWebInfoTblHTTPPort_Object = MibTableColumn
vServerUiWebInfoTblHTTPPort = _VServerUiWebInfoTblHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 1, 1, 3),
    _VServerUiWebInfoTblHTTPPort_Type()
)
vServerUiWebInfoTblHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUiWebInfoTblHTTPPort.setStatus("current")
_VServerUiWebInfoTblHTTPSPort_Type = Unsigned32
_VServerUiWebInfoTblHTTPSPort_Object = MibTableColumn
vServerUiWebInfoTblHTTPSPort = _VServerUiWebInfoTblHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 1, 1, 4),
    _VServerUiWebInfoTblHTTPSPort_Type()
)
vServerUiWebInfoTblHTTPSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUiWebInfoTblHTTPSPort.setStatus("current")
_VServerUserConfTbl_Object = MibTable
vServerUserConfTbl = _VServerUserConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vServerUserConfTbl.setStatus("obsolete")
_VServerUserConfTblEntry_Object = MibTableRow
vServerUserConfTblEntry = _VServerUserConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 2, 1)
)
vServerUserConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerUserConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerUserConfTblEntry.setStatus("obsolete")
_VServerUserConfTblIndex_Type = Unsigned32
_VServerUserConfTblIndex_Object = MibTableColumn
vServerUserConfTblIndex = _VServerUserConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 2, 1, 1),
    _VServerUserConfTblIndex_Type()
)
vServerUserConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerUserConfTblIndex.setStatus("obsolete")
_VServerUserConfTblClientAccessNum_Type = Unsigned32
_VServerUserConfTblClientAccessNum_Object = MibTableColumn
vServerUserConfTblClientAccessNum = _VServerUserConfTblClientAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 2, 1, 2),
    _VServerUserConfTblClientAccessNum_Type()
)
vServerUserConfTblClientAccessNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUserConfTblClientAccessNum.setStatus("obsolete")


class _VServerUserConfTblUTdisp_Type(OctetString):
    """Custom type vServerUserConfTblUTdisp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerUserConfTblUTdisp_Type.__name__ = "OctetString"
_VServerUserConfTblUTdisp_Object = MibTableColumn
vServerUserConfTblUTdisp = _VServerUserConfTblUTdisp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 2, 1, 3),
    _VServerUserConfTblUTdisp_Type()
)
vServerUserConfTblUTdisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUserConfTblUTdisp.setStatus("obsolete")
_VServerUserConfTblUTIP_Type = IpAddress
_VServerUserConfTblUTIP_Object = MibTableColumn
vServerUserConfTblUTIP = _VServerUserConfTblUTIP_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 2, 1, 4),
    _VServerUserConfTblUTIP_Type()
)
vServerUserConfTblUTIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUserConfTblUTIP.setStatus("obsolete")


class _VServerUserConfTblCUdisp_Type(OctetString):
    """Custom type vServerUserConfTblCUdisp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerUserConfTblCUdisp_Type.__name__ = "OctetString"
_VServerUserConfTblCUdisp_Object = MibTableColumn
vServerUserConfTblCUdisp = _VServerUserConfTblCUdisp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 2, 1, 5),
    _VServerUserConfTblCUdisp_Type()
)
vServerUserConfTblCUdisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUserConfTblCUdisp.setStatus("obsolete")
_VServerUserConfTblCUIP_Type = IpAddress
_VServerUserConfTblCUIP_Object = MibTableColumn
vServerUserConfTblCUIP = _VServerUserConfTblCUIP_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 1, 2, 2, 1, 6),
    _VServerUserConfTblCUIP_Type()
)
vServerUserConfTblCUIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerUserConfTblCUIP.setStatus("obsolete")
_VServerConfFeature_ObjectIdentity = ObjectIdentity
vServerConfFeature = _VServerConfFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 2)
)
_VServerConfFeatureScalars_ObjectIdentity = ObjectIdentity
vServerConfFeatureScalars = _VServerConfFeatureScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 2, 1)
)
_VServerFeatCtrlTblVirtVS_Type = VenturiBooleanType
_VServerFeatCtrlTblVirtVS_Object = MibScalar
vServerFeatCtrlTblVirtVS = _VServerFeatCtrlTblVirtVS_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 2, 1, 1),
    _VServerFeatCtrlTblVirtVS_Type()
)
vServerFeatCtrlTblVirtVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerFeatCtrlTblVirtVS.setStatus("current")
_VServerFeatCtrlTblIpTransparency_Type = VenturiBooleanType
_VServerFeatCtrlTblIpTransparency_Object = MibScalar
vServerFeatCtrlTblIpTransparency = _VServerFeatCtrlTblIpTransparency_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 2, 1, 2),
    _VServerFeatCtrlTblIpTransparency_Type()
)
vServerFeatCtrlTblIpTransparency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFeatCtrlTblIpTransparency.setStatus("current")
_VServerFeatCtrlTblEnableRouting_Type = VenturiBooleanType
_VServerFeatCtrlTblEnableRouting_Object = MibScalar
vServerFeatCtrlTblEnableRouting = _VServerFeatCtrlTblEnableRouting_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 2, 1, 3),
    _VServerFeatCtrlTblEnableRouting_Type()
)
vServerFeatCtrlTblEnableRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFeatCtrlTblEnableRouting.setStatus("current")
_VServerFeatCtrlTblRadiusAcct_Type = VenturiBooleanType
_VServerFeatCtrlTblRadiusAcct_Object = MibScalar
vServerFeatCtrlTblRadiusAcct = _VServerFeatCtrlTblRadiusAcct_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 2, 1, 4),
    _VServerFeatCtrlTblRadiusAcct_Type()
)
vServerFeatCtrlTblRadiusAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFeatCtrlTblRadiusAcct.setStatus("current")
_VServerFeatCtrlTblRtspEnable_Type = VenturiBooleanType
_VServerFeatCtrlTblRtspEnable_Object = MibScalar
vServerFeatCtrlTblRtspEnable = _VServerFeatCtrlTblRtspEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 2, 1, 5),
    _VServerFeatCtrlTblRtspEnable_Type()
)
vServerFeatCtrlTblRtspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFeatCtrlTblRtspEnable.setStatus("current")
_VServerConfPush_ObjectIdentity = ObjectIdentity
vServerConfPush = _VServerConfPush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4)
)
_VServerConfPushScalars_ObjectIdentity = ObjectIdentity
vServerConfPushScalars = _VServerConfPushScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 1)
)
_VServerConfPushTimeout_Type = Unsigned32
_VServerConfPushTimeout_Object = MibScalar
vServerConfPushTimeout = _VServerConfPushTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 1, 1),
    _VServerConfPushTimeout_Type()
)
vServerConfPushTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfPushTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vServerConfPushTimeout.setUnits("seconds")
_VServerConfPushRetryCount_Type = Unsigned32
_VServerConfPushRetryCount_Object = MibScalar
vServerConfPushRetryCount = _VServerConfPushRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 1, 2),
    _VServerConfPushRetryCount_Type()
)
vServerConfPushRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfPushRetryCount.setStatus("current")
_VServerConfPushDeliveryPeriod_Type = Unsigned32
_VServerConfPushDeliveryPeriod_Object = MibScalar
vServerConfPushDeliveryPeriod = _VServerConfPushDeliveryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 1, 3),
    _VServerConfPushDeliveryPeriod_Type()
)
vServerConfPushDeliveryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfPushDeliveryPeriod.setStatus("current")
if mibBuilder.loadTexts:
    vServerConfPushDeliveryPeriod.setUnits("minutes")
_VServerConfigPushCstatsAccountingMode_Type = Unsigned32
_VServerConfigPushCstatsAccountingMode_Object = MibScalar
vServerConfigPushCstatsAccountingMode = _VServerConfigPushCstatsAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 1, 4),
    _VServerConfigPushCstatsAccountingMode_Type()
)
vServerConfigPushCstatsAccountingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfigPushCstatsAccountingMode.setStatus("current")
_VServerConfPushTbls_ObjectIdentity = ObjectIdentity
vServerConfPushTbls = _VServerConfPushTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2)
)
_VServerPushTgtTbl_Object = MibTable
vServerPushTgtTbl = _VServerPushTgtTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vServerPushTgtTbl.setStatus("current")
_VServerPushTgtEntry_Object = MibTableRow
vServerPushTgtEntry = _VServerPushTgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1)
)
vServerPushTgtEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerPushTgtIndex"),
)
if mibBuilder.loadTexts:
    vServerPushTgtEntry.setStatus("current")
_VServerPushTgtIndex_Type = Unsigned32
_VServerPushTgtIndex_Object = MibTableColumn
vServerPushTgtIndex = _VServerPushTgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 1),
    _VServerPushTgtIndex_Type()
)
vServerPushTgtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerPushTgtIndex.setStatus("current")
_VServerPushTgtEnable_Type = VenturiBooleanType
_VServerPushTgtEnable_Object = MibTableColumn
vServerPushTgtEnable = _VServerPushTgtEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 2),
    _VServerPushTgtEnable_Type()
)
vServerPushTgtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushTgtEnable.setStatus("current")


class _VServerPushTgtHost_Type(OctetString):
    """Custom type vServerPushTgtHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerPushTgtHost_Type.__name__ = "OctetString"
_VServerPushTgtHost_Object = MibTableColumn
vServerPushTgtHost = _VServerPushTgtHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 3),
    _VServerPushTgtHost_Type()
)
vServerPushTgtHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushTgtHost.setStatus("current")
_VServerPushTgtPort_Type = Unsigned32
_VServerPushTgtPort_Object = MibTableColumn
vServerPushTgtPort = _VServerPushTgtPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 4),
    _VServerPushTgtPort_Type()
)
vServerPushTgtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushTgtPort.setStatus("current")


class _VServerPushTgtUser_Type(OctetString):
    """Custom type vServerPushTgtUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerPushTgtUser_Type.__name__ = "OctetString"
_VServerPushTgtUser_Object = MibTableColumn
vServerPushTgtUser = _VServerPushTgtUser_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 5),
    _VServerPushTgtUser_Type()
)
vServerPushTgtUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushTgtUser.setStatus("current")


class _VServerPushTgtPassword_Type(OctetString):
    """Custom type vServerPushTgtPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerPushTgtPassword_Type.__name__ = "OctetString"
_VServerPushTgtPassword_Object = MibTableColumn
vServerPushTgtPassword = _VServerPushTgtPassword_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 6),
    _VServerPushTgtPassword_Type()
)
vServerPushTgtPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushTgtPassword.setStatus("current")


class _VServerPushTgtDirectory_Type(OctetString):
    """Custom type vServerPushTgtDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_VServerPushTgtDirectory_Type.__name__ = "OctetString"
_VServerPushTgtDirectory_Object = MibTableColumn
vServerPushTgtDirectory = _VServerPushTgtDirectory_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 7),
    _VServerPushTgtDirectory_Type()
)
vServerPushTgtDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushTgtDirectory.setStatus("current")
_VServerPushTgtTrapNotification_Type = VenturiBooleanType
_VServerPushTgtTrapNotification_Object = MibTableColumn
vServerPushTgtTrapNotification = _VServerPushTgtTrapNotification_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 8),
    _VServerPushTgtTrapNotification_Type()
)
vServerPushTgtTrapNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushTgtTrapNotification.setStatus("current")


class _VServerPushProtocol_Type(Integer32):
    """Custom type vServerPushProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 2),
          ("sftp", 3))
    )


_VServerPushProtocol_Type.__name__ = "Integer32"
_VServerPushProtocol_Object = MibTableColumn
vServerPushProtocol = _VServerPushProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 9),
    _VServerPushProtocol_Type()
)
vServerPushProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushProtocol.setStatus("current")


class _VServerPushFileTypes_Type(Bits):
    """Custom type vServerPushFileTypes based on Bits"""
    namedValues = NamedValues(
        *(("logs", 0),
          ("transactions", 1),
          ("stats", 2),
          ("clientStats", 3),
          ("clientUpg", 4),
          ("cdclogs", 5),
          ("gwcstats", 6))
    )

_VServerPushFileTypes_Type.__name__ = "Bits"
_VServerPushFileTypes_Object = MibTableColumn
vServerPushFileTypes = _VServerPushFileTypes_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 4, 2, 1, 1, 10),
    _VServerPushFileTypes_Type()
)
vServerPushFileTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerPushFileTypes.setStatus("current")
_VServerConfAlert_ObjectIdentity = ObjectIdentity
vServerConfAlert = _VServerConfAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5)
)
_VServerConfAlertScalars_ObjectIdentity = ObjectIdentity
vServerConfAlertScalars = _VServerConfAlertScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1)
)


class _VServerConfAlertEmailTO_Type(OctetString):
    """Custom type vServerConfAlertEmailTO based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerConfAlertEmailTO_Type.__name__ = "OctetString"
_VServerConfAlertEmailTO_Object = MibScalar
vServerConfAlertEmailTO = _VServerConfAlertEmailTO_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1, 1),
    _VServerConfAlertEmailTO_Type()
)
vServerConfAlertEmailTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAlertEmailTO.setStatus("current")


class _VServerConfAlertEmailFROM_Type(OctetString):
    """Custom type vServerConfAlertEmailFROM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerConfAlertEmailFROM_Type.__name__ = "OctetString"
_VServerConfAlertEmailFROM_Object = MibScalar
vServerConfAlertEmailFROM = _VServerConfAlertEmailFROM_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1, 2),
    _VServerConfAlertEmailFROM_Type()
)
vServerConfAlertEmailFROM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAlertEmailFROM.setStatus("current")


class _VServerConfAlertSMTPServer_Type(OctetString):
    """Custom type vServerConfAlertSMTPServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerConfAlertSMTPServer_Type.__name__ = "OctetString"
_VServerConfAlertSMTPServer_Object = MibScalar
vServerConfAlertSMTPServer = _VServerConfAlertSMTPServer_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1, 3),
    _VServerConfAlertSMTPServer_Type()
)
vServerConfAlertSMTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAlertSMTPServer.setStatus("current")
_VServerConfAlertThreshold_Type = VenturiThresholdLevels
_VServerConfAlertThreshold_Object = MibScalar
vServerConfAlertThreshold = _VServerConfAlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1, 4),
    _VServerConfAlertThreshold_Type()
)
vServerConfAlertThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAlertThreshold.setStatus("current")
_VServerConfAlertDebugLogEnable_Type = VenturiBooleanType
_VServerConfAlertDebugLogEnable_Object = MibScalar
vServerConfAlertDebugLogEnable = _VServerConfAlertDebugLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1, 5),
    _VServerConfAlertDebugLogEnable_Type()
)
vServerConfAlertDebugLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAlertDebugLogEnable.setStatus("current")
_VServerConfAlertSNMPTrapsEnable_Type = VenturiBooleanType
_VServerConfAlertSNMPTrapsEnable_Object = MibScalar
vServerConfAlertSNMPTrapsEnable = _VServerConfAlertSNMPTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1, 6),
    _VServerConfAlertSNMPTrapsEnable_Type()
)
vServerConfAlertSNMPTrapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAlertSNMPTrapsEnable.setStatus("current")


class _VServerConfAlertSyslogServer_Type(OctetString):
    """Custom type vServerConfAlertSyslogServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerConfAlertSyslogServer_Type.__name__ = "OctetString"
_VServerConfAlertSyslogServer_Object = MibScalar
vServerConfAlertSyslogServer = _VServerConfAlertSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1, 7),
    _VServerConfAlertSyslogServer_Type()
)
vServerConfAlertSyslogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAlertSyslogServer.setStatus("current")
_VServerConfAlertSyslogFacility_Type = VenturiSyslogFacilityType
_VServerConfAlertSyslogFacility_Object = MibScalar
vServerConfAlertSyslogFacility = _VServerConfAlertSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 1, 8),
    _VServerConfAlertSyslogFacility_Type()
)
vServerConfAlertSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAlertSyslogFacility.setStatus("current")
_VServerConfAlertTbls_ObjectIdentity = ObjectIdentity
vServerConfAlertTbls = _VServerConfAlertTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2)
)
_VServerLogModuleConfTbl_Object = MibTable
vServerLogModuleConfTbl = _VServerLogModuleConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vServerLogModuleConfTbl.setStatus("current")
_VServerLogModuleConfTblEntry_Object = MibTableRow
vServerLogModuleConfTblEntry = _VServerLogModuleConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 1, 1)
)
vServerLogModuleConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerLogModuleConfTblModule"),
)
if mibBuilder.loadTexts:
    vServerLogModuleConfTblEntry.setStatus("current")
_VServerLogModuleConfTblModule_Type = VenturiLogModuleType
_VServerLogModuleConfTblModule_Object = MibTableColumn
vServerLogModuleConfTblModule = _VServerLogModuleConfTblModule_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 1, 1, 1),
    _VServerLogModuleConfTblModule_Type()
)
vServerLogModuleConfTblModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerLogModuleConfTblModule.setStatus("current")
_VServerLogModuleConfTblThreshold_Type = VenturiThresholdLevels
_VServerLogModuleConfTblThreshold_Object = MibTableColumn
vServerLogModuleConfTblThreshold = _VServerLogModuleConfTblThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 1, 1, 2),
    _VServerLogModuleConfTblThreshold_Type()
)
vServerLogModuleConfTblThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerLogModuleConfTblThreshold.setStatus("current")
_VServerAlertRoutingTbl_Object = MibTable
vServerAlertRoutingTbl = _VServerAlertRoutingTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    vServerAlertRoutingTbl.setStatus("current")
_VServerAlertRoutingTblEntry_Object = MibTableRow
vServerAlertRoutingTblEntry = _VServerAlertRoutingTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 2, 1)
)
vServerAlertRoutingTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerAlertIndex"),
)
if mibBuilder.loadTexts:
    vServerAlertRoutingTblEntry.setStatus("current")
_VServerAlertIndex_Type = Unsigned32
_VServerAlertIndex_Object = MibTableColumn
vServerAlertIndex = _VServerAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 2, 1, 1),
    _VServerAlertIndex_Type()
)
vServerAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAlertIndex.setStatus("current")


class _VServerAlertEventName_Type(OctetString):
    """Custom type vServerAlertEventName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerAlertEventName_Type.__name__ = "OctetString"
_VServerAlertEventName_Object = MibTableColumn
vServerAlertEventName = _VServerAlertEventName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 2, 1, 2),
    _VServerAlertEventName_Type()
)
vServerAlertEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAlertEventName.setStatus("current")
_VServerAlertPriority_Type = VenturiLogLevels
_VServerAlertPriority_Object = MibTableColumn
vServerAlertPriority = _VServerAlertPriority_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 2, 1, 3),
    _VServerAlertPriority_Type()
)
vServerAlertPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAlertPriority.setStatus("current")


class _VServerAlertMethods_Type(Bits):
    """Custom type vServerAlertMethods based on Bits"""
    namedValues = NamedValues(
        *(("logfile", 0),
          ("email", 1),
          ("snmptrap", 2),
          ("syslog", 3))
    )

_VServerAlertMethods_Type.__name__ = "Bits"
_VServerAlertMethods_Object = MibTableColumn
vServerAlertMethods = _VServerAlertMethods_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 2, 1, 4),
    _VServerAlertMethods_Type()
)
vServerAlertMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAlertMethods.setStatus("current")
_VServerAlertCurrent_Type = VenturiBooleanType
_VServerAlertCurrent_Object = MibTableColumn
vServerAlertCurrent = _VServerAlertCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 2, 1, 5),
    _VServerAlertCurrent_Type()
)
vServerAlertCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAlertCurrent.setStatus("current")
_VServerAlertTrapSeverity_Type = VenturiTrapSeverity
_VServerAlertTrapSeverity_Object = MibTableColumn
vServerAlertTrapSeverity = _VServerAlertTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 5, 2, 2, 1, 6),
    _VServerAlertTrapSeverity_Type()
)
vServerAlertTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAlertTrapSeverity.setStatus("current")
_VServerConfSnmp_ObjectIdentity = ObjectIdentity
vServerConfSnmp = _VServerConfSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6)
)
_VServerConfSnmpScalars_ObjectIdentity = ObjectIdentity
vServerConfSnmpScalars = _VServerConfSnmpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1)
)
_VServerSnmpConfTblAgentEnabled_Type = VenturiBooleanType
_VServerSnmpConfTblAgentEnabled_Object = MibScalar
vServerSnmpConfTblAgentEnabled = _VServerSnmpConfTblAgentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 1),
    _VServerSnmpConfTblAgentEnabled_Type()
)
vServerSnmpConfTblAgentEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSnmpConfTblAgentEnabled.setStatus("current")
_VServerSnmpConfTblAgentPort_Type = Unsigned32
_VServerSnmpConfTblAgentPort_Object = MibScalar
vServerSnmpConfTblAgentPort = _VServerSnmpConfTblAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 2),
    _VServerSnmpConfTblAgentPort_Type()
)
vServerSnmpConfTblAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSnmpConfTblAgentPort.setStatus("current")


class _VServerSnmpConfTblReadOnlyCommunity_Type(OctetString):
    """Custom type vServerSnmpConfTblReadOnlyCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerSnmpConfTblReadOnlyCommunity_Type.__name__ = "OctetString"
_VServerSnmpConfTblReadOnlyCommunity_Object = MibScalar
vServerSnmpConfTblReadOnlyCommunity = _VServerSnmpConfTblReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 3),
    _VServerSnmpConfTblReadOnlyCommunity_Type()
)
vServerSnmpConfTblReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSnmpConfTblReadOnlyCommunity.setStatus("current")


class _VServerSnmpConfTblReadWriteCommunity_Type(OctetString):
    """Custom type vServerSnmpConfTblReadWriteCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerSnmpConfTblReadWriteCommunity_Type.__name__ = "OctetString"
_VServerSnmpConfTblReadWriteCommunity_Object = MibScalar
vServerSnmpConfTblReadWriteCommunity = _VServerSnmpConfTblReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 4),
    _VServerSnmpConfTblReadWriteCommunity_Type()
)
vServerSnmpConfTblReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSnmpConfTblReadWriteCommunity.setStatus("current")


class _VServerSnmpConfTblSysContact_Type(OctetString):
    """Custom type vServerSnmpConfTblSysContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerSnmpConfTblSysContact_Type.__name__ = "OctetString"
_VServerSnmpConfTblSysContact_Object = MibScalar
vServerSnmpConfTblSysContact = _VServerSnmpConfTblSysContact_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 5),
    _VServerSnmpConfTblSysContact_Type()
)
vServerSnmpConfTblSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSnmpConfTblSysContact.setStatus("current")


class _VServerSnmpConfTblSysLocation_Type(OctetString):
    """Custom type vServerSnmpConfTblSysLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerSnmpConfTblSysLocation_Type.__name__ = "OctetString"
_VServerSnmpConfTblSysLocation_Object = MibScalar
vServerSnmpConfTblSysLocation = _VServerSnmpConfTblSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 6),
    _VServerSnmpConfTblSysLocation_Type()
)
vServerSnmpConfTblSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSnmpConfTblSysLocation.setStatus("current")
_VServerSNMPTrapTgtRetryCount_Type = Unsigned32
_VServerSNMPTrapTgtRetryCount_Object = MibScalar
vServerSNMPTrapTgtRetryCount = _VServerSNMPTrapTgtRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 7),
    _VServerSNMPTrapTgtRetryCount_Type()
)
vServerSNMPTrapTgtRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtRetryCount.setStatus("current")
_VServerSNMPTrapTgtTimeout_Type = Unsigned32
_VServerSNMPTrapTgtTimeout_Object = MibScalar
vServerSNMPTrapTgtTimeout = _VServerSNMPTrapTgtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 8),
    _VServerSNMPTrapTgtTimeout_Type()
)
vServerSNMPTrapTgtTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtTimeout.setStatus("current")
_VServerSNMPTrapTgtTrapFrequency_Type = Unsigned32
_VServerSNMPTrapTgtTrapFrequency_Object = MibScalar
vServerSNMPTrapTgtTrapFrequency = _VServerSNMPTrapTgtTrapFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 9),
    _VServerSNMPTrapTgtTrapFrequency_Type()
)
vServerSNMPTrapTgtTrapFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtTrapFrequency.setStatus("current")
_VServerSnmpConfTblHealthCheckAgentEnabled_Type = VenturiBooleanType
_VServerSnmpConfTblHealthCheckAgentEnabled_Object = MibScalar
vServerSnmpConfTblHealthCheckAgentEnabled = _VServerSnmpConfTblHealthCheckAgentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 1, 10),
    _VServerSnmpConfTblHealthCheckAgentEnabled_Type()
)
vServerSnmpConfTblHealthCheckAgentEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSnmpConfTblHealthCheckAgentEnabled.setStatus("current")
_VServerConfSnmpTbls_ObjectIdentity = ObjectIdentity
vServerConfSnmpTbls = _VServerConfSnmpTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 2)
)
_VServerSNMPTrapTgt_Object = MibTable
vServerSNMPTrapTgt = _VServerSNMPTrapTgt_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vServerSNMPTrapTgt.setStatus("current")
_VServerSNMPTrapTgtEntry_Object = MibTableRow
vServerSNMPTrapTgtEntry = _VServerSNMPTrapTgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 2, 1, 1)
)
vServerSNMPTrapTgtEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerSNMPTrapTgtIndex"),
)
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtEntry.setStatus("current")
_VServerSNMPTrapTgtIndex_Type = Unsigned32
_VServerSNMPTrapTgtIndex_Object = MibTableColumn
vServerSNMPTrapTgtIndex = _VServerSNMPTrapTgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 2, 1, 1, 1),
    _VServerSNMPTrapTgtIndex_Type()
)
vServerSNMPTrapTgtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtIndex.setStatus("current")


class _VServerSNMPTrapTgtHost_Type(OctetString):
    """Custom type vServerSNMPTrapTgtHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerSNMPTrapTgtHost_Type.__name__ = "OctetString"
_VServerSNMPTrapTgtHost_Object = MibTableColumn
vServerSNMPTrapTgtHost = _VServerSNMPTrapTgtHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 2, 1, 1, 2),
    _VServerSNMPTrapTgtHost_Type()
)
vServerSNMPTrapTgtHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtHost.setStatus("current")
_VServerSNMPTrapTgtPort_Type = Unsigned32
_VServerSNMPTrapTgtPort_Object = MibTableColumn
vServerSNMPTrapTgtPort = _VServerSNMPTrapTgtPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 2, 1, 1, 3),
    _VServerSNMPTrapTgtPort_Type()
)
vServerSNMPTrapTgtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtPort.setStatus("current")


class _VServerSNMPTrapTgtCommunity_Type(OctetString):
    """Custom type vServerSNMPTrapTgtCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerSNMPTrapTgtCommunity_Type.__name__ = "OctetString"
_VServerSNMPTrapTgtCommunity_Object = MibTableColumn
vServerSNMPTrapTgtCommunity = _VServerSNMPTrapTgtCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 2, 1, 1, 4),
    _VServerSNMPTrapTgtCommunity_Type()
)
vServerSNMPTrapTgtCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtCommunity.setStatus("current")
_VServerSNMPTrapTgtTrapType_Type = VenturiTrapType
_VServerSNMPTrapTgtTrapType_Object = MibTableColumn
vServerSNMPTrapTgtTrapType = _VServerSNMPTrapTgtTrapType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 6, 2, 1, 1, 5),
    _VServerSNMPTrapTgtTrapType_Type()
)
vServerSNMPTrapTgtTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSNMPTrapTgtTrapType.setStatus("current")
_VServerConfLog_ObjectIdentity = ObjectIdentity
vServerConfLog = _VServerConfLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 7)
)
_VServerConfLogScalars_ObjectIdentity = ObjectIdentity
vServerConfLogScalars = _VServerConfLogScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 7, 1)
)
_VServerHttpLogFullUrl_Type = VenturiBooleanType
_VServerHttpLogFullUrl_Object = MibScalar
vServerHttpLogFullUrl = _VServerHttpLogFullUrl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 7, 1, 1),
    _VServerHttpLogFullUrl_Type()
)
vServerHttpLogFullUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpLogFullUrl.setStatus("current")
_VServerHttpLogHideIp_Type = VenturiBooleanType
_VServerHttpLogHideIp_Object = MibScalar
vServerHttpLogHideIp = _VServerHttpLogHideIp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 7, 1, 2),
    _VServerHttpLogHideIp_Type()
)
vServerHttpLogHideIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerHttpLogHideIp.setStatus("current")
_VServerTransactionLoggingEnabled_Type = VenturiBooleanType
_VServerTransactionLoggingEnabled_Object = MibScalar
vServerTransactionLoggingEnabled = _VServerTransactionLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 7, 1, 3),
    _VServerTransactionLoggingEnabled_Type()
)
vServerTransactionLoggingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerTransactionLoggingEnabled.setStatus("current")
_VServerDisconnectedUserLoggingEnabled_Type = VenturiBooleanType
_VServerDisconnectedUserLoggingEnabled_Object = MibScalar
vServerDisconnectedUserLoggingEnabled = _VServerDisconnectedUserLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 7, 1, 4),
    _VServerDisconnectedUserLoggingEnabled_Type()
)
vServerDisconnectedUserLoggingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerDisconnectedUserLoggingEnabled.setStatus("current")
_VServerConfLogTbls_ObjectIdentity = ObjectIdentity
vServerConfLogTbls = _VServerConfLogTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 7, 2)
)
_VServerConfCache_ObjectIdentity = ObjectIdentity
vServerConfCache = _VServerConfCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8)
)
_VServerConfCacheScalars_ObjectIdentity = ObjectIdentity
vServerConfCacheScalars = _VServerConfCacheScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 1)
)
_VServerMaxCacheObjectSize_Type = Unsigned32
_VServerMaxCacheObjectSize_Object = MibScalar
vServerMaxCacheObjectSize = _VServerMaxCacheObjectSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 1, 1),
    _VServerMaxCacheObjectSize_Type()
)
vServerMaxCacheObjectSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerMaxCacheObjectSize.setStatus("current")
_VServerConfCacheTbls_ObjectIdentity = ObjectIdentity
vServerConfCacheTbls = _VServerConfCacheTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2)
)
_VServerCacheBypassTbl_Object = MibTable
vServerCacheBypassTbl = _VServerCacheBypassTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vServerCacheBypassTbl.setStatus("current")
_VServerCacheBypassTblEntry_Object = MibTableRow
vServerCacheBypassTblEntry = _VServerCacheBypassTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 1, 1)
)
vServerCacheBypassTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerCacheBypassTblIndex"),
)
if mibBuilder.loadTexts:
    vServerCacheBypassTblEntry.setStatus("current")
_VServerCacheBypassTblIndex_Type = Unsigned32
_VServerCacheBypassTblIndex_Object = MibTableColumn
vServerCacheBypassTblIndex = _VServerCacheBypassTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 1, 1, 1),
    _VServerCacheBypassTblIndex_Type()
)
vServerCacheBypassTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCacheBypassTblIndex.setStatus("current")


class _VServerCacheBypassTblHostname_Type(OctetString):
    """Custom type vServerCacheBypassTblHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerCacheBypassTblHostname_Type.__name__ = "OctetString"
_VServerCacheBypassTblHostname_Object = MibTableColumn
vServerCacheBypassTblHostname = _VServerCacheBypassTblHostname_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 1, 1, 2),
    _VServerCacheBypassTblHostname_Type()
)
vServerCacheBypassTblHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheBypassTblHostname.setStatus("current")
_VServerCacheBypassTblIpaddr_Type = IpAddress
_VServerCacheBypassTblIpaddr_Object = MibTableColumn
vServerCacheBypassTblIpaddr = _VServerCacheBypassTblIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 1, 1, 3),
    _VServerCacheBypassTblIpaddr_Type()
)
vServerCacheBypassTblIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheBypassTblIpaddr.setStatus("current")


class _VServerCacheBypassTblPortRange_Type(OctetString):
    """Custom type vServerCacheBypassTblPortRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerCacheBypassTblPortRange_Type.__name__ = "OctetString"
_VServerCacheBypassTblPortRange_Object = MibTableColumn
vServerCacheBypassTblPortRange = _VServerCacheBypassTblPortRange_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 1, 1, 4),
    _VServerCacheBypassTblPortRange_Type()
)
vServerCacheBypassTblPortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheBypassTblPortRange.setStatus("current")


class _VServerCacheBypassTblDestinations_Type(OctetString):
    """Custom type vServerCacheBypassTblDestinations based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerCacheBypassTblDestinations_Type.__name__ = "OctetString"
_VServerCacheBypassTblDestinations_Object = MibTableColumn
vServerCacheBypassTblDestinations = _VServerCacheBypassTblDestinations_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 1, 1, 5),
    _VServerCacheBypassTblDestinations_Type()
)
vServerCacheBypassTblDestinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheBypassTblDestinations.setStatus("current")
_VServerCacheConfTbl_Object = MibTable
vServerCacheConfTbl = _VServerCacheConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 2)
)
if mibBuilder.loadTexts:
    vServerCacheConfTbl.setStatus("current")
_VServerCacheConfTblEntry_Object = MibTableRow
vServerCacheConfTblEntry = _VServerCacheConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 2, 1)
)
vServerCacheConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerCacheConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerCacheConfTblEntry.setStatus("current")
_VServerCacheConfTblIndex_Type = Unsigned32
_VServerCacheConfTblIndex_Object = MibTableColumn
vServerCacheConfTblIndex = _VServerCacheConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 2, 1, 1),
    _VServerCacheConfTblIndex_Type()
)
vServerCacheConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCacheConfTblIndex.setStatus("current")
_VServerCacheConfTblMode_Type = Unsigned32
_VServerCacheConfTblMode_Object = MibTableColumn
vServerCacheConfTblMode = _VServerCacheConfTblMode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 2, 1, 2),
    _VServerCacheConfTblMode_Type()
)
vServerCacheConfTblMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheConfTblMode.setStatus("current")


class _VServerCacheConfTblExtCacheURL_Type(OctetString):
    """Custom type vServerCacheConfTblExtCacheURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerCacheConfTblExtCacheURL_Type.__name__ = "OctetString"
_VServerCacheConfTblExtCacheURL_Object = MibTableColumn
vServerCacheConfTblExtCacheURL = _VServerCacheConfTblExtCacheURL_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 2, 1, 3),
    _VServerCacheConfTblExtCacheURL_Type()
)
vServerCacheConfTblExtCacheURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheConfTblExtCacheURL.setStatus("current")
_VServerCacheACLConfTbl_Object = MibTable
vServerCacheACLConfTbl = _VServerCacheACLConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 3)
)
if mibBuilder.loadTexts:
    vServerCacheACLConfTbl.setStatus("current")
_VServerCacheACLConfTblEntry_Object = MibTableRow
vServerCacheACLConfTblEntry = _VServerCacheACLConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 3, 1)
)
vServerCacheACLConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerCacheACLConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerCacheACLConfTblEntry.setStatus("current")
_VServerCacheACLConfTblIndex_Type = Unsigned32
_VServerCacheACLConfTblIndex_Object = MibTableColumn
vServerCacheACLConfTblIndex = _VServerCacheACLConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 3, 1, 1),
    _VServerCacheACLConfTblIndex_Type()
)
vServerCacheACLConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCacheACLConfTblIndex.setStatus("current")


class _VServerCacheACLConfTblName_Type(OctetString):
    """Custom type vServerCacheACLConfTblName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VServerCacheACLConfTblName_Type.__name__ = "OctetString"
_VServerCacheACLConfTblName_Object = MibTableColumn
vServerCacheACLConfTblName = _VServerCacheACLConfTblName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 3, 1, 2),
    _VServerCacheACLConfTblName_Type()
)
vServerCacheACLConfTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheACLConfTblName.setStatus("current")


class _VServerCacheACLConfTblMatchType_Type(OctetString):
    """Custom type vServerCacheACLConfTblMatchType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VServerCacheACLConfTblMatchType_Type.__name__ = "OctetString"
_VServerCacheACLConfTblMatchType_Object = MibTableColumn
vServerCacheACLConfTblMatchType = _VServerCacheACLConfTblMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 3, 1, 3),
    _VServerCacheACLConfTblMatchType_Type()
)
vServerCacheACLConfTblMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheACLConfTblMatchType.setStatus("current")


class _VServerCacheACLConfTblMatchArgs_Type(OctetString):
    """Custom type vServerCacheACLConfTblMatchArgs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VServerCacheACLConfTblMatchArgs_Type.__name__ = "OctetString"
_VServerCacheACLConfTblMatchArgs_Object = MibTableColumn
vServerCacheACLConfTblMatchArgs = _VServerCacheACLConfTblMatchArgs_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 3, 1, 4),
    _VServerCacheACLConfTblMatchArgs_Type()
)
vServerCacheACLConfTblMatchArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheACLConfTblMatchArgs.setStatus("current")
_VServerCacheRPConfTbl_Object = MibTable
vServerCacheRPConfTbl = _VServerCacheRPConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 4)
)
if mibBuilder.loadTexts:
    vServerCacheRPConfTbl.setStatus("current")
_VServerCacheRPConfTblEntry_Object = MibTableRow
vServerCacheRPConfTblEntry = _VServerCacheRPConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 4, 1)
)
vServerCacheRPConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerCacheRPConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerCacheRPConfTblEntry.setStatus("current")
_VServerCacheRPConfTblIndex_Type = Unsigned32
_VServerCacheRPConfTblIndex_Object = MibTableColumn
vServerCacheRPConfTblIndex = _VServerCacheRPConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 4, 1, 1),
    _VServerCacheRPConfTblIndex_Type()
)
vServerCacheRPConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCacheRPConfTblIndex.setStatus("current")


class _VServerCacheRPConfTblPattern_Type(OctetString):
    """Custom type vServerCacheRPConfTblPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VServerCacheRPConfTblPattern_Type.__name__ = "OctetString"
_VServerCacheRPConfTblPattern_Object = MibTableColumn
vServerCacheRPConfTblPattern = _VServerCacheRPConfTblPattern_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 4, 1, 2),
    _VServerCacheRPConfTblPattern_Type()
)
vServerCacheRPConfTblPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheRPConfTblPattern.setStatus("current")
_VServerCacheRPConfTblMin_Type = Unsigned32
_VServerCacheRPConfTblMin_Object = MibTableColumn
vServerCacheRPConfTblMin = _VServerCacheRPConfTblMin_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 4, 1, 3),
    _VServerCacheRPConfTblMin_Type()
)
vServerCacheRPConfTblMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheRPConfTblMin.setStatus("current")
_VServerCacheRPConfTblMax_Type = Unsigned32
_VServerCacheRPConfTblMax_Object = MibTableColumn
vServerCacheRPConfTblMax = _VServerCacheRPConfTblMax_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 4, 1, 4),
    _VServerCacheRPConfTblMax_Type()
)
vServerCacheRPConfTblMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheRPConfTblMax.setStatus("current")
_VServerCacheRPConfTblPercent_Type = Unsigned32
_VServerCacheRPConfTblPercent_Object = MibTableColumn
vServerCacheRPConfTblPercent = _VServerCacheRPConfTblPercent_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 4, 1, 5),
    _VServerCacheRPConfTblPercent_Type()
)
vServerCacheRPConfTblPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheRPConfTblPercent.setStatus("current")
_VServerCacheHierarchyConfTbl_Object = MibTable
vServerCacheHierarchyConfTbl = _VServerCacheHierarchyConfTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 5)
)
if mibBuilder.loadTexts:
    vServerCacheHierarchyConfTbl.setStatus("current")
_VServerCacheHierarchyConfTblEntry_Object = MibTableRow
vServerCacheHierarchyConfTblEntry = _VServerCacheHierarchyConfTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 5, 1)
)
vServerCacheHierarchyConfTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerCacheHierarchyConfTblIndex"),
)
if mibBuilder.loadTexts:
    vServerCacheHierarchyConfTblEntry.setStatus("current")
_VServerCacheHierarchyConfTblIndex_Type = Unsigned32
_VServerCacheHierarchyConfTblIndex_Object = MibTableColumn
vServerCacheHierarchyConfTblIndex = _VServerCacheHierarchyConfTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 5, 1, 1),
    _VServerCacheHierarchyConfTblIndex_Type()
)
vServerCacheHierarchyConfTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCacheHierarchyConfTblIndex.setStatus("current")


class _VServerCacheHierarchyConfTblIpAndPort_Type(OctetString):
    """Custom type vServerCacheHierarchyConfTblIpAndPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerCacheHierarchyConfTblIpAndPort_Type.__name__ = "OctetString"
_VServerCacheHierarchyConfTblIpAndPort_Object = MibTableColumn
vServerCacheHierarchyConfTblIpAndPort = _VServerCacheHierarchyConfTblIpAndPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 5, 1, 2),
    _VServerCacheHierarchyConfTblIpAndPort_Type()
)
vServerCacheHierarchyConfTblIpAndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheHierarchyConfTblIpAndPort.setStatus("current")


class _VServerCacheHierarchyConfTblRelationType_Type(OctetString):
    """Custom type vServerCacheHierarchyConfTblRelationType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VServerCacheHierarchyConfTblRelationType_Type.__name__ = "OctetString"
_VServerCacheHierarchyConfTblRelationType_Object = MibTableColumn
vServerCacheHierarchyConfTblRelationType = _VServerCacheHierarchyConfTblRelationType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 8, 2, 5, 1, 3),
    _VServerCacheHierarchyConfTblRelationType_Type()
)
vServerCacheHierarchyConfTblRelationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerCacheHierarchyConfTblRelationType.setStatus("current")
_VServerConfAuth_ObjectIdentity = ObjectIdentity
vServerConfAuth = _VServerConfAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9)
)
_VServerConfAuthScalars_ObjectIdentity = ObjectIdentity
vServerConfAuthScalars = _VServerConfAuthScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 1)
)


class _VServerConfAuthMethod_Type(Integer32):
    """Custom type vServerConfAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authnone", 1),
          ("authsimple", 2),
          ("authradius", 3))
    )


_VServerConfAuthMethod_Type.__name__ = "Integer32"
_VServerConfAuthMethod_Object = MibScalar
vServerConfAuthMethod = _VServerConfAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 1, 1),
    _VServerConfAuthMethod_Type()
)
vServerConfAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAuthMethod.setStatus("current")


class _VServerConfAuthString_Type(OctetString):
    """Custom type vServerConfAuthString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerConfAuthString_Type.__name__ = "OctetString"
_VServerConfAuthString_Object = MibScalar
vServerConfAuthString = _VServerConfAuthString_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 1, 2),
    _VServerConfAuthString_Type()
)
vServerConfAuthString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfAuthString.setStatus("current")
_VServerConfAuthTbls_ObjectIdentity = ObjectIdentity
vServerConfAuthTbls = _VServerConfAuthTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2)
)
_VServerradiusCfgTbl_Object = MibTable
vServerradiusCfgTbl = _VServerradiusCfgTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1)
)
if mibBuilder.loadTexts:
    vServerradiusCfgTbl.setStatus("current")
_VServerradiusCfgTblEntry_Object = MibTableRow
vServerradiusCfgTblEntry = _VServerradiusCfgTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1)
)
vServerradiusCfgTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerradiusCfgTblIndex"),
)
if mibBuilder.loadTexts:
    vServerradiusCfgTblEntry.setStatus("current")
_VServerradiusCfgTblIndex_Type = Unsigned32
_VServerradiusCfgTblIndex_Object = MibTableColumn
vServerradiusCfgTblIndex = _VServerradiusCfgTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 1),
    _VServerradiusCfgTblIndex_Type()
)
vServerradiusCfgTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerradiusCfgTblIndex.setStatus("current")
_VServerradiusCfgTblRadEnable_Type = VenturiBooleanType
_VServerradiusCfgTblRadEnable_Object = MibTableColumn
vServerradiusCfgTblRadEnable = _VServerradiusCfgTblRadEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 2),
    _VServerradiusCfgTblRadEnable_Type()
)
vServerradiusCfgTblRadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblRadEnable.setStatus("current")
_VServerradiusCfgTblRadSvrRetryCount_Type = Integer32
_VServerradiusCfgTblRadSvrRetryCount_Object = MibTableColumn
vServerradiusCfgTblRadSvrRetryCount = _VServerradiusCfgTblRadSvrRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 3),
    _VServerradiusCfgTblRadSvrRetryCount_Type()
)
vServerradiusCfgTblRadSvrRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblRadSvrRetryCount.setStatus("current")
_VServerradiusCfgTblRadSvrTimeout_Type = Integer32
_VServerradiusCfgTblRadSvrTimeout_Object = MibTableColumn
vServerradiusCfgTblRadSvrTimeout = _VServerradiusCfgTblRadSvrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 4),
    _VServerradiusCfgTblRadSvrTimeout_Type()
)
vServerradiusCfgTblRadSvrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblRadSvrTimeout.setStatus("current")


class _VServerradiusCfgTblRadSvrKey_Type(OctetString):
    """Custom type vServerradiusCfgTblRadSvrKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerradiusCfgTblRadSvrKey_Type.__name__ = "OctetString"
_VServerradiusCfgTblRadSvrKey_Object = MibTableColumn
vServerradiusCfgTblRadSvrKey = _VServerradiusCfgTblRadSvrKey_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 5),
    _VServerradiusCfgTblRadSvrKey_Type()
)
vServerradiusCfgTblRadSvrKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblRadSvrKey.setStatus("current")
_VServerradiusCfgTblRadSvrCount_Type = Integer32
_VServerradiusCfgTblRadSvrCount_Object = MibTableColumn
vServerradiusCfgTblRadSvrCount = _VServerradiusCfgTblRadSvrCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 6),
    _VServerradiusCfgTblRadSvrCount_Type()
)
vServerradiusCfgTblRadSvrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblRadSvrCount.setStatus("current")
_VServerradiusCfgTblListenPort_Type = Integer32
_VServerradiusCfgTblListenPort_Object = MibTableColumn
vServerradiusCfgTblListenPort = _VServerradiusCfgTblListenPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 7),
    _VServerradiusCfgTblListenPort_Type()
)
vServerradiusCfgTblListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblListenPort.setStatus("current")
_VServerradiusCfgTblAccountEnable_Type = VenturiBooleanType
_VServerradiusCfgTblAccountEnable_Object = MibTableColumn
vServerradiusCfgTblAccountEnable = _VServerradiusCfgTblAccountEnable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 8),
    _VServerradiusCfgTblAccountEnable_Type()
)
vServerradiusCfgTblAccountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblAccountEnable.setStatus("current")
_VServerradiusCfgTblServerHost_Type = IpAddress
_VServerradiusCfgTblServerHost_Object = MibTableColumn
vServerradiusCfgTblServerHost = _VServerradiusCfgTblServerHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 9),
    _VServerradiusCfgTblServerHost_Type()
)
vServerradiusCfgTblServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblServerHost.setStatus("current")
_VServerradiusCfgTblServerPort_Type = Integer32
_VServerradiusCfgTblServerPort_Object = MibTableColumn
vServerradiusCfgTblServerPort = _VServerradiusCfgTblServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 10),
    _VServerradiusCfgTblServerPort_Type()
)
vServerradiusCfgTblServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblServerPort.setStatus("current")
_VServerradiusCfgTblSharedSecret_Type = OctetString
_VServerradiusCfgTblSharedSecret_Object = MibTableColumn
vServerradiusCfgTblSharedSecret = _VServerradiusCfgTblSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 1, 1, 11),
    _VServerradiusCfgTblSharedSecret_Type()
)
vServerradiusCfgTblSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusCfgTblSharedSecret.setStatus("current")
_VServerradiusSvrCfgTbl_Object = MibTable
vServerradiusSvrCfgTbl = _VServerradiusSvrCfgTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 2)
)
if mibBuilder.loadTexts:
    vServerradiusSvrCfgTbl.setStatus("current")
_VServerradiusSvrCfgTblEntry_Object = MibTableRow
vServerradiusSvrCfgTblEntry = _VServerradiusSvrCfgTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 2, 1)
)
vServerradiusSvrCfgTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerradiusSvrCfgTblIndex"),
)
if mibBuilder.loadTexts:
    vServerradiusSvrCfgTblEntry.setStatus("current")
_VServerradiusSvrCfgTblIndex_Type = Unsigned32
_VServerradiusSvrCfgTblIndex_Object = MibTableColumn
vServerradiusSvrCfgTblIndex = _VServerradiusSvrCfgTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 2, 1, 1),
    _VServerradiusSvrCfgTblIndex_Type()
)
vServerradiusSvrCfgTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerradiusSvrCfgTblIndex.setStatus("current")
_VServerradiusSvrCfgTblRadSvrAddr_Type = IpAddress
_VServerradiusSvrCfgTblRadSvrAddr_Object = MibTableColumn
vServerradiusSvrCfgTblRadSvrAddr = _VServerradiusSvrCfgTblRadSvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 2, 1, 2),
    _VServerradiusSvrCfgTblRadSvrAddr_Type()
)
vServerradiusSvrCfgTblRadSvrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusSvrCfgTblRadSvrAddr.setStatus("current")
_VServerradiusSvrCfgTblRadSvrAuthPort_Type = Integer32
_VServerradiusSvrCfgTblRadSvrAuthPort_Object = MibTableColumn
vServerradiusSvrCfgTblRadSvrAuthPort = _VServerradiusSvrCfgTblRadSvrAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 2, 1, 3),
    _VServerradiusSvrCfgTblRadSvrAuthPort_Type()
)
vServerradiusSvrCfgTblRadSvrAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusSvrCfgTblRadSvrAuthPort.setStatus("current")
_VServerradiusSvrCfgTblRadSvrAcctPort_Type = Integer32
_VServerradiusSvrCfgTblRadSvrAcctPort_Object = MibTableColumn
vServerradiusSvrCfgTblRadSvrAcctPort = _VServerradiusSvrCfgTblRadSvrAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 2, 1, 4),
    _VServerradiusSvrCfgTblRadSvrAcctPort_Type()
)
vServerradiusSvrCfgTblRadSvrAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusSvrCfgTblRadSvrAcctPort.setStatus("current")
_VServerradiusSvrCfgTblRadSvrActive_Type = VenturiBooleanType
_VServerradiusSvrCfgTblRadSvrActive_Object = MibTableColumn
vServerradiusSvrCfgTblRadSvrActive = _VServerradiusSvrCfgTblRadSvrActive_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 2, 1, 5),
    _VServerradiusSvrCfgTblRadSvrActive_Type()
)
vServerradiusSvrCfgTblRadSvrActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerradiusSvrCfgTblRadSvrActive.setStatus("current")
_VServerAuthAllowDenyTbl_Object = MibTable
vServerAuthAllowDenyTbl = _VServerAuthAllowDenyTbl_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 3)
)
if mibBuilder.loadTexts:
    vServerAuthAllowDenyTbl.setStatus("current")
_VServerAuthAllowDenyTblEntry_Object = MibTableRow
vServerAuthAllowDenyTblEntry = _VServerAuthAllowDenyTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 3, 1)
)
vServerAuthAllowDenyTblEntry.setIndexNames(
    (0, "VENTURI-SERVER-CONFIG-MIB", "vServerAuthAllowDenyTblIndex"),
)
if mibBuilder.loadTexts:
    vServerAuthAllowDenyTblEntry.setStatus("current")
_VServerAuthAllowDenyTblIndex_Type = Unsigned32
_VServerAuthAllowDenyTblIndex_Object = MibTableColumn
vServerAuthAllowDenyTblIndex = _VServerAuthAllowDenyTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 3, 1, 1),
    _VServerAuthAllowDenyTblIndex_Type()
)
vServerAuthAllowDenyTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAuthAllowDenyTblIndex.setStatus("current")
_VServerAuthAllowDenyTblAllowFlag_Type = VenturiBooleanType
_VServerAuthAllowDenyTblAllowFlag_Object = MibTableColumn
vServerAuthAllowDenyTblAllowFlag = _VServerAuthAllowDenyTblAllowFlag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 3, 1, 2),
    _VServerAuthAllowDenyTblAllowFlag_Type()
)
vServerAuthAllowDenyTblAllowFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAuthAllowDenyTblAllowFlag.setStatus("current")


class _VServerAuthAllowDenyTblPattern_Type(OctetString):
    """Custom type vServerAuthAllowDenyTblPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerAuthAllowDenyTblPattern_Type.__name__ = "OctetString"
_VServerAuthAllowDenyTblPattern_Object = MibTableColumn
vServerAuthAllowDenyTblPattern = _VServerAuthAllowDenyTblPattern_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 9, 2, 3, 1, 3),
    _VServerAuthAllowDenyTblPattern_Type()
)
vServerAuthAllowDenyTblPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerAuthAllowDenyTblPattern.setStatus("current")
_VServerConfScheduledBoot_ObjectIdentity = ObjectIdentity
vServerConfScheduledBoot = _VServerConfScheduledBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10)
)
_VServerConfScheduledBootScalars_ObjectIdentity = ObjectIdentity
vServerConfScheduledBootScalars = _VServerConfScheduledBootScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10, 1)
)


class _VServerConfScheduledBootActive_Type(Integer32):
    """Custom type vServerConfScheduledBootActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rebootnone", 1),
          ("rebootsched", 2),
          ("rebootcancel", 3))
    )


_VServerConfScheduledBootActive_Type.__name__ = "Integer32"
_VServerConfScheduledBootActive_Object = MibScalar
vServerConfScheduledBootActive = _VServerConfScheduledBootActive_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10, 1, 1),
    _VServerConfScheduledBootActive_Type()
)
vServerConfScheduledBootActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfScheduledBootActive.setStatus("current")


class _VServerConfScheduledBootMode_Type(Integer32):
    """Custom type vServerConfScheduledBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rebootperiodic", 1),
          ("rebootat", 2),
          ("rebootin", 3))
    )


_VServerConfScheduledBootMode_Type.__name__ = "Integer32"
_VServerConfScheduledBootMode_Object = MibScalar
vServerConfScheduledBootMode = _VServerConfScheduledBootMode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10, 1, 2),
    _VServerConfScheduledBootMode_Type()
)
vServerConfScheduledBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfScheduledBootMode.setStatus("current")
_VServerConfScheduledBootMonth_Type = Unsigned32
_VServerConfScheduledBootMonth_Object = MibScalar
vServerConfScheduledBootMonth = _VServerConfScheduledBootMonth_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10, 1, 3),
    _VServerConfScheduledBootMonth_Type()
)
vServerConfScheduledBootMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfScheduledBootMonth.setStatus("current")
_VServerConfScheduledBootDay_Type = Unsigned32
_VServerConfScheduledBootDay_Object = MibScalar
vServerConfScheduledBootDay = _VServerConfScheduledBootDay_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10, 1, 4),
    _VServerConfScheduledBootDay_Type()
)
vServerConfScheduledBootDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfScheduledBootDay.setStatus("current")
_VServerConfScheduledBootHour_Type = Unsigned32
_VServerConfScheduledBootHour_Object = MibScalar
vServerConfScheduledBootHour = _VServerConfScheduledBootHour_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10, 1, 5),
    _VServerConfScheduledBootHour_Type()
)
vServerConfScheduledBootHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfScheduledBootHour.setStatus("current")
_VServerConfScheduledBootMinute_Type = Unsigned32
_VServerConfScheduledBootMinute_Object = MibScalar
vServerConfScheduledBootMinute = _VServerConfScheduledBootMinute_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10, 1, 6),
    _VServerConfScheduledBootMinute_Type()
)
vServerConfScheduledBootMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConfScheduledBootMinute.setStatus("current")
_VServerConfScheduledBootTbls_ObjectIdentity = ObjectIdentity
vServerConfScheduledBootTbls = _VServerConfScheduledBootTbls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 10, 2)
)
_VServerConfSoftwareMgmt_ObjectIdentity = ObjectIdentity
vServerConfSoftwareMgmt = _VServerConfSoftwareMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11)
)
_VServerSoftwareMgmtScalars_ObjectIdentity = ObjectIdentity
vServerSoftwareMgmtScalars = _VServerSoftwareMgmtScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1)
)


class _VServerSoftwareMgmtBootFrom_Type(OctetString):
    """Custom type vServerSoftwareMgmtBootFrom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerSoftwareMgmtBootFrom_Type.__name__ = "OctetString"
_VServerSoftwareMgmtBootFrom_Object = MibScalar
vServerSoftwareMgmtBootFrom = _VServerSoftwareMgmtBootFrom_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 1),
    _VServerSoftwareMgmtBootFrom_Type()
)
vServerSoftwareMgmtBootFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtBootFrom.setStatus("current")
_VServerSoftwareMgmtBootSlot_Type = Unsigned32
_VServerSoftwareMgmtBootSlot_Object = MibScalar
vServerSoftwareMgmtBootSlot = _VServerSoftwareMgmtBootSlot_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 2),
    _VServerSoftwareMgmtBootSlot_Type()
)
vServerSoftwareMgmtBootSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtBootSlot.setStatus("current")


class _VServerSoftwareMgmtLastURL_Type(OctetString):
    """Custom type vServerSoftwareMgmtLastURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerSoftwareMgmtLastURL_Type.__name__ = "OctetString"
_VServerSoftwareMgmtLastURL_Object = MibScalar
vServerSoftwareMgmtLastURL = _VServerSoftwareMgmtLastURL_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 3),
    _VServerSoftwareMgmtLastURL_Type()
)
vServerSoftwareMgmtLastURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtLastURL.setStatus("current")


class _VServerSoftwareMgmtURL_Type(OctetString):
    """Custom type vServerSoftwareMgmtURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerSoftwareMgmtURL_Type.__name__ = "OctetString"
_VServerSoftwareMgmtURL_Object = MibScalar
vServerSoftwareMgmtURL = _VServerSoftwareMgmtURL_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 4),
    _VServerSoftwareMgmtURL_Type()
)
vServerSoftwareMgmtURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtURL.setStatus("current")


class _VServerSoftwareMgmtInstallDest_Type(OctetString):
    """Custom type vServerSoftwareMgmtInstallDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerSoftwareMgmtInstallDest_Type.__name__ = "OctetString"
_VServerSoftwareMgmtInstallDest_Object = MibScalar
vServerSoftwareMgmtInstallDest = _VServerSoftwareMgmtInstallDest_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 5),
    _VServerSoftwareMgmtInstallDest_Type()
)
vServerSoftwareMgmtInstallDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtInstallDest.setStatus("current")


class _VServerSoftwareMgmtNextBoot_Type(OctetString):
    """Custom type vServerSoftwareMgmtNextBoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerSoftwareMgmtNextBoot_Type.__name__ = "OctetString"
_VServerSoftwareMgmtNextBoot_Object = MibScalar
vServerSoftwareMgmtNextBoot = _VServerSoftwareMgmtNextBoot_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 6),
    _VServerSoftwareMgmtNextBoot_Type()
)
vServerSoftwareMgmtNextBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtNextBoot.setStatus("current")
_VServerSoftwareMgmtDiskStatus_Type = Unsigned32
_VServerSoftwareMgmtDiskStatus_Object = MibScalar
vServerSoftwareMgmtDiskStatus = _VServerSoftwareMgmtDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 7),
    _VServerSoftwareMgmtDiskStatus_Type()
)
vServerSoftwareMgmtDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtDiskStatus.setStatus("current")
_VServerSoftwareMgmtInstStatus_Type = Unsigned32
_VServerSoftwareMgmtInstStatus_Object = MibScalar
vServerSoftwareMgmtInstStatus = _VServerSoftwareMgmtInstStatus_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 8),
    _VServerSoftwareMgmtInstStatus_Type()
)
vServerSoftwareMgmtInstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtInstStatus.setStatus("current")
_VServerSoftwareMgmtInstStatusDetail_Type = Unsigned32
_VServerSoftwareMgmtInstStatusDetail_Object = MibScalar
vServerSoftwareMgmtInstStatusDetail = _VServerSoftwareMgmtInstStatusDetail_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 9),
    _VServerSoftwareMgmtInstStatusDetail_Type()
)
vServerSoftwareMgmtInstStatusDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtInstStatusDetail.setStatus("current")
_VServerSoftwareMgmtVPID_Type = Integer32
_VServerSoftwareMgmtVPID_Object = MibScalar
vServerSoftwareMgmtVPID = _VServerSoftwareMgmtVPID_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 10),
    _VServerSoftwareMgmtVPID_Type()
)
vServerSoftwareMgmtVPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtVPID.setStatus("current")
_VServerSoftwareMgmtVerifyResult_Type = Integer32
_VServerSoftwareMgmtVerifyResult_Object = MibScalar
vServerSoftwareMgmtVerifyResult = _VServerSoftwareMgmtVerifyResult_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 11),
    _VServerSoftwareMgmtVerifyResult_Type()
)
vServerSoftwareMgmtVerifyResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtVerifyResult.setStatus("current")
_VServerSoftwareMgmtVerify_Type = Integer32
_VServerSoftwareMgmtVerify_Object = MibScalar
vServerSoftwareMgmtVerify = _VServerSoftwareMgmtVerify_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 12),
    _VServerSoftwareMgmtVerify_Type()
)
vServerSoftwareMgmtVerify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtVerify.setStatus("current")


class _VServerSoftwareMgmtBackupURL_Type(OctetString):
    """Custom type vServerSoftwareMgmtBackupURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerSoftwareMgmtBackupURL_Type.__name__ = "OctetString"
_VServerSoftwareMgmtBackupURL_Object = MibScalar
vServerSoftwareMgmtBackupURL = _VServerSoftwareMgmtBackupURL_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 13),
    _VServerSoftwareMgmtBackupURL_Type()
)
vServerSoftwareMgmtBackupURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtBackupURL.setStatus("current")


class _VServerSoftwareMgmtBackupSrc_Type(OctetString):
    """Custom type vServerSoftwareMgmtBackupSrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerSoftwareMgmtBackupSrc_Type.__name__ = "OctetString"
_VServerSoftwareMgmtBackupSrc_Object = MibScalar
vServerSoftwareMgmtBackupSrc = _VServerSoftwareMgmtBackupSrc_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 14),
    _VServerSoftwareMgmtBackupSrc_Type()
)
vServerSoftwareMgmtBackupSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtBackupSrc.setStatus("current")


class _VServerSoftwareMgmtBackupType_Type(OctetString):
    """Custom type vServerSoftwareMgmtBackupType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VServerSoftwareMgmtBackupType_Type.__name__ = "OctetString"
_VServerSoftwareMgmtBackupType_Object = MibScalar
vServerSoftwareMgmtBackupType = _VServerSoftwareMgmtBackupType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 15),
    _VServerSoftwareMgmtBackupType_Type()
)
vServerSoftwareMgmtBackupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtBackupType.setStatus("current")
_VServerSoftwareMgmtBackupStatus_Type = Unsigned32
_VServerSoftwareMgmtBackupStatus_Object = MibScalar
vServerSoftwareMgmtBackupStatus = _VServerSoftwareMgmtBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 16),
    _VServerSoftwareMgmtBackupStatus_Type()
)
vServerSoftwareMgmtBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtBackupStatus.setStatus("current")
_VServerSoftwareMgmtBackupStatusDetailed_Type = Unsigned32
_VServerSoftwareMgmtBackupStatusDetailed_Object = MibScalar
vServerSoftwareMgmtBackupStatusDetailed = _VServerSoftwareMgmtBackupStatusDetailed_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 17),
    _VServerSoftwareMgmtBackupStatusDetailed_Type()
)
vServerSoftwareMgmtBackupStatusDetailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtBackupStatusDetailed.setStatus("current")
_VServerSoftwareMgmtRequireReboot_Type = Unsigned32
_VServerSoftwareMgmtRequireReboot_Object = MibScalar
vServerSoftwareMgmtRequireReboot = _VServerSoftwareMgmtRequireReboot_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 11, 1, 18),
    _VServerSoftwareMgmtRequireReboot_Type()
)
vServerSoftwareMgmtRequireReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSoftwareMgmtRequireReboot.setStatus("current")
_VServerConfSecurityMgmt_ObjectIdentity = ObjectIdentity
vServerConfSecurityMgmt = _VServerConfSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 12)
)
_VServerSecurityMgmtScalars_ObjectIdentity = ObjectIdentity
vServerSecurityMgmtScalars = _VServerSecurityMgmtScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 12, 1)
)
_VServerSecurityMgmtEnableMaintAccess_Type = VenturiBooleanType
_VServerSecurityMgmtEnableMaintAccess_Object = MibScalar
vServerSecurityMgmtEnableMaintAccess = _VServerSecurityMgmtEnableMaintAccess_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 12, 1, 1),
    _VServerSecurityMgmtEnableMaintAccess_Type()
)
vServerSecurityMgmtEnableMaintAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSecurityMgmtEnableMaintAccess.setStatus("current")


class _VServerSecurityMgmtCurrAdminPwd_Type(OctetString):
    """Custom type vServerSecurityMgmtCurrAdminPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerSecurityMgmtCurrAdminPwd_Type.__name__ = "OctetString"
_VServerSecurityMgmtCurrAdminPwd_Object = MibScalar
vServerSecurityMgmtCurrAdminPwd = _VServerSecurityMgmtCurrAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 12, 1, 2),
    _VServerSecurityMgmtCurrAdminPwd_Type()
)
vServerSecurityMgmtCurrAdminPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSecurityMgmtCurrAdminPwd.setStatus("current")


class _VServerSecurityMgmtNewAdminPwd_Type(OctetString):
    """Custom type vServerSecurityMgmtNewAdminPwd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VServerSecurityMgmtNewAdminPwd_Type.__name__ = "OctetString"
_VServerSecurityMgmtNewAdminPwd_Object = MibScalar
vServerSecurityMgmtNewAdminPwd = _VServerSecurityMgmtNewAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 12, 1, 3),
    _VServerSecurityMgmtNewAdminPwd_Type()
)
vServerSecurityMgmtNewAdminPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerSecurityMgmtNewAdminPwd.setStatus("current")
_VServerSecurityMgmtAdminPwdUpstatus_Type = Integer32
_VServerSecurityMgmtAdminPwdUpstatus_Object = MibScalar
vServerSecurityMgmtAdminPwdUpstatus = _VServerSecurityMgmtAdminPwdUpstatus_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 3, 12, 1, 4),
    _VServerSecurityMgmtAdminPwdUpstatus_Type()
)
vServerSecurityMgmtAdminPwdUpstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSecurityMgmtAdminPwdUpstatus.setStatus("current")
_VServerConfActionSvcs_ObjectIdentity = ObjectIdentity
vServerConfActionSvcs = _VServerConfActionSvcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 4)
)
_VServerConfActionSvcsScalars_ObjectIdentity = ObjectIdentity
vServerConfActionSvcsScalars = _VServerConfActionSvcsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 4, 1)
)


class _VServerStagingCtlValResp_Type(OctetString):
    """Custom type vServerStagingCtlValResp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerStagingCtlValResp_Type.__name__ = "OctetString"
_VServerStagingCtlValResp_Object = MibScalar
vServerStagingCtlValResp = _VServerStagingCtlValResp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 4, 1, 1),
    _VServerStagingCtlValResp_Type()
)
vServerStagingCtlValResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStagingCtlValResp.setStatus("current")


class _VServerStagingCtlClearResp_Type(OctetString):
    """Custom type vServerStagingCtlClearResp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerStagingCtlClearResp_Type.__name__ = "OctetString"
_VServerStagingCtlClearResp_Object = MibScalar
vServerStagingCtlClearResp = _VServerStagingCtlClearResp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 4, 1, 2),
    _VServerStagingCtlClearResp_Type()
)
vServerStagingCtlClearResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStagingCtlClearResp.setStatus("current")


class _VServerStagingCtlCommitResp_Type(OctetString):
    """Custom type vServerStagingCtlCommitResp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VServerStagingCtlCommitResp_Type.__name__ = "OctetString"
_VServerStagingCtlCommitResp_Object = MibScalar
vServerStagingCtlCommitResp = _VServerStagingCtlCommitResp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 4, 1, 3),
    _VServerStagingCtlCommitResp_Type()
)
vServerStagingCtlCommitResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStagingCtlCommitResp.setStatus("current")
_VServerStagingCtlClearResult_Type = Unsigned32
_VServerStagingCtlClearResult_Object = MibScalar
vServerStagingCtlClearResult = _VServerStagingCtlClearResult_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 4, 1, 4),
    _VServerStagingCtlClearResult_Type()
)
vServerStagingCtlClearResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStagingCtlClearResult.setStatus("current")
_VServerStagingCtlCommitResult_Type = Unsigned32
_VServerStagingCtlCommitResult_Object = MibScalar
vServerStagingCtlCommitResult = _VServerStagingCtlCommitResult_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 4, 4, 1, 5),
    _VServerStagingCtlCommitResult_Type()
)
vServerStagingCtlCommitResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStagingCtlCommitResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VENTURI-SERVER-CONFIG-MIB",
    **{"vServerConf": vServerConf,
       "vServerConfIPSvcs": vServerConfIPSvcs,
       "vServerConfIPSvcsPhysicalIf": vServerConfIPSvcsPhysicalIf,
       "vServerConfIPSvcsPhysicalScalars": vServerConfIPSvcsPhysicalScalars,
       "vServerConfIPSvcsPhysicalTbls": vServerConfIPSvcsPhysicalTbls,
       "vServerEthConfTbl": vServerEthConfTbl,
       "vServerEthConfTblEntry": vServerEthConfTblEntry,
       "vServerEthConfTblIndex": vServerEthConfTblIndex,
       "vServerEthConfTblIfName": vServerEthConfTblIfName,
       "vServerEthConfTblMACAddress": vServerEthConfTblMACAddress,
       "vServerEthConfTblMTU": vServerEthConfTblMTU,
       "vServerEthConfTblCurConf": vServerEthConfTblCurConf,
       "vServerEthConfTblNewConf": vServerEthConfTblNewConf,
       "vServerConfIPSvcsLogicalIf": vServerConfIPSvcsLogicalIf,
       "vServerConfIPSvcsLogicalScalars": vServerConfIPSvcsLogicalScalars,
       "vServerConfIPSvcsLogicalTbls": vServerConfIPSvcsLogicalTbls,
       "vServerLogicalIfTbl": vServerLogicalIfTbl,
       "vServerLogicalIfTblEntry": vServerLogicalIfTblEntry,
       "vServerLogicalIfTblIndex": vServerLogicalIfTblIndex,
       "vServerLogicalIfTblName": vServerLogicalIfTblName,
       "vServerLogicalIfTblMode": vServerLogicalIfTblMode,
       "vServerLogicalIfTblParams": vServerLogicalIfTblParams,
       "vServerConfIPSvcsMgmtIf": vServerConfIPSvcsMgmtIf,
       "vServerConfIPSvcsMgmtScalars": vServerConfIPSvcsMgmtScalars,
       "vServerConfIPSvcsMgmtTbls": vServerConfIPSvcsMgmtTbls,
       "vServerMgmtIfTbl": vServerMgmtIfTbl,
       "vServerMgmtIfTblEntry": vServerMgmtIfTblEntry,
       "vServerMgmtIfTblIndex": vServerMgmtIfTblIndex,
       "vServerMgmtIfTblIp": vServerMgmtIfTblIp,
       "vServerMgmtIfTblNetmask": vServerMgmtIfTblNetmask,
       "vServerMgmtIfTblDefaultGw": vServerMgmtIfTblDefaultGw,
       "vServerMgmtIfTblBroadcast": vServerMgmtIfTblBroadcast,
       "vServerMgmtIfTblDns1": vServerMgmtIfTblDns1,
       "vServerMgmtIfTblDns2": vServerMgmtIfTblDns2,
       "vServerMgmtIfTblDns3": vServerMgmtIfTblDns3,
       "vServerMgmtIfTblDnsdomain": vServerMgmtIfTblDnsdomain,
       "vServerMgmtIfTblLogicalNicID": vServerMgmtIfTblLogicalNicID,
       "vServerMgmtIfTblNetifId": vServerMgmtIfTblNetifId,
       "vServerConfIPSvcsDataIf": vServerConfIPSvcsDataIf,
       "vServerConfIPSvcsDataScalars": vServerConfIPSvcsDataScalars,
       "vServerConfIPSvcsDataTbls": vServerConfIPSvcsDataTbls,
       "vServerTransLstnPorts": vServerTransLstnPorts,
       "vServerTransLstnPortsEntry": vServerTransLstnPortsEntry,
       "vServerTransLstnPortsIndex": vServerTransLstnPortsIndex,
       "vServerTransLstnPortsIp": vServerTransLstnPortsIp,
       "vServerTransLstnPortsNetmask": vServerTransLstnPortsNetmask,
       "vServerTransLstnPortsDefaultGw": vServerTransLstnPortsDefaultGw,
       "vServerTransLstnPortsBroadcast": vServerTransLstnPortsBroadcast,
       "vServerTransLstnPortsDns1": vServerTransLstnPortsDns1,
       "vServerTransLstnPortsDns2": vServerTransLstnPortsDns2,
       "vServerTransLstnPortsDns3": vServerTransLstnPortsDns3,
       "vServerTransLstnPortsDnsdomain": vServerTransLstnPortsDnsdomain,
       "vServerTransLstnPortsUdpPort": vServerTransLstnPortsUdpPort,
       "vServerTransLstnPortsTcpPort": vServerTransLstnPortsTcpPort,
       "vServerTransLstnPortsNetifId": vServerTransLstnPortsNetifId,
       "vServerTransLstnPortsFlag": vServerTransLstnPortsFlag,
       "vServerTransLstnPortsLogicalNicID": vServerTransLstnPortsLogicalNicID,
       "vServerConfIPSvcsAdvanced": vServerConfIPSvcsAdvanced,
       "vServerConfIPSvcsAdvancedScalars": vServerConfIPSvcsAdvancedScalars,
       "vServerConfIPSvcsAdvancedTbls": vServerConfIPSvcsAdvancedTbls,
       "vServerVirtSvr": vServerVirtSvr,
       "vServerVirtSvrEntry": vServerVirtSvrEntry,
       "vServerVirtSvrIndex": vServerVirtSvrIndex,
       "vServerVirtSvrHostname": vServerVirtSvrHostname,
       "vServerVirtSvrIpaddr": vServerVirtSvrIpaddr,
       "vServerVirtSvrPortRange": vServerVirtSvrPortRange,
       "vServerVirtSvrDestinations": vServerVirtSvrDestinations,
       "vServerDefaultDestTbl": vServerDefaultDestTbl,
       "vServerDefaultDestTblEntry": vServerDefaultDestTblEntry,
       "vServerDefaultDestTblIndex": vServerDefaultDestTblIndex,
       "vServerDefaultDestTblDestinations": vServerDefaultDestTblDestinations,
       "vServerConfIPSvcsPxy": vServerConfIPSvcsPxy,
       "vServerConfIPSvcsPxyScalars": vServerConfIPSvcsPxyScalars,
       "vServerConfIPSvcsPxyTbls": vServerConfIPSvcsPxyTbls,
       "vServerVSPxyTbl": vServerVSPxyTbl,
       "vServerVSPxyTblEntry": vServerVSPxyTblEntry,
       "vServerVSPxyTblIndex": vServerVSPxyTblIndex,
       "vServerVSPxyTblHnameIp": vServerVSPxyTblHnameIp,
       "vServerVSPxyTblPort": vServerVSPxyTblPort,
       "vServerVSPxyTblTpType": vServerVSPxyTblTpType,
       "vServerVSPxyTblBalance": vServerVSPxyTblBalance,
       "vServerVSPxyTblHealthCheck": vServerVSPxyTblHealthCheck,
       "vServerConfIPSvcsStatic": vServerConfIPSvcsStatic,
       "vServerConfIPSvcsStaticScalars": vServerConfIPSvcsStaticScalars,
       "vServerConfIPSvcsStaticTbls": vServerConfIPSvcsStaticTbls,
       "vServerStaticRouteTbl": vServerStaticRouteTbl,
       "vServerStaticRouteTblEntry": vServerStaticRouteTblEntry,
       "vServerStaticRouteTblIndex": vServerStaticRouteTblIndex,
       "vServerStaticRouteTblAllowRelay": vServerStaticRouteTblAllowRelay,
       "vServerStaticRouteTblMaskSize": vServerStaticRouteTblMaskSize,
       "vServerStaticRouteTblAddress": vServerStaticRouteTblAddress,
       "vServerStaticRouteTblGatewayAddr": vServerStaticRouteTblGatewayAddr,
       "vServerConfIPSvcsDscp": vServerConfIPSvcsDscp,
       "vServerConfIPSvcsDscpScalars": vServerConfIPSvcsDscpScalars,
       "vServerCLPreserveDscp": vServerCLPreserveDscp,
       "vServerCLDscpForObjectsServedFromCache": vServerCLDscpForObjectsServedFromCache,
       "vServerCSPreserveDscp": vServerCSPreserveDscp,
       "vServerCSDscpForObjectsServedFromCache": vServerCSDscpForObjectsServedFromCache,
       "vServerCSDscpForTrafficMarkedDscp0": vServerCSDscpForTrafficMarkedDscp0,
       "vServerCSDscpForVTPControlTraffic": vServerCSDscpForVTPControlTraffic,
       "vServerConfGwCStatsIntermediateUpdate": vServerConfGwCStatsIntermediateUpdate,
       "vServerCLDscpForTrafficMarkedDscp0": vServerCLDscpForTrafficMarkedDscp0,
       "vServerConfIntermediateUpdateEnable": vServerConfIntermediateUpdateEnable,
       "vServerConfIPSvcsDscpTbls": vServerConfIPSvcsDscpTbls,
       "vServerConfDscpFilterTbl": vServerConfDscpFilterTbl,
       "vServerConfDscpFilterEntry": vServerConfDscpFilterEntry,
       "vServerConfDscpFilterIndex": vServerConfDscpFilterIndex,
       "vServerConfDscpFilterValue": vServerConfDscpFilterValue,
       "vServerConfDscpFilterUseForBwEst": vServerConfDscpFilterUseForBwEst,
       "vServerConfGwIpMaskFilterTbl": vServerConfGwIpMaskFilterTbl,
       "vServerConfGwIpMaskFilterEntry": vServerConfGwIpMaskFilterEntry,
       "vServerConfGwIpMaskFilterIndex": vServerConfGwIpMaskFilterIndex,
       "vServerConfGwNetworkIp": vServerConfGwNetworkIp,
       "vServerConfGwNetmask": vServerConfGwNetmask,
       "vServerConfTransBucketMappingTbl": vServerConfTransBucketMappingTbl,
       "vServerConfTransBucketEntry": vServerConfTransBucketEntry,
       "vServerConfTransMappingIndex": vServerConfTransMappingIndex,
       "vServerConfTransMappingDscp": vServerConfTransMappingDscp,
       "vServerConfTransMappingBucket": vServerConfTransMappingBucket,
       "vServerConfIPSvcsQos": vServerConfIPSvcsQos,
       "vServerConfIPSvcsQosScalars": vServerConfIPSvcsQosScalars,
       "vServerConfDscpReclassificationEnable": vServerConfDscpReclassificationEnable,
       "vServerConfShapingMinBandwidth": vServerConfShapingMinBandwidth,
       "vServerConfShapingMinFscValue": vServerConfShapingMinFscValue,
       "vServerConfShapingFscNumerator": vServerConfShapingFscNumerator,
       "vServerConfDSCPToTransportShapingEnable": vServerConfDSCPToTransportShapingEnable,
       "vServerConfShapingMaxSubscriberCount": vServerConfShapingMaxSubscriberCount,
       "vServerConfIPSvcsQosTbls": vServerConfIPSvcsQosTbls,
       "vServerConfClientedReclassifyTbl": vServerConfClientedReclassifyTbl,
       "vServerConfClientedReclassifyEntry": vServerConfClientedReclassifyEntry,
       "vServerConfClientedReclassifyIndex": vServerConfClientedReclassifyIndex,
       "vServerConfClientedReclassifyPorts": vServerConfClientedReclassifyPorts,
       "vServerConfClientedReclassifyIngressDscp": vServerConfClientedReclassifyIngressDscp,
       "vServerConfClientedReclassifyContentType": vServerConfClientedReclassifyContentType,
       "vServerConfClientedReclassifySizeThreshold": vServerConfClientedReclassifySizeThreshold,
       "vServerConfClientedReclassifyPeriodicClear": vServerConfClientedReclassifyPeriodicClear,
       "vServerConfClientedReclassifyPeriodicClearSecs": vServerConfClientedReclassifyPeriodicClearSecs,
       "vServerConfClientedReclassifyEgressDscp": vServerConfClientedReclassifyEgressDscp,
       "vServerConfVtpShapingClassTbl": vServerConfVtpShapingClassTbl,
       "vServerConfVtpShapingClassEntry": vServerConfVtpShapingClassEntry,
       "vServerConfVtpShapingClassIndex": vServerConfVtpShapingClassIndex,
       "vServerConfVtpShaping": vServerConfVtpShaping,
       "vServerConfVtpShapingClassThreshold": vServerConfVtpShapingClassThreshold,
       "vServerConfVtpShapingClassFscEnable": vServerConfVtpShapingClassFscEnable,
       "vServerConfVtpShapingClassScale0": vServerConfVtpShapingClassScale0,
       "vServerConfVtpShapingClassScale1": vServerConfVtpShapingClassScale1,
       "vServerConfVtpShapingClassScale2": vServerConfVtpShapingClassScale2,
       "vServerConfVtpShapingClassScale3": vServerConfVtpShapingClassScale3,
       "vServerConfAppSvcs": vServerConfAppSvcs,
       "vServerConfAppSvcsTransport": vServerConfAppSvcsTransport,
       "vServerConfAppSvcsTransportScalars": vServerConfAppSvcsTransportScalars,
       "vServerUDPXportConfigMtu": vServerUDPXportConfigMtu,
       "vServerTransportConfigDoMtuDisc": vServerTransportConfigDoMtuDisc,
       "vServerUDPXportConfigMaxBwExt": vServerUDPXportConfigMaxBwExt,
       "vServerUDPXportConfigMaxBw2client": vServerUDPXportConfigMaxBw2client,
       "vServerTransConfigAutoTuneEnable": vServerTransConfigAutoTuneEnable,
       "vServerTransConfigTcpCongControlType": vServerTransConfigTcpCongControlType,
       "vServerTransConfigTcpInitialWindowSize": vServerTransConfigTcpInitialWindowSize,
       "vServerTransConfigFastHttpRendering": vServerTransConfigFastHttpRendering,
       "vServerTransConfigTimeWaitTimeout": vServerTransConfigTimeWaitTimeout,
       "vServerTransConfigIdleTimeout": vServerTransConfigIdleTimeout,
       "vServerTransConfigHttpReqOptimization": vServerTransConfigHttpReqOptimization,
       "vServerConfAppSvcsTransportTbls": vServerConfAppSvcsTransportTbls,
       "vServerMasterPxyTbl": vServerMasterPxyTbl,
       "vServerMasterPxyTblEntry": vServerMasterPxyTblEntry,
       "vServerMasterPxyTblIndex": vServerMasterPxyTblIndex,
       "vServerMasterPxyTblPxyMethName": vServerMasterPxyTblPxyMethName,
       "vServerMasterPxyTblStatsName": vServerMasterPxyTblStatsName,
       "vServerMasterPxyTblFlags": vServerMasterPxyTblFlags,
       "vServerMasterPxyTblPxyHost": vServerMasterPxyTblPxyHost,
       "vServerMasterPxyTblPxyPort": vServerMasterPxyTblPxyPort,
       "vServerMasterPxyTblDestHost": vServerMasterPxyTblDestHost,
       "vServerMasterPxyTblDestPort": vServerMasterPxyTblDestPort,
       "vServerMasterPxyTblTCPKeepAlive": vServerMasterPxyTblTCPKeepAlive,
       "vServerMasterPxyTblTCPKeepAliveTime": vServerMasterPxyTblTCPKeepAliveTime,
       "vServerMasterPxyTblTCPKeepAliveProbes": vServerMasterPxyTblTCPKeepAliveProbes,
       "vServerMasterPxyTblTCPKeepAliveIntvl": vServerMasterPxyTblTCPKeepAliveIntvl,
       "vServerTransConfTbl": vServerTransConfTbl,
       "vServerTransConfTblEntry": vServerTransConfTblEntry,
       "vServerTransConfTblIndex": vServerTransConfTblIndex,
       "vServerTransConfTblMode": vServerTransConfTblMode,
       "vServerTransConfTblType": vServerTransConfTblType,
       "vServerTransConfTblAutodetect": vServerTransConfTblAutodetect,
       "vServerTransPxyPmapTbl": vServerTransPxyPmapTbl,
       "vServerTransPxyPmapTblEntry": vServerTransPxyPmapTblEntry,
       "vServerTransPxyPmapTblIndex": vServerTransPxyPmapTblIndex,
       "vServerTransPxyPmapTblName": vServerTransPxyPmapTblName,
       "vServerTransPxyPmapTblPorts": vServerTransPxyPmapTblPorts,
       "vServerTransPxyPmapTblReDirect": vServerTransPxyPmapTblReDirect,
       "vServerTransPxyPmapTblAppMethName": vServerTransPxyPmapTblAppMethName,
       "vServerTransPxyPmapTblSPort": vServerTransPxyPmapTblSPort,
       "vServerDefTransPxyPmapTbl": vServerDefTransPxyPmapTbl,
       "vServerDefTransPxyPmapTblEntry": vServerDefTransPxyPmapTblEntry,
       "vServerDefTransPxyPmapTblIndex": vServerDefTransPxyPmapTblIndex,
       "vServerDefTransPxyPmapTblName": vServerDefTransPxyPmapTblName,
       "vServerDefTransPxyPmapTblPorts": vServerDefTransPxyPmapTblPorts,
       "vServerDefTransPxyPmapTblReDirect": vServerDefTransPxyPmapTblReDirect,
       "vServerDefTransPxyPmapTblAppMethName": vServerDefTransPxyPmapTblAppMethName,
       "vServerDefTransPxyPmapTblSPort": vServerDefTransPxyPmapTblSPort,
       "vServerConfAppSvcsCompression": vServerConfAppSvcsCompression,
       "vServerConfAppSvcsCompressionScalars": vServerConfAppSvcsCompressionScalars,
       "vServerConfAppSvcsCompressionTbls": vServerConfAppSvcsCompressionTbls,
       "vServerSvrCompCfgTbl": vServerSvrCompCfgTbl,
       "vServerSvrCompCfgTblEntry": vServerSvrCompCfgTblEntry,
       "vServerSvrCompCfgTblIndex": vServerSvrCompCfgTblIndex,
       "vServerSvrCompCfgTblGif2Png": vServerSvrCompCfgTblGif2Png,
       "vServerSvrCompCfgTblPng2Png": vServerSvrCompCfgTblPng2Png,
       "vServerSvrCompCfgTblPPM": vServerSvrCompCfgTblPPM,
       "vServerSvrCompCfgTblJ2k": vServerSvrCompCfgTblJ2k,
       "vServerSvrCompCfgTblAZ": vServerSvrCompCfgTblAZ,
       "vServerSvrCompCfgTblPrgJpeg": vServerSvrCompCfgTblPrgJpeg,
       "vServerSvrCompCfgTblReqCompContentCS": vServerSvrCompCfgTblReqCompContentCS,
       "vServerSvrCompCfgTblReqCompContentCless": vServerSvrCompCfgTblReqCompContentCless,
       "vServerSvrCompCfgTblJPegArith": vServerSvrCompCfgTblJPegArith,
       "vServerSvrCompCfgTblLossyHtml": vServerSvrCompCfgTblLossyHtml,
       "vServerCompSvrTbl": vServerCompSvrTbl,
       "vServerCompSvrTblEntry": vServerCompSvrTblEntry,
       "vServerCompSvrTblIndex": vServerCompSvrTblIndex,
       "vServerCompSvrTblJPegSize": vServerCompSvrTblJPegSize,
       "vServerCompSvrTblJPegMinSize": vServerCompSvrTblJPegMinSize,
       "vServerCompSvrTblJPegMethod": vServerCompSvrTblJPegMethod,
       "vServerCompSvrTblMaxChunk": vServerCompSvrTblMaxChunk,
       "vServerCompSvrTblGzipSize": vServerCompSvrTblGzipSize,
       "vServerCompSvrTblJ2kSize": vServerCompSvrTblJ2kSize,
       "vServerCompSvrTblJ2kMinSize": vServerCompSvrTblJ2kMinSize,
       "vServerCompSvrTblJpgMaxPix4J2k": vServerCompSvrTblJpgMaxPix4J2k,
       "vServerCompSvrTblJpgMaxPix4Opt": vServerCompSvrTblJpgMaxPix4Opt,
       "vServerCompSvrTblAzMaxSize": vServerCompSvrTblAzMaxSize,
       "vServerCompSvrTblJpegMinBpp": vServerCompSvrTblJpegMinBpp,
       "vServerHttpConfTbl": vServerHttpConfTbl,
       "vServerHttpConfTblEntry": vServerHttpConfTblEntry,
       "vServerHttpConfTblIndex": vServerHttpConfTblIndex,
       "vServerHttpConfTblPrefetch": vServerHttpConfTblPrefetch,
       "vServerHttpConfTblIdentify": vServerHttpConfTblIdentify,
       "vServerHttpConfTblXForwardFor": vServerHttpConfTblXForwardFor,
       "vServerHttpConfTblCompObjEnabled": vServerHttpConfTblCompObjEnabled,
       "vServerHttpConfTblSSCLCompFlag": vServerHttpConfTblSSCLCompFlag,
       "vServerHttpConfTblSSCompFlag": vServerHttpConfTblSSCompFlag,
       "vServerHttpConfTblKeepAlive": vServerHttpConfTblKeepAlive,
       "vServerHttpConfTblKATimeOut": vServerHttpConfTblKATimeOut,
       "vServerHttpConfTblProxyOverride": vServerHttpConfTblProxyOverride,
       "vServerHttpConfTblSSStdIComp": vServerHttpConfTblSSStdIComp,
       "vServerSIEConfTbl": vServerSIEConfTbl,
       "vServerSIEConfTblEntry": vServerSIEConfTblEntry,
       "vServerSIEConfTblIndex": vServerSIEConfTblIndex,
       "vServerSIEConfTblEnabled": vServerSIEConfTblEnabled,
       "vServerSIEConfTblHttpEnabled": vServerSIEConfTblHttpEnabled,
       "vServerSIEConfTblFtpEnabled": vServerSIEConfTblFtpEnabled,
       "vServerSIEConfTblEmailEnabled": vServerSIEConfTblEmailEnabled,
       "vServerSIEConfTblStatsEnabled": vServerSIEConfTblStatsEnabled,
       "vServerImageCompTbl": vServerImageCompTbl,
       "vServerImageCompTblEntry": vServerImageCompTblEntry,
       "vServerImageCompTblIndex": vServerImageCompTblIndex,
       "vServerImageCompTblName": vServerImageCompTblName,
       "vServerImageCompTblId": vServerImageCompTblId,
       "vServerImageCompTblType0": vServerImageCompTblType0,
       "vServerImageCompTblLevel0": vServerImageCompTblLevel0,
       "vServerImageCompTblType1": vServerImageCompTblType1,
       "vServerImageCompTblLevel1": vServerImageCompTblLevel1,
       "vServerImageCompTblType2": vServerImageCompTblType2,
       "vServerImageCompTblLevel2": vServerImageCompTblLevel2,
       "vServerImageCompTblType3": vServerImageCompTblType3,
       "vServerImageCompTblLevel3": vServerImageCompTblLevel3,
       "vServerImageCompTblType4": vServerImageCompTblType4,
       "vServerImageCompTblLevel4": vServerImageCompTblLevel4,
       "vServerHttpHdrAccessConfigTbl": vServerHttpHdrAccessConfigTbl,
       "vServerHttpHdrAccessTblEntry": vServerHttpHdrAccessTblEntry,
       "vServerHttpHdrAccessTblIndex": vServerHttpHdrAccessTblIndex,
       "vServerHttpHdrAccessTblHdrFieldName": vServerHttpHdrAccessTblHdrFieldName,
       "vServerHttpHdrAccessTblAllowDeny": vServerHttpHdrAccessTblAllowDeny,
       "vServerConfAppSvcsClient": vServerConfAppSvcsClient,
       "vServerConfAppSvcsClientScalars": vServerConfAppSvcsClientScalars,
       "vServerClientlessEnabled": vServerClientlessEnabled,
       "vServerClientlessTransInterceptEnable": vServerClientlessTransInterceptEnable,
       "vServerConfAppSvcsClientTbls": vServerConfAppSvcsClientTbls,
       "vServerAppClientUpdateTbl": vServerAppClientUpdateTbl,
       "vServerAppClientUpdateTblEntry": vServerAppClientUpdateTblEntry,
       "vServerAppClientUpdateTblIndex": vServerAppClientUpdateTblIndex,
       "vServerAppClientUpdateTblLocalURL": vServerAppClientUpdateTblLocalURL,
       "vServerAppClientUpdateTblPort": vServerAppClientUpdateTblPort,
       "vServerAppClientlessConfTbl": vServerAppClientlessConfTbl,
       "vServerAppClientlessConfTblEntry": vServerAppClientlessConfTblEntry,
       "vServerAppClientlessConfTblIndex": vServerAppClientlessConfTblIndex,
       "vServerAppClientlessConfTblEnable": vServerAppClientlessConfTblEnable,
       "vServerAppClientlessConfTblURL": vServerAppClientlessConfTblURL,
       "vServerAppClientlessConfTblIdle": vServerAppClientlessConfTblIdle,
       "vServerClientAutoUpgGblTbl": vServerClientAutoUpgGblTbl,
       "vServerClientAutoUpgGblTblEntry": vServerClientAutoUpgGblTblEntry,
       "vServerClientAutoUpgGblTblIndex": vServerClientAutoUpgGblTblIndex,
       "vServerClientAutoUpgGblTblEnable": vServerClientAutoUpgGblTblEnable,
       "vServerClientAutoUpgGblTblUpgTimeInterval": vServerClientAutoUpgGblTblUpgTimeInterval,
       "vServerClientAutoUpgGblTblMaxClientVerStored": vServerClientAutoUpgGblTblMaxClientVerStored,
       "vServerClientAutoUpgConfTgtTbl": vServerClientAutoUpgConfTgtTbl,
       "vServerClientAutoUpgConfTgtTblEntry": vServerClientAutoUpgConfTgtTblEntry,
       "vServerClientAutoUpgConfTgtTblIndex": vServerClientAutoUpgConfTgtTblIndex,
       "vServerClientAutoUpgConfTgtTblHourPerDay": vServerClientAutoUpgConfTgtTblHourPerDay,
       "vServerClientAutoUpgConfTgtTblSunday": vServerClientAutoUpgConfTgtTblSunday,
       "vServerClientAutoUpgConfTgtTblMonday": vServerClientAutoUpgConfTgtTblMonday,
       "vServerClientAutoUpgConfTgtTblTuesday": vServerClientAutoUpgConfTgtTblTuesday,
       "vServerClientAutoUpgConfTgtTblWednesday": vServerClientAutoUpgConfTgtTblWednesday,
       "vServerClientAutoUpgConfTgtTblThursday": vServerClientAutoUpgConfTgtTblThursday,
       "vServerClientAutoUpgConfTgtTblFriday": vServerClientAutoUpgConfTgtTblFriday,
       "vServerClientAutoUpgConfTgtTblSaturday": vServerClientAutoUpgConfTgtTblSaturday,
       "vServerClientAutoUpgVerTgtTbl": vServerClientAutoUpgVerTgtTbl,
       "vServerClientAutoUpgVerTgtTblEntry": vServerClientAutoUpgVerTgtTblEntry,
       "vServerClientAutoUpgVerTgtTblIndex": vServerClientAutoUpgVerTgtTblIndex,
       "vServerClientAutoUpgVerTgtTblRow": vServerClientAutoUpgVerTgtTblRow,
       "vServerClientAutoUpgVerTgtTblVer": vServerClientAutoUpgVerTgtTblVer,
       "vServerClientAutoUpgVerTgtTblPlatform": vServerClientAutoUpgVerTgtTblPlatform,
       "vServerClientAutoUpgVerTgtTblClientPayload": vServerClientAutoUpgVerTgtTblClientPayload,
       "vServerClientUpdateInfo": vServerClientUpdateInfo,
       "vServerClientUpdateInfoEntry": vServerClientUpdateInfoEntry,
       "vServerClientUpdateInfoIndex": vServerClientUpdateInfoIndex,
       "vServerClientUpdateInfoSendClntUpdate": vServerClientUpdateInfoSendClntUpdate,
       "vServerClientUpdateInfoClientVer": vServerClientUpdateInfoClientVer,
       "vServerClientUpdateInfoUrl": vServerClientUpdateInfoUrl,
       "vServerClientUpdateInfoExpTime": vServerClientUpdateInfoExpTime,
       "vServerConfAppSvcsFtp": vServerConfAppSvcsFtp,
       "vServerConfAppSvcsFtpScalars": vServerConfAppSvcsFtpScalars,
       "vServerConfAppSvcsFtpTbls": vServerConfAppSvcsFtpTbls,
       "vServerFtpConfTbl": vServerFtpConfTbl,
       "vServerFtpConfTblEntry": vServerFtpConfTblEntry,
       "vServerFtpConfTblIndex": vServerFtpConfTblIndex,
       "vServerFtpConfTblDataMethName": vServerFtpConfTblDataMethName,
       "vServerFtpConfTblSocksMethName": vServerFtpConfTblSocksMethName,
       "vServerFtpConfTblTimeout": vServerFtpConfTblTimeout,
       "vServerFtpConfTblDelay": vServerFtpConfTblDelay,
       "vServerConfAppSvcsQOS": vServerConfAppSvcsQOS,
       "vServerConfAppSvcsQOSScalars": vServerConfAppSvcsQOSScalars,
       "vServerConfQOSLicensed": vServerConfQOSLicensed,
       "vServerConfQOSEnabled": vServerConfQOSEnabled,
       "vServerConfUpdateQOSProfilesNow": vServerConfUpdateQOSProfilesNow,
       "vServerConfUpdQOSProfName": vServerConfUpdQOSProfName,
       "vServerConfAssignDefProfName": vServerConfAssignDefProfName,
       "vServerConfAppSvcsQOSTbls": vServerConfAppSvcsQOSTbls,
       "vServerConfAppSvcsUserAgent": vServerConfAppSvcsUserAgent,
       "vServerConfAppSvcsUserAgentScalars": vServerConfAppSvcsUserAgentScalars,
       "vServerConfAppSvcsUserAgentTbls": vServerConfAppSvcsUserAgentTbls,
       "vServerUACfgTbl": vServerUACfgTbl,
       "vServerUACfgTblEntry": vServerUACfgTblEntry,
       "vServerUACfgTblIndex": vServerUACfgTblIndex,
       "vServerUAId": vServerUAId,
       "vServerUAHeaderSig": vServerUAHeaderSig,
       "vServerUAMultiPartId": vServerUAMultiPartId,
       "vServerUAGZIPEnabled": vServerUAGZIPEnabled,
       "vServerUACLPerRedEnabled": vServerUACLPerRedEnabled,
       "vServerUAPrgJpegEnabled": vServerUAPrgJpegEnabled,
       "vServerUALossyJpegEnabled": vServerUALossyJpegEnabled,
       "vServerUALossyGifEnabled": vServerUALossyGifEnabled,
       "vServerUALossyHtmlEnabled": vServerUALossyHtmlEnabled,
       "vServerUALossyPngEnabled": vServerUALossyPngEnabled,
       "vServerUAItractivNoChunk": vServerUAItractivNoChunk,
       "vServerUAMultiPartCfgTbl": vServerUAMultiPartCfgTbl,
       "vServerUAMultiPartCfgTblEntry": vServerUAMultiPartCfgTblEntry,
       "vServerUAMPartCfgTblIndex": vServerUAMPartCfgTblIndex,
       "vServerUAMPartId": vServerUAMPartId,
       "vServerUAMPartEnable": vServerUAMPartEnable,
       "vServerUAMPartMaxPartSize": vServerUAMPartMaxPartSize,
       "vServerUAMPartMaxPackSize": vServerUAMPartMaxPackSize,
       "vServerUAMPartMaxWaitTime": vServerUAMPartMaxWaitTime,
       "vServerUAMPartUseMixedType": vServerUAMPartUseMixedType,
       "vServerUAMPartEnableMFilter": vServerUAMPartEnableMFilter,
       "vServerUAMPartNoOtherDomObj": vServerUAMPartNoOtherDomObj,
       "vServerUAMPartIncludeTxt": vServerUAMPartIncludeTxt,
       "vServerUAMPartIncludeImg": vServerUAMPartIncludeImg,
       "vServerUAMPartIncludeCss": vServerUAMPartIncludeCss,
       "vServerUAMPartIncludeJs": vServerUAMPartIncludeJs,
       "vServerUAMPartCacheSubObjects": vServerUAMPartCacheSubObjects,
       "vServerConfAppSvcsSIC": vServerConfAppSvcsSIC,
       "vServerConfAppSvcsSICScalars": vServerConfAppSvcsSICScalars,
       "vServerConfAppSvcsSICTbls": vServerConfAppSvcsSICTbls,
       "vServerConfAppSvcsDBoard": vServerConfAppSvcsDBoard,
       "vServerConfAppSvcsDBoardScalars": vServerConfAppSvcsDBoardScalars,
       "vServerDBoardCUsrCnt": vServerDBoardCUsrCnt,
       "vServerDBoardCLUsrCnt": vServerDBoardCLUsrCnt,
       "vServerDBoardCConn": vServerDBoardCConn,
       "vServerDBoardCLConn": vServerDBoardCLConn,
       "vServerDBoardTotalConn": vServerDBoardTotalConn,
       "vServerDBoardCTraffic": vServerDBoardCTraffic,
       "vServerDBoardCLTraffic": vServerDBoardCLTraffic,
       "vServerDBoardTotalTraffic": vServerDBoardTotalTraffic,
       "vServerDBoardDownStreamSavings": vServerDBoardDownStreamSavings,
       "vServerDBoardUpStreamSavings": vServerDBoardUpStreamSavings,
       "vServerDBoardCPULoad": vServerDBoardCPULoad,
       "vServerDBoardMemUsed": vServerDBoardMemUsed,
       "vServerDBoardMemFree": vServerDBoardMemFree,
       "vServerDBoardMemSwap": vServerDBoardMemSwap,
       "vServerDBoardDiskSpace": vServerDBoardDiskSpace,
       "vServerConfAppSvcsDBoardTbls": vServerConfAppSvcsDBoardTbls,
       "vServerConfAppSvcsIPE": vServerConfAppSvcsIPE,
       "vServerConfAppSvcsIPEScalars": vServerConfAppSvcsIPEScalars,
       "vServerConfAppSvcsIPETbls": vServerConfAppSvcsIPETbls,
       "vServerIPEFilterTbl": vServerIPEFilterTbl,
       "vServerIPEFilterTblEntry": vServerIPEFilterTblEntry,
       "vServerIPEFilterIndex": vServerIPEFilterIndex,
       "vServerIPEFilterEnabled": vServerIPEFilterEnabled,
       "vServerIPEFilterAddress": vServerIPEFilterAddress,
       "vServerIPEFilterMaskSize": vServerIPEFilterMaskSize,
       "vServerConfAppSvcsHHI": vServerConfAppSvcsHHI,
       "vSvrConfAppSvcsHHIScalars": vSvrConfAppSvcsHHIScalars,
       "vSvrConfAppSvcsHHITbls": vSvrConfAppSvcsHHITbls,
       "vSvrConfHHIMain": vSvrConfHHIMain,
       "vSvrConfHHIMainEntry": vSvrConfHHIMainEntry,
       "vSvrConfHHIMainIndex": vSvrConfHHIMainIndex,
       "vSvrConfHHIMainURL": vSvrConfHHIMainURL,
       "vSvrConfHHIMainTmplID": vSvrConfHHIMainTmplID,
       "vSvrConfHHITmpl": vSvrConfHHITmpl,
       "vSvrConfHHITmplEntry": vSvrConfHHITmplEntry,
       "vSvrConfHHITmplIndex": vSvrConfHHITmplIndex,
       "vSvrConfHHITmplTmplName": vSvrConfHHITmplTmplName,
       "vSvrConfHHITmplFlds": vSvrConfHHITmplFlds,
       "vSvrConfHHIHdr": vSvrConfHHIHdr,
       "vSvrConfHHIHdrEntry": vSvrConfHHIHdrEntry,
       "vSvrConfHHIHdrIndex": vSvrConfHHIHdrIndex,
       "vSvrConfHHIHdrHdrName": vSvrConfHHIHdrHdrName,
       "vSvrConfHHIHdrHdrRadType": vSvrConfHHIHdrHdrRadType,
       "vSvrConfHHIHdrHdrRadVndId": vSvrConfHHIHdrHdrRadVndId,
       "vSvrConfHHIHdrHdrRadVndType": vSvrConfHHIHdrHdrRadVndType,
       "vSvrConfHHIHdrHdrHint": vSvrConfHHIHdrHdrHint,
       "vSvrConfHHIFtp": vSvrConfHHIFtp,
       "vSvrConfHHIFtpEntry": vSvrConfHHIFtpEntry,
       "vSvrConfHHIFtpIndex": vSvrConfHHIFtpIndex,
       "vSvrConfHHIFtpHost": vSvrConfHHIFtpHost,
       "vSvrConfHHIFtpDir": vSvrConfHHIFtpDir,
       "vSvrConfHHIFtpFile": vSvrConfHHIFtpFile,
       "vSvrConfHHIFtpUser": vSvrConfHHIFtpUser,
       "vSvrConfHHIFtpPasswd": vSvrConfHHIFtpPasswd,
       "vSvrConfHHIFtpAction": vSvrConfHHIFtpAction,
       "vSvrConfHHIFtpNow": vSvrConfHHIFtpNow,
       "vSvrConfHHIFtpResult": vSvrConfHHIFtpResult,
       "vServerConfAppSvcsWebNotifier": vServerConfAppSvcsWebNotifier,
       "vServerConfAppSvcsWebNotifierScalars": vServerConfAppSvcsWebNotifierScalars,
       "vServerConfAppSvcsWebNotifierTbls": vServerConfAppSvcsWebNotifierTbls,
       "vServerWebNotifierTbl": vServerWebNotifierTbl,
       "vServerWebNotifierTblEntry": vServerWebNotifierTblEntry,
       "vServerWebNotifierTblIndex": vServerWebNotifierTblIndex,
       "vServerWebNotifierTblEnable": vServerWebNotifierTblEnable,
       "vServerWebNotifierTblLocation": vServerWebNotifierTblLocation,
       "vServerWebNotifierTblAddString": vServerWebNotifierTblAddString,
       "vServerWebNotifierHostTbl": vServerWebNotifierHostTbl,
       "vServerWebNotifierHostTblEntry": vServerWebNotifierHostTblEntry,
       "vServerWebNotifierHostTblIndex": vServerWebNotifierHostTblIndex,
       "vServerWebNotifierHostTblHost": vServerWebNotifierHostTblHost,
       "vServerConfMgmtSvcs": vServerConfMgmtSvcs,
       "vServerConfDeviceGlobals": vServerConfDeviceGlobals,
       "vServerConfDeviceGlobalsScalars": vServerConfDeviceGlobalsScalars,
       "vServerDateAndTime": vServerDateAndTime,
       "vServerTZRegion": vServerTZRegion,
       "vServerTimeZone": vServerTimeZone,
       "vServerTimeServerURL": vServerTimeServerURL,
       "vServerTimeServerProtocol": vServerTimeServerProtocol,
       "vServerTimeServerInterval": vServerTimeServerInterval,
       "vServerFormatOnBoot": vServerFormatOnBoot,
       "vServerSSHEnabled": vServerSSHEnabled,
       "vServerHostname": vServerHostname,
       "vServerServerIdForClient": vServerServerIdForClient,
       "vServerConfDeviceGlobalsTbls": vServerConfDeviceGlobalsTbls,
       "vServerUiWebInfoTbl": vServerUiWebInfoTbl,
       "vServerUiWebInfoTblEntry": vServerUiWebInfoTblEntry,
       "vServerUiWebInfoTblIndex": vServerUiWebInfoTblIndex,
       "vServerUiWebInfoTblActive": vServerUiWebInfoTblActive,
       "vServerUiWebInfoTblHTTPPort": vServerUiWebInfoTblHTTPPort,
       "vServerUiWebInfoTblHTTPSPort": vServerUiWebInfoTblHTTPSPort,
       "vServerUserConfTbl": vServerUserConfTbl,
       "vServerUserConfTblEntry": vServerUserConfTblEntry,
       "vServerUserConfTblIndex": vServerUserConfTblIndex,
       "vServerUserConfTblClientAccessNum": vServerUserConfTblClientAccessNum,
       "vServerUserConfTblUTdisp": vServerUserConfTblUTdisp,
       "vServerUserConfTblUTIP": vServerUserConfTblUTIP,
       "vServerUserConfTblCUdisp": vServerUserConfTblCUdisp,
       "vServerUserConfTblCUIP": vServerUserConfTblCUIP,
       "vServerConfFeature": vServerConfFeature,
       "vServerConfFeatureScalars": vServerConfFeatureScalars,
       "vServerFeatCtrlTblVirtVS": vServerFeatCtrlTblVirtVS,
       "vServerFeatCtrlTblIpTransparency": vServerFeatCtrlTblIpTransparency,
       "vServerFeatCtrlTblEnableRouting": vServerFeatCtrlTblEnableRouting,
       "vServerFeatCtrlTblRadiusAcct": vServerFeatCtrlTblRadiusAcct,
       "vServerFeatCtrlTblRtspEnable": vServerFeatCtrlTblRtspEnable,
       "vServerConfPush": vServerConfPush,
       "vServerConfPushScalars": vServerConfPushScalars,
       "vServerConfPushTimeout": vServerConfPushTimeout,
       "vServerConfPushRetryCount": vServerConfPushRetryCount,
       "vServerConfPushDeliveryPeriod": vServerConfPushDeliveryPeriod,
       "vServerConfigPushCstatsAccountingMode": vServerConfigPushCstatsAccountingMode,
       "vServerConfPushTbls": vServerConfPushTbls,
       "vServerPushTgtTbl": vServerPushTgtTbl,
       "vServerPushTgtEntry": vServerPushTgtEntry,
       "vServerPushTgtIndex": vServerPushTgtIndex,
       "vServerPushTgtEnable": vServerPushTgtEnable,
       "vServerPushTgtHost": vServerPushTgtHost,
       "vServerPushTgtPort": vServerPushTgtPort,
       "vServerPushTgtUser": vServerPushTgtUser,
       "vServerPushTgtPassword": vServerPushTgtPassword,
       "vServerPushTgtDirectory": vServerPushTgtDirectory,
       "vServerPushTgtTrapNotification": vServerPushTgtTrapNotification,
       "vServerPushProtocol": vServerPushProtocol,
       "vServerPushFileTypes": vServerPushFileTypes,
       "vServerConfAlert": vServerConfAlert,
       "vServerConfAlertScalars": vServerConfAlertScalars,
       "vServerConfAlertEmailTO": vServerConfAlertEmailTO,
       "vServerConfAlertEmailFROM": vServerConfAlertEmailFROM,
       "vServerConfAlertSMTPServer": vServerConfAlertSMTPServer,
       "vServerConfAlertThreshold": vServerConfAlertThreshold,
       "vServerConfAlertDebugLogEnable": vServerConfAlertDebugLogEnable,
       "vServerConfAlertSNMPTrapsEnable": vServerConfAlertSNMPTrapsEnable,
       "vServerConfAlertSyslogServer": vServerConfAlertSyslogServer,
       "vServerConfAlertSyslogFacility": vServerConfAlertSyslogFacility,
       "vServerConfAlertTbls": vServerConfAlertTbls,
       "vServerLogModuleConfTbl": vServerLogModuleConfTbl,
       "vServerLogModuleConfTblEntry": vServerLogModuleConfTblEntry,
       "vServerLogModuleConfTblModule": vServerLogModuleConfTblModule,
       "vServerLogModuleConfTblThreshold": vServerLogModuleConfTblThreshold,
       "vServerAlertRoutingTbl": vServerAlertRoutingTbl,
       "vServerAlertRoutingTblEntry": vServerAlertRoutingTblEntry,
       "vServerAlertIndex": vServerAlertIndex,
       "vServerAlertEventName": vServerAlertEventName,
       "vServerAlertPriority": vServerAlertPriority,
       "vServerAlertMethods": vServerAlertMethods,
       "vServerAlertCurrent": vServerAlertCurrent,
       "vServerAlertTrapSeverity": vServerAlertTrapSeverity,
       "vServerConfSnmp": vServerConfSnmp,
       "vServerConfSnmpScalars": vServerConfSnmpScalars,
       "vServerSnmpConfTblAgentEnabled": vServerSnmpConfTblAgentEnabled,
       "vServerSnmpConfTblAgentPort": vServerSnmpConfTblAgentPort,
       "vServerSnmpConfTblReadOnlyCommunity": vServerSnmpConfTblReadOnlyCommunity,
       "vServerSnmpConfTblReadWriteCommunity": vServerSnmpConfTblReadWriteCommunity,
       "vServerSnmpConfTblSysContact": vServerSnmpConfTblSysContact,
       "vServerSnmpConfTblSysLocation": vServerSnmpConfTblSysLocation,
       "vServerSNMPTrapTgtRetryCount": vServerSNMPTrapTgtRetryCount,
       "vServerSNMPTrapTgtTimeout": vServerSNMPTrapTgtTimeout,
       "vServerSNMPTrapTgtTrapFrequency": vServerSNMPTrapTgtTrapFrequency,
       "vServerSnmpConfTblHealthCheckAgentEnabled": vServerSnmpConfTblHealthCheckAgentEnabled,
       "vServerConfSnmpTbls": vServerConfSnmpTbls,
       "vServerSNMPTrapTgt": vServerSNMPTrapTgt,
       "vServerSNMPTrapTgtEntry": vServerSNMPTrapTgtEntry,
       "vServerSNMPTrapTgtIndex": vServerSNMPTrapTgtIndex,
       "vServerSNMPTrapTgtHost": vServerSNMPTrapTgtHost,
       "vServerSNMPTrapTgtPort": vServerSNMPTrapTgtPort,
       "vServerSNMPTrapTgtCommunity": vServerSNMPTrapTgtCommunity,
       "vServerSNMPTrapTgtTrapType": vServerSNMPTrapTgtTrapType,
       "vServerConfLog": vServerConfLog,
       "vServerConfLogScalars": vServerConfLogScalars,
       "vServerHttpLogFullUrl": vServerHttpLogFullUrl,
       "vServerHttpLogHideIp": vServerHttpLogHideIp,
       "vServerTransactionLoggingEnabled": vServerTransactionLoggingEnabled,
       "vServerDisconnectedUserLoggingEnabled": vServerDisconnectedUserLoggingEnabled,
       "vServerConfLogTbls": vServerConfLogTbls,
       "vServerConfCache": vServerConfCache,
       "vServerConfCacheScalars": vServerConfCacheScalars,
       "vServerMaxCacheObjectSize": vServerMaxCacheObjectSize,
       "vServerConfCacheTbls": vServerConfCacheTbls,
       "vServerCacheBypassTbl": vServerCacheBypassTbl,
       "vServerCacheBypassTblEntry": vServerCacheBypassTblEntry,
       "vServerCacheBypassTblIndex": vServerCacheBypassTblIndex,
       "vServerCacheBypassTblHostname": vServerCacheBypassTblHostname,
       "vServerCacheBypassTblIpaddr": vServerCacheBypassTblIpaddr,
       "vServerCacheBypassTblPortRange": vServerCacheBypassTblPortRange,
       "vServerCacheBypassTblDestinations": vServerCacheBypassTblDestinations,
       "vServerCacheConfTbl": vServerCacheConfTbl,
       "vServerCacheConfTblEntry": vServerCacheConfTblEntry,
       "vServerCacheConfTblIndex": vServerCacheConfTblIndex,
       "vServerCacheConfTblMode": vServerCacheConfTblMode,
       "vServerCacheConfTblExtCacheURL": vServerCacheConfTblExtCacheURL,
       "vServerCacheACLConfTbl": vServerCacheACLConfTbl,
       "vServerCacheACLConfTblEntry": vServerCacheACLConfTblEntry,
       "vServerCacheACLConfTblIndex": vServerCacheACLConfTblIndex,
       "vServerCacheACLConfTblName": vServerCacheACLConfTblName,
       "vServerCacheACLConfTblMatchType": vServerCacheACLConfTblMatchType,
       "vServerCacheACLConfTblMatchArgs": vServerCacheACLConfTblMatchArgs,
       "vServerCacheRPConfTbl": vServerCacheRPConfTbl,
       "vServerCacheRPConfTblEntry": vServerCacheRPConfTblEntry,
       "vServerCacheRPConfTblIndex": vServerCacheRPConfTblIndex,
       "vServerCacheRPConfTblPattern": vServerCacheRPConfTblPattern,
       "vServerCacheRPConfTblMin": vServerCacheRPConfTblMin,
       "vServerCacheRPConfTblMax": vServerCacheRPConfTblMax,
       "vServerCacheRPConfTblPercent": vServerCacheRPConfTblPercent,
       "vServerCacheHierarchyConfTbl": vServerCacheHierarchyConfTbl,
       "vServerCacheHierarchyConfTblEntry": vServerCacheHierarchyConfTblEntry,
       "vServerCacheHierarchyConfTblIndex": vServerCacheHierarchyConfTblIndex,
       "vServerCacheHierarchyConfTblIpAndPort": vServerCacheHierarchyConfTblIpAndPort,
       "vServerCacheHierarchyConfTblRelationType": vServerCacheHierarchyConfTblRelationType,
       "vServerConfAuth": vServerConfAuth,
       "vServerConfAuthScalars": vServerConfAuthScalars,
       "vServerConfAuthMethod": vServerConfAuthMethod,
       "vServerConfAuthString": vServerConfAuthString,
       "vServerConfAuthTbls": vServerConfAuthTbls,
       "vServerradiusCfgTbl": vServerradiusCfgTbl,
       "vServerradiusCfgTblEntry": vServerradiusCfgTblEntry,
       "vServerradiusCfgTblIndex": vServerradiusCfgTblIndex,
       "vServerradiusCfgTblRadEnable": vServerradiusCfgTblRadEnable,
       "vServerradiusCfgTblRadSvrRetryCount": vServerradiusCfgTblRadSvrRetryCount,
       "vServerradiusCfgTblRadSvrTimeout": vServerradiusCfgTblRadSvrTimeout,
       "vServerradiusCfgTblRadSvrKey": vServerradiusCfgTblRadSvrKey,
       "vServerradiusCfgTblRadSvrCount": vServerradiusCfgTblRadSvrCount,
       "vServerradiusCfgTblListenPort": vServerradiusCfgTblListenPort,
       "vServerradiusCfgTblAccountEnable": vServerradiusCfgTblAccountEnable,
       "vServerradiusCfgTblServerHost": vServerradiusCfgTblServerHost,
       "vServerradiusCfgTblServerPort": vServerradiusCfgTblServerPort,
       "vServerradiusCfgTblSharedSecret": vServerradiusCfgTblSharedSecret,
       "vServerradiusSvrCfgTbl": vServerradiusSvrCfgTbl,
       "vServerradiusSvrCfgTblEntry": vServerradiusSvrCfgTblEntry,
       "vServerradiusSvrCfgTblIndex": vServerradiusSvrCfgTblIndex,
       "vServerradiusSvrCfgTblRadSvrAddr": vServerradiusSvrCfgTblRadSvrAddr,
       "vServerradiusSvrCfgTblRadSvrAuthPort": vServerradiusSvrCfgTblRadSvrAuthPort,
       "vServerradiusSvrCfgTblRadSvrAcctPort": vServerradiusSvrCfgTblRadSvrAcctPort,
       "vServerradiusSvrCfgTblRadSvrActive": vServerradiusSvrCfgTblRadSvrActive,
       "vServerAuthAllowDenyTbl": vServerAuthAllowDenyTbl,
       "vServerAuthAllowDenyTblEntry": vServerAuthAllowDenyTblEntry,
       "vServerAuthAllowDenyTblIndex": vServerAuthAllowDenyTblIndex,
       "vServerAuthAllowDenyTblAllowFlag": vServerAuthAllowDenyTblAllowFlag,
       "vServerAuthAllowDenyTblPattern": vServerAuthAllowDenyTblPattern,
       "vServerConfScheduledBoot": vServerConfScheduledBoot,
       "vServerConfScheduledBootScalars": vServerConfScheduledBootScalars,
       "vServerConfScheduledBootActive": vServerConfScheduledBootActive,
       "vServerConfScheduledBootMode": vServerConfScheduledBootMode,
       "vServerConfScheduledBootMonth": vServerConfScheduledBootMonth,
       "vServerConfScheduledBootDay": vServerConfScheduledBootDay,
       "vServerConfScheduledBootHour": vServerConfScheduledBootHour,
       "vServerConfScheduledBootMinute": vServerConfScheduledBootMinute,
       "vServerConfScheduledBootTbls": vServerConfScheduledBootTbls,
       "vServerConfSoftwareMgmt": vServerConfSoftwareMgmt,
       "vServerSoftwareMgmtScalars": vServerSoftwareMgmtScalars,
       "vServerSoftwareMgmtBootFrom": vServerSoftwareMgmtBootFrom,
       "vServerSoftwareMgmtBootSlot": vServerSoftwareMgmtBootSlot,
       "vServerSoftwareMgmtLastURL": vServerSoftwareMgmtLastURL,
       "vServerSoftwareMgmtURL": vServerSoftwareMgmtURL,
       "vServerSoftwareMgmtInstallDest": vServerSoftwareMgmtInstallDest,
       "vServerSoftwareMgmtNextBoot": vServerSoftwareMgmtNextBoot,
       "vServerSoftwareMgmtDiskStatus": vServerSoftwareMgmtDiskStatus,
       "vServerSoftwareMgmtInstStatus": vServerSoftwareMgmtInstStatus,
       "vServerSoftwareMgmtInstStatusDetail": vServerSoftwareMgmtInstStatusDetail,
       "vServerSoftwareMgmtVPID": vServerSoftwareMgmtVPID,
       "vServerSoftwareMgmtVerifyResult": vServerSoftwareMgmtVerifyResult,
       "vServerSoftwareMgmtVerify": vServerSoftwareMgmtVerify,
       "vServerSoftwareMgmtBackupURL": vServerSoftwareMgmtBackupURL,
       "vServerSoftwareMgmtBackupSrc": vServerSoftwareMgmtBackupSrc,
       "vServerSoftwareMgmtBackupType": vServerSoftwareMgmtBackupType,
       "vServerSoftwareMgmtBackupStatus": vServerSoftwareMgmtBackupStatus,
       "vServerSoftwareMgmtBackupStatusDetailed": vServerSoftwareMgmtBackupStatusDetailed,
       "vServerSoftwareMgmtRequireReboot": vServerSoftwareMgmtRequireReboot,
       "vServerConfSecurityMgmt": vServerConfSecurityMgmt,
       "vServerSecurityMgmtScalars": vServerSecurityMgmtScalars,
       "vServerSecurityMgmtEnableMaintAccess": vServerSecurityMgmtEnableMaintAccess,
       "vServerSecurityMgmtCurrAdminPwd": vServerSecurityMgmtCurrAdminPwd,
       "vServerSecurityMgmtNewAdminPwd": vServerSecurityMgmtNewAdminPwd,
       "vServerSecurityMgmtAdminPwdUpstatus": vServerSecurityMgmtAdminPwdUpstatus,
       "vServerConfActionSvcs": vServerConfActionSvcs,
       "vServerConfActionSvcsScalars": vServerConfActionSvcsScalars,
       "vServerStagingCtlValResp": vServerStagingCtlValResp,
       "vServerStagingCtlClearResp": vServerStagingCtlClearResp,
       "vServerStagingCtlCommitResp": vServerStagingCtlCommitResp,
       "vServerStagingCtlClearResult": vServerStagingCtlClearResult,
       "vServerStagingCtlCommitResult": vServerStagingCtlCommitResult}
)
