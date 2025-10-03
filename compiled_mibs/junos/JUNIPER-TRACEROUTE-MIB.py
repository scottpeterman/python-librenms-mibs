# SNMP MIB module (JUNIPER-TRACEROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-TRACEROUTE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:56 2025
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

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

jnxTraceRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxTraceRouteObjects_ObjectIdentity = ObjectIdentity
jnxTraceRouteObjects = _JnxTraceRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 8, 1)
)
_JnxTraceRouteCtlTable_Object = MibTable
jnxTraceRouteCtlTable = _JnxTraceRouteCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2)
)
if mibBuilder.loadTexts:
    jnxTraceRouteCtlTable.setStatus("current")
_JnxTraceRouteCtlEntry_Object = MibTableRow
jnxTraceRouteCtlEntry = _JnxTraceRouteCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1)
)
jnxTraceRouteCtlEntry.setIndexNames(
    (0, "JUNIPER-TRACEROUTE-MIB", "jnxTRCtlOwnerIndex"),
    (0, "JUNIPER-TRACEROUTE-MIB", "jnxTRCtlTestName"),
)
if mibBuilder.loadTexts:
    jnxTraceRouteCtlEntry.setStatus("current")


class _JnxTRCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type jnxTRCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxTRCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_JnxTRCtlOwnerIndex_Object = MibTableColumn
jnxTRCtlOwnerIndex = _JnxTRCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 1),
    _JnxTRCtlOwnerIndex_Type()
)
jnxTRCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTRCtlOwnerIndex.setStatus("current")


class _JnxTRCtlTestName_Type(SnmpAdminString):
    """Custom type jnxTRCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxTRCtlTestName_Type.__name__ = "SnmpAdminString"
_JnxTRCtlTestName_Object = MibTableColumn
jnxTRCtlTestName = _JnxTRCtlTestName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 2),
    _JnxTRCtlTestName_Type()
)
jnxTRCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTRCtlTestName.setStatus("current")


class _JnxTRCtlIfName_Type(DisplayString):
    """Custom type jnxTRCtlIfName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_JnxTRCtlIfName_Type.__name__ = "DisplayString"
_JnxTRCtlIfName_Object = MibTableColumn
jnxTRCtlIfName = _JnxTRCtlIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 3),
    _JnxTRCtlIfName_Type()
)
jnxTRCtlIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxTRCtlIfName.setStatus("current")


class _JnxTRCtlRoutingInstanceName_Type(DisplayString):
    """Custom type jnxTRCtlRoutingInstanceName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxTRCtlRoutingInstanceName_Type.__name__ = "DisplayString"
_JnxTRCtlRoutingInstanceName_Object = MibTableColumn
jnxTRCtlRoutingInstanceName = _JnxTRCtlRoutingInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 4),
    _JnxTRCtlRoutingInstanceName_Type()
)
jnxTRCtlRoutingInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxTRCtlRoutingInstanceName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-TRACEROUTE-MIB",
    **{"jnxTraceRouteMIB": jnxTraceRouteMIB,
       "jnxTraceRouteObjects": jnxTraceRouteObjects,
       "jnxTraceRouteCtlTable": jnxTraceRouteCtlTable,
       "jnxTraceRouteCtlEntry": jnxTraceRouteCtlEntry,
       "jnxTRCtlOwnerIndex": jnxTRCtlOwnerIndex,
       "jnxTRCtlTestName": jnxTRCtlTestName,
       "jnxTRCtlIfName": jnxTRCtlIfName,
       "jnxTRCtlRoutingInstanceName": jnxTRCtlRoutingInstanceName}
)
