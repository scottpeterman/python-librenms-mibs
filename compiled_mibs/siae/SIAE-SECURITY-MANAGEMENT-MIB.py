# SNMP MIB module (SIAE-SECURITY-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-SECURITY-MANAGEMENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:37 2025
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

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

securityManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82)
)
if mibBuilder.loadTexts:
    securityManagement.setRevisions(
        ("2014-04-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SecurityManagementMibVersion_Type = Integer32
_SecurityManagementMibVersion_Object = MibScalar
securityManagementMibVersion = _SecurityManagementMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 1),
    _SecurityManagementMibVersion_Type()
)
securityManagementMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityManagementMibVersion.setStatus("current")
_ServicesTable_Object = MibTable
servicesTable = _ServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2)
)
if mibBuilder.loadTexts:
    servicesTable.setStatus("current")
_ServiceEntry_Object = MibTableRow
serviceEntry = _ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1)
)
serviceEntry.setIndexNames(
    (0, "SIAE-SECURITY-MANAGEMENT-MIB", "serviceIndex"),
)
if mibBuilder.loadTexts:
    serviceEntry.setStatus("current")
_ServiceIndex_Type = Integer32
_ServiceIndex_Object = MibTableColumn
serviceIndex = _ServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 1),
    _ServiceIndex_Type()
)
serviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceIndex.setStatus("current")


class _ServiceName_Type(DisplayString):
    """Custom type serviceName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServiceName_Type.__name__ = "DisplayString"
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 2),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")


class _ServiceProtocolVersion_Type(DisplayString):
    """Custom type serviceProtocolVersion based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ServiceProtocolVersion_Type.__name__ = "DisplayString"
_ServiceProtocolVersion_Object = MibTableColumn
serviceProtocolVersion = _ServiceProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 3),
    _ServiceProtocolVersion_Type()
)
serviceProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceProtocolVersion.setStatus("current")


class _ServiceAdminStatus_Type(Integer32):
    """Custom type serviceAdminStatus based on Integer32"""
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


_ServiceAdminStatus_Type.__name__ = "Integer32"
_ServiceAdminStatus_Object = MibTableColumn
serviceAdminStatus = _ServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 4),
    _ServiceAdminStatus_Type()
)
serviceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceAdminStatus.setStatus("current")


class _ServiceOperStatus_Type(Integer32):
    """Custom type serviceOperStatus based on Integer32"""
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
        *(("notAvailable", 0),
          ("running", 1),
          ("stopped", 2))
    )


_ServiceOperStatus_Type.__name__ = "Integer32"
_ServiceOperStatus_Object = MibTableColumn
serviceOperStatus = _ServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 5),
    _ServiceOperStatus_Type()
)
serviceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceOperStatus.setStatus("current")
_ServiceRowStatus_Type = RowStatus
_ServiceRowStatus_Object = MibTableColumn
serviceRowStatus = _ServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 6),
    _ServiceRowStatus_Type()
)
serviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    serviceRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-SECURITY-MANAGEMENT-MIB",
    **{"securityManagement": securityManagement,
       "securityManagementMibVersion": securityManagementMibVersion,
       "servicesTable": servicesTable,
       "serviceEntry": serviceEntry,
       "serviceIndex": serviceIndex,
       "serviceName": serviceName,
       "serviceProtocolVersion": serviceProtocolVersion,
       "serviceAdminStatus": serviceAdminStatus,
       "serviceOperStatus": serviceOperStatus,
       "serviceRowStatus": serviceRowStatus}
)
