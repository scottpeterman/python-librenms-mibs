# SNMP MIB module (SENSATRONICS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sensatronics\SENSATRONICS-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:23 2025
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

sensatronics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16174)
)
if mibBuilder.loadTexts:
    sensatronics.setRevisions(
        ("2004-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConsumerProducts_ObjectIdentity = ObjectIdentity
consumerProducts = _ConsumerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1)
)
if mibBuilder.loadTexts:
    consumerProducts.setStatus("current")
_EnvMonitors_ObjectIdentity = ObjectIdentity
envMonitors = _EnvMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1)
)
if mibBuilder.loadTexts:
    envMonitors.setStatus("current")
_ProductITTM_ObjectIdentity = ObjectIdentity
productITTM = _ProductITTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1)
)
if mibBuilder.loadTexts:
    productITTM.setStatus("current")
_ProductCRYO_ObjectIdentity = ObjectIdentity
productCRYO = _ProductCRYO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 2)
)
if mibBuilder.loadTexts:
    productCRYO.setStatus("current")
_ProductEM1_ObjectIdentity = ObjectIdentity
productEM1 = _ProductEM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3)
)
if mibBuilder.loadTexts:
    productEM1.setStatus("current")
_ConsumerTools_ObjectIdentity = ObjectIdentity
consumerTools = _ConsumerTools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 2)
)
if mibBuilder.loadTexts:
    consumerTools.setStatus("current")
_CustomProducts_ObjectIdentity = ObjectIdentity
customProducts = _CustomProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 3)
)
if mibBuilder.loadTexts:
    customProducts.setStatus("current")
_CustomTools_ObjectIdentity = ObjectIdentity
customTools = _CustomTools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 4)
)
if mibBuilder.loadTexts:
    customTools.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENSATRONICS-SMI",
    **{"sensatronics": sensatronics,
       "consumerProducts": consumerProducts,
       "envMonitors": envMonitors,
       "productITTM": productITTM,
       "productCRYO": productCRYO,
       "productEM1": productEM1,
       "consumerTools": consumerTools,
       "customProducts": customProducts,
       "customTools": customTools}
)
