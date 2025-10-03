# SNMP MIB module (WAYSTREAM-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\waystream\WAYSTREAM-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:58 2025
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

waystream = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303)
)
if mibBuilder.loadTexts:
    waystream.setRevisions(
        ("2017-02-10 11:00",
         "2011-01-11 18:01",
         "2009-03-23 10:39",
         "2008-01-17 14:05",
         "2007-05-11 12:28")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsProduct_ObjectIdentity = ObjectIdentity
wsProduct = _WsProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 1)
)
if mibBuilder.loadTexts:
    wsProduct.setStatus("current")
_WsConfig_ObjectIdentity = ObjectIdentity
wsConfig = _WsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 2)
)
if mibBuilder.loadTexts:
    wsConfig.setStatus("current")
_IpdConfig_ObjectIdentity = ObjectIdentity
ipdConfig = _IpdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 2, 1)
)
if mibBuilder.loadTexts:
    ipdConfig.setStatus("current")
_WsExperiment_ObjectIdentity = ObjectIdentity
wsExperiment = _WsExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 3)
)
if mibBuilder.loadTexts:
    wsExperiment.setStatus("current")
_WsMgmt_ObjectIdentity = ObjectIdentity
wsMgmt = _WsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4)
)
if mibBuilder.loadTexts:
    wsMgmt.setStatus("current")
_WsModules_ObjectIdentity = ObjectIdentity
wsModules = _WsModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 5)
)
if mibBuilder.loadTexts:
    wsModules.setStatus("current")
_PfSW_ObjectIdentity = ObjectIdentity
pfSW = _PfSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 6)
)
if mibBuilder.loadTexts:
    pfSW.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAYSTREAM-SMI",
    **{"waystream": waystream,
       "wsProduct": wsProduct,
       "wsConfig": wsConfig,
       "ipdConfig": ipdConfig,
       "wsExperiment": wsExperiment,
       "wsMgmt": wsMgmt,
       "wsModules": wsModules,
       "pfSW": pfSW}
)
