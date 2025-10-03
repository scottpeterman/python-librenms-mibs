# SNMP MIB module (FORCE10-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\FORCE10-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:02 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

force10 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027)
)
if mibBuilder.loadTexts:
    force10.setRevisions(
        ("2007-06-15 12:00",
         "1900-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10Products_ObjectIdentity = ObjectIdentity
f10Products = _F10Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1)
)
if mibBuilder.loadTexts:
    f10Products.setStatus("current")
_F10Common_ObjectIdentity = ObjectIdentity
f10Common = _F10Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 2)
)
if mibBuilder.loadTexts:
    f10Common.setStatus("current")
_F10Mgmt_ObjectIdentity = ObjectIdentity
f10Mgmt = _F10Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3)
)
if mibBuilder.loadTexts:
    f10Mgmt.setStatus("current")
_F10Modules_ObjectIdentity = ObjectIdentity
f10Modules = _F10Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 4)
)
if mibBuilder.loadTexts:
    f10Modules.setStatus("current")
_F10Experiment_ObjectIdentity = ObjectIdentity
f10Experiment = _F10Experiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20)
)
if mibBuilder.loadTexts:
    f10Experiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-SMI",
    **{"force10": force10,
       "f10Products": f10Products,
       "f10Common": f10Common,
       "f10Mgmt": f10Mgmt,
       "f10Modules": f10Modules,
       "f10Experiment": f10Experiment}
)
