# SNMP MIB module (PROFLINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\profline\PROFLINE
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:30 2025
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

profline = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21222)
)
if mibBuilder.loadTexts:
    profline.setRevisions(
        ("2012-03-23 10:34",
         "2011-06-24 12:30",
         "2010-11-23 11:24",
         "2008-11-07 09:32",
         "2008-09-18 09:30",
         "2008-04-16 11:06",
         "2001-08-07 14:35")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1)
)
_Receivers_ObjectIdentity = ObjectIdentity
receivers = _Receivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 1)
)
_Modulators_ObjectIdentity = ObjectIdentity
modulators = _Modulators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 2)
)
_Processors_ObjectIdentity = ObjectIdentity
processors = _Processors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 3)
)
_Demodulators_ObjectIdentity = ObjectIdentity
demodulators = _Demodulators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 4)
)
_Switchers_ObjectIdentity = ObjectIdentity
switchers = _Switchers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 1, 5)
)
_ProflineExperimental_ObjectIdentity = ObjectIdentity
proflineExperimental = _ProflineExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 2)
)
_ExpReceivers_ObjectIdentity = ObjectIdentity
expReceivers = _ExpReceivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 2, 1)
)
_ExpModulators_ObjectIdentity = ObjectIdentity
expModulators = _ExpModulators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 2, 2)
)
_ExpProcessors_ObjectIdentity = ObjectIdentity
expProcessors = _ExpProcessors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 2, 3)
)
_ExpDemodulators_ObjectIdentity = ObjectIdentity
expDemodulators = _ExpDemodulators_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 2, 4)
)
_ExpSwitchers_ObjectIdentity = ObjectIdentity
expSwitchers = _ExpSwitchers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21222, 2, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROFLINE-MIB",
    **{"profline": profline,
       "products": products,
       "receivers": receivers,
       "modulators": modulators,
       "processors": processors,
       "demodulators": demodulators,
       "switchers": switchers,
       "proflineExperimental": proflineExperimental,
       "expReceivers": expReceivers,
       "expModulators": expModulators,
       "expProcessors": expProcessors,
       "expDemodulators": expDemodulators,
       "expSwitchers": expSwitchers}
)
