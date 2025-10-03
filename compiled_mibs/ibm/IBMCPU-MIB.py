# SNMP MIB module (IBMCPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ibm\IBMCPU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:55 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm6611_ObjectIdentity = ObjectIdentity
ibm6611 = _Ibm6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2)
)
_Ibmsystem_ObjectIdentity = ObjectIdentity
ibmsystem = _Ibmsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4)
)
_IbmMainProcessorLoadTable_Object = MibTable
ibmMainProcessorLoadTable = _IbmMainProcessorLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ibmMainProcessorLoadTable.setStatus("mandatory")
_IbmMainProcessorLoadEntry_Object = MibTableRow
ibmMainProcessorLoadEntry = _IbmMainProcessorLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1)
)
ibmMainProcessorLoadEntry.setIndexNames(
    (0, "IBMCPU-MIB", "ibmMainProcessorLoadIndex"),
)
if mibBuilder.loadTexts:
    ibmMainProcessorLoadEntry.setStatus("mandatory")


class _IbmMainProcessorLoadIndex_Type(Integer32):
    """Custom type ibmMainProcessorLoadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IbmMainProcessorLoadIndex_Type.__name__ = "Integer32"
_IbmMainProcessorLoadIndex_Object = MibTableColumn
ibmMainProcessorLoadIndex = _IbmMainProcessorLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1, 1),
    _IbmMainProcessorLoadIndex_Type()
)
ibmMainProcessorLoadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMainProcessorLoadIndex.setStatus("mandatory")
_IbmMainProcessorLoad_Type = Gauge32
_IbmMainProcessorLoad_Object = MibTableColumn
ibmMainProcessorLoad = _IbmMainProcessorLoad_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1, 2),
    _IbmMainProcessorLoad_Type()
)
ibmMainProcessorLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmMainProcessorLoad.setStatus("mandatory")
_NetView6000SubAgent_ObjectIdentity = ObjectIdentity
netView6000SubAgent = _NetView6000SubAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 4)
)
_Nv6saComputerSystem_ObjectIdentity = ObjectIdentity
nv6saComputerSystem = _Nv6saComputerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 5)
)
_Nv6saComputerSystemLoad_Type = Gauge32
_Nv6saComputerSystemLoad_Object = MibScalar
nv6saComputerSystemLoad = _Nv6saComputerSystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 5, 1),
    _Nv6saComputerSystemLoad_Type()
)
nv6saComputerSystemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nv6saComputerSystemLoad.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMCPU-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm6611": ibm6611,
       "ibmsystem": ibmsystem,
       "ibmMainProcessorLoadTable": ibmMainProcessorLoadTable,
       "ibmMainProcessorLoadEntry": ibmMainProcessorLoadEntry,
       "ibmMainProcessorLoadIndex": ibmMainProcessorLoadIndex,
       "ibmMainProcessorLoad": ibmMainProcessorLoad,
       "netView6000SubAgent": netView6000SubAgent,
       "nv6saComputerSystem": nv6saComputerSystem,
       "nv6saComputerSystemLoad": nv6saComputerSystemLoad}
)
