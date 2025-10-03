# SNMP MIB module (TELDAT-MON-CPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teldat\TELDAT-MON-CPU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:57 2025
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

(telProdNpMonitSistema,) = mibBuilder.importSymbols(
    "TELDAT-SW-STRUCTURE-MIB",
    "telProdNpMonitSistema")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TeldatCPUMonMIB_ObjectIdentity = ObjectIdentity
teldatCPUMonMIB = _TeldatCPUMonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2)
)
_TeldatCPUMonMIBObjects_ObjectIdentity = ObjectIdentity
teldatCPUMonMIBObjects = _TeldatCPUMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1)
)
_TeldatCPUBusyGroup_ObjectIdentity = ObjectIdentity
teldatCPUBusyGroup = _TeldatCPUBusyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1)
)
_TeldatCPUBusy5sec_Type = Gauge32
_TeldatCPUBusy5sec_Object = MibScalar
teldatCPUBusy5sec = _TeldatCPUBusy5sec_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 1),
    _TeldatCPUBusy5sec_Type()
)
teldatCPUBusy5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCPUBusy5sec.setStatus("mandatory")
_TeldatCPUBusy1min_Type = Gauge32
_TeldatCPUBusy1min_Object = MibScalar
teldatCPUBusy1min = _TeldatCPUBusy1min_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 2),
    _TeldatCPUBusy1min_Type()
)
teldatCPUBusy1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCPUBusy1min.setStatus("mandatory")
_TeldatCPUBusy5min_Type = Gauge32
_TeldatCPUBusy5min_Object = MibScalar
teldatCPUBusy5min = _TeldatCPUBusy5min_Object(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 3),
    _TeldatCPUBusy5min_Type()
)
teldatCPUBusy5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teldatCPUBusy5min.setStatus("mandatory")
_TeldatCPUMonMIBNotifPrefix_ObjectIdentity = ObjectIdentity
teldatCPUMonMIBNotifPrefix = _TeldatCPUMonMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 2)
)
_TeldatCPUMonMIBNotifs_ObjectIdentity = ObjectIdentity
teldatCPUMonMIBNotifs = _TeldatCPUMonMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 2, 0)
)
_TeldatCPUMonMIBConformance_ObjectIdentity = ObjectIdentity
teldatCPUMonMIBConformance = _TeldatCPUMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3)
)
_TeldatCPUCompliances_ObjectIdentity = ObjectIdentity
teldatCPUCompliances = _TeldatCPUCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3, 1)
)
_TeldatCPUGroups_ObjectIdentity = ObjectIdentity
teldatCPUGroups = _TeldatCPUGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELDAT-MON-CPU-MIB",
    **{"teldatCPUMonMIB": teldatCPUMonMIB,
       "teldatCPUMonMIBObjects": teldatCPUMonMIBObjects,
       "teldatCPUBusyGroup": teldatCPUBusyGroup,
       "teldatCPUBusy5sec": teldatCPUBusy5sec,
       "teldatCPUBusy1min": teldatCPUBusy1min,
       "teldatCPUBusy5min": teldatCPUBusy5min,
       "teldatCPUMonMIBNotifPrefix": teldatCPUMonMIBNotifPrefix,
       "teldatCPUMonMIBNotifs": teldatCPUMonMIBNotifs,
       "teldatCPUMonMIBConformance": teldatCPUMonMIBConformance,
       "teldatCPUCompliances": teldatCPUCompliances,
       "teldatCPUGroups": teldatCPUGroups}
)
