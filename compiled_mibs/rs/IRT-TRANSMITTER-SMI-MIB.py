# SNMP MIB module (IRT-TRANSMITTER-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\rs\IRT-TRANSMITTER-SMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:35 2025
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

irt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19831)
)
if mibBuilder.loadTexts:
    irt.setRevisions(
        ("2007-05-04 14:00",
         "2006-12-20 14:00",
         "2006-09-07 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SelectManualAuto(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("manual", 1),
          ("automatic", 2))
    )



class SelectOnOff(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("on", 1),
          ("off", 2))
    )



class Input1Input2(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("input1", 1),
          ("input2", 2))
    )



class OkNotOk(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("ok", 1),
          ("notok", 2))
    )



class FaultOK(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("fault", 1),
          ("ok", 2))
    )



class WarningOK(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("warning", 1),
          ("ok", 2))
    )



class LocalRemote(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("local", 1),
          ("remote", 2))
    )



class MuteOk(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("mute", 1),
          ("ok", 2))
    )



class ReadyNotReady(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("ready", 1),
          ("notready", 2))
    )



class ExecutedNotExecuted(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("executed", 1),
          ("notexecuted", 2))
    )



class PresentNotPresent(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("present", 1),
          ("notpresent", 2))
    )



class SFNMFN(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("sfn", 1),
          ("mfn", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Broadcast_ObjectIdentity = ObjectIdentity
broadcast = _Broadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1)
)
_Transmitter_ObjectIdentity = ObjectIdentity
transmitter = _Transmitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1)
)
_DvbT_ObjectIdentity = ObjectIdentity
dvbT = _DvbT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1)
)
_Dab_ObjectIdentity = ObjectIdentity
dab = _Dab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 2)
)
_Fm_ObjectIdentity = ObjectIdentity
fm = _Fm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 3)
)
_Drm_ObjectIdentity = ObjectIdentity
drm = _Drm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 4)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IRT-TRANSMITTER-SMI-MIB",
    **{"SelectManualAuto": SelectManualAuto,
       "SelectOnOff": SelectOnOff,
       "Input1Input2": Input1Input2,
       "OkNotOk": OkNotOk,
       "FaultOK": FaultOK,
       "WarningOK": WarningOK,
       "LocalRemote": LocalRemote,
       "MuteOk": MuteOk,
       "ReadyNotReady": ReadyNotReady,
       "ExecutedNotExecuted": ExecutedNotExecuted,
       "PresentNotPresent": PresentNotPresent,
       "SFNMFN": SFNMFN,
       "irt": irt,
       "broadcast": broadcast,
       "transmitter": transmitter,
       "dvbT": dvbT,
       "dab": dab,
       "fm": fm,
       "drm": drm,
       "common": common}
)
