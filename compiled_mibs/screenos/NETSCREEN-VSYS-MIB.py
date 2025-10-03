# SNMP MIB module (NETSCREEN-VSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-VSYS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:15 2025
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

(netscreenVsys,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVsys")

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

netscreenVsysMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 15, 0)
)
if mibBuilder.loadTexts:
    netscreenVsysMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2000-05-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVsysCfg_ObjectIdentity = ObjectIdentity
nsVsysCfg = _NsVsysCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 15, 1)
)
_NsVsysCfgTable_Object = MibTable
nsVsysCfgTable = _NsVsysCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 15, 1, 1)
)
if mibBuilder.loadTexts:
    nsVsysCfgTable.setStatus("current")
_NsVsysCfgEntry_Object = MibTableRow
nsVsysCfgEntry = _NsVsysCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1)
)
nsVsysCfgEntry.setIndexNames(
    (0, "NETSCREEN-VSYS-MIB", "nsVsysCfgId"),
)
if mibBuilder.loadTexts:
    nsVsysCfgEntry.setStatus("current")


class _NsVsysCfgId_Type(Integer32):
    """Custom type nsVsysCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVsysCfgId_Type.__name__ = "Integer32"
_NsVsysCfgId_Object = MibTableColumn
nsVsysCfgId = _NsVsysCfgId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1, 1),
    _NsVsysCfgId_Type()
)
nsVsysCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVsysCfgId.setStatus("current")


class _NsVsysCfgName_Type(DisplayString):
    """Custom type nsVsysCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVsysCfgName_Type.__name__ = "DisplayString"
_NsVsysCfgName_Object = MibTableColumn
nsVsysCfgName = _NsVsysCfgName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1, 2),
    _NsVsysCfgName_Type()
)
nsVsysCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVsysCfgName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VSYS-MIB",
    **{"netscreenVsysMibModule": netscreenVsysMibModule,
       "nsVsysCfg": nsVsysCfg,
       "nsVsysCfgTable": nsVsysCfgTable,
       "nsVsysCfgEntry": nsVsysCfgEntry,
       "nsVsysCfgId": nsVsysCfgId,
       "nsVsysCfgName": nsVsysCfgName}
)
