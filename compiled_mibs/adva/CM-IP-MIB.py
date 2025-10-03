# SNMP MIB module (CM-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-IP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:13 2025
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

(IpVersion,
 VlanId) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "IpVersion",
    "VlanId")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

cmIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11)
)
if mibBuilder.loadTexts:
    cmIPMIB.setRevisions(
        ("2019-03-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CmDhcpRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-client", 1),
          ("dhcp-server", 2))
    )



class IpManagementTunnelType(TextualConvention, Integer32):
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
        *(("macbased", 1),
          ("vlanbased", 2),
          ("itagbased", 3),
          ("gcc0based", 4),
          ("gcc1based", 5),
          ("gcc2based", 6))
    )



class IpManagementTunnelEncapsulationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ppp", 2))
    )



class IpEntryType(TextualConvention, Integer32):
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



class IpSourceAddrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemipaddr", 1),
          ("outipinterfaceaddr", 2))
    )



class IpActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("initiate", 1))
    )



class Ipv6OverIpv4TunnelType(TextualConvention, Integer32):
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
        *(("sixToFour", 1),
          ("ipv4-compatible", 2),
          ("isatap", 3),
          ("static-config", 4),
          ("gre", 5),
          ("ipv6-6rd", 6))
    )



class IpMode(TextualConvention, Integer32):
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
        *(("ipv4-only", 0),
          ("ipv6-only", 1),
          ("ipv4-and-ipv6", 2))
    )



class DHCPCIDType(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("sysName", 2),
          ("macAddr", 3),
          ("userDefined", 4),
          ("serialNumber", 5))
    )



class DHCPHostNameType(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("sysName", 2),
          ("userDefined", 3))
    )



class PtpArpActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("retrieve", 1))
    )



class DHCPVendorInfoType(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("sysName", 2),
          ("userDefined", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CmIpObjects_ObjectIdentity = ObjectIdentity
cmIpObjects = _CmIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1)
)
_CmIpInterfaceTable_Object = MibTable
cmIpInterfaceTable = _CmIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1)
)
if mibBuilder.loadTexts:
    cmIpInterfaceTable.setStatus("current")
_CmIpInterfaceEntry_Object = MibTableRow
cmIpInterfaceEntry = _CmIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1)
)
cmIpInterfaceEntry.setIndexNames(
    (0, "CM-IP-MIB", "cmIpInterfaceName"),
)
if mibBuilder.loadTexts:
    cmIpInterfaceEntry.setStatus("current")


class _CmIpInterfaceName_Type(DisplayString):
    """Custom type cmIpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CmIpInterfaceName_Type.__name__ = "DisplayString"
_CmIpInterfaceName_Object = MibTableColumn
cmIpInterfaceName = _CmIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 1),
    _CmIpInterfaceName_Type()
)
cmIpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIpInterfaceName.setStatus("current")
_CmIpInterface_Type = IpAddress
_CmIpInterface_Object = MibTableColumn
cmIpInterface = _CmIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 2),
    _CmIpInterface_Type()
)
cmIpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterface.setStatus("current")
_CmIpInterfaceMask_Type = IpAddress
_CmIpInterfaceMask_Object = MibTableColumn
cmIpInterfaceMask = _CmIpInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 3),
    _CmIpInterfaceMask_Type()
)
cmIpInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceMask.setStatus("current")
_CmIpInterfaceDhcpEnabled_Type = TruthValue
_CmIpInterfaceDhcpEnabled_Object = MibTableColumn
cmIpInterfaceDhcpEnabled = _CmIpInterfaceDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 4),
    _CmIpInterfaceDhcpEnabled_Type()
)
cmIpInterfaceDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpEnabled.setStatus("current")


class _CmIpInterfaceMTU_Type(Integer32):
    """Custom type cmIpInterfaceMTU based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_CmIpInterfaceMTU_Type.__name__ = "Integer32"
_CmIpInterfaceMTU_Object = MibTableColumn
cmIpInterfaceMTU = _CmIpInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 5),
    _CmIpInterfaceMTU_Type()
)
cmIpInterfaceMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceMTU.setStatus("current")
_CmIpInterfaceDhcpRole_Type = CmDhcpRole
_CmIpInterfaceDhcpRole_Object = MibTableColumn
cmIpInterfaceDhcpRole = _CmIpInterfaceDhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 6),
    _CmIpInterfaceDhcpRole_Type()
)
cmIpInterfaceDhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpRole.setStatus("current")


class _CmIpInterfacePhysicalAddress_Type(DisplayString):
    """Custom type cmIpInterfacePhysicalAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmIpInterfacePhysicalAddress_Type.__name__ = "DisplayString"
_CmIpInterfacePhysicalAddress_Object = MibTableColumn
cmIpInterfacePhysicalAddress = _CmIpInterfacePhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 7),
    _CmIpInterfacePhysicalAddress_Type()
)
cmIpInterfacePhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIpInterfacePhysicalAddress.setStatus("current")
_CmIpInterfaceRIPv2Enabled_Type = TruthValue
_CmIpInterfaceRIPv2Enabled_Object = MibTableColumn
cmIpInterfaceRIPv2Enabled = _CmIpInterfaceRIPv2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 8),
    _CmIpInterfaceRIPv2Enabled_Type()
)
cmIpInterfaceRIPv2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceRIPv2Enabled.setStatus("current")
_CmIpInterfaceDHCPClientIdEnabled_Type = TruthValue
_CmIpInterfaceDHCPClientIdEnabled_Object = MibTableColumn
cmIpInterfaceDHCPClientIdEnabled = _CmIpInterfaceDHCPClientIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 9),
    _CmIpInterfaceDHCPClientIdEnabled_Type()
)
cmIpInterfaceDHCPClientIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDHCPClientIdEnabled.setStatus("current")


class _CmIpInterfaceDHCPClientId_Type(DisplayString):
    """Custom type cmIpInterfaceDHCPClientId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CmIpInterfaceDHCPClientId_Type.__name__ = "DisplayString"
_CmIpInterfaceDHCPClientId_Object = MibTableColumn
cmIpInterfaceDHCPClientId = _CmIpInterfaceDHCPClientId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 10),
    _CmIpInterfaceDHCPClientId_Type()
)
cmIpInterfaceDHCPClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDHCPClientId.setStatus("current")
_CmIpInterfaceIpMode_Type = IpMode
_CmIpInterfaceIpMode_Object = MibTableColumn
cmIpInterfaceIpMode = _CmIpInterfaceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 11),
    _CmIpInterfaceIpMode_Type()
)
cmIpInterfaceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceIpMode.setStatus("current")
_CmIpInterfaceDhcpClassIdEnabled_Type = TruthValue
_CmIpInterfaceDhcpClassIdEnabled_Object = MibTableColumn
cmIpInterfaceDhcpClassIdEnabled = _CmIpInterfaceDhcpClassIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 12),
    _CmIpInterfaceDhcpClassIdEnabled_Type()
)
cmIpInterfaceDhcpClassIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpClassIdEnabled.setStatus("current")
_CmIpInterfaceDhcpHostNameEnabled_Type = TruthValue
_CmIpInterfaceDhcpHostNameEnabled_Object = MibTableColumn
cmIpInterfaceDhcpHostNameEnabled = _CmIpInterfaceDhcpHostNameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 13),
    _CmIpInterfaceDhcpHostNameEnabled_Type()
)
cmIpInterfaceDhcpHostNameEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpHostNameEnabled.setStatus("current")
_CmIpInterfaceDhcpHostName_Type = DisplayString
_CmIpInterfaceDhcpHostName_Object = MibTableColumn
cmIpInterfaceDhcpHostName = _CmIpInterfaceDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 14),
    _CmIpInterfaceDhcpHostName_Type()
)
cmIpInterfaceDhcpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpHostName.setStatus("current")
_CmIpInterfaceDhcpLogServerEnabled_Type = TruthValue
_CmIpInterfaceDhcpLogServerEnabled_Object = MibTableColumn
cmIpInterfaceDhcpLogServerEnabled = _CmIpInterfaceDhcpLogServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 15),
    _CmIpInterfaceDhcpLogServerEnabled_Type()
)
cmIpInterfaceDhcpLogServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpLogServerEnabled.setStatus("current")
_CmIpInterfaceDhcpNTPServerEnabled_Type = TruthValue
_CmIpInterfaceDhcpNTPServerEnabled_Object = MibTableColumn
cmIpInterfaceDhcpNTPServerEnabled = _CmIpInterfaceDhcpNTPServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 16),
    _CmIpInterfaceDhcpNTPServerEnabled_Type()
)
cmIpInterfaceDhcpNTPServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpNTPServerEnabled.setStatus("current")
_CmIpInterfaceDhcpClientIdType_Type = DHCPCIDType
_CmIpInterfaceDhcpClientIdType_Object = MibTableColumn
cmIpInterfaceDhcpClientIdType = _CmIpInterfaceDhcpClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 17),
    _CmIpInterfaceDhcpClientIdType_Type()
)
cmIpInterfaceDhcpClientIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpClientIdType.setStatus("current")
_CmIpInterfaceDhcpHostNameType_Type = DHCPHostNameType
_CmIpInterfaceDhcpHostNameType_Object = MibTableColumn
cmIpInterfaceDhcpHostNameType = _CmIpInterfaceDhcpHostNameType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 18),
    _CmIpInterfaceDhcpHostNameType_Type()
)
cmIpInterfaceDhcpHostNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpHostNameType.setStatus("current")
_CmIpInterfaceDhcpVendorInfoEnabled_Type = TruthValue
_CmIpInterfaceDhcpVendorInfoEnabled_Object = MibTableColumn
cmIpInterfaceDhcpVendorInfoEnabled = _CmIpInterfaceDhcpVendorInfoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 19),
    _CmIpInterfaceDhcpVendorInfoEnabled_Type()
)
cmIpInterfaceDhcpVendorInfoEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpVendorInfoEnabled.setStatus("current")
_CmIpInterfaceDhcpVendorInfoType_Type = DHCPVendorInfoType
_CmIpInterfaceDhcpVendorInfoType_Object = MibTableColumn
cmIpInterfaceDhcpVendorInfoType = _CmIpInterfaceDhcpVendorInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 20),
    _CmIpInterfaceDhcpVendorInfoType_Type()
)
cmIpInterfaceDhcpVendorInfoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpVendorInfoType.setStatus("current")
_CmIpInterfaceDhcpVendorInfo_Type = DisplayString
_CmIpInterfaceDhcpVendorInfo_Object = MibTableColumn
cmIpInterfaceDhcpVendorInfo = _CmIpInterfaceDhcpVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 21),
    _CmIpInterfaceDhcpVendorInfo_Type()
)
cmIpInterfaceDhcpVendorInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpVendorInfo.setStatus("current")
_CmIpInterfaceDhcpVendorInfoHideControl_Type = TruthValue
_CmIpInterfaceDhcpVendorInfoHideControl_Object = MibTableColumn
cmIpInterfaceDhcpVendorInfoHideControl = _CmIpInterfaceDhcpVendorInfoHideControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 22),
    _CmIpInterfaceDhcpVendorInfoHideControl_Type()
)
cmIpInterfaceDhcpVendorInfoHideControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceDhcpVendorInfoHideControl.setStatus("current")
_CmIpInterfaceGateway_Type = IpAddress
_CmIpInterfaceGateway_Object = MibTableColumn
cmIpInterfaceGateway = _CmIpInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 1, 1, 23),
    _CmIpInterfaceGateway_Type()
)
cmIpInterfaceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInterfaceGateway.setStatus("current")
_CmStaticRouteTable_Object = MibTable
cmStaticRouteTable = _CmStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2)
)
if mibBuilder.loadTexts:
    cmStaticRouteTable.setStatus("current")
_CmStaticRouteEntry_Object = MibTableRow
cmStaticRouteEntry = _CmStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2, 1)
)
cmStaticRouteEntry.setIndexNames(
    (0, "CM-IP-MIB", "cmStaticRouteDest"),
    (0, "CM-IP-MIB", "cmStaticRouteMask"),
    (0, "CM-IP-MIB", "cmStaticRouteNextHop"),
    (0, "CM-IP-MIB", "cmStaticRouteInterface"),
)
if mibBuilder.loadTexts:
    cmStaticRouteEntry.setStatus("current")
_CmStaticRouteDest_Type = IpAddress
_CmStaticRouteDest_Object = MibTableColumn
cmStaticRouteDest = _CmStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2, 1, 1),
    _CmStaticRouteDest_Type()
)
cmStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmStaticRouteDest.setStatus("current")
_CmStaticRouteMask_Type = IpAddress
_CmStaticRouteMask_Object = MibTableColumn
cmStaticRouteMask = _CmStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2, 1, 2),
    _CmStaticRouteMask_Type()
)
cmStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmStaticRouteMask.setStatus("current")
_CmStaticRouteNextHop_Type = IpAddress
_CmStaticRouteNextHop_Object = MibTableColumn
cmStaticRouteNextHop = _CmStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2, 1, 3),
    _CmStaticRouteNextHop_Type()
)
cmStaticRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmStaticRouteNextHop.setStatus("current")


class _CmStaticRouteMetric_Type(Integer32):
    """Custom type cmStaticRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmStaticRouteMetric_Type.__name__ = "Integer32"
_CmStaticRouteMetric_Object = MibTableColumn
cmStaticRouteMetric = _CmStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2, 1, 4),
    _CmStaticRouteMetric_Type()
)
cmStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmStaticRouteMetric.setStatus("current")
_CmStaticRouteRowStatus_Type = RowStatus
_CmStaticRouteRowStatus_Object = MibTableColumn
cmStaticRouteRowStatus = _CmStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2, 1, 5),
    _CmStaticRouteRowStatus_Type()
)
cmStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmStaticRouteRowStatus.setStatus("current")


class _CmStaticRouteInterface_Type(DisplayString):
    """Custom type cmStaticRouteInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CmStaticRouteInterface_Type.__name__ = "DisplayString"
_CmStaticRouteInterface_Object = MibTableColumn
cmStaticRouteInterface = _CmStaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2, 1, 6),
    _CmStaticRouteInterface_Type()
)
cmStaticRouteInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmStaticRouteInterface.setStatus("current")
_CmStaticRouteAdvertise_Type = TruthValue
_CmStaticRouteAdvertise_Object = MibTableColumn
cmStaticRouteAdvertise = _CmStaticRouteAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 2, 1, 7),
    _CmStaticRouteAdvertise_Type()
)
cmStaticRouteAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmStaticRouteAdvertise.setStatus("current")
_CmARPTable_Object = MibTable
cmARPTable = _CmARPTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3)
)
if mibBuilder.loadTexts:
    cmARPTable.setStatus("current")
_CmARPEntry_Object = MibTableRow
cmARPEntry = _CmARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3, 1)
)
cmARPEntry.setIndexNames(
    (0, "CM-IP-MIB", "cmARPInterface"),
    (0, "CM-IP-MIB", "cmARPIPAddress"),
)
if mibBuilder.loadTexts:
    cmARPEntry.setStatus("current")


class _CmARPIndex_Type(Integer32):
    """Custom type cmARPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmARPIndex_Type.__name__ = "Integer32"
_CmARPIndex_Object = MibTableColumn
cmARPIndex = _CmARPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3, 1, 1),
    _CmARPIndex_Type()
)
cmARPIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmARPIndex.setStatus("deprecated")
_CmARPIPAddress_Type = IpAddress
_CmARPIPAddress_Object = MibTableColumn
cmARPIPAddress = _CmARPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3, 1, 2),
    _CmARPIPAddress_Type()
)
cmARPIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmARPIPAddress.setStatus("current")
_CmARPMacAddress_Type = MacAddress
_CmARPMacAddress_Object = MibTableColumn
cmARPMacAddress = _CmARPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3, 1, 3),
    _CmARPMacAddress_Type()
)
cmARPMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmARPMacAddress.setStatus("current")


class _CmARPInterface_Type(DisplayString):
    """Custom type cmARPInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CmARPInterface_Type.__name__ = "DisplayString"
_CmARPInterface_Object = MibTableColumn
cmARPInterface = _CmARPInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3, 1, 4),
    _CmARPInterface_Type()
)
cmARPInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmARPInterface.setStatus("current")
_CmARPStorageType_Type = StorageType
_CmARPStorageType_Object = MibTableColumn
cmARPStorageType = _CmARPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3, 1, 5),
    _CmARPStorageType_Type()
)
cmARPStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmARPStorageType.setStatus("current")
_CmARPRowStatus_Type = RowStatus
_CmARPRowStatus_Object = MibTableColumn
cmARPRowStatus = _CmARPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3, 1, 6),
    _CmARPRowStatus_Type()
)
cmARPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmARPRowStatus.setStatus("current")
_CmARPEntryType_Type = IpEntryType
_CmARPEntryType_Object = MibTableColumn
cmARPEntryType = _CmARPEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 3, 1, 7),
    _CmARPEntryType_Type()
)
cmARPEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmARPEntryType.setStatus("current")
_CmProxyARPTable_Object = MibTable
cmProxyARPTable = _CmProxyARPTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 4)
)
if mibBuilder.loadTexts:
    cmProxyARPTable.setStatus("current")
_CmProxyARPEntry_Object = MibTableRow
cmProxyARPEntry = _CmProxyARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 4, 1)
)
cmProxyARPEntry.setIndexNames(
    (0, "CM-IP-MIB", "cmProxyARPInterface"),
    (0, "CM-IP-MIB", "cmProxyARPIPAddress"),
    (0, "CM-IP-MIB", "cmProxyARPSubnetMask"),
)
if mibBuilder.loadTexts:
    cmProxyARPEntry.setStatus("current")


class _CmProxyARPIndex_Type(Integer32):
    """Custom type cmProxyARPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmProxyARPIndex_Type.__name__ = "Integer32"
_CmProxyARPIndex_Object = MibTableColumn
cmProxyARPIndex = _CmProxyARPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 4, 1, 1),
    _CmProxyARPIndex_Type()
)
cmProxyARPIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmProxyARPIndex.setStatus("deprecated")
_CmProxyARPIPAddress_Type = IpAddress
_CmProxyARPIPAddress_Object = MibTableColumn
cmProxyARPIPAddress = _CmProxyARPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 4, 1, 2),
    _CmProxyARPIPAddress_Type()
)
cmProxyARPIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmProxyARPIPAddress.setStatus("current")
_CmProxyARPSubnetMask_Type = IpAddress
_CmProxyARPSubnetMask_Object = MibTableColumn
cmProxyARPSubnetMask = _CmProxyARPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 4, 1, 3),
    _CmProxyARPSubnetMask_Type()
)
cmProxyARPSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmProxyARPSubnetMask.setStatus("current")


class _CmProxyARPInterface_Type(DisplayString):
    """Custom type cmProxyARPInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CmProxyARPInterface_Type.__name__ = "DisplayString"
_CmProxyARPInterface_Object = MibTableColumn
cmProxyARPInterface = _CmProxyARPInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 4, 1, 4),
    _CmProxyARPInterface_Type()
)
cmProxyARPInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmProxyARPInterface.setStatus("current")
_CmProxyARPStorageType_Type = StorageType
_CmProxyARPStorageType_Object = MibTableColumn
cmProxyARPStorageType = _CmProxyARPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 4, 1, 5),
    _CmProxyARPStorageType_Type()
)
cmProxyARPStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmProxyARPStorageType.setStatus("current")
_CmProxyARPRowStatus_Type = RowStatus
_CmProxyARPRowStatus_Object = MibTableColumn
cmProxyARPRowStatus = _CmProxyARPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 4, 1, 6),
    _CmProxyARPRowStatus_Type()
)
cmProxyARPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmProxyARPRowStatus.setStatus("current")
_IpManagementTunnelTable_Object = MibTable
ipManagementTunnelTable = _IpManagementTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5)
)
if mibBuilder.loadTexts:
    ipManagementTunnelTable.setStatus("current")
_IpManagementTunnelEntry_Object = MibTableRow
ipManagementTunnelEntry = _IpManagementTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1)
)
ipManagementTunnelEntry.setIndexNames(
    (0, "CM-IP-MIB", "ipManagementTunnelIndex"),
)
if mibBuilder.loadTexts:
    ipManagementTunnelEntry.setStatus("current")


class _IpManagementTunnelIndex_Type(Integer32):
    """Custom type ipManagementTunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpManagementTunnelIndex_Type.__name__ = "Integer32"
_IpManagementTunnelIndex_Object = MibTableColumn
ipManagementTunnelIndex = _IpManagementTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 1),
    _IpManagementTunnelIndex_Type()
)
ipManagementTunnelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelIndex.setStatus("current")
_IpManagementTunnelAssociatedPort_Type = VariablePointer
_IpManagementTunnelAssociatedPort_Object = MibTableColumn
ipManagementTunnelAssociatedPort = _IpManagementTunnelAssociatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 2),
    _IpManagementTunnelAssociatedPort_Type()
)
ipManagementTunnelAssociatedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelAssociatedPort.setStatus("current")


class _IpManagementTunnelName_Type(DisplayString):
    """Custom type ipManagementTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpManagementTunnelName_Type.__name__ = "DisplayString"
_IpManagementTunnelName_Object = MibTableColumn
ipManagementTunnelName = _IpManagementTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 3),
    _IpManagementTunnelName_Type()
)
ipManagementTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelName.setStatus("current")
_IpManagementTunnelType_Type = IpManagementTunnelType
_IpManagementTunnelType_Object = MibTableColumn
ipManagementTunnelType = _IpManagementTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 4),
    _IpManagementTunnelType_Type()
)
ipManagementTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelType.setStatus("current")
_IpManagementTunnelMTU_Type = Integer32
_IpManagementTunnelMTU_Object = MibTableColumn
ipManagementTunnelMTU = _IpManagementTunnelMTU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 5),
    _IpManagementTunnelMTU_Type()
)
ipManagementTunnelMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelMTU.setStatus("current")
_IpManagementTunnelEncapsulationType_Type = IpManagementTunnelEncapsulationType
_IpManagementTunnelEncapsulationType_Object = MibTableColumn
ipManagementTunnelEncapsulationType = _IpManagementTunnelEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 6),
    _IpManagementTunnelEncapsulationType_Type()
)
ipManagementTunnelEncapsulationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelEncapsulationType.setStatus("current")
_IpManagementTunnelIpAddress_Type = IpAddress
_IpManagementTunnelIpAddress_Object = MibTableColumn
ipManagementTunnelIpAddress = _IpManagementTunnelIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 7),
    _IpManagementTunnelIpAddress_Type()
)
ipManagementTunnelIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelIpAddress.setStatus("current")
_IpManagementTunnelSubnetMask_Type = IpAddress
_IpManagementTunnelSubnetMask_Object = MibTableColumn
ipManagementTunnelSubnetMask = _IpManagementTunnelSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 8),
    _IpManagementTunnelSubnetMask_Type()
)
ipManagementTunnelSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelSubnetMask.setStatus("current")
_IpManagementTunnelVlanId_Type = VlanId
_IpManagementTunnelVlanId_Object = MibTableColumn
ipManagementTunnelVlanId = _IpManagementTunnelVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 9),
    _IpManagementTunnelVlanId_Type()
)
ipManagementTunnelVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelVlanId.setStatus("current")
_IpManagementTunnelSVlanEnabled_Type = TruthValue
_IpManagementTunnelSVlanEnabled_Object = MibTableColumn
ipManagementTunnelSVlanEnabled = _IpManagementTunnelSVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 10),
    _IpManagementTunnelSVlanEnabled_Type()
)
ipManagementTunnelSVlanEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelSVlanEnabled.setStatus("current")
_IpManagementTunnelSVlanId_Type = VlanId
_IpManagementTunnelSVlanId_Object = MibTableColumn
ipManagementTunnelSVlanId = _IpManagementTunnelSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 11),
    _IpManagementTunnelSVlanId_Type()
)
ipManagementTunnelSVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelSVlanId.setStatus("current")
_IpManagementTunnelDhcpEnabled_Type = TruthValue
_IpManagementTunnelDhcpEnabled_Object = MibTableColumn
ipManagementTunnelDhcpEnabled = _IpManagementTunnelDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 12),
    _IpManagementTunnelDhcpEnabled_Type()
)
ipManagementTunnelDhcpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpEnabled.setStatus("current")
_IpManagementTunnelRip2PktsEnabled_Type = TruthValue
_IpManagementTunnelRip2PktsEnabled_Object = MibTableColumn
ipManagementTunnelRip2PktsEnabled = _IpManagementTunnelRip2PktsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 13),
    _IpManagementTunnelRip2PktsEnabled_Type()
)
ipManagementTunnelRip2PktsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelRip2PktsEnabled.setStatus("current")
_IpManagementTunnelPhysicalAddress_Type = DisplayString
_IpManagementTunnelPhysicalAddress_Object = MibTableColumn
ipManagementTunnelPhysicalAddress = _IpManagementTunnelPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 14),
    _IpManagementTunnelPhysicalAddress_Type()
)
ipManagementTunnelPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipManagementTunnelPhysicalAddress.setStatus("current")


class _IpManagementTunnelCOS_Type(Integer32):
    """Custom type ipManagementTunnelCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IpManagementTunnelCOS_Type.__name__ = "Integer32"
_IpManagementTunnelCOS_Object = MibTableColumn
ipManagementTunnelCOS = _IpManagementTunnelCOS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 15),
    _IpManagementTunnelCOS_Type()
)
ipManagementTunnelCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelCOS.setStatus("current")
_IpManagementTunnelCIR_Type = Unsigned32
_IpManagementTunnelCIR_Object = MibTableColumn
ipManagementTunnelCIR = _IpManagementTunnelCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 16),
    _IpManagementTunnelCIR_Type()
)
ipManagementTunnelCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelCIR.setStatus("current")
_IpManagementTunnelEIR_Type = Unsigned32
_IpManagementTunnelEIR_Object = MibTableColumn
ipManagementTunnelEIR = _IpManagementTunnelEIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 17),
    _IpManagementTunnelEIR_Type()
)
ipManagementTunnelEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelEIR.setStatus("current")
_IpManagementTunnelBufferSize_Type = Unsigned32
_IpManagementTunnelBufferSize_Object = MibTableColumn
ipManagementTunnelBufferSize = _IpManagementTunnelBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 18),
    _IpManagementTunnelBufferSize_Type()
)
ipManagementTunnelBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelBufferSize.setStatus("current")
_IpManagementTunnelStorageType_Type = StorageType
_IpManagementTunnelStorageType_Object = MibTableColumn
ipManagementTunnelStorageType = _IpManagementTunnelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 19),
    _IpManagementTunnelStorageType_Type()
)
ipManagementTunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipManagementTunnelStorageType.setStatus("current")
_IpManagementTunnelRowStatus_Type = RowStatus
_IpManagementTunnelRowStatus_Object = MibTableColumn
ipManagementTunnelRowStatus = _IpManagementTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 20),
    _IpManagementTunnelRowStatus_Type()
)
ipManagementTunnelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelRowStatus.setStatus("current")
_IpManagementTunnelDHCPClientIdEnabled_Type = TruthValue
_IpManagementTunnelDHCPClientIdEnabled_Object = MibTableColumn
ipManagementTunnelDHCPClientIdEnabled = _IpManagementTunnelDHCPClientIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 21),
    _IpManagementTunnelDHCPClientIdEnabled_Type()
)
ipManagementTunnelDHCPClientIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDHCPClientIdEnabled.setStatus("current")


class _IpManagementTunnelDHCPClientId_Type(DisplayString):
    """Custom type ipManagementTunnelDHCPClientId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpManagementTunnelDHCPClientId_Type.__name__ = "DisplayString"
_IpManagementTunnelDHCPClientId_Object = MibTableColumn
ipManagementTunnelDHCPClientId = _IpManagementTunnelDHCPClientId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 22),
    _IpManagementTunnelDHCPClientId_Type()
)
ipManagementTunnelDHCPClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDHCPClientId.setStatus("current")
_IpManagementTunnelQosQueueProfile_Type = VariablePointer
_IpManagementTunnelQosQueueProfile_Object = MibTableColumn
ipManagementTunnelQosQueueProfile = _IpManagementTunnelQosQueueProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 23),
    _IpManagementTunnelQosQueueProfile_Type()
)
ipManagementTunnelQosQueueProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelQosQueueProfile.setStatus("current")
_IpManagementTunnelCVlanEnabled_Type = TruthValue
_IpManagementTunnelCVlanEnabled_Object = MibTableColumn
ipManagementTunnelCVlanEnabled = _IpManagementTunnelCVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 24),
    _IpManagementTunnelCVlanEnabled_Type()
)
ipManagementTunnelCVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelCVlanEnabled.setStatus("current")
_IpManagementTunnelDHCPv6Enabled_Type = TruthValue
_IpManagementTunnelDHCPv6Enabled_Object = MibTableColumn
ipManagementTunnelDHCPv6Enabled = _IpManagementTunnelDHCPv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 25),
    _IpManagementTunnelDHCPv6Enabled_Type()
)
ipManagementTunnelDHCPv6Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDHCPv6Enabled.setStatus("current")
_IpManagementTunnelIpv6Address_Type = Ipv6Address
_IpManagementTunnelIpv6Address_Object = MibTableColumn
ipManagementTunnelIpv6Address = _IpManagementTunnelIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 26),
    _IpManagementTunnelIpv6Address_Type()
)
ipManagementTunnelIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelIpv6Address.setStatus("current")


class _IpManagementTunnelIpv6AddrPrefixLen_Type(Integer32):
    """Custom type ipManagementTunnelIpv6AddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IpManagementTunnelIpv6AddrPrefixLen_Type.__name__ = "Integer32"
_IpManagementTunnelIpv6AddrPrefixLen_Object = MibTableColumn
ipManagementTunnelIpv6AddrPrefixLen = _IpManagementTunnelIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 27),
    _IpManagementTunnelIpv6AddrPrefixLen_Type()
)
ipManagementTunnelIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelIpv6AddrPrefixLen.setStatus("current")
_IpManagementTunnelIpv6StateAddrAutoConfigEnabled_Type = TruthValue
_IpManagementTunnelIpv6StateAddrAutoConfigEnabled_Object = MibTableColumn
ipManagementTunnelIpv6StateAddrAutoConfigEnabled = _IpManagementTunnelIpv6StateAddrAutoConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 28),
    _IpManagementTunnelIpv6StateAddrAutoConfigEnabled_Type()
)
ipManagementTunnelIpv6StateAddrAutoConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelIpv6StateAddrAutoConfigEnabled.setStatus("current")
_IpManagementTunnellinkLocIpv6Addr_Type = Ipv6Address
_IpManagementTunnellinkLocIpv6Addr_Object = MibTableColumn
ipManagementTunnellinkLocIpv6Addr = _IpManagementTunnellinkLocIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 29),
    _IpManagementTunnellinkLocIpv6Addr_Type()
)
ipManagementTunnellinkLocIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipManagementTunnellinkLocIpv6Addr.setStatus("current")


class _IpManagementTunnellinkLocIpv6AddrPrefixLen_Type(Integer32):
    """Custom type ipManagementTunnellinkLocIpv6AddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IpManagementTunnellinkLocIpv6AddrPrefixLen_Type.__name__ = "Integer32"
_IpManagementTunnellinkLocIpv6AddrPrefixLen_Object = MibTableColumn
ipManagementTunnellinkLocIpv6AddrPrefixLen = _IpManagementTunnellinkLocIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 30),
    _IpManagementTunnellinkLocIpv6AddrPrefixLen_Type()
)
ipManagementTunnellinkLocIpv6AddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipManagementTunnellinkLocIpv6AddrPrefixLen.setStatus("current")
_IpManagementTunnelIpv6PrefixAdvertiseEnabled_Type = TruthValue
_IpManagementTunnelIpv6PrefixAdvertiseEnabled_Object = MibTableColumn
ipManagementTunnelIpv6PrefixAdvertiseEnabled = _IpManagementTunnelIpv6PrefixAdvertiseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 31),
    _IpManagementTunnelIpv6PrefixAdvertiseEnabled_Type()
)
ipManagementTunnelIpv6PrefixAdvertiseEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelIpv6PrefixAdvertiseEnabled.setStatus("current")
_IpManagementTunnelIpv6Prefix_Type = Ipv6Address
_IpManagementTunnelIpv6Prefix_Object = MibTableColumn
ipManagementTunnelIpv6Prefix = _IpManagementTunnelIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 32),
    _IpManagementTunnelIpv6Prefix_Type()
)
ipManagementTunnelIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelIpv6Prefix.setStatus("current")


class _IpManagementTunnelIpv6PrefixLen_Type(Integer32):
    """Custom type ipManagementTunnelIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IpManagementTunnelIpv6PrefixLen_Type.__name__ = "Integer32"
_IpManagementTunnelIpv6PrefixLen_Object = MibTableColumn
ipManagementTunnelIpv6PrefixLen = _IpManagementTunnelIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 33),
    _IpManagementTunnelIpv6PrefixLen_Type()
)
ipManagementTunnelIpv6PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelIpv6PrefixLen.setStatus("current")
_IpManagementTunnelIpMode_Type = IpMode
_IpManagementTunnelIpMode_Object = MibTableColumn
ipManagementTunnelIpMode = _IpManagementTunnelIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 34),
    _IpManagementTunnelIpMode_Type()
)
ipManagementTunnelIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelIpMode.setStatus("current")
_IpManagementTunnelIpv6RipngEnabled_Type = TruthValue
_IpManagementTunnelIpv6RipngEnabled_Object = MibTableColumn
ipManagementTunnelIpv6RipngEnabled = _IpManagementTunnelIpv6RipngEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 35),
    _IpManagementTunnelIpv6RipngEnabled_Type()
)
ipManagementTunnelIpv6RipngEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelIpv6RipngEnabled.setStatus("current")
_IpManagementTunnelDhcpClassIdEnabled_Type = TruthValue
_IpManagementTunnelDhcpClassIdEnabled_Object = MibTableColumn
ipManagementTunnelDhcpClassIdEnabled = _IpManagementTunnelDhcpClassIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 36),
    _IpManagementTunnelDhcpClassIdEnabled_Type()
)
ipManagementTunnelDhcpClassIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpClassIdEnabled.setStatus("current")
_IpManagementTunnelDhcpHostNameEnabled_Type = TruthValue
_IpManagementTunnelDhcpHostNameEnabled_Object = MibTableColumn
ipManagementTunnelDhcpHostNameEnabled = _IpManagementTunnelDhcpHostNameEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 37),
    _IpManagementTunnelDhcpHostNameEnabled_Type()
)
ipManagementTunnelDhcpHostNameEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpHostNameEnabled.setStatus("current")
_IpManagementTunnelDhcpHostName_Type = DisplayString
_IpManagementTunnelDhcpHostName_Object = MibTableColumn
ipManagementTunnelDhcpHostName = _IpManagementTunnelDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 38),
    _IpManagementTunnelDhcpHostName_Type()
)
ipManagementTunnelDhcpHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpHostName.setStatus("current")
_IpManagementTunnelDhcpLogServerEnabled_Type = TruthValue
_IpManagementTunnelDhcpLogServerEnabled_Object = MibTableColumn
ipManagementTunnelDhcpLogServerEnabled = _IpManagementTunnelDhcpLogServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 39),
    _IpManagementTunnelDhcpLogServerEnabled_Type()
)
ipManagementTunnelDhcpLogServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpLogServerEnabled.setStatus("current")
_IpManagementTunnelDhcpNTPServerEnabled_Type = TruthValue
_IpManagementTunnelDhcpNTPServerEnabled_Object = MibTableColumn
ipManagementTunnelDhcpNTPServerEnabled = _IpManagementTunnelDhcpNTPServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 40),
    _IpManagementTunnelDhcpNTPServerEnabled_Type()
)
ipManagementTunnelDhcpNTPServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpNTPServerEnabled.setStatus("current")
_IpManagementTunnelDhcpClientIdType_Type = DHCPCIDType
_IpManagementTunnelDhcpClientIdType_Object = MibTableColumn
ipManagementTunnelDhcpClientIdType = _IpManagementTunnelDhcpClientIdType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 41),
    _IpManagementTunnelDhcpClientIdType_Type()
)
ipManagementTunnelDhcpClientIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpClientIdType.setStatus("current")
_IpManagementTunnelDhcpHostNameType_Type = DHCPHostNameType
_IpManagementTunnelDhcpHostNameType_Object = MibTableColumn
ipManagementTunnelDhcpHostNameType = _IpManagementTunnelDhcpHostNameType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 42),
    _IpManagementTunnelDhcpHostNameType_Type()
)
ipManagementTunnelDhcpHostNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpHostNameType.setStatus("current")
_IpManagementTunnelDhcpVendorInfoEnabled_Type = TruthValue
_IpManagementTunnelDhcpVendorInfoEnabled_Object = MibTableColumn
ipManagementTunnelDhcpVendorInfoEnabled = _IpManagementTunnelDhcpVendorInfoEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 43),
    _IpManagementTunnelDhcpVendorInfoEnabled_Type()
)
ipManagementTunnelDhcpVendorInfoEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpVendorInfoEnabled.setStatus("current")
_IpManagementTunnelDhcpVendorInfoType_Type = DHCPVendorInfoType
_IpManagementTunnelDhcpVendorInfoType_Object = MibTableColumn
ipManagementTunnelDhcpVendorInfoType = _IpManagementTunnelDhcpVendorInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 44),
    _IpManagementTunnelDhcpVendorInfoType_Type()
)
ipManagementTunnelDhcpVendorInfoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpVendorInfoType.setStatus("current")
_IpManagementTunnelDhcpVendorInfo_Type = DisplayString
_IpManagementTunnelDhcpVendorInfo_Object = MibTableColumn
ipManagementTunnelDhcpVendorInfo = _IpManagementTunnelDhcpVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 45),
    _IpManagementTunnelDhcpVendorInfo_Type()
)
ipManagementTunnelDhcpVendorInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpVendorInfo.setStatus("current")
_IpManagementTunnelDhcpVendorInfoHideControl_Type = TruthValue
_IpManagementTunnelDhcpVendorInfoHideControl_Object = MibTableColumn
ipManagementTunnelDhcpVendorInfoHideControl = _IpManagementTunnelDhcpVendorInfoHideControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 46),
    _IpManagementTunnelDhcpVendorInfoHideControl_Type()
)
ipManagementTunnelDhcpVendorInfoHideControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelDhcpVendorInfoHideControl.setStatus("current")
_IpManagementTunnelSharedVim_Type = TruthValue
_IpManagementTunnelSharedVim_Object = MibTableColumn
ipManagementTunnelSharedVim = _IpManagementTunnelSharedVim_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 5, 1, 47),
    _IpManagementTunnelSharedVim_Type()
)
ipManagementTunnelSharedVim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipManagementTunnelSharedVim.setStatus("current")
_CmIpv6InterfaceTable_Object = MibTable
cmIpv6InterfaceTable = _CmIpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6)
)
if mibBuilder.loadTexts:
    cmIpv6InterfaceTable.setStatus("current")
_CmIpv6InterfaceEntry_Object = MibTableRow
cmIpv6InterfaceEntry = _CmIpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cmIpv6InterfaceEntry.setStatus("current")
_CmIpv6InterfaceMTU_Type = Integer32
_CmIpv6InterfaceMTU_Object = MibTableColumn
cmIpv6InterfaceMTU = _CmIpv6InterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 1),
    _CmIpv6InterfaceMTU_Type()
)
cmIpv6InterfaceMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6InterfaceMTU.setStatus("current")
_CmIpv6UnicastAddr_Type = Ipv6Address
_CmIpv6UnicastAddr_Object = MibTableColumn
cmIpv6UnicastAddr = _CmIpv6UnicastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 2),
    _CmIpv6UnicastAddr_Type()
)
cmIpv6UnicastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6UnicastAddr.setStatus("current")


class _CmIpv6UnicastAddrPrefixLen_Type(Integer32):
    """Custom type cmIpv6UnicastAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CmIpv6UnicastAddrPrefixLen_Type.__name__ = "Integer32"
_CmIpv6UnicastAddrPrefixLen_Object = MibTableColumn
cmIpv6UnicastAddrPrefixLen = _CmIpv6UnicastAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 3),
    _CmIpv6UnicastAddrPrefixLen_Type()
)
cmIpv6UnicastAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6UnicastAddrPrefixLen.setStatus("current")
_CmIpv6PrefixAdvertiseEnabled_Type = TruthValue
_CmIpv6PrefixAdvertiseEnabled_Object = MibTableColumn
cmIpv6PrefixAdvertiseEnabled = _CmIpv6PrefixAdvertiseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 4),
    _CmIpv6PrefixAdvertiseEnabled_Type()
)
cmIpv6PrefixAdvertiseEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6PrefixAdvertiseEnabled.setStatus("current")
_CmIpv6RAPrefix_Type = Ipv6Address
_CmIpv6RAPrefix_Object = MibTableColumn
cmIpv6RAPrefix = _CmIpv6RAPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 5),
    _CmIpv6RAPrefix_Type()
)
cmIpv6RAPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6RAPrefix.setStatus("current")


class _CmIpv6RAPrefixLength_Type(Integer32):
    """Custom type cmIpv6RAPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CmIpv6RAPrefixLength_Type.__name__ = "Integer32"
_CmIpv6RAPrefixLength_Object = MibTableColumn
cmIpv6RAPrefixLength = _CmIpv6RAPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 6),
    _CmIpv6RAPrefixLength_Type()
)
cmIpv6RAPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6RAPrefixLength.setStatus("current")
_CmIpv6StateAddrAutoConfigEnabled_Type = TruthValue
_CmIpv6StateAddrAutoConfigEnabled_Object = MibTableColumn
cmIpv6StateAddrAutoConfigEnabled = _CmIpv6StateAddrAutoConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 7),
    _CmIpv6StateAddrAutoConfigEnabled_Type()
)
cmIpv6StateAddrAutoConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6StateAddrAutoConfigEnabled.setStatus("current")
_CmIpv6DhcpEnabled_Type = TruthValue
_CmIpv6DhcpEnabled_Object = MibTableColumn
cmIpv6DhcpEnabled = _CmIpv6DhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 8),
    _CmIpv6DhcpEnabled_Type()
)
cmIpv6DhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6DhcpEnabled.setStatus("current")
_CmIpv6DhcpRole_Type = CmDhcpRole
_CmIpv6DhcpRole_Object = MibTableColumn
cmIpv6DhcpRole = _CmIpv6DhcpRole_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 9),
    _CmIpv6DhcpRole_Type()
)
cmIpv6DhcpRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6DhcpRole.setStatus("current")
_CmIpv6RIPngEnabled_Type = TruthValue
_CmIpv6RIPngEnabled_Object = MibTableColumn
cmIpv6RIPngEnabled = _CmIpv6RIPngEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 10),
    _CmIpv6RIPngEnabled_Type()
)
cmIpv6RIPngEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6RIPngEnabled.setStatus("current")
_CmIpv6LinkLocAddr_Type = Ipv6Address
_CmIpv6LinkLocAddr_Object = MibTableColumn
cmIpv6LinkLocAddr = _CmIpv6LinkLocAddr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 11),
    _CmIpv6LinkLocAddr_Type()
)
cmIpv6LinkLocAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIpv6LinkLocAddr.setStatus("current")


class _CmIpv6LinkLocAddrPrefixLen_Type(Integer32):
    """Custom type cmIpv6LinkLocAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CmIpv6LinkLocAddrPrefixLen_Type.__name__ = "Integer32"
_CmIpv6LinkLocAddrPrefixLen_Object = MibTableColumn
cmIpv6LinkLocAddrPrefixLen = _CmIpv6LinkLocAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 12),
    _CmIpv6LinkLocAddrPrefixLen_Type()
)
cmIpv6LinkLocAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIpv6LinkLocAddrPrefixLen.setStatus("current")
_CmIpv6InterfaceGateway_Type = Ipv6Address
_CmIpv6InterfaceGateway_Object = MibTableColumn
cmIpv6InterfaceGateway = _CmIpv6InterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 6, 1, 13),
    _CmIpv6InterfaceGateway_Type()
)
cmIpv6InterfaceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6InterfaceGateway.setStatus("current")
_CmIpv6StaticRouteTable_Object = MibTable
cmIpv6StaticRouteTable = _CmIpv6StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7)
)
if mibBuilder.loadTexts:
    cmIpv6StaticRouteTable.setStatus("current")
_CmIpv6StaticRouteEntry_Object = MibTableRow
cmIpv6StaticRouteEntry = _CmIpv6StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7, 1)
)
cmIpv6StaticRouteEntry.setIndexNames(
    (0, "CM-IP-MIB", "cmIpv6StaticRouteDest"),
    (0, "CM-IP-MIB", "cmIpv6StaticRoutePrefixLen"),
    (0, "CM-IP-MIB", "cmIpv6StaticRouteNextHop"),
    (0, "CM-IP-MIB", "cmIpv6StaticRouteInterface"),
)
if mibBuilder.loadTexts:
    cmIpv6StaticRouteEntry.setStatus("current")
_CmIpv6StaticRouteDest_Type = Ipv6Address
_CmIpv6StaticRouteDest_Object = MibTableColumn
cmIpv6StaticRouteDest = _CmIpv6StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7, 1, 1),
    _CmIpv6StaticRouteDest_Type()
)
cmIpv6StaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmIpv6StaticRouteDest.setStatus("current")


class _CmIpv6StaticRoutePrefixLen_Type(Integer32):
    """Custom type cmIpv6StaticRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CmIpv6StaticRoutePrefixLen_Type.__name__ = "Integer32"
_CmIpv6StaticRoutePrefixLen_Object = MibTableColumn
cmIpv6StaticRoutePrefixLen = _CmIpv6StaticRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7, 1, 2),
    _CmIpv6StaticRoutePrefixLen_Type()
)
cmIpv6StaticRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmIpv6StaticRoutePrefixLen.setStatus("current")
_CmIpv6StaticRouteNextHop_Type = Ipv6Address
_CmIpv6StaticRouteNextHop_Object = MibTableColumn
cmIpv6StaticRouteNextHop = _CmIpv6StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7, 1, 3),
    _CmIpv6StaticRouteNextHop_Type()
)
cmIpv6StaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmIpv6StaticRouteNextHop.setStatus("current")


class _CmIpv6StaticRouteMetric_Type(Integer32):
    """Custom type cmIpv6StaticRouteMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmIpv6StaticRouteMetric_Type.__name__ = "Integer32"
_CmIpv6StaticRouteMetric_Object = MibTableColumn
cmIpv6StaticRouteMetric = _CmIpv6StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7, 1, 4),
    _CmIpv6StaticRouteMetric_Type()
)
cmIpv6StaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmIpv6StaticRouteMetric.setStatus("current")
_CmIpv6StaticRouteRowStatus_Type = RowStatus
_CmIpv6StaticRouteRowStatus_Object = MibTableColumn
cmIpv6StaticRouteRowStatus = _CmIpv6StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7, 1, 5),
    _CmIpv6StaticRouteRowStatus_Type()
)
cmIpv6StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmIpv6StaticRouteRowStatus.setStatus("current")


class _CmIpv6StaticRouteInterface_Type(DisplayString):
    """Custom type cmIpv6StaticRouteInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CmIpv6StaticRouteInterface_Type.__name__ = "DisplayString"
_CmIpv6StaticRouteInterface_Object = MibTableColumn
cmIpv6StaticRouteInterface = _CmIpv6StaticRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7, 1, 6),
    _CmIpv6StaticRouteInterface_Type()
)
cmIpv6StaticRouteInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmIpv6StaticRouteInterface.setStatus("current")
_CmIpv6StaticRouteAdvertise_Type = TruthValue
_CmIpv6StaticRouteAdvertise_Object = MibTableColumn
cmIpv6StaticRouteAdvertise = _CmIpv6StaticRouteAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 7, 1, 7),
    _CmIpv6StaticRouteAdvertise_Type()
)
cmIpv6StaticRouteAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmIpv6StaticRouteAdvertise.setStatus("current")
_CmNDPTable_Object = MibTable
cmNDPTable = _CmNDPTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 8)
)
if mibBuilder.loadTexts:
    cmNDPTable.setStatus("current")
_CmNDPEntry_Object = MibTableRow
cmNDPEntry = _CmNDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 8, 1)
)
cmNDPEntry.setIndexNames(
    (0, "CM-IP-MIB", "cmNDPInterface"),
    (0, "CM-IP-MIB", "cmNDPIpv6Address"),
)
if mibBuilder.loadTexts:
    cmNDPEntry.setStatus("current")
_CmNDPIpv6Address_Type = Ipv6Address
_CmNDPIpv6Address_Object = MibTableColumn
cmNDPIpv6Address = _CmNDPIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 8, 1, 1),
    _CmNDPIpv6Address_Type()
)
cmNDPIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmNDPIpv6Address.setStatus("current")
_CmNDPMacAddress_Type = MacAddress
_CmNDPMacAddress_Object = MibTableColumn
cmNDPMacAddress = _CmNDPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 8, 1, 2),
    _CmNDPMacAddress_Type()
)
cmNDPMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmNDPMacAddress.setStatus("current")


class _CmNDPInterface_Type(DisplayString):
    """Custom type cmNDPInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CmNDPInterface_Type.__name__ = "DisplayString"
_CmNDPInterface_Object = MibTableColumn
cmNDPInterface = _CmNDPInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 8, 1, 3),
    _CmNDPInterface_Type()
)
cmNDPInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmNDPInterface.setStatus("current")
_CmNDPStorageType_Type = StorageType
_CmNDPStorageType_Object = MibTableColumn
cmNDPStorageType = _CmNDPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 8, 1, 4),
    _CmNDPStorageType_Type()
)
cmNDPStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmNDPStorageType.setStatus("current")
_CmNDPRowStatus_Type = RowStatus
_CmNDPRowStatus_Object = MibTableColumn
cmNDPRowStatus = _CmNDPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 8, 1, 5),
    _CmNDPRowStatus_Type()
)
cmNDPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmNDPRowStatus.setStatus("current")
_CmNDPEntryType_Type = IpEntryType
_CmNDPEntryType_Object = MibTableColumn
cmNDPEntryType = _CmNDPEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 8, 1, 6),
    _CmNDPEntryType_Type()
)
cmNDPEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmNDPEntryType.setStatus("current")
_CmProxyNDPTable_Object = MibTable
cmProxyNDPTable = _CmProxyNDPTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 9)
)
if mibBuilder.loadTexts:
    cmProxyNDPTable.setStatus("current")
_CmProxyNDPEntry_Object = MibTableRow
cmProxyNDPEntry = _CmProxyNDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 9, 1)
)
cmProxyNDPEntry.setIndexNames(
    (0, "CM-IP-MIB", "cmProxyNDPInterface"),
    (0, "CM-IP-MIB", "cmProxyNDPIpv6Address"),
    (0, "CM-IP-MIB", "cmProxyNDPIpv6PrefixLen"),
)
if mibBuilder.loadTexts:
    cmProxyNDPEntry.setStatus("current")
_CmProxyNDPIpv6Address_Type = Ipv6Address
_CmProxyNDPIpv6Address_Object = MibTableColumn
cmProxyNDPIpv6Address = _CmProxyNDPIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 9, 1, 1),
    _CmProxyNDPIpv6Address_Type()
)
cmProxyNDPIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmProxyNDPIpv6Address.setStatus("current")


class _CmProxyNDPIpv6PrefixLen_Type(Integer32):
    """Custom type cmProxyNDPIpv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CmProxyNDPIpv6PrefixLen_Type.__name__ = "Integer32"
_CmProxyNDPIpv6PrefixLen_Object = MibTableColumn
cmProxyNDPIpv6PrefixLen = _CmProxyNDPIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 9, 1, 2),
    _CmProxyNDPIpv6PrefixLen_Type()
)
cmProxyNDPIpv6PrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmProxyNDPIpv6PrefixLen.setStatus("current")


class _CmProxyNDPInterface_Type(DisplayString):
    """Custom type cmProxyNDPInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CmProxyNDPInterface_Type.__name__ = "DisplayString"
_CmProxyNDPInterface_Object = MibTableColumn
cmProxyNDPInterface = _CmProxyNDPInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 9, 1, 3),
    _CmProxyNDPInterface_Type()
)
cmProxyNDPInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmProxyNDPInterface.setStatus("current")
_CmProxyNDPStorageType_Type = StorageType
_CmProxyNDPStorageType_Object = MibTableColumn
cmProxyNDPStorageType = _CmProxyNDPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 9, 1, 4),
    _CmProxyNDPStorageType_Type()
)
cmProxyNDPStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmProxyNDPStorageType.setStatus("current")
_CmProxyNDPRowStatus_Type = RowStatus
_CmProxyNDPRowStatus_Object = MibTableColumn
cmProxyNDPRowStatus = _CmProxyNDPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 9, 1, 5),
    _CmProxyNDPRowStatus_Type()
)
cmProxyNDPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmProxyNDPRowStatus.setStatus("current")
_CmIpv6OverIpv4TunnelTable_Object = MibTable
cmIpv6OverIpv4TunnelTable = _CmIpv6OverIpv4TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10)
)
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelTable.setStatus("current")
_CmIpv6OverIpv4TunnelEntry_Object = MibTableRow
cmIpv6OverIpv4TunnelEntry = _CmIpv6OverIpv4TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1)
)
cmIpv6OverIpv4TunnelEntry.setIndexNames(
    (0, "CM-IP-MIB", "cmIpv6OverIpv4TunnelIndex"),
)
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelEntry.setStatus("current")
_CmIpv6OverIpv4TunnelIndex_Type = Integer32
_CmIpv6OverIpv4TunnelIndex_Object = MibTableColumn
cmIpv6OverIpv4TunnelIndex = _CmIpv6OverIpv4TunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 1),
    _CmIpv6OverIpv4TunnelIndex_Type()
)
cmIpv6OverIpv4TunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelIndex.setStatus("current")


class _CmIpv6OverIpv4TunnelName_Type(DisplayString):
    """Custom type cmIpv6OverIpv4TunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CmIpv6OverIpv4TunnelName_Type.__name__ = "DisplayString"
_CmIpv6OverIpv4TunnelName_Object = MibTableColumn
cmIpv6OverIpv4TunnelName = _CmIpv6OverIpv4TunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 2),
    _CmIpv6OverIpv4TunnelName_Type()
)
cmIpv6OverIpv4TunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelName.setStatus("current")
_CmIpv6OverIpv4TunnelType_Type = Ipv6OverIpv4TunnelType
_CmIpv6OverIpv4TunnelType_Object = MibTableColumn
cmIpv6OverIpv4TunnelType = _CmIpv6OverIpv4TunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 3),
    _CmIpv6OverIpv4TunnelType_Type()
)
cmIpv6OverIpv4TunnelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelType.setStatus("current")
_CmIpv6OverIpv4TunnelDestIpv4Addr_Type = IpAddress
_CmIpv6OverIpv4TunnelDestIpv4Addr_Object = MibTableColumn
cmIpv6OverIpv4TunnelDestIpv4Addr = _CmIpv6OverIpv4TunnelDestIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 4),
    _CmIpv6OverIpv4TunnelDestIpv4Addr_Type()
)
cmIpv6OverIpv4TunnelDestIpv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelDestIpv4Addr.setStatus("current")
_CmIpv6OverIpv4TunnelIpv6UnicastAddress_Type = Ipv6Address
_CmIpv6OverIpv4TunnelIpv6UnicastAddress_Object = MibTableColumn
cmIpv6OverIpv4TunnelIpv6UnicastAddress = _CmIpv6OverIpv4TunnelIpv6UnicastAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 5),
    _CmIpv6OverIpv4TunnelIpv6UnicastAddress_Type()
)
cmIpv6OverIpv4TunnelIpv6UnicastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelIpv6UnicastAddress.setStatus("current")


class _CmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen_Type(Integer32):
    """Custom type cmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen_Type.__name__ = "Integer32"
_CmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen_Object = MibTableColumn
cmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen = _CmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 6),
    _CmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen_Type()
)
cmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen.setStatus("current")
_CmIpv6OverIpv4TunnelLinkLocalAddress_Type = Ipv6Address
_CmIpv6OverIpv4TunnelLinkLocalAddress_Object = MibTableColumn
cmIpv6OverIpv4TunnelLinkLocalAddress = _CmIpv6OverIpv4TunnelLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 7),
    _CmIpv6OverIpv4TunnelLinkLocalAddress_Type()
)
cmIpv6OverIpv4TunnelLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelLinkLocalAddress.setStatus("current")
_CmIpv60verIpv4TunnelLinkLocalAddrPrefixLen_Type = Integer32
_CmIpv60verIpv4TunnelLinkLocalAddrPrefixLen_Object = MibTableColumn
cmIpv60verIpv4TunnelLinkLocalAddrPrefixLen = _CmIpv60verIpv4TunnelLinkLocalAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 8),
    _CmIpv60verIpv4TunnelLinkLocalAddrPrefixLen_Type()
)
cmIpv60verIpv4TunnelLinkLocalAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIpv60verIpv4TunnelLinkLocalAddrPrefixLen.setStatus("current")
_CmIpv6OverIpv4TunnelAssociatedIpv4Interface_Type = VariablePointer
_CmIpv6OverIpv4TunnelAssociatedIpv4Interface_Object = MibTableColumn
cmIpv6OverIpv4TunnelAssociatedIpv4Interface = _CmIpv6OverIpv4TunnelAssociatedIpv4Interface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 9),
    _CmIpv6OverIpv4TunnelAssociatedIpv4Interface_Type()
)
cmIpv6OverIpv4TunnelAssociatedIpv4Interface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelAssociatedIpv4Interface.setStatus("current")
_CmIpv6OverIpv4TunnelStorageType_Type = StorageType
_CmIpv6OverIpv4TunnelStorageType_Object = MibTableColumn
cmIpv6OverIpv4TunnelStorageType = _CmIpv6OverIpv4TunnelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 10),
    _CmIpv6OverIpv4TunnelStorageType_Type()
)
cmIpv6OverIpv4TunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelStorageType.setStatus("current")
_CmIpv6OverIpv4TunnelRowStatus_Type = RowStatus
_CmIpv6OverIpv4TunnelRowStatus_Object = MibTableColumn
cmIpv6OverIpv4TunnelRowStatus = _CmIpv6OverIpv4TunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 11),
    _CmIpv6OverIpv4TunnelRowStatus_Type()
)
cmIpv6OverIpv4TunnelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4TunnelRowStatus.setStatus("current")
_CmIpv6OverIpv4PotentialRouterList_Type = DisplayString
_CmIpv6OverIpv4PotentialRouterList_Object = MibTableColumn
cmIpv6OverIpv4PotentialRouterList = _CmIpv6OverIpv4PotentialRouterList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 10, 1, 12),
    _CmIpv6OverIpv4PotentialRouterList_Type()
)
cmIpv6OverIpv4PotentialRouterList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmIpv6OverIpv4PotentialRouterList.setStatus("current")
_IpLoopbackInterfaceTable_Object = MibTable
ipLoopbackInterfaceTable = _IpLoopbackInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11)
)
if mibBuilder.loadTexts:
    ipLoopbackInterfaceTable.setStatus("current")
_IpLoopbackInterfaceEntry_Object = MibTableRow
ipLoopbackInterfaceEntry = _IpLoopbackInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1)
)
ipLoopbackInterfaceEntry.setIndexNames(
    (0, "CM-IP-MIB", "ipLoopbackInterfaceIndex"),
)
if mibBuilder.loadTexts:
    ipLoopbackInterfaceEntry.setStatus("current")


class _IpLoopbackInterfaceIndex_Type(Integer32):
    """Custom type ipLoopbackInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpLoopbackInterfaceIndex_Type.__name__ = "Integer32"
_IpLoopbackInterfaceIndex_Object = MibTableColumn
ipLoopbackInterfaceIndex = _IpLoopbackInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 1),
    _IpLoopbackInterfaceIndex_Type()
)
ipLoopbackInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceIndex.setStatus("current")


class _IpLoopbackInterfaceName_Type(DisplayString):
    """Custom type ipLoopbackInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpLoopbackInterfaceName_Type.__name__ = "DisplayString"
_IpLoopbackInterfaceName_Object = MibTableColumn
ipLoopbackInterfaceName = _IpLoopbackInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 2),
    _IpLoopbackInterfaceName_Type()
)
ipLoopbackInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceName.setStatus("current")
_IpLoopbackInterfaceIpAddress_Type = IpAddress
_IpLoopbackInterfaceIpAddress_Object = MibTableColumn
ipLoopbackInterfaceIpAddress = _IpLoopbackInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 3),
    _IpLoopbackInterfaceIpAddress_Type()
)
ipLoopbackInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceIpAddress.setStatus("current")
_IpLoopbackInterfaceMask_Type = IpAddress
_IpLoopbackInterfaceMask_Object = MibTableColumn
ipLoopbackInterfaceMask = _IpLoopbackInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 4),
    _IpLoopbackInterfaceMask_Type()
)
ipLoopbackInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceMask.setStatus("current")
_IpLoopbackInterfaceStorageType_Type = StorageType
_IpLoopbackInterfaceStorageType_Object = MibTableColumn
ipLoopbackInterfaceStorageType = _IpLoopbackInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 5),
    _IpLoopbackInterfaceStorageType_Type()
)
ipLoopbackInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceStorageType.setStatus("current")
_IpLoopbackInterfaceRowStatus_Type = RowStatus
_IpLoopbackInterfaceRowStatus_Object = MibTableColumn
ipLoopbackInterfaceRowStatus = _IpLoopbackInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 6),
    _IpLoopbackInterfaceRowStatus_Type()
)
ipLoopbackInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceRowStatus.setStatus("current")
_IpLoopbackInterfaceIpMode_Type = IpMode
_IpLoopbackInterfaceIpMode_Object = MibTableColumn
ipLoopbackInterfaceIpMode = _IpLoopbackInterfaceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 7),
    _IpLoopbackInterfaceIpMode_Type()
)
ipLoopbackInterfaceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceIpMode.setStatus("current")
_IpLoopbackInterfaceIpv6Address_Type = Ipv6Address
_IpLoopbackInterfaceIpv6Address_Object = MibTableColumn
ipLoopbackInterfaceIpv6Address = _IpLoopbackInterfaceIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 8),
    _IpLoopbackInterfaceIpv6Address_Type()
)
ipLoopbackInterfaceIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceIpv6Address.setStatus("current")
_IpLoopbackInterfaceIpv6AddrPrefixLen_Type = Integer32
_IpLoopbackInterfaceIpv6AddrPrefixLen_Object = MibTableColumn
ipLoopbackInterfaceIpv6AddrPrefixLen = _IpLoopbackInterfaceIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 1, 11, 1, 9),
    _IpLoopbackInterfaceIpv6AddrPrefixLen_Type()
)
ipLoopbackInterfaceIpv6AddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipLoopbackInterfaceIpv6AddrPrefixLen.setStatus("current")
_CmIpConformance_ObjectIdentity = ObjectIdentity
cmIpConformance = _CmIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 2)
)
_IpCompliances_ObjectIdentity = ObjectIdentity
ipCompliances = _IpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 2, 1)
)
_IpGroups_ObjectIdentity = ObjectIdentity
ipGroups = _IpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 2, 2)
)
_CmIpScalars_ObjectIdentity = ObjectIdentity
cmIpScalars = _CmIpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3)
)
_CmIpSystemScalars_ObjectIdentity = ObjectIdentity
cmIpSystemScalars = _CmIpSystemScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1)
)
_CmIpFlushARPCacheAction_Type = IpActionType
_CmIpFlushARPCacheAction_Object = MibScalar
cmIpFlushARPCacheAction = _CmIpFlushARPCacheAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 1),
    _CmIpFlushARPCacheAction_Type()
)
cmIpFlushARPCacheAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpFlushARPCacheAction.setStatus("current")
_CmIpProxyARPEnabled_Type = TruthValue
_CmIpProxyARPEnabled_Object = MibScalar
cmIpProxyARPEnabled = _CmIpProxyARPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 2),
    _CmIpProxyARPEnabled_Type()
)
cmIpProxyARPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpProxyARPEnabled.setStatus("current")
_CmIpPingDestination_Type = IpAddress
_CmIpPingDestination_Object = MibScalar
cmIpPingDestination = _CmIpPingDestination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 3),
    _CmIpPingDestination_Type()
)
cmIpPingDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpPingDestination.setStatus("current")
_CmIpInitiatePingAction_Type = IpActionType
_CmIpInitiatePingAction_Object = MibScalar
cmIpInitiatePingAction = _CmIpInitiatePingAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 4),
    _CmIpInitiatePingAction_Type()
)
cmIpInitiatePingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInitiatePingAction.setStatus("current")


class _CmIpPingResult_Type(DisplayString):
    """Custom type cmIpPingResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CmIpPingResult_Type.__name__ = "DisplayString"
_CmIpPingResult_Object = MibScalar
cmIpPingResult = _CmIpPingResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 5),
    _CmIpPingResult_Type()
)
cmIpPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIpPingResult.setStatus("current")
_CmIpTraceRouteDestination_Type = IpAddress
_CmIpTraceRouteDestination_Object = MibScalar
cmIpTraceRouteDestination = _CmIpTraceRouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 6),
    _CmIpTraceRouteDestination_Type()
)
cmIpTraceRouteDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpTraceRouteDestination.setStatus("current")
_CmIpInitiateTraceRouteAction_Type = IpActionType
_CmIpInitiateTraceRouteAction_Object = MibScalar
cmIpInitiateTraceRouteAction = _CmIpInitiateTraceRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 7),
    _CmIpInitiateTraceRouteAction_Type()
)
cmIpInitiateTraceRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpInitiateTraceRouteAction.setStatus("current")


class _CmIpTraceRouteResult_Type(DisplayString):
    """Custom type cmIpTraceRouteResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CmIpTraceRouteResult_Type.__name__ = "DisplayString"
_CmIpTraceRouteResult_Object = MibScalar
cmIpTraceRouteResult = _CmIpTraceRouteResult_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 8),
    _CmIpTraceRouteResult_Type()
)
cmIpTraceRouteResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIpTraceRouteResult.setStatus("current")
_CmIpManagementTrafficBridgingEnabled_Type = TruthValue
_CmIpManagementTrafficBridgingEnabled_Object = MibScalar
cmIpManagementTrafficBridgingEnabled = _CmIpManagementTrafficBridgingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 9),
    _CmIpManagementTrafficBridgingEnabled_Type()
)
cmIpManagementTrafficBridgingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpManagementTrafficBridgingEnabled.setStatus("current")
_CmIpManagementTrafficBridgingSecurityEnabled_Type = TruthValue
_CmIpManagementTrafficBridgingSecurityEnabled_Object = MibScalar
cmIpManagementTrafficBridgingSecurityEnabled = _CmIpManagementTrafficBridgingSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 10),
    _CmIpManagementTrafficBridgingSecurityEnabled_Type()
)
cmIpManagementTrafficBridgingSecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpManagementTrafficBridgingSecurityEnabled.setStatus("current")
_CmIpv6PingInterface_Type = DisplayString
_CmIpv6PingInterface_Object = MibScalar
cmIpv6PingInterface = _CmIpv6PingInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 11),
    _CmIpv6PingInterface_Type()
)
cmIpv6PingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6PingInterface.setStatus("current")
_CmIpv6PingDestination_Type = Ipv6Address
_CmIpv6PingDestination_Object = MibScalar
cmIpv6PingDestination = _CmIpv6PingDestination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 12),
    _CmIpv6PingDestination_Type()
)
cmIpv6PingDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6PingDestination.setStatus("current")
_CmIpv6InitiatePingAction_Type = IpActionType
_CmIpv6InitiatePingAction_Object = MibScalar
cmIpv6InitiatePingAction = _CmIpv6InitiatePingAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 13),
    _CmIpv6InitiatePingAction_Type()
)
cmIpv6InitiatePingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6InitiatePingAction.setStatus("current")
_CmIpv6TraceRouteDestination_Type = Ipv6Address
_CmIpv6TraceRouteDestination_Object = MibScalar
cmIpv6TraceRouteDestination = _CmIpv6TraceRouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 14),
    _CmIpv6TraceRouteDestination_Type()
)
cmIpv6TraceRouteDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6TraceRouteDestination.setStatus("current")
_CmIpv6InitiateTraceRouteAction_Type = IpActionType
_CmIpv6InitiateTraceRouteAction_Object = MibScalar
cmIpv6InitiateTraceRouteAction = _CmIpv6InitiateTraceRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 15),
    _CmIpv6InitiateTraceRouteAction_Type()
)
cmIpv6InitiateTraceRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6InitiateTraceRouteAction.setStatus("current")
_CmIpv6ProxyNDPEnabled_Type = TruthValue
_CmIpv6ProxyNDPEnabled_Object = MibScalar
cmIpv6ProxyNDPEnabled = _CmIpv6ProxyNDPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 16),
    _CmIpv6ProxyNDPEnabled_Type()
)
cmIpv6ProxyNDPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6ProxyNDPEnabled.setStatus("current")
_CmIpv6FwdEnabled_Type = TruthValue
_CmIpv6FwdEnabled_Object = MibScalar
cmIpv6FwdEnabled = _CmIpv6FwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 17),
    _CmIpv6FwdEnabled_Type()
)
cmIpv6FwdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6FwdEnabled.setStatus("current")
_CmIpFlushNDPCacheAction_Type = IpActionType
_CmIpFlushNDPCacheAction_Object = MibScalar
cmIpFlushNDPCacheAction = _CmIpFlushNDPCacheAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 18),
    _CmIpFlushNDPCacheAction_Type()
)
cmIpFlushNDPCacheAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpFlushNDPCacheAction.setStatus("current")
_CmIpPtpArpRtrvAction_Type = PtpArpActionType
_CmIpPtpArpRtrvAction_Object = MibScalar
cmIpPtpArpRtrvAction = _CmIpPtpArpRtrvAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 19),
    _CmIpPtpArpRtrvAction_Type()
)
cmIpPtpArpRtrvAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpPtpArpRtrvAction.setStatus("current")
_CmIpManagementTrafficDscpEnabled_Type = TruthValue
_CmIpManagementTrafficDscpEnabled_Object = MibScalar
cmIpManagementTrafficDscpEnabled = _CmIpManagementTrafficDscpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 20),
    _CmIpManagementTrafficDscpEnabled_Type()
)
cmIpManagementTrafficDscpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpManagementTrafficDscpEnabled.setStatus("current")


class _CmIpManagementTrafficDscp_Type(Unsigned32):
    """Custom type cmIpManagementTrafficDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CmIpManagementTrafficDscp_Type.__name__ = "Unsigned32"
_CmIpManagementTrafficDscp_Object = MibScalar
cmIpManagementTrafficDscp = _CmIpManagementTrafficDscp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 21),
    _CmIpManagementTrafficDscp_Type()
)
cmIpManagementTrafficDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpManagementTrafficDscp.setStatus("current")


class _CmIpManagementTrafficBridgingInterface_Type(DisplayString):
    """Custom type cmIpManagementTrafficBridgingInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CmIpManagementTrafficBridgingInterface_Type.__name__ = "DisplayString"
_CmIpManagementTrafficBridgingInterface_Object = MibScalar
cmIpManagementTrafficBridgingInterface = _CmIpManagementTrafficBridgingInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 22),
    _CmIpManagementTrafficBridgingInterface_Type()
)
cmIpManagementTrafficBridgingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpManagementTrafficBridgingInterface.setStatus("current")
_CmIpManagementTrafficBridgingIpv4Gateway_Type = IpAddress
_CmIpManagementTrafficBridgingIpv4Gateway_Object = MibScalar
cmIpManagementTrafficBridgingIpv4Gateway = _CmIpManagementTrafficBridgingIpv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 23),
    _CmIpManagementTrafficBridgingIpv4Gateway_Type()
)
cmIpManagementTrafficBridgingIpv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpManagementTrafficBridgingIpv4Gateway.setStatus("current")
_CmIpManagementTrafficBridgingIpv6Gateway_Type = Ipv6Address
_CmIpManagementTrafficBridgingIpv6Gateway_Object = MibScalar
cmIpManagementTrafficBridgingIpv6Gateway = _CmIpManagementTrafficBridgingIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 24),
    _CmIpManagementTrafficBridgingIpv6Gateway_Type()
)
cmIpManagementTrafficBridgingIpv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpManagementTrafficBridgingIpv6Gateway.setStatus("current")
_CmPingInterface_Type = DisplayString
_CmPingInterface_Object = MibScalar
cmPingInterface = _CmPingInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 25),
    _CmPingInterface_Type()
)
cmPingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPingInterface.setStatus("current")
_CmIpTraceRouteInterface_Type = DisplayString
_CmIpTraceRouteInterface_Object = MibScalar
cmIpTraceRouteInterface = _CmIpTraceRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 26),
    _CmIpTraceRouteInterface_Type()
)
cmIpTraceRouteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpTraceRouteInterface.setStatus("current")
_CmIpv6TraceRouteInterface_Type = DisplayString
_CmIpv6TraceRouteInterface_Object = MibScalar
cmIpv6TraceRouteInterface = _CmIpv6TraceRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 1, 27),
    _CmIpv6TraceRouteInterface_Type()
)
cmIpv6TraceRouteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpv6TraceRouteInterface.setStatus("current")
_CmIpSourceAddrScalars_ObjectIdentity = ObjectIdentity
cmIpSourceAddrScalars = _CmIpSourceAddrScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 2)
)


class _CmIpSNMPv1InterfaceName_Type(DisplayString):
    """Custom type cmIpSNMPv1InterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CmIpSNMPv1InterfaceName_Type.__name__ = "DisplayString"
_CmIpSNMPv1InterfaceName_Object = MibScalar
cmIpSNMPv1InterfaceName = _CmIpSNMPv1InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 2, 1),
    _CmIpSNMPv1InterfaceName_Type()
)
cmIpSNMPv1InterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpSNMPv1InterfaceName.setStatus("current")
_CmIpSourceAddressType_Type = IpSourceAddrType
_CmIpSourceAddressType_Object = MibScalar
cmIpSourceAddressType = _CmIpSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 2, 2),
    _CmIpSourceAddressType_Type()
)
cmIpSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpSourceAddressType.setStatus("current")


class _CmIpSourceAddressInterfaceName_Type(DisplayString):
    """Custom type cmIpSourceAddressInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CmIpSourceAddressInterfaceName_Type.__name__ = "DisplayString"
_CmIpSourceAddressInterfaceName_Object = MibScalar
cmIpSourceAddressInterfaceName = _CmIpSourceAddressInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 3, 2, 3),
    _CmIpSourceAddressInterfaceName_Type()
)
cmIpSourceAddressInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIpSourceAddressInterfaceName.setStatus("current")
cmIpInterfaceEntry.registerAugmentions(
    ("CM-IP-MIB",
     "cmIpv6InterfaceEntry")
)
cmIpv6InterfaceEntry.setIndexNames(*cmIpInterfaceEntry.getIndexNames())

# Managed Objects groups

ipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 2, 2, 1)
)
ipGroup.setObjects(
      *(("CM-IP-MIB", "cmIpFlushARPCacheAction"),
        ("CM-IP-MIB", "cmIpProxyARPEnabled"),
        ("CM-IP-MIB", "cmIpPingDestination"),
        ("CM-IP-MIB", "cmIpInitiatePingAction"),
        ("CM-IP-MIB", "cmIpPingResult"),
        ("CM-IP-MIB", "cmPingInterface"),
        ("CM-IP-MIB", "cmIpTraceRouteDestination"),
        ("CM-IP-MIB", "cmIpInitiateTraceRouteAction"),
        ("CM-IP-MIB", "cmIpTraceRouteResult"),
        ("CM-IP-MIB", "cmIpTraceRouteInterface"),
        ("CM-IP-MIB", "cmIpSNMPv1InterfaceName"),
        ("CM-IP-MIB", "cmIpSourceAddressType"),
        ("CM-IP-MIB", "cmIpSourceAddressInterfaceName"),
        ("CM-IP-MIB", "cmIpManagementTrafficBridgingEnabled"),
        ("CM-IP-MIB", "cmIpManagementTrafficBridgingSecurityEnabled"),
        ("CM-IP-MIB", "cmIpInterfaceName"),
        ("CM-IP-MIB", "cmIpInterface"),
        ("CM-IP-MIB", "cmIpInterfaceMask"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpEnabled"),
        ("CM-IP-MIB", "cmIpInterfaceMTU"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpRole"),
        ("CM-IP-MIB", "cmIpInterfacePhysicalAddress"),
        ("CM-IP-MIB", "cmIpInterfaceRIPv2Enabled"),
        ("CM-IP-MIB", "cmIpInterfaceDHCPClientIdEnabled"),
        ("CM-IP-MIB", "cmIpInterfaceDHCPClientId"),
        ("CM-IP-MIB", "cmIpInterfaceIpMode"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpClassIdEnabled"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpHostNameEnabled"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpHostName"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpLogServerEnabled"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpNTPServerEnabled"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpClientIdType"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpHostNameType"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpVendorInfoEnabled"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpVendorInfoType"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpVendorInfo"),
        ("CM-IP-MIB", "cmIpInterfaceDhcpVendorInfoHideControl"),
        ("CM-IP-MIB", "cmIpInterfaceGateway"),
        ("CM-IP-MIB", "cmStaticRouteDest"),
        ("CM-IP-MIB", "cmStaticRouteMask"),
        ("CM-IP-MIB", "cmStaticRouteNextHop"),
        ("CM-IP-MIB", "cmStaticRouteMetric"),
        ("CM-IP-MIB", "cmStaticRouteRowStatus"),
        ("CM-IP-MIB", "cmStaticRouteInterface"),
        ("CM-IP-MIB", "cmStaticRouteAdvertise"),
        ("CM-IP-MIB", "cmARPIndex"),
        ("CM-IP-MIB", "cmARPIPAddress"),
        ("CM-IP-MIB", "cmARPMacAddress"),
        ("CM-IP-MIB", "cmARPInterface"),
        ("CM-IP-MIB", "cmARPStorageType"),
        ("CM-IP-MIB", "cmARPRowStatus"),
        ("CM-IP-MIB", "cmARPEntryType"),
        ("CM-IP-MIB", "cmProxyARPIndex"),
        ("CM-IP-MIB", "cmProxyARPIPAddress"),
        ("CM-IP-MIB", "cmProxyARPSubnetMask"),
        ("CM-IP-MIB", "cmProxyARPInterface"),
        ("CM-IP-MIB", "cmProxyARPStorageType"),
        ("CM-IP-MIB", "cmProxyARPRowStatus"),
        ("CM-IP-MIB", "ipManagementTunnelIndex"),
        ("CM-IP-MIB", "ipManagementTunnelAssociatedPort"),
        ("CM-IP-MIB", "ipManagementTunnelName"),
        ("CM-IP-MIB", "ipManagementTunnelType"),
        ("CM-IP-MIB", "ipManagementTunnelMTU"),
        ("CM-IP-MIB", "ipManagementTunnelEncapsulationType"),
        ("CM-IP-MIB", "ipManagementTunnelIpAddress"),
        ("CM-IP-MIB", "ipManagementTunnelSubnetMask"),
        ("CM-IP-MIB", "ipManagementTunnelVlanId"),
        ("CM-IP-MIB", "ipManagementTunnelSVlanEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelSVlanId"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelRip2PktsEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelPhysicalAddress"),
        ("CM-IP-MIB", "ipManagementTunnelCOS"),
        ("CM-IP-MIB", "ipManagementTunnelCIR"),
        ("CM-IP-MIB", "ipManagementTunnelEIR"),
        ("CM-IP-MIB", "ipManagementTunnelBufferSize"),
        ("CM-IP-MIB", "ipManagementTunnelStorageType"),
        ("CM-IP-MIB", "ipManagementTunnelRowStatus"),
        ("CM-IP-MIB", "ipManagementTunnelQosQueueProfile"),
        ("CM-IP-MIB", "ipManagementTunnelDHCPClientIdEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelDHCPClientId"),
        ("CM-IP-MIB", "ipManagementTunnelCVlanEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelIpMode"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpClassIdEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpHostNameEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpHostName"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpLogServerEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpNTPServerEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpClientIdType"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpHostNameType"),
        ("CM-IP-MIB", "cmIpManagementTrafficDscpEnabled"),
        ("CM-IP-MIB", "cmIpManagementTrafficDscp"),
        ("CM-IP-MIB", "cmIpManagementTrafficBridgingInterface"),
        ("CM-IP-MIB", "cmIpManagementTrafficBridgingIpv4Gateway"),
        ("CM-IP-MIB", "cmIpManagementTrafficBridgingIpv6Gateway"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpVendorInfoEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpVendorInfoType"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpVendorInfo"),
        ("CM-IP-MIB", "ipManagementTunnelDhcpVendorInfoHideControl"),
        ("CM-IP-MIB", "ipManagementTunnelSharedVim"))
)
if mibBuilder.loadTexts:
    ipGroup.setStatus("current")

ipv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 2, 2, 2)
)
ipv6Group.setObjects(
      *(("CM-IP-MIB", "ipManagementTunnelDHCPv6Enabled"),
        ("CM-IP-MIB", "ipManagementTunnelIpv6Address"),
        ("CM-IP-MIB", "ipManagementTunnelIpv6AddrPrefixLen"),
        ("CM-IP-MIB", "ipManagementTunnelIpv6StateAddrAutoConfigEnabled"),
        ("CM-IP-MIB", "ipManagementTunnellinkLocIpv6Addr"),
        ("CM-IP-MIB", "ipManagementTunnellinkLocIpv6AddrPrefixLen"),
        ("CM-IP-MIB", "ipManagementTunnelIpv6PrefixAdvertiseEnabled"),
        ("CM-IP-MIB", "ipManagementTunnelIpv6Prefix"),
        ("CM-IP-MIB", "ipManagementTunnelIpv6PrefixLen"),
        ("CM-IP-MIB", "ipManagementTunnelIpv6RipngEnabled"),
        ("CM-IP-MIB", "cmIpv6InterfaceMTU"),
        ("CM-IP-MIB", "cmIpv6UnicastAddr"),
        ("CM-IP-MIB", "cmIpv6UnicastAddrPrefixLen"),
        ("CM-IP-MIB", "cmIpv6PrefixAdvertiseEnabled"),
        ("CM-IP-MIB", "cmIpv6RAPrefix"),
        ("CM-IP-MIB", "cmIpv6RAPrefixLength"),
        ("CM-IP-MIB", "cmIpv6StateAddrAutoConfigEnabled"),
        ("CM-IP-MIB", "cmIpv6DhcpEnabled"),
        ("CM-IP-MIB", "cmIpv6DhcpRole"),
        ("CM-IP-MIB", "cmIpv6RIPngEnabled"),
        ("CM-IP-MIB", "cmIpv6LinkLocAddr"),
        ("CM-IP-MIB", "cmIpv6LinkLocAddrPrefixLen"),
        ("CM-IP-MIB", "cmIpv6InterfaceGateway"),
        ("CM-IP-MIB", "cmIpv6StaticRouteDest"),
        ("CM-IP-MIB", "cmIpv6StaticRoutePrefixLen"),
        ("CM-IP-MIB", "cmIpv6StaticRouteNextHop"),
        ("CM-IP-MIB", "cmIpv6StaticRouteMetric"),
        ("CM-IP-MIB", "cmIpv6StaticRouteRowStatus"),
        ("CM-IP-MIB", "cmIpv6StaticRouteInterface"),
        ("CM-IP-MIB", "cmIpv6StaticRouteAdvertise"),
        ("CM-IP-MIB", "cmNDPIpv6Address"),
        ("CM-IP-MIB", "cmNDPMacAddress"),
        ("CM-IP-MIB", "cmNDPInterface"),
        ("CM-IP-MIB", "cmNDPStorageType"),
        ("CM-IP-MIB", "cmNDPRowStatus"),
        ("CM-IP-MIB", "cmNDPEntryType"),
        ("CM-IP-MIB", "cmProxyNDPIpv6Address"),
        ("CM-IP-MIB", "cmProxyNDPIpv6PrefixLen"),
        ("CM-IP-MIB", "cmProxyNDPInterface"),
        ("CM-IP-MIB", "cmProxyNDPStorageType"),
        ("CM-IP-MIB", "cmProxyNDPRowStatus"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelIndex"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelName"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelType"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelDestIpv4Addr"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelIpv6UnicastAddress"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelAssociatedIpv4Interface"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelStorageType"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelRowStatus"),
        ("CM-IP-MIB", "cmIpv6InitiatePingAction"),
        ("CM-IP-MIB", "cmIpv6InitiatePingAction"),
        ("CM-IP-MIB", "cmIpv6TraceRouteDestination"),
        ("CM-IP-MIB", "cmIpv6InitiateTraceRouteAction"),
        ("CM-IP-MIB", "cmIpv6PingInterface"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen"),
        ("CM-IP-MIB", "cmIpv6OverIpv4TunnelLinkLocalAddress"),
        ("CM-IP-MIB", "cmIpv60verIpv4TunnelLinkLocalAddrPrefixLen"),
        ("CM-IP-MIB", "cmIpv6OverIpv4PotentialRouterList"),
        ("CM-IP-MIB", "cmIpv6FwdEnabled"),
        ("CM-IP-MIB", "cmIpv6ProxyNDPEnabled"),
        ("CM-IP-MIB", "cmIpFlushNDPCacheAction"),
        ("CM-IP-MIB", "cmIpPtpArpRtrvAction"),
        ("CM-IP-MIB", "ipLoopbackInterfaceIndex"),
        ("CM-IP-MIB", "ipLoopbackInterfaceName"),
        ("CM-IP-MIB", "ipLoopbackInterfaceIpAddress"),
        ("CM-IP-MIB", "ipLoopbackInterfaceMask"),
        ("CM-IP-MIB", "ipLoopbackInterfaceStorageType"),
        ("CM-IP-MIB", "ipLoopbackInterfaceRowStatus"),
        ("CM-IP-MIB", "ipLoopbackInterfaceIpMode"),
        ("CM-IP-MIB", "ipLoopbackInterfaceIpv6Address"),
        ("CM-IP-MIB", "ipLoopbackInterfaceIpv6AddrPrefixLen"))
)
if mibBuilder.loadTexts:
    ipv6Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 11, 2, 1, 1)
)
ipCompliance.setObjects(
    ("CM-IP-MIB", "ipGroup")
)
if mibBuilder.loadTexts:
    ipCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-IP-MIB",
    **{"CmDhcpRole": CmDhcpRole,
       "IpManagementTunnelType": IpManagementTunnelType,
       "IpManagementTunnelEncapsulationType": IpManagementTunnelEncapsulationType,
       "IpEntryType": IpEntryType,
       "IpSourceAddrType": IpSourceAddrType,
       "IpActionType": IpActionType,
       "Ipv6OverIpv4TunnelType": Ipv6OverIpv4TunnelType,
       "IpMode": IpMode,
       "DHCPCIDType": DHCPCIDType,
       "DHCPHostNameType": DHCPHostNameType,
       "PtpArpActionType": PtpArpActionType,
       "DHCPVendorInfoType": DHCPVendorInfoType,
       "cmIPMIB": cmIPMIB,
       "cmIpObjects": cmIpObjects,
       "cmIpInterfaceTable": cmIpInterfaceTable,
       "cmIpInterfaceEntry": cmIpInterfaceEntry,
       "cmIpInterfaceName": cmIpInterfaceName,
       "cmIpInterface": cmIpInterface,
       "cmIpInterfaceMask": cmIpInterfaceMask,
       "cmIpInterfaceDhcpEnabled": cmIpInterfaceDhcpEnabled,
       "cmIpInterfaceMTU": cmIpInterfaceMTU,
       "cmIpInterfaceDhcpRole": cmIpInterfaceDhcpRole,
       "cmIpInterfacePhysicalAddress": cmIpInterfacePhysicalAddress,
       "cmIpInterfaceRIPv2Enabled": cmIpInterfaceRIPv2Enabled,
       "cmIpInterfaceDHCPClientIdEnabled": cmIpInterfaceDHCPClientIdEnabled,
       "cmIpInterfaceDHCPClientId": cmIpInterfaceDHCPClientId,
       "cmIpInterfaceIpMode": cmIpInterfaceIpMode,
       "cmIpInterfaceDhcpClassIdEnabled": cmIpInterfaceDhcpClassIdEnabled,
       "cmIpInterfaceDhcpHostNameEnabled": cmIpInterfaceDhcpHostNameEnabled,
       "cmIpInterfaceDhcpHostName": cmIpInterfaceDhcpHostName,
       "cmIpInterfaceDhcpLogServerEnabled": cmIpInterfaceDhcpLogServerEnabled,
       "cmIpInterfaceDhcpNTPServerEnabled": cmIpInterfaceDhcpNTPServerEnabled,
       "cmIpInterfaceDhcpClientIdType": cmIpInterfaceDhcpClientIdType,
       "cmIpInterfaceDhcpHostNameType": cmIpInterfaceDhcpHostNameType,
       "cmIpInterfaceDhcpVendorInfoEnabled": cmIpInterfaceDhcpVendorInfoEnabled,
       "cmIpInterfaceDhcpVendorInfoType": cmIpInterfaceDhcpVendorInfoType,
       "cmIpInterfaceDhcpVendorInfo": cmIpInterfaceDhcpVendorInfo,
       "cmIpInterfaceDhcpVendorInfoHideControl": cmIpInterfaceDhcpVendorInfoHideControl,
       "cmIpInterfaceGateway": cmIpInterfaceGateway,
       "cmStaticRouteTable": cmStaticRouteTable,
       "cmStaticRouteEntry": cmStaticRouteEntry,
       "cmStaticRouteDest": cmStaticRouteDest,
       "cmStaticRouteMask": cmStaticRouteMask,
       "cmStaticRouteNextHop": cmStaticRouteNextHop,
       "cmStaticRouteMetric": cmStaticRouteMetric,
       "cmStaticRouteRowStatus": cmStaticRouteRowStatus,
       "cmStaticRouteInterface": cmStaticRouteInterface,
       "cmStaticRouteAdvertise": cmStaticRouteAdvertise,
       "cmARPTable": cmARPTable,
       "cmARPEntry": cmARPEntry,
       "cmARPIndex": cmARPIndex,
       "cmARPIPAddress": cmARPIPAddress,
       "cmARPMacAddress": cmARPMacAddress,
       "cmARPInterface": cmARPInterface,
       "cmARPStorageType": cmARPStorageType,
       "cmARPRowStatus": cmARPRowStatus,
       "cmARPEntryType": cmARPEntryType,
       "cmProxyARPTable": cmProxyARPTable,
       "cmProxyARPEntry": cmProxyARPEntry,
       "cmProxyARPIndex": cmProxyARPIndex,
       "cmProxyARPIPAddress": cmProxyARPIPAddress,
       "cmProxyARPSubnetMask": cmProxyARPSubnetMask,
       "cmProxyARPInterface": cmProxyARPInterface,
       "cmProxyARPStorageType": cmProxyARPStorageType,
       "cmProxyARPRowStatus": cmProxyARPRowStatus,
       "ipManagementTunnelTable": ipManagementTunnelTable,
       "ipManagementTunnelEntry": ipManagementTunnelEntry,
       "ipManagementTunnelIndex": ipManagementTunnelIndex,
       "ipManagementTunnelAssociatedPort": ipManagementTunnelAssociatedPort,
       "ipManagementTunnelName": ipManagementTunnelName,
       "ipManagementTunnelType": ipManagementTunnelType,
       "ipManagementTunnelMTU": ipManagementTunnelMTU,
       "ipManagementTunnelEncapsulationType": ipManagementTunnelEncapsulationType,
       "ipManagementTunnelIpAddress": ipManagementTunnelIpAddress,
       "ipManagementTunnelSubnetMask": ipManagementTunnelSubnetMask,
       "ipManagementTunnelVlanId": ipManagementTunnelVlanId,
       "ipManagementTunnelSVlanEnabled": ipManagementTunnelSVlanEnabled,
       "ipManagementTunnelSVlanId": ipManagementTunnelSVlanId,
       "ipManagementTunnelDhcpEnabled": ipManagementTunnelDhcpEnabled,
       "ipManagementTunnelRip2PktsEnabled": ipManagementTunnelRip2PktsEnabled,
       "ipManagementTunnelPhysicalAddress": ipManagementTunnelPhysicalAddress,
       "ipManagementTunnelCOS": ipManagementTunnelCOS,
       "ipManagementTunnelCIR": ipManagementTunnelCIR,
       "ipManagementTunnelEIR": ipManagementTunnelEIR,
       "ipManagementTunnelBufferSize": ipManagementTunnelBufferSize,
       "ipManagementTunnelStorageType": ipManagementTunnelStorageType,
       "ipManagementTunnelRowStatus": ipManagementTunnelRowStatus,
       "ipManagementTunnelDHCPClientIdEnabled": ipManagementTunnelDHCPClientIdEnabled,
       "ipManagementTunnelDHCPClientId": ipManagementTunnelDHCPClientId,
       "ipManagementTunnelQosQueueProfile": ipManagementTunnelQosQueueProfile,
       "ipManagementTunnelCVlanEnabled": ipManagementTunnelCVlanEnabled,
       "ipManagementTunnelDHCPv6Enabled": ipManagementTunnelDHCPv6Enabled,
       "ipManagementTunnelIpv6Address": ipManagementTunnelIpv6Address,
       "ipManagementTunnelIpv6AddrPrefixLen": ipManagementTunnelIpv6AddrPrefixLen,
       "ipManagementTunnelIpv6StateAddrAutoConfigEnabled": ipManagementTunnelIpv6StateAddrAutoConfigEnabled,
       "ipManagementTunnellinkLocIpv6Addr": ipManagementTunnellinkLocIpv6Addr,
       "ipManagementTunnellinkLocIpv6AddrPrefixLen": ipManagementTunnellinkLocIpv6AddrPrefixLen,
       "ipManagementTunnelIpv6PrefixAdvertiseEnabled": ipManagementTunnelIpv6PrefixAdvertiseEnabled,
       "ipManagementTunnelIpv6Prefix": ipManagementTunnelIpv6Prefix,
       "ipManagementTunnelIpv6PrefixLen": ipManagementTunnelIpv6PrefixLen,
       "ipManagementTunnelIpMode": ipManagementTunnelIpMode,
       "ipManagementTunnelIpv6RipngEnabled": ipManagementTunnelIpv6RipngEnabled,
       "ipManagementTunnelDhcpClassIdEnabled": ipManagementTunnelDhcpClassIdEnabled,
       "ipManagementTunnelDhcpHostNameEnabled": ipManagementTunnelDhcpHostNameEnabled,
       "ipManagementTunnelDhcpHostName": ipManagementTunnelDhcpHostName,
       "ipManagementTunnelDhcpLogServerEnabled": ipManagementTunnelDhcpLogServerEnabled,
       "ipManagementTunnelDhcpNTPServerEnabled": ipManagementTunnelDhcpNTPServerEnabled,
       "ipManagementTunnelDhcpClientIdType": ipManagementTunnelDhcpClientIdType,
       "ipManagementTunnelDhcpHostNameType": ipManagementTunnelDhcpHostNameType,
       "ipManagementTunnelDhcpVendorInfoEnabled": ipManagementTunnelDhcpVendorInfoEnabled,
       "ipManagementTunnelDhcpVendorInfoType": ipManagementTunnelDhcpVendorInfoType,
       "ipManagementTunnelDhcpVendorInfo": ipManagementTunnelDhcpVendorInfo,
       "ipManagementTunnelDhcpVendorInfoHideControl": ipManagementTunnelDhcpVendorInfoHideControl,
       "ipManagementTunnelSharedVim": ipManagementTunnelSharedVim,
       "cmIpv6InterfaceTable": cmIpv6InterfaceTable,
       "cmIpv6InterfaceEntry": cmIpv6InterfaceEntry,
       "cmIpv6InterfaceMTU": cmIpv6InterfaceMTU,
       "cmIpv6UnicastAddr": cmIpv6UnicastAddr,
       "cmIpv6UnicastAddrPrefixLen": cmIpv6UnicastAddrPrefixLen,
       "cmIpv6PrefixAdvertiseEnabled": cmIpv6PrefixAdvertiseEnabled,
       "cmIpv6RAPrefix": cmIpv6RAPrefix,
       "cmIpv6RAPrefixLength": cmIpv6RAPrefixLength,
       "cmIpv6StateAddrAutoConfigEnabled": cmIpv6StateAddrAutoConfigEnabled,
       "cmIpv6DhcpEnabled": cmIpv6DhcpEnabled,
       "cmIpv6DhcpRole": cmIpv6DhcpRole,
       "cmIpv6RIPngEnabled": cmIpv6RIPngEnabled,
       "cmIpv6LinkLocAddr": cmIpv6LinkLocAddr,
       "cmIpv6LinkLocAddrPrefixLen": cmIpv6LinkLocAddrPrefixLen,
       "cmIpv6InterfaceGateway": cmIpv6InterfaceGateway,
       "cmIpv6StaticRouteTable": cmIpv6StaticRouteTable,
       "cmIpv6StaticRouteEntry": cmIpv6StaticRouteEntry,
       "cmIpv6StaticRouteDest": cmIpv6StaticRouteDest,
       "cmIpv6StaticRoutePrefixLen": cmIpv6StaticRoutePrefixLen,
       "cmIpv6StaticRouteNextHop": cmIpv6StaticRouteNextHop,
       "cmIpv6StaticRouteMetric": cmIpv6StaticRouteMetric,
       "cmIpv6StaticRouteRowStatus": cmIpv6StaticRouteRowStatus,
       "cmIpv6StaticRouteInterface": cmIpv6StaticRouteInterface,
       "cmIpv6StaticRouteAdvertise": cmIpv6StaticRouteAdvertise,
       "cmNDPTable": cmNDPTable,
       "cmNDPEntry": cmNDPEntry,
       "cmNDPIpv6Address": cmNDPIpv6Address,
       "cmNDPMacAddress": cmNDPMacAddress,
       "cmNDPInterface": cmNDPInterface,
       "cmNDPStorageType": cmNDPStorageType,
       "cmNDPRowStatus": cmNDPRowStatus,
       "cmNDPEntryType": cmNDPEntryType,
       "cmProxyNDPTable": cmProxyNDPTable,
       "cmProxyNDPEntry": cmProxyNDPEntry,
       "cmProxyNDPIpv6Address": cmProxyNDPIpv6Address,
       "cmProxyNDPIpv6PrefixLen": cmProxyNDPIpv6PrefixLen,
       "cmProxyNDPInterface": cmProxyNDPInterface,
       "cmProxyNDPStorageType": cmProxyNDPStorageType,
       "cmProxyNDPRowStatus": cmProxyNDPRowStatus,
       "cmIpv6OverIpv4TunnelTable": cmIpv6OverIpv4TunnelTable,
       "cmIpv6OverIpv4TunnelEntry": cmIpv6OverIpv4TunnelEntry,
       "cmIpv6OverIpv4TunnelIndex": cmIpv6OverIpv4TunnelIndex,
       "cmIpv6OverIpv4TunnelName": cmIpv6OverIpv4TunnelName,
       "cmIpv6OverIpv4TunnelType": cmIpv6OverIpv4TunnelType,
       "cmIpv6OverIpv4TunnelDestIpv4Addr": cmIpv6OverIpv4TunnelDestIpv4Addr,
       "cmIpv6OverIpv4TunnelIpv6UnicastAddress": cmIpv6OverIpv4TunnelIpv6UnicastAddress,
       "cmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen": cmIpv6OverIpv4TunnelIpv6UnicastAddrPrefixLen,
       "cmIpv6OverIpv4TunnelLinkLocalAddress": cmIpv6OverIpv4TunnelLinkLocalAddress,
       "cmIpv60verIpv4TunnelLinkLocalAddrPrefixLen": cmIpv60verIpv4TunnelLinkLocalAddrPrefixLen,
       "cmIpv6OverIpv4TunnelAssociatedIpv4Interface": cmIpv6OverIpv4TunnelAssociatedIpv4Interface,
       "cmIpv6OverIpv4TunnelStorageType": cmIpv6OverIpv4TunnelStorageType,
       "cmIpv6OverIpv4TunnelRowStatus": cmIpv6OverIpv4TunnelRowStatus,
       "cmIpv6OverIpv4PotentialRouterList": cmIpv6OverIpv4PotentialRouterList,
       "ipLoopbackInterfaceTable": ipLoopbackInterfaceTable,
       "ipLoopbackInterfaceEntry": ipLoopbackInterfaceEntry,
       "ipLoopbackInterfaceIndex": ipLoopbackInterfaceIndex,
       "ipLoopbackInterfaceName": ipLoopbackInterfaceName,
       "ipLoopbackInterfaceIpAddress": ipLoopbackInterfaceIpAddress,
       "ipLoopbackInterfaceMask": ipLoopbackInterfaceMask,
       "ipLoopbackInterfaceStorageType": ipLoopbackInterfaceStorageType,
       "ipLoopbackInterfaceRowStatus": ipLoopbackInterfaceRowStatus,
       "ipLoopbackInterfaceIpMode": ipLoopbackInterfaceIpMode,
       "ipLoopbackInterfaceIpv6Address": ipLoopbackInterfaceIpv6Address,
       "ipLoopbackInterfaceIpv6AddrPrefixLen": ipLoopbackInterfaceIpv6AddrPrefixLen,
       "cmIpConformance": cmIpConformance,
       "ipCompliances": ipCompliances,
       "ipCompliance": ipCompliance,
       "ipGroups": ipGroups,
       "ipGroup": ipGroup,
       "ipv6Group": ipv6Group,
       "cmIpScalars": cmIpScalars,
       "cmIpSystemScalars": cmIpSystemScalars,
       "cmIpFlushARPCacheAction": cmIpFlushARPCacheAction,
       "cmIpProxyARPEnabled": cmIpProxyARPEnabled,
       "cmIpPingDestination": cmIpPingDestination,
       "cmIpInitiatePingAction": cmIpInitiatePingAction,
       "cmIpPingResult": cmIpPingResult,
       "cmIpTraceRouteDestination": cmIpTraceRouteDestination,
       "cmIpInitiateTraceRouteAction": cmIpInitiateTraceRouteAction,
       "cmIpTraceRouteResult": cmIpTraceRouteResult,
       "cmIpManagementTrafficBridgingEnabled": cmIpManagementTrafficBridgingEnabled,
       "cmIpManagementTrafficBridgingSecurityEnabled": cmIpManagementTrafficBridgingSecurityEnabled,
       "cmIpv6PingInterface": cmIpv6PingInterface,
       "cmIpv6PingDestination": cmIpv6PingDestination,
       "cmIpv6InitiatePingAction": cmIpv6InitiatePingAction,
       "cmIpv6TraceRouteDestination": cmIpv6TraceRouteDestination,
       "cmIpv6InitiateTraceRouteAction": cmIpv6InitiateTraceRouteAction,
       "cmIpv6ProxyNDPEnabled": cmIpv6ProxyNDPEnabled,
       "cmIpv6FwdEnabled": cmIpv6FwdEnabled,
       "cmIpFlushNDPCacheAction": cmIpFlushNDPCacheAction,
       "cmIpPtpArpRtrvAction": cmIpPtpArpRtrvAction,
       "cmIpManagementTrafficDscpEnabled": cmIpManagementTrafficDscpEnabled,
       "cmIpManagementTrafficDscp": cmIpManagementTrafficDscp,
       "cmIpManagementTrafficBridgingInterface": cmIpManagementTrafficBridgingInterface,
       "cmIpManagementTrafficBridgingIpv4Gateway": cmIpManagementTrafficBridgingIpv4Gateway,
       "cmIpManagementTrafficBridgingIpv6Gateway": cmIpManagementTrafficBridgingIpv6Gateway,
       "cmPingInterface": cmPingInterface,
       "cmIpTraceRouteInterface": cmIpTraceRouteInterface,
       "cmIpv6TraceRouteInterface": cmIpv6TraceRouteInterface,
       "cmIpSourceAddrScalars": cmIpSourceAddrScalars,
       "cmIpSNMPv1InterfaceName": cmIpSNMPv1InterfaceName,
       "cmIpSourceAddressType": cmIpSourceAddressType,
       "cmIpSourceAddressInterfaceName": cmIpSourceAddressInterfaceName}
)
